import ipaddress
ip=input("Enter Ip address: ")

try:
    ipaddress.ip_address(ip)
    print("Valid IP")
except ValueError:
    print("Invalid IP")
