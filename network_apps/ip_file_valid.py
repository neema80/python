import os.path
import sys

# checking IP address file content and validity
def ip_file_valid():
    
    # Prompting user for input
    ip_file = input("\n# Enter IP file path and name (e.g. D:\\folder\\myfile.txt): ")

    # Checking if the file exists
    if os.path.isfile(ip_file) == True:
        print("\n* IP file is valid :)\n")
    else:
        print("\n* File {} does not exist :( please check and try again.\n".format(ip_file))
        sys.exit()
    
    # Open user selected file for reading (IP Addresses file)
    selected_ip_file = open(ip_file,'r')
    # Starting from the beginning
    selected_ip_file.seek(0)
    # Reading each line (IP address) in file
    ip_list = selected_ip_file.readlines()
    # closing the file
    selected_ip_file.close()
    # with open(ip_file,"r") as f:
    #     f.seek(0)
    #     ip_list = f.readlines()
    return ip_list