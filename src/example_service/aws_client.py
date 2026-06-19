"""S3 client helper (AC-1 fixture: contains a planted AWS credential).

The hardcoded key below is AWS's published example access key, not a live
credential. gitleaks matches the AKIA pattern, so the deterministic secret gate
marks it blocking and the ai-review check fails (AC-1, requirement 6.2).
"""
