#!/usr/bin/python3.10

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
try:
    lost = "lost_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{lost}'...")
    f = open(lost, "r")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")
try:
    perm = "classified_vault.txt"
    print(f"CRISIS ALERT: Attempting access to '{perm}'...")
    f = open(perm, "r")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")
standard = "standard_archive.txt"
print(f"ROUTINE ACCESS: Attempting access to '{standard}'...")
with open(standard, "r"):
    f = open(standard, "r")
    content = f.read()
    print(f"SUCCESS: Archive recovered - ''{content}''")
    print("STATUS: Normal operations resumed\n")
print("All crisis scenarios handled successfully. Archives secure.")
