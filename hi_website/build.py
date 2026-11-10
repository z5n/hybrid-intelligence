#!/usr/bin/env python
"""Vercel build step for the Django site.

Runs after dependencies are installed. Collects CSS, JavaScript and images
into staticfiles/ (Vercel serves that folder from its CDN) and, when
DATABASE_URL is set, applies migrations to Postgres.
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANAGE = ROOT / "manage.py"


def run(args):
    print("+", " ".join(args), flush=True)
    subprocess.run(args, check=True, cwd=ROOT)


def main():
    if not os.environ.get("DJANGO_SECRET_KEY"):
        print(
            "DJANGO_SECRET_KEY is not set. Static files will still be collected. "
            "Add the variable in Vercel (Project → Settings → Environment Variables) "
            "and redeploy, or the live site will refuse to start.",
            flush=True,
        )
    py = sys.executable
    run([py, str(MANAGE), "collectstatic", "--noinput"])
    if os.environ.get("DATABASE_URL"):
        run([py, str(MANAGE), "migrate", "--noinput"])
    else:
        print(
            "DATABASE_URL is not set, so migrations were skipped. "
            "Pages will still deploy. Sign-ups need a Postgres database "
            "attached to the Vercel project, which sets DATABASE_URL.",
            flush=True,
        )


if __name__ == "__main__":
    main()
