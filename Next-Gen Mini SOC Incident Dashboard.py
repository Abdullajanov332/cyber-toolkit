"""
Cyber Security Toolkit - Next-Gen Mini SOC Dashboard
Author: @abdullajaanov
Role: Chief Cyber Architect
"""

import time
from enum import Enum
from typing import List, Dict, Any

class Severity(Enum):
    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class SecurityIncident:
    def __init__(self, severity: Severity, message: str, source: str) -> None:
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.severity = severity
        self.message = message
        self.source = source

class MiniSOCDashboard:
    """Professional Security Operations Center event-bus and correlation dashboard."""
    
    def __init__(self) -> None:
        self._incident_pool: List[SecurityIncident] = []
        print("[*] @abdullajaanov SOC Core Engine Online.")

    def ingest_incident(self, severity: Severity, message: str, source: str) -> None:
        """Ingests raw metrics into classified security alerts."""
        incident = SecurityIncident(severity, message, source)
        self._incident_pool.append(incident)
        
        # Real-time console projection
        prefix = f"[!!! {severity.value} !!!]" if severity in [Severity.HIGH, Severity.CRITICAL] else f"[{severity.value}]"
        print(f"{prefix} {incident.timestamp} | Source: {source} -> {message}")

    def generate_cyber_report(self, export_path: str = "soc_threat_intel.json") -> None:
        """Compiles standard automated Threat Intelligence reports."""
        import json
        
        serialized_data = [
            {
                "time": i.timestamp,
                "severity": i.severity.value,
                "message": i.message,
                "source": i.source
            } for i in self._incident_pool
        ]
        
        metadata = {
            "analyst": "@abdullajaanov",
            "total_events": len(self._incident_pool),
            "incidents": serialized_data
        }
        
        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=4)
        print(f"\n[+] Threat Intelligence Exported to -> {export_path}")

if __name__ == "__main__":
    soc = MiniSOCDashboard()
    soc.ingest_incident(Severity.CRITICAL, "SQL Injection detected via API gateway", "Web_Monitor")
    soc.generate_cyber_report()
