"""A tiny, deliberately boring arithmetic module.

Just enough real behaviour to have unit tests that pass on the clean baseline and
can be broken by the AC-5 case patch to fail the Flow B test stage. Nothing here
is secret or sensitive; the interesting fixtures are the case patches that add a
planted credential (AC-1) or a configured keyword (AC-4).
"""

from __future__ import annotations


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def subtract(left: int, right: int) -> int:
    """Return the difference of two integers."""
    return left - right


def multiply(left: int, right: int) -> int:
    """Return the product of two integers."""
    return left * right
