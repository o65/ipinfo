def main():
    from requests import get
    from time import sleep
    from os import name, system
    from re import match

    def ipinfo(): #define printing out ip info
        if len(r) == 1: #if length returned is 1
           print("Lookup failed.")
        else:
            print("Displaying your ip info...")
            print("Success!\n")
            print("IP: " + r["query"])
            print("Country: " + r["country"])
            print("Region: " + r["regionName"])
            print("City: " + r["city"])
            print("ISP: " + r["isp"])
            print("Organization: " + r["org"])
            print("VPN: " + str(r["proxy"]) + "\n") #prints proxy as a string to stop crashing

    ipv4 = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$" #simple regex for an ipv4 address
    print('Type "help" for a list of commands')
    while True:
        a = input("IP Lookup: ")
        if a == "help":
            print('\n"exit" - Exit the application')
            print('"myip" - See your own ip info')
            print('"clear" - Clear the window\n')
        elif a == "clear":
            if name == "nt": #if on windows
                system("cls")
            else: #if on anything but windows
                system("clear")
            print('Type "help" for a list of commands')
        elif a == "exit":
            print("Exiting...")
            sleep(1)
            exit()
        elif a == "myip":
            r = get("http://ip-api.com/json/?fields=140825").json() #requests with no input (defaults to your ip)
            ipinfo() #print ip info
        elif not match(ipv4, a): #if ipv4 regex doesn't match input
            print("Error: Invalid IP")
        else:
            r = get(f"http://ip-api.com/json/{a}?fields=140825").json() #requests with your input
            ipinfo() #print ip info

if __name__ == '__main__':
    main()
