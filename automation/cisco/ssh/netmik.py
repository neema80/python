#!/usr/bin/env python
# multiple vlans for a switch using netmiko and SSH
from netmiko import ConnectHandler

iosv_l2 = {
    "device_type": "cisco_ios",
    "ip": "10.10.10.10",
    "username": "david",
    "password": "cisco",
    "port": "22",
    "secret": "cisco", # the password itself
    "verbose": False,
}

net_connect = ConnectHandler(**iosv_l2)
#net_connect.find_prompt()
output = net_connect.send_command("show ip int brief")
print(output)

config_commands = ["int loop 0", "ip address 1.1.1.1 255.255.255.0"]
output = net_connect.send_config_set(config_commands)
print(output)

for vlan in range (2,11):
    print("Creating VLAN " + str(vlan))
    config_commands = ["vlan " + str(vlan), "name Python_VLAN_" + str(vlan)]
    output = net_connect.send_config_set(config_commands)
    print(output) 