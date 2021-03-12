import random, json, constants

def create(path):
  file = open(path, "x")
  file.write("This is a new configuration file.")
  file.close()

def GenerateRandomCode(length):
  randCode = ""
  for i in range(0, length):
    num = random.randint(0, 9)
    randCode = randCode + str(num)
  return randCode

def extractDataFromObjects(listToDisect):
  listDat = listToDisect.copy()
  i = 0
  for entry in listDat:
    data = entry.dumpToDict()
    listDat[i] = data
    i += 1
  return listDat

def extractBooksFromDict(catalogList):
  i = 0
  for item in catalogList:
    obj = constants.CatalogItem(item.get("title"), item.get("author"), item.get("code"), item.get("copies"), item.get("copiesAvailable"), item.get("returntime"), item.get("agerestricted"))
    catalogList[i] = obj
    i += 1
  return catalogList

def extractUsersFromDict(usersList):
  i = 0
  for item in usersList:
    dob = item.get("dateofbirth").split(", ")
    obj = constants.User(item.get("username"), item.get("email"), int(dob[0]), int(dob[1]), int(dob[2]), item.get("hometown"), item.get("userID"))
    usersList[i] = obj
    i += 1
  return usersList

def dumpFile(dictToDump, fileName):
  file = open(fileName, "w+")
  #dumped = False
  #while (dumped == False or not dictToDump == json.load(file)):
  json.dump(dictToDump, file)
    #dumped = True
  file.close()