import subprocess

#Renames computer name, host name, and local host name
name = raw_input("What is the computer name: ")
subprocess.call(["sudo", "scutil", "--set", "LocalHostName", name])
subprocess.call(["sudo", "scutil", "--set", "HostName", name])
subprocess.call(["sudo", "scutil", "--set", "ComputerName", name])