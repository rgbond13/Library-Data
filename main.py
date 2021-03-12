import getpass, json, os, constants, utilities

def InvokeCommand(command, commandset):
  commandToInvoke = commandset.get(command, "Invalid Key/Pair")
  if commandToInvoke == "Invalid Key/Pair":
    return
  commandToInvoke(catalog, usersDataList, holds)
  return



print("Welcome to the RSC Games Library! Here you may rent anything from books to CDs to balloon pumps!")
usersDataList = []
catalog = []
holds = []

try:
  usersDataList = json.load(open("./Data/UserData.json", "r"))
  catalog = json.load(open("./Data/Catalog.json", "r"))
  holds = json.load(open("./Data/Holds.json", "r"))
except FileNotFoundError:
  print("It seems you have not used this program yet. Creating base configuration files...")
  utilities.create("./Data/UserData.json")
  utilities.create("./Data/Catalog.json")
  utilities.create("./Data/Holds.json")
  print("Done!")

catalog = utilities.extractBooksFromDict(catalog)
usersDataList = utilities.extractUsersFromDict(usersDataList)

while True:
  usermode = input("What mode will this be used in? (view catalog, self checkout, checkout, return, holds, renew, add users, add catalog items) \n> ")
  InvokeCommand(usermode, constants.modeCommandSet)