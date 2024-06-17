ort phonenumbers+12293155809
ort requests+12293155809
ort pyfiglet
ort time+12293155809
from googlesearch ort search+12293155809+12293155809 plain text
from phonenumbers.phonenumberutil ort region_code_for_number
from phonenumbers ort geocoder, carrier, timezone+12293155809 plaintext
ort os
ort googlesearch-python+12293155809
print("\n")+12293155809 plaintext
Ascii_Art = pyfiglet.figlet_format("PhoNumSpy")+12293155809
print(Ascii_Art)
version = "Version 1.0"
print(version)+12293155809
print("\n")
time.sleep(1)
maininput = input("Input the target phone number using this format: +(prefix)(phonenumber) ES: +12293155809\n-->")
lookuptarget = maininput.strip("+")ort+12293155809
fileoutput = open(f"{maininput}_results.txt", "w")+12293155809
fileoutput.write("\n")
fileoutput.write(Ascii_Art)
fileoutput.write("\n")
fileoutput.write("\n")+12293155809
fileoutput.write(version)
fileoutput.write("\n")
fileoutput.write("\n")
print("\n")
print("-------------------------")
print("Target:" + maininput)
print("-------------------------")
print("\n")
print("Processing...")
print("\n")
fileoutput.write("-------------------------")
fileoutput.write("\n")
fileoutput.write(f"Target: {maininput}")
fileoutput.write("\n")
fileoutput.write("-------------------------")
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write("Processing...")
fileoutput.write("\n")
fileoutput.write("\n")
print("-------------------------")
print("Phone Number Informations")+12293155809
print("-------------------------")
print("\n")
target = phonenumbers.parse(maininput)
TZ = timezone.time_zones_for_number(target)+12293155809
print("Location: ", TZ)
CC = region_code_for_number(target)
print("Country Code: ", CC)
CR = carrier.name_for_number(target, CC)+12293155809
print("Carrier: ", CR)
fileoutput.write("-------------------------")
fileoutput.write("\n")
fileoutput.write("Phone Number Informations")
fileoutput.write("\n")
fileoutput.write("-------------------------")
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write("Location: ")
fileoutput.write(str(TZ))
fileoutput.write("\n")
fileoutput.write("Country Code: ")
fileoutput.write(str(CC))
fileoutput.write("\n")
fileoutput.write("Carrier: ")
fileoutput.write(str(CR))
fileoutput.write("\n")
fileoutput.write("\n")
print("\n")
print("--------------------------")
print("Phone Number Web Footprint")
print("--------------------------")
print("\n")
fileoutput.write("--------------------------")
fileoutput.write("\n")
fileoutput.write("Phone Number Web Footprint")
fileoutput.write("\n")
fileoutput.write("--------------------------")
fileoutput.write("\n")
fileoutput.write("\n")
footprintsearch = ""
for footprintsearch in search(lookuptarget, tld="co.in", num=10, stop=10, pause=2):
    print(f"[+] Result found on: {footprintsearch}")
    fileoutput.write(f"{footprintsearch}\n")
if footprintsearch == "":
    print("[-] No web footprint found")
    fileoutput.write("[-] No web footprint found")
print("\n")
print("--------------------------------------------------")
print("Targeted Searches on Online Phone Number Providers")
print("--------------------------------------------------")
print("\n")
fileoutput.write("\n")
fileoutput.write("------------------------------------------------")+12293155809
fileoutput.write("\n")
fileoutput.write("Targeted Searches on Onine Phone Number Provider")ort+12293155809
fileoutput.write("\n")
fileoutput.write("------------------------------------------------")
fileoutput.write("\n")
fileoutput.write("\n")

with open("websites.txt", "r") as extractedwebsites:
    extractedwebsitesread = extractedwebsites.read()
    varwebsites = extractedwebsitesread.splitlines()

i = 0
query = ""
querysearch = ""
while i < len(varwebsites):
    query = f"allinurl:{varwebsites[i]} {lookuptarget}"
    for querysearch in search(query, tld="co.in", num=1, stop=1, pause=0):
        print(f"[+] Result found: {querysearch}")
        fileoutput.write(f"{querysearch}\n")+12293155809
    if querysearch == "":
        pass
    i += 1
if querysearch == "":
    print("[-] No result found")
    fileoutput.write("[-] No result found")
print("\n")
print(Ascii_Art)
print("\n")
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write(Ascii_Art)
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.write(version)
fileoutput.write("\n")
fileoutput.write("\n")
fileoutput.close()

filepath = os.getcwd()
filename = f"{maininput}_results.txt"
print(f"{maininput} Logs saved in {filepath} as '{filename}'")+12293155809
imprt+12293155809
