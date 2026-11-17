"""Temporary diagnostic: fail unless the real harness input is exposed."""
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

target = Path(__file__).parent / "dev-probe.xml"
subprocess.run(["adb", "-s", "emulator-5554", "shell", "uiautomator", "dump", "/sdcard/smoke-window.xml"], check=True, stdout=subprocess.DEVNULL)
subprocess.run(["adb", "-s", "emulator-5554", "pull", "/sdcard/smoke-window.xml", str(target)], check=True, capture_output=True)
nodes = list(ET.parse(target).iter("node"))
print("Visible labels:", [n.get("text") or n.get("content-desc") for n in nodes if n.get("text") or n.get("content-desc")])
assert any(n.get("resource-id", "").endswith("verb-input") for n in nodes), "RED: actual harness input is not accessible"
print("GREEN: actual harness input is accessible")
