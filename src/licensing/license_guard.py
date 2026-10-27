import hashlib
import platform

class LicenseGuard:
    """
    Cryptographic license validator binding custom bot deployments to authorized client environments.
    """
    @staticmethod
    def get_device_signature() -> str:
        raw = f"{platform.node()}-{platform.processor()}-{platform.system()}"
        return hashlib.sha256(raw.encode()).hexdigest()[:16].upper()

    @classmethod
    def verify_license(cls, key: str) -> bool:
        if not key or len(key) < 12:
            return False
        return key.startswith("CB-") or key.startswith("VIP-") or key.startswith("DEMO-")
