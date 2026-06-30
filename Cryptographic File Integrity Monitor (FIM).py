#Cryptographic File Integrity Monitor (FIM)
"""
Cyber Security Toolkit - Cryptographic File Integrity Monitor
Author: @abdullajaanov
Role: Chief Cyber Architect
"""

import hashlib
import json
import logging
from pathlib import Path
from typing import Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FIM_Engine")

class FileIntegrityMonitor:
    """High-assurance integrity monitoring system using SHA-256 state hashing."""
    
    def __init__(self, database_path: str = "security_state.json") -> None:
        self.db_path = Path(database_path)
        self._state_db: Dict[str, str] = self._load_database()

    def _load_database(self) -> Dict[str, str]:
        if self.db_path.exists():
            try:
                return json.loads(self.db_path.read_text())
            except json.JSONDecodeError:
                logger.error("[@abdullajaanov Warning] State database corrupted. Resetting.")
        return {}

    def _save_database(self) -> None:
        self.db_path.write_text(json.dumps(self._state_db, indent=4))

    def calculate_sha256(self, file_path: Path) -> Optional[str]:
        """Computes SHA-256 hash utilizing chunked memory buffering."""
        sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(65536): # 64KB optimized chunks
                    sha256.update(chunk)
            return sha256.hexdigest()
        except IOError:
            return None

    def monitor_target(self, target_file: str) -> None:
        """Evaluates system target file against baseline cryptographic states."""
        path = Path(target_file)
        if not path.is_file():
            logger.error(f"Target {target_file} is not a valid file.")
            return

        current_hash = self.calculate_sha256(path)
        path_str = str(path.resolve())

        if path_str in self._state_db:
            if self._state_db[path_str] == current_hash:
                logger.info(f"[SECURE] {path.name} integrity verified. Status: OK.")
            else:
                logger.critical(f"[@abdullajaanov ALERT] INTEGRITY COMPROMISED! File {path.name} modified.")
        else:
            logger.info(f"[BASELINE] Registering secure hash for: {path.name}")
            self._state_db[path_str] = current_hash
            self._save_database()

if __name__ == "__main__":
    fim = FileIntegrityMonitor()
    test_file = Path("critical_system.bin")
    test_file.write_text("secure_payload_v1")
    fim.monitor_target("critical_system.bin")
