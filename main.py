def main():
    from requests import get
    from time import sleep
    from os import name, system
    from re import match
    import sys

    def ipinfo(local): #define printing out ip info
        if len(request) == 1: #if length returned is 1
           print("Lookup failed.")
        else:
            if local:
                print("Displaying your ip info...")
            if not local:
                print("Displaying ip info...")
            print("Success!\n")
            print("IP: " + request["query"])
            print("Country: " + request["country"])
            print("Region: " + request["regionName"])
            print("City: " + request["city"])
            print("ISP: " + request["isp"])
            print("Organization: " + request["org"])
            print("VPN: " + str(request["proxy"]) + "\n") #prints proxy as a string to stop crashing

    ipv4 = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$" #simple regex for an ipv4 address
    print('Type "help" for a list of commands')
    while True:
        command = input("IP Lookup: ")
        if command == "help":
            print('\n"exit" - Exit the application')
            print('"myip" - See your own ip info')
            print('"clear" - Clear the window\n')
        elif command == "clear":
            if name == "nt": #if on windows
                system("cls")
            else: #if on anything but windows
                system("clear")
        elif command == "exit":
            print("Exiting...")
            sleep(1)
            sys.exit()
        elif command == "myip":
            request = get("http://ip-api.com/json/?fields=140825").json() #requests with no input (defaults to your ip)
            ipinfo(True) #print ip info
        elif not match(ipv4, command): #if ipv4 regex doesn't match input
            print("Error: Invalid IP")
        else:
            request = get(f"http://ip-api.com/json/{command}?fields=140825").json() #requests with your input
            ipinfo(False) #print ip info

if __name__ == '__main__':
    main()
