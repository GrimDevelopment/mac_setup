" MacSetup.py to automate the early setup procedure's for Macs"
#!/usr/local/bin/python
import subprocess

clients_list = []

class Client:
    def __init__(self, name, addigy, munki):
        self.clientname = name
        self.addigy_download = addigy
	self.munki = munki

    def print_obj(self):
        print(self.clientname)
        print(self.addigy_download)
	print(self.munki)

def rename():
    name = raw_input("What is the computer name: ")
    subprocess.call(["sudo", "scutil", "--set", "LocalHostName", name])
    subprocess.call(["sudo", "scutil", "--set", "HostName", name])
    subprocess.call(["sudo", "scutil", "--set", "ComputerName", name])
    return

def add_client(client_list):
    clients = open("clients.txt")
    while True:
	line = str(clients.readline())
	if not line: break
        client_name = line
	line = clients.readline()
        addigy_download = line
        line = clients.readline()
        munki = line
        client_list.append(Client(client_name, addigy_download, munki))
    clients.close()
    return

def install_addigy(clients):
    client_name = str(raw_input("Client name: "))+'\n'
    for x in range(len(clients_list)):
	print (x)
	name = str(clients_list[x].clientname)
        if (client_name == name):
	    print ("installing addigy")
            subprocess.call(str([clients[x].addigy_download]))
            return

def run_munki(clients):
    client = raw_input("Client?: ")+'\n'
    for x in range(len(clients)):
        if (clients[x].clientname == client):
            subprocess.call([clients[x].munki])
            return

def all():
    client = raw_input("Client?: ")
    for x in range(len(clients_list)):
        if clients_list[x].clientname == client:
            rename()
            subprocess.call([clients_list[x].addigy_download])
            subprocess.call([clients_list[x].munki])
            return

def check_clients(client_list):
    for x in range(len(client_list)):
        print(client_list[x].clientname)
    return

def status(client_list):
    for x in range(len(client_list)):
        client_list[x].print_obj()
    return

def main_menu():
    while True:
        x = raw_input("1 to rename, 2 to install addigy, 3 to run munki, 4 for all three, 5 to check client list: ")

        if x == "1":
            rename()
        if x == "2":
            install_addigy(clients_list)
        if x == "3":
            run_munki(clients_list)
        if x == "4":
            all()
        if x == "5":
            check_clients(clients_list)
	if x == "18405087":
            status(clients_list)
        else:
            print("Not valid input\n")

def main():
    add_client(clients_list)
    main_menu()

if __name__ == "__main__":
    main()