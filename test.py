import json
import MySQLdb,MySQLdb.cursors
from passwd import *
import urllib2
import traceback
from loadfile import *
from globals import *




from websiteGeneration import *

def createTables():
    global db
    cur = db.cursor()
    
    loadfile(cur,"createtables.sql")
    
    fichierItemClass=open("itemClass.txt","r")
    line=fichierItemClass.readline()
    while line != "":
        splitedLine=line.split(",",1)
        line=fichierItemClass.readline()
        print splitedLine[0],splitedLine[1]
        cur.execute("INSERT INTO ITEMCLASS VALUES("+splitedLine[0]+",'"+splitedLine[1].split("\n")[0]+"')")
    fichierItemClass.close()



    fichierItemSubClass=open("itemSubClass.txt","r")
    line=fichierItemSubClass.readline()
    while line != "":
        splitedLine = line.split(",")
        cur.execute("INSERT INTO ITEMSUBCLASS VALUES("+splitedLine[0]+","+splitedLine[1]+",'"+splitedLine[2]+"','"+splitedLine[3].split("\n")[0]+"')")
        line=fichierItemSubClass.readline()

    fichierItemSubClass.close()

    ##Save results 
    db.commit()
    
    


def getDataFromUrl(url,local="fr"):
    global LOCALS
    global DEBUG
    try:
        if DEBUG:
            print url+LOCALS[local]
        jsonFile=urllib2.urlopen(url+LOCALS[local])
        data=json.load(jsonFile)
        return data
    except :
        if DEBUG:
            print traceback.format_exc()
        return None


def getPlayerProfile(serverName,playerName,field=""):
    return getDataFromUrl(WOW_API_URL+"character/"+serverName+"/"+playerName+field,"None")
def getLeader3V3(ranking,moreInfo=True):
    assert(ranking>=1)
    # No trycatch 
    info = getDataFromUrl(WOW_API_URL+"leaderboard/3v3")["rows"][ranking-1]
    if moreInfo:
        return info,info["name"],info["realmName"]

def addItemDescription(curseurDb,item):
    try:
        print "SELECT id FROM ITEMSDESCRIPTIONS WHERE description=\""+item["description"].encode("utf-8")+"\""
        curseurDb.execute("SELECT id FROM ITEMSDESCRIPTIONS WHERE description=\""+item["description"].encode("utf-8")+"\"")
    
        row =curseurDb.fetchone() 
        print row
        if row != None:
            keyDescription=row[0]
            print keyDescription
        else:
            curseurDb.execute("SELECT MAX(id) FROM ITEMSDESCRIPTIONS ")
            row =curseurDb.fetchone()
            if row[0] == None:
                maxIdItemsPicture=0
            else:
                print row
                maxIdItemsPicture=int(row[0])+1
            keyDescription=maxIdItemsPicture
            curseurDb.execute("INSERT INTO ITEMSDESCRIPTIONS VALUES("+str(keyDescription)+",\""+item["description"].encode("utf-8")+"\")")
    except:
        print traceback.format_exc()
        return None
    return keyDescription
    



def addItemPicture(curseurDb,item):
    try:
        print "SELECT id FROM ITEMSPICTURES WHERE name=\""+item["icon"].encode("utf-8")+"\""
        curseurDb.execute("SELECT id FROM ITEMSPICTURES WHERE name=\""+item["icon"].encode("utf-8")+"\"")
    
        row =curseurDb.fetchone() 
        print row
        if row != None:
            keyPicture=row[0]
            print keyPicture
        else:
            curseurDb.execute("SELECT MAX(id) FROM ITEMSPICTURES ")
            row =curseurDb.fetchone()
            if row[0] == None:
                maxIdItemsPicture=0
            else:
                print row
                maxIdItemsPicture=int(row[0])+1
            keyPicture=maxIdItemsPicture
            curseurDb.execute("INSERT INTO ITEMSPICTURES VALUES("+str(keyPicture)+",\""+item["icon"].encode("utf-8")+"\")")
    except:
        print traceback.format_exc()
        return None
    return keyPicture

def addItemsPlayer(curseurDb,items):
    itemsToBeAdded=[items["back"],
                    items["feet"],
                    items["finger1"],
                    items["finger2"],
                    items["chest"],
                    items["hands"],
                    items["legs"],
                    items["mainHand"],
                    items["neck"],
                    items["shoulder"],
                    items["trinket1"],
                    items["trinket2"],
                    items["waist"],
                    items["wrist"]]
    for i in range(len(itemsToBeAdded)):
        item=getItem(itemsToBeAdded[i]["id"])
        addItemToDB(curseurDb,item)
    
def addPlayerToDB(curseurDb,infoPlayer,playerName,serverName):
    itemsProfile=getPlayerProfile(serverName,playerName,"?fields=items")
    try:
        curseurDb.execute("""INSERT INTO PLAYERS VALUES(
                          \"{playerNamee}\",
                          \"{serverNamee}\",
                          {genderId},
                          {factionId},
                          {raceId},
                          {level},
                          \"{thumbnail}\",
                          {backId},
                          {chestId},
                          {feetId},
                          {finger1Id},
                          {finger2Id},
                          {handsId},
                          {legsId},
                          {mainHandId},
                          {neckId},
                          {shoulderId},
                          {trinket1Id},
                          {trinket2Id},
                          {waistId},
                          {wristId})""".format(playerNamee=playerName,
                                               serverNamee=serverName,
                                               genderId=str(infoPlayer["genderId"]),
                                               factionId=str(infoPlayer["factionId"]),
                                               raceId=str(infoPlayer["raceId"]),
                                               level=str(itemsProfile["level"]),
                                               thumbnail=itemsProfile["thumbnail"],
                                               backId=str(itemsProfile["items"]["back"]["id"]),
                                               chestId=str(itemsProfile["items"]["chest"]["id"]),
                                               feetId=str(itemsProfile["items"]["feet"]["id"]),
                                               finger1Id=str(itemsProfile["items"]["finger1"]["id"]),
                                               finger2Id=str(itemsProfile["items"]["finger2"]["id"]),
                                               handsId=str(itemsProfile["items"]["hands"]["id"]),
                                               legsId=str(itemsProfile["items"]["legs"]["id"]),
                                               mainHandId=str(itemsProfile["items"]["mainHand"]["id"]),
                                               neckId=str(itemsProfile["items"]["neck"]["id"]),
                                               shoulderId=str(itemsProfile["items"]["shoulder"]["id"]),
                                               trinket1Id=str(itemsProfile["items"]["trinket1"]["id"]),
                                               trinket2Id=str(itemsProfile["items"]["trinket2"]["id"]),
                                               waistId=str(itemsProfile["items"]["waist"]["id"]),
                                               wristId=str(itemsProfile["items"]["wrist"]["id"])))
        addItemsPlayer(curseurDb,itemsProfile["items"])
        return True
    except :
        print traceback.format_exc()
        print itemsProfile
        return None
    
    
def addItemToDB(curseurDb,item):

    keyPicture=addItemPicture(curseurDb,item)
    if keyPicture == None:
        return None

    
    keyDescription=addItemDescription(curseurDb,item)
    if keyDescription == None:
        return None

    try:        
        curseurDb.execute("INSERT INTO ITEMS VALUES("+str(item["id"])+","+str(item["itemClass"])+","+str(item["itemSubClass"])+",\""+item["name"].encode("utf-8")+"\","+str(keyDescription)+","+str(item["itemLevel"])+","+str(keyPicture)+","+str(item["quality"])+")")

    except:
        print "INSERT INTO ITEMS VALUES("+str(item["id"])+","+str(item["itemClass"])+","+str(item["itemSubClass"])+",\""+item["name"].encode("utf-8")+"\","+str(keyDescription)+","+str(item["itemLevel"])+","+str(keyPicture)+","+str(item["quality"])+")"
        
        print traceback.format_exc()
    

def getItem(i):
    return getDataFromUrl(WOW_API_URL+"item/"+str(i))
        



def testAddPlayer(ranking):
    info,name,server=getLeader3V3(ranking)
    cur=db.cursor()
    if(addPlayerToDB(cur,info,name,server)!=None):
        db.commit()
    cur.close()

def testAddItem(start,end):
    cursorDb=db.cursor()
    for i in range(start,end):
        item=getItem(i)
        if item != None:
            addItemToDB(cursorDb,item)
        db.commit()
    cursorDb.close()
    

##generateWebSite()
# info,name,server=getLeader3V3(3)
# cur=db.cursor()
# if(addPlayerToDB(cur,info,name,server)!=None):

#     db.commit()
#     generateWebSite()
