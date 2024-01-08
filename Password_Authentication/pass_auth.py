import getpass

database = {
    "Tanay Dwivedi": "837219",
    "Anurag Singh": "604831",
    "Shrey Srivastava": "195024",
    "Rohan Sharma": "763508",
    "Sarthak Mishra": "321975",
    "Priyansh Rastogi": "489623",
}

username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break

print("Verified")
