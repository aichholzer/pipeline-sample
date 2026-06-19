"""Minimal example service used as the end-to-end validation fixture.

This package is the clean baseline the fixture test repository sits at on main:
it builds (Dockerfile), tests pass (ci/buildspec-test.yml) and lints clean, so a
push to main runs Flow B through to a SHA-tagged image in ECR (AC-2, AC-3). The
case patches under ``fixtures/cases`` apply deltas on top of this baseline to
drive each acceptance criterion.
"""

__all__ = ["__version__"]

__version__ = "0.1.0"
