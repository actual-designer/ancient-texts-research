"""Extract searchable text from PDF source files and save as .txt.

Part of the Chronos Archive verification toolkit.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from scripts.verify.config import EXTRACTED_DIR, TEXTS_DIR, UNVERIFIABLE_PDFS
from scripts.verify.utils import slugify


def log(msg: str) -> None:
    """Log to stderr so stdout stays clean for piping."""
    print(msg, file=sys.stderr)


def extract_text_with_pdftotext(pdf_path: Path) -> str:
    """Extract all text from a PDF using pdftotext -layout.

    Returns the raw text (without page markers).
    """
    result = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        log(f"  [WARN] pdftotext failed for {pdf_path.name}: {result.stderr.strip()}")
        return ""
    return result.stdout


def extract_text_by_pages(pdf_path: Path) -> str:
    """Extract text with --- PAGE {N} --- markers inserted between pages.

    Uses pdftotext -layout which emits form-feed characters between pages.
    Falls back to whole-document extraction if page count cannot be determined.
    """
    text = extract_text_with_pdftotext(pdf_path)
    if not text:
        return ""

    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()

    if not pages:
        return ""

    marked: list[str] = []
    for idx, page_text in enumerate(pages, start=1):
        marked.append(f"--- PAGE {idx} ---\n{page_text}")

    return "\n".join(marked)


def is_scanned_pdf(pdf_path: Path) -> bool:
    """Heuristic: if pdftotext yields very little text, the PDF is likely image-based."""
    text = extract_text_with_pdftotext(pdf_path)
    stripped = text.strip()
    return len(stripped) < 200


def attempt_ocr(pdf_path: Path) -> str | None:
    """Try to OCR a scanned PDF using ocrmypdf + tesseract.

    Returns extracted text on success, None on failure.
    Does not modify the original PDF.
    """
    if not shutil.which("ocrmypdf"):
        log("  [INFO] ocrmypdf not installed; skipping OCR attempt")
        return None

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        log(f"  [INFO] Running OCR on {pdf_path.name} ...")
        ocr_result = subprocess.run(
            ["ocrmypdf", "--force-ocr", str(pdf_path), str(tmp_path)],
            capture_output=True,
            text=True,
        )
        if ocr_result.returncode != 0:
            log(f"  [WARN] OCR failed for {pdf_path.name}: {ocr_result.stderr.strip()}")
            return None

        text = extract_text_by_pages(tmp_path)
        return text
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def process_pdf(
    pdf_path: Path,
    *,
    skip_existing: bool,
    overwrite: bool,
) -> tuple[bool, bool]:
    """Extract text from a single PDF.

    Returns (success, skipped).
    """
    slug = slugify(pdf_path.name)
    out_path = EXTRACTED_DIR / f"{slug}.txt"

    if out_path.exists():
        if skip_existing and not overwrite:
            log(f"[SKIP] {pdf_path.name} -> {out_path.name} (already exists)")
            return True, True
        if not overwrite:
            log(f"[SKIP] {pdf_path.name} -> {out_path.name} (already exists, use --overwrite)")
            return True, True

    log(f"[EXTRACT] {pdf_path.name} -> {out_path.name}")

    if pdf_path.name in UNVERIFIABLE_PDFS:
        log(f"  [INFO] {pdf_path.name} is known to be unverifiable (scanned/no text layer)")

    if is_scanned_pdf(pdf_path):
        log(f"  [INFO] {pdf_path.name} appears to be scanned; attempting OCR ...")
        text = attempt_ocr(pdf_path)
        if text is None:
            log(f"  [FAIL] Could not extract text from scanned PDF: {pdf_path.name}")
            return False, False
    else:
        text = extract_text_by_pages(pdf_path)

    if not text.strip():
        log(f"  [FAIL] Extracted text is empty for {pdf_path.name}")
        return False, False

    EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    log(f"  [OK] Saved {out_path.name}")
    return True, False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract searchable text from PDFs in texts/ and save to texts/extracted/.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip PDFs that already have a corresponding .txt file",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Force re-extraction even if a .txt file already exists",
    )
    args = parser.parse_args(argv)

    if args.skip_existing and args.overwrite:
        log("[ERROR] --skip-existing and --overwrite are mutually exclusive")
        return 1

    pdf_files = sorted(TEXTS_DIR.glob("*.pdf"))
    if not pdf_files:
        log("[WARN] No PDF files found in texts/")
        return 1

    extracted = 0
    skipped = 0
    failed = 0

    for pdf_path in pdf_files:
        success, was_skipped = process_pdf(
            pdf_path,
            skip_existing=args.skip_existing,
            overwrite=args.overwrite,
        )
        if was_skipped:
            skipped += 1
        elif success:
            extracted += 1
        else:
            failed += 1

    log("")
    log("=" * 50)
    log(f"Summary: {extracted} extracted, {skipped} skipped, {failed} failed")
    log("=" * 50)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
