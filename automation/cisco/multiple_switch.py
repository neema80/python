#!/usr/bin/env python
# in this file we are going to connect to multiple switch at the same time and
# configure vlans on them
import getpass
import telnetlib
# as long as the username and password for all the devices are the same
# we put the prompts at the beginning of the file
user = input("Enter your telnet username: ")
password = getpass.getpass()

inventory = open("inventory.txt")
for IP in inventory:
    IP = IP.strip() # to remove any additional spaces if there are any
    print("Configuring Switch " + str((IP)))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
        # to make things simpler we can give our user privilege level 15
        # so we can get rid of the line 24 and 25
        tn.write(b"enable\n")
        tn.write(b"cisco\n") # this is our enable password
        tn.write(b"conf t\n")
        for vlans in range(2,10):
            tn.write(b"vlan " + str(vlans).encode("ascii") + b"\n")
            tn.write(b"name Python_VLAN_" + str(vlans).encode("ascii") + b"\n")
        tn.write(b"end\n")
        tn.write(b"exit\n")
        print(tn.read_all().decode("ascii"))
inventory.close()


