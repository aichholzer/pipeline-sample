"""S3 client helper (AC-1 fixture: contains a planted AWS credential).

The hardcoded key below is AWS's published example access key, not a live
credential. gitleaks matches the AKIA pattern, so the deterministic secret gate
marks it blocking and the ai-review check fails (AC-1, requirement 6.2).
"""

import boto3

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
