#!/usr/bin/env python
# the needed setting is to set the 'terminal length 0' 
# in order to eliminate pressing enter to passing thorough config pages everytime
import getpass
import telnetlib
user = input("Enter your telnet username: ")
password = getpass.getpass()
inventory = open("inventory.txt")
for IP in inventory:
    IP = IP.strip() # to remove any additional spaces if there are any
    print("Getting running config from Switch " + str((IP)))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
        tn.write(b"terminal length 0\n")
	    tn.write(b"show run\n")
	    tn.write(b"exit\n")
        readoutput = tn.read_all()
        saveoutput =  open("switch" + HOST, "w")
        saveoutput.write(readoutput.decode("ascii"))
        saveoutput.write("\n")
	    saveoutput.close
        print(tn.read_all().decode("ascii"))
inventory.close()