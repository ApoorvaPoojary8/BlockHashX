import hashlib


def sha256_hash(data: str) -> str:
    """
    Standalone hashing utility
    """
    return hashlib.sha256(data.encode()).hexdigest()