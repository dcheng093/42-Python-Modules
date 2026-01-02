#!/usr/bin/python3.10

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
data = "classified_data.txt"
security = "security_protocols.txt"
print("Vault connection establish with failsafe protocols\n")
with open(data, 'r'):
    print("SECURE EXTRACTION:")
    f = open(data, 'r')
    content = f.read()
    print(content)
with open(security, 'r'):
    print("\nSECURE PRESERVATION:")
    f = open(security, 'r')
    content = f.read()
    print(content)
    print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
