def ip_address(address):
    new_ip_address = ""
    split_ip_address = address.split(".")
    ip_seperator = "[.]"
    new_ip_address = ip_seperator.join(split_ip_address)
    return new_ip_address


ipAddress = ip_address("123.131.237.101")
print(ipAddress)
