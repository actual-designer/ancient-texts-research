#!/usr/bin/env python3
"""
run_all.py — Orchestration script for the full verification suite.

Usage:
    python3 scripts/verify/run_all.py

Runs all verification steps sequentially:
  1. PDF text extraction
  2. Quote extraction from markdown
  3. Link validation
  4. Quote verification (fuzzy matching)
  5. Cross-reference verification
  6. Numerical consistency check
  7. NHI source verification
  8. Report generation
"""

import sys
import time
from pathlib import Path

# Ensure we can import from scripts.verify
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))


def step(name: str, module: str) -> bool:
    """Run a verification step by module import and call its main()."""
    print(f"\n{'='*60}")
    print(f"  STEP: {name}")
    print(f"{'='*60}")
    try:
        __import__(f"scripts.verify.{module}", fromlist=["main"])
        mod = sys.modules[f"scripts.verify.{module}"]
        if hasattr(mod, "main"):
            mod.main()
        print(f"  ✓ {name} completed")
        return True
    except Exception as e:
        print(f"  ✗ {name} FAILED: {e}", file=sys.stderr)
        return False


def main():
    start = time.time()
    print("Chronos Archive — Full Verification Suite")
    print(f"Starting at {time.ctime()}")
    print()

    steps = [
        ("PDF Text Extraction", "extract_pdf_text"),
        ("Quote Extraction", "extract_quotes"),
        ("Link Validation", "verify_links"),
        ("Quote Verification", "verify_quotes"),
        ("Cross-Reference Verification", "verify_cross_refs"),
        ("Numerical Consistency Check", "verify_numerical"),
        ("NHI Source Verification", "verify_nhi_sources"),
        ("Report Generation", "generate_report"),
    ]

    results = []
    for name, module in steps:
        ok = step(name, module)
        results.append((name, ok))

    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"  VERIFICATION COMPLETE ({elapsed:.1f}s)")
    print(f"{'='*60}")
    for name, ok in results:
        status = "✓" if ok else "✗"
        print(f"  {status} {name}")
    print()
    all_ok = all(ok for _, ok in results)
    print(f"  Overall: {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
