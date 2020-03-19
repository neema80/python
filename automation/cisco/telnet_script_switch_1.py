# useful link https://docs.python.org/3/library/telnetlib.html
import getpass
import telnetlib
""" This is to create vlans on the
Switch we provide ip address to it
Using for loop to decrease code
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
#!/usr/bin/env python
# then passed our username to the device
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
# this checks if the password is provided then runs the
# steps below
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n") # this is our enable password
    tn.write(b"conf t\n")
    # this loops makes our code smaller and more efficient hence lesser chance of bugs
    for vlans in range(2,10):
        tn.write(b"vlan " + str(vlans).encode('ascii') + b"\n")
        tn.write(b"name Python_VLAN_" + str(vlans).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
# this is simple print statement to show us the output
# of the script on the screen
print(tn.read_all().decode('ascii'))