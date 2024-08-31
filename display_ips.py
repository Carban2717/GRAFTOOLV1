# import time

while True:
    try:
        with open('/data/data/com.termux/files/home/ip_addresses.txt', 'r') as f:
            ip_addresses = f.readlines()
        print("Logged IP Addresses:")
        for ip in ip_addresses:
            print(ip.strip())
    except FileNotFoundError:
        print("No IP address file found.")
    time.sleep(10) 
