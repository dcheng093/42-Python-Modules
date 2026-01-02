#!/usr/bin/python3.10

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
newfile = "new_discovery.txt"
print(f"Initializing new storage unit: {newfile}")
f = open(newfile, "w", encoding="utf-8")
print("Storage unit created successfully...\n")
print("Inscribing preservation data...")
line1 = "{[}ENTRY 001{]} New quantum algorithm discovered\n"
line2 = "{[}ENTRY 002{]} Efficiency increased by 347%\n"
line3 = "{[}ENTRY 003{]} Archived by Data Archivist trainee"
print(line1 + line2 + line3)
f.write(line1)
f.write(line2)
f.write(line3)
print("")
print("Datat inscription complete. Storage unit sealed.")
f.close()
print(f"Archive '{newfile}' ready for long-term preservation.")
