import subprocess

try:
    wifi_name = next((line.split(":")[1].strip() for line in subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True, check=True).stdout.splitlines() if "SSID" in line), "none")
except subprocess.CalledProcessError:
    wifi_name = "none"

print("Current Wi-Fi name:", wifi_name)
