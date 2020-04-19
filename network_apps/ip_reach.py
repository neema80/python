import sys
import subprocess

#Checking IP reachability
def ip_reach(list):

    for ip in list:
        ip = ip.rstrip("\n")
        # ping /n 2 means to sent two packets
        # the stdout and stderr is used to suppress any messages that system gives us and make the output clean
        # ip, is a tuple
        ping_reply = subprocess.call('ping %s -n 2' % (ip,), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # if the type is 0 means we have the reply from the ip address
        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue
        
        else:
            print('\n* {} not reachable :( Check connectivity and try again.'.format(ip))
            sys.exit()