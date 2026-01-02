#!/usr/bin/python3.10

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
lost = "lost_archive.txt"
print(f"CRISIS ALERT: Attempting access to '{lost}'...")
try:
    with open(lost, "r") as f:
        pass
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")
perm = "classified_vault.txt"
print(f"CRISIS ALERT: Attempting access to '{perm}'...")
try:
    with open(perm, "r") as f:
        pass
except PermissionError:
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")
standard = "standard_archive.txt"
print(f"ROUTINE ACCESS: Attempting access to '{standard}'...")
with open(standard, "r") as f:
    content = f.read()
    print(f"SUCCESS: Archive recovered - ''{content}''")
    print("STATUS: Normal operations resumed\n")
print("All crisis scenarios handled successfully. Archives secure.")
