import subprocess

#Opens computer name text ile
comp = open("comp_names.txt")

#Gathers current computer name
current_name = subprocess.call(["scutil", "--get", "computerName"])

#Finds current computer name in text file and compares to current computer name
for x in range(len(clients_list)):
    line = str(clients.readline())
    if not line: break


    #Renames computer name, host name, and local host name
    subprocess.call(["sudo", "scutil", "--set", "LocalHostName", name])
    subprocess.call(["sudo", "scutil", "--set", "HostName", name])
    subprocess.call(["sudo", "scutil", "--set", "ComputerName", name])