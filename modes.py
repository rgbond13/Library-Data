import json, constants, utilities

def ViewCatalog(catalog, users, holds):
  pass

def SelfCheckout(catalog, users, holds):
  while True:
    userID = input("Please enter your ID (or hit enter to exit): ")
    loginUser = None
    if userID == "":
      break
    for user in users:
      if userID == user.userID:
        loginUser = user
        break
    
    if loginUser == None:
      print("That user does not exist. Please try again.")
      continue
    
    ans = input("Is this your name? \nName: " + loginUser.username + "? ")
    if (ans.lower().startswith("y")):
      pass
    else:
      continue

    while True:
      ans = input("Enter Item Code (or hit enter to exit): ")
      itemToCheckout = None
      if ans == "":
        break
      for item in catalog:
        if (item.code == ans):
          itemToCheckout = item
          break
        
      if itemToCheckout == None:
        print("Invalid Item Code. Try again.")
        continue
      
      print("\nItem Details: \n" + itemToCheckout.toString() + "\n")
      ans = input("Do you want to check out this title? ")
      if ans.lower().startswith("y"):
        if (itemToCheckout.copiesAvailable <= 0):
          ans = input("Title is not available. Place a hold on it? ")
          if (ans.lower().startswith("y")):
            print("Hold placed.")
            print("Holds are not available right now.")
          else:
            print("Hold not placed. Check back later.")
        else:  
          print("Title added to your loans.")
          itemToCheckout.copiesAvailable -= 1
          print("Title is due back in " + str(itemToCheckout.returnTime) + " days.")
          #TODO: Create checkout item object and add it to user's bill.
      else:
        print("Title rejected. Not added to loans.")
      
      print()
    
    catalogdump = utilities.extractDataFromObjects(catalog)
    utilities.dumpFile(catalogdump, "./Data/Catalog.json")

    

def Checkout(catalog, users, holds):
  pass

def ReturnItem(catalog, users, holds):
  while True:
    ans = input("Enter item code to return (or type enter to exit): ")
    if (ans == ""):
      break
    itemToReturn = None
    userWithItem = None
    i = 0
    for user in users:
      i = 0
      for item in user.booksCheckedOut:
        if item.code == ans:
          itemToReturn = item
          break
        i += 1
      if item != None:
        userWithItem = user
        break
    
    itemToReturn.catalogItemPointer.copiesAvailable += 1
    print("One item checked in. Here are the details: \n")
    itemToReturn.toString()
    userWithItem.booksCheckedOut[i] = None
    print()
  
  catalogdump = utilities.extractDataFromObjects(catalog)


def HoldEdit(catalog, users, holds):
  pass

def RenewItems(catalog, users, holds):
  pass

def AddUsers(catalog, users, holds):
  while True:
    ans = input("Would you like to add a new User to the Library? ")
    if ans == "y":
      pass
    else:
      break
    
    username = input("Enter user's name: ")
    email = input("Enter user's email: ")
    dob = input("Enter user's date of birth delimited by commas and separated by spaces: ")
    dob = dob.split(", ")
    hometown = input("Enter user's hometown: ")
    print("Generating User ID. Please wait...")
    userID = utilities.GenerateRandomCode(16)
    print("ID generated. Code is " + userID)
    
    user = constants.User(username, email, int(dob[2]), int(dob[0]), int(dob[1]), hometown, userID)
    users.append(user)
    print("User added to record.")
  
  usersdump = utilities.extractDataFromObjects(users)
  utilities.dumpFile(usersdump, "./Data/UserData.json")

def AddCatalogItem(catalog, users, holds):
  while True:
    ans = input("Would you like to add a new item to the Catalog? ")
    if ans == "y":
      pass
    else:
      break
    
    title = input("Enter item's title: ")
    author = input("Enter item's author: ")
    code = input("Enter item's barcode: ")
    copies = input("Enter amount of copies: ")
    returnTime = input("Enter checkout length: ")
    ageRestriction = input("Enter minimum age to check out: ")

    item = constants.CatalogItem(title, author, code, copies, copies, returnTime, ageRestriction)
    catalog.append(item)
    print("Item added to catalog.")
    
  catalogdump = utilities.extractDataFromObjects(catalog)
  utilities.dumpFile(catalogdump, "./Data/Catalog.json")
