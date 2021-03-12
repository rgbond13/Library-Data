import modes, datetime

modeCommandSet = {
  "view catalog": modes.ViewCatalog,
  "self checkout": modes.SelfCheckout,
  "checkout": modes.Checkout,
  "return": modes.ReturnItem,
  "holds": modes.HoldEdit,
  "renew": modes.RenewItems,
  "add users": modes.AddUsers,
  "add catalog items": modes.AddCatalogItem
}

def extractDataFromObjects(listDat):
  i = 0
  for entry in listDat:
    data = entry.dumpToDict()
    listDat[i] = data
    i += 1
  return listDat

class User():
  username = ""
  email = ""
  dateofbirth = datetime.datetime(1, 1, 1)
  hometown = ""
  userID = ""
  booksCheckedOut = []

  def __init__(self, username, email, year, month, day, hometown, userID):
    self.username = username
    self.email = email
    self.dateofbirth = datetime.datetime(year, month, day)
    self.hometown = hometown
    self.userID = userID

  def getID(self):
    return self.userID

  def dumpToDict(self):
    self.booksCheckedOut = extractDataFromObjects(self.bookCheckedOut)
    dob = str(self.dateofbirth.year) + ", " + str(self.dateofbirth.month) + ", " + str(self.dateofbirth.day)
    retDict = {"username": self.username, "email": self.email, "dateofbirth": dob, "hometown": self.hometown, "userID": self.userID, "booksOut": self.booksCheckedOut}
    return retDict

class CatalogItem():
  title = ""
  author = ""
  code = ""
  copies = 0
  copiesAvailable = 0
  returnTime = 1
  agerestricted = 0

  def __init__(self, title, author, code, copies, copiesAvailable, returnTime, agerestriction):
    self.title = title
    self.author = author
    self.code = code
    self.copies = int(copies)
    self.copiesAvailable = int(copiesAvailable)
    self.returnTime = int(returnTime)
    self.agerestricted = int(agerestriction)

  def dumpToDict(self):
    retDict = {"title": self.title, "author": self.author, "code": self.code, "copies": self.copies, "copiesAvailable": self.copiesAvailable, "returntime": self.returnTime, "agerestricted": self.agerestricted}
    return retDict

  def toString(self):
    return "Title: " + self.title + "\nAuthor: " + self.author + "\nCode: " + self.code + "\nCopies: " + str(self.copies) + "\nCopies Available: " + str(self.copiesAvailable) + "\nAge Restricted: " + str(self.agerestricted) + " years or older \nReturn Time: " + str(self.returnTime) + " days"

class CheckedOutBook(CatalogItem):
  returnday = datetime.datetime(1, 1, 1, 23, 59, 59)
  catalogItemPointer = None

  def __init__(self, returnday, pointer):
    self.returnday = returnday
    self.catalogItemPointer = pointer

  def dumpToDict(self):
    retday = self.returnday.year + ", " + self.returnday.month + ", " + self.returnday.day + ", " + self.returnday.hour + ", " + self.returnday.minute + ", " + self.returnday.second
    retDict = {"title": self.title, "author": self.author, "code": self.code, "copies": self.copies, "copiesAvailable": self.copiesAvailable, "returntime": self.returnTime, "agerestricted": self.agerestricted, "returndate: ": retday, "catalogItemPointer": self.catalogItemPointer.title}
    return retDict