#!/usr/bin/env python
# useful link https://docs.python.org/3/library/telnetlib.html
import getpass
# import sys
import telnetlib
""" This is to create loopback on the
Router we provide ip address to it
and Run OSPF 1 instance
"""
# hostname is the ip address of the device
HOST = input("Enter your hostname ip address: ")
# stores the username
user = input("Enter your telnet username: ")
# stores the password of the device
password = getpass.getpass()
# this module connects us to the devices thorough telnet
tn = telnetlib.Telnet(HOST)

# this waits until sees the Username prompt on the device
# then passed our username to the device
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
# this checks if the password is provided then runs the
# steps below
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n") # this is our enable password
    tn.write(b"conf t\n")
    tn.write(b"int loop 0\n")
    tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
    tn.write(b"int loop 1\n")
    tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
    tn.write(b"router ospf 1\n")
    tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
# this is simple print statement to show us the output
# of the script on the screen
print(tn.read_all().decode("ascii"))