# Defanging IP Address: Problem Statement
# To convert an IP address to a defanged IP address, we need to replace “.” with “[.]”. During coding interviews, 
# a standard problem for changing an IP address is that you receive a valid IP address, 
# you must return a defanged version of that IP address.

def ip_address(address):
    new_address =""
    split_address = address.split('.')
    Separator = "[.]"
    new_address = Separator.join(split_address)
    return new_address
ipaddress = ip_address("1.1.2.3")
print(ipaddress)
    

