import json
import MySQLdb,MySQLdb.cursors
from passwd import *
import urllib2
from httplib2 import iri2uri
import traceback
from loadfile import *
from globals import *
import os



from websiteGeneration import *


def bonusStats(filename="bonusStats.txt"):
    database=db
    cur = database.cursor()
    fichier=open(filename,"r")
    line=fichier.readline()
    while line != "":
        splited1=line.split(":")
        idStat=splited1[0]
        name=splited1[1].split(",")[0]
        if DEBUG:
            print idStat,name
            print "INSERT INTO BONUSSTATS VALUES({id},\"{description}\")".format(id=idStat,description=name)
        cur.execute("INSERT INTO BONUSSTATS VALUES({id},{description})".format(id=idStat,description=name))
        line=fichier.readline()
    cur.close()
    database.commit()
    

def createTables():
    global db
    cur = db.cursor()
    
    ##loadfile(cur,"createtables.sql")
   ## cur.execute("source createtables.sql")
    fichierItemClass=open("itemClass.txt","r")
    line=fichierItemClass.readline()
    while line != "":
        splitedLine=line.split(",",1)
       
       ## print splitedLine[0],splitedLine[1]
        cur.execute("INSERT INTO ITEMCLASS VALUES("+splitedLine[0]+",'"+splitedLine[1].split("\n")[0]+"')")
        line=fichierItemClass.readline()
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
    
    

def saveData(data,filename):
    filename.write(data)
def getDataFromUrl(url,local="fr"):
    global LOCALS
    global DEBUG
    url = iri2uri(url)
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
    if not os.path.exists("players"):
        os.makedirs("players")
    try:
        testfile=open("players/leaderboard3V3.json","r")
        info=json.load(testfile)
        info=info["rows"][ranking-1]
        testfile.close()
    except:
        if DEBUG :
            print traceback.format_exc()
        raw = getDataFromUrl(WOW_API_URL+"leaderboard/3v3")
        info=raw["rows"][ranking-1]
        testfile=open("players/leaderboard3V3.json","w")
        json.dump(raw,testfile)
        testfile.close()
    if moreInfo:
        return info,info["name"],info["realmName"]
    else:
        return info

def addItemDescription(database,item):
    curseurDb=database.cursor()
    try:
        if DEBUG:
            print "SELECT id FROM ITEMSDESCRIPTIONS WHERE description=\""+item["description"].encode("utf-8")+"\""
        curseurDb.execute("SELECT id FROM ITEMSDESCRIPTIONS WHERE description=\""+item["description"].encode("utf-8")+"\"")
    
        row =curseurDb.fetchone() 
        if DEBUG:
            print row
        if row != None:
            keyDescription=row[0]
            if DEBUG:
                print keyDescription
        else:
            curseurDb.execute("SELECT MAX(id) FROM ITEMSDESCRIPTIONS ")
            row =curseurDb.fetchone()
            if row[0] == None:
                maxIdItemsPicture=1
            else:
                if DEBUG:
                    print row
                maxIdItemsPicture=int(row[0])+1
            keyDescription=maxIdItemsPicture
            curseurDb.execute("INSERT INTO ITEMSDESCRIPTIONS VALUES(NULL,\""+item["description"].encode("utf-8")+"\")")
            database.commit()
    except:
        print traceback.format_exc()
        return None
    return keyDescription
    



def addItemPicture(database,item):
    curseurDb=database.cursor()
    try:
        if DEBUG:
            print "SELECT id FROM ITEMSPICTURES WHERE name=\""+item["icon"].encode("utf-8")+"\""
        curseurDb.execute("SELECT id FROM ITEMSPICTURES WHERE name=\""+item["icon"].encode("utf-8")+"\"")
    
        row =curseurDb.fetchone() 
        if DEBUG:
            print row
        if row != None:
            keyPicture=row[0]
            if DEBUG:
                print keyPicture
        else:
            curseurDb.execute("SELECT MAX(id) FROM ITEMSPICTURES ")
            row =curseurDb.fetchone()
            if row[0] == None:
                maxIdItemsPicture=1
            else:
                if DEBUG:
                    print row
                maxIdItemsPicture=int(row[0])+1
            keyPicture=maxIdItemsPicture
            if DEBUG :
                print "INSERT INTO ITEMSPICTURES VALUES(NULL,\""+item["icon"].encode("utf-8")+"\")"
            curseurDb.execute("INSERT INTO ITEMSPICTURES VALUES(NULL,\""+item["icon"].encode("utf-8")+"\")")
            database.commit()
           
    except:
        print traceback.format_exc()
        return None
    return keyPicture

def addItemsPlayer(database,items):
    curseurDb=database.cursor()
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
        addItemToDB(database,item)
    
def addPlayerToDB(database,infoPlayer,playerName,serverName):
    curseurDb=database.cursor()
    itemsProfile=getPlayerProfile(serverName,playerName,"?fields=items")
    try:
        addItemsPlayer(database,itemsProfile["items"])
        curseurDb.execute("""INSERT INTO PLAYERS VALUES(NULL,
                          \"{playerNamee}\",
                          {serverId},
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
                          {wristId})""".format(playerNamee=playerName.encode("utf-8"),
                                               serverId=str(addServerToDB(database,getServer(serverName))),
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
        database.commit()
      
        return True
    except :
        print traceback.format_exc()
      ##  print itemsProfile
        return None
    
    
def addItemWeapon(database,item):
    curseurDb=database.cursor()
    weaponInfo=item["weaponInfo"]
    try:
        curseurDb.execute("""INSERT INTO WEAPON VALUES(
                         {id},
                         {dmgMax},
                         {dmgMin},
                         {dps},
                         {weaponspeed})
                          """.format(id=item["id"],
                                     dmgMax=weaponInfo["damage"]["max"],
                                     dmgMin=weaponInfo["damage"]["min"],
                                     dps=int(weaponInfo["dps"]),
                                     weaponspeed=weaponInfo["weaponSpeed"]))
        database.commit()
    except:
        print traceback.format_exc()

def getStatFromId(database,stat):
    curseurDb=database.cursor()
    curseurDb.execute("SELECT * FROM BONUSSTATS WHERE id={id}".format(id=stat))
    row=curseurDb.fetchone()
    if row == None:
        return None
    else :
        return row[0]

def addItemToDB(database,item):
    curseurDb=database.cursor()
    keyPicture=addItemPicture(database,item)
    if keyPicture == None:
        return None
    if DEBUG :
        print "KEYPICTURE : "+str(keyPicture)
    
    keyDescription=addItemDescription(database,item)
    if keyDescription == None:
        return None
    
    

    try:        

        curseurDb.execute("INSERT INTO ITEMS VALUES("+str(item["id"])+","+str(item["itemClass"])+","+str(item["itemSubClass"])+",\""+item["name"].encode("utf-8")+"\","+str(keyDescription)+","+str(item["itemLevel"])+","+str(keyPicture)+","+str(item["quality"])+")")
        
        cursorDb2=MySQLdb.cursors.DictCursor(database)
        cursorDb2.execute("SELECT * FROM ITEMCLASS WHERE id={idItem}".format(idItem=str(item["itemClass"]))) 
        row = cursorDb2.fetchone()
        if row["name"] == "Weapon":
            addItemWeapon(database,item)


            
            
        bonusStats=item["bonusStats"]
        nbStat=len(bonusStats)
        if len(bonusStats) > 0 :
            for i in range(len(bonusStats)):
                stat=bonusStats[i]
                if  getStatFromId(database,stat["stat"]) != None :
                    if DEBUG:
                        print "ADDITEMSTAT"
                    cursorDb2.execute("""INSERT INTO ITEMSTAT VALUES(
                                 {id},
                                 {statid},
                                 {amount})
                              """.format(id=item["id"],
                                         statid=stat["stat"],
                                         amount=stat["amount"]))
                    database.commit()
        cursorDb2.close()

        

    except:
        print "INSERT INTO ITEMS VALUES("+str(item["id"])+","+str(item["itemClass"])+","+str(item["itemSubClass"])+",\""+item["name"].encode("utf-8")+"\","+str(keyDescription)+","+str(item["itemLevel"])+","+str(keyPicture)+","+str(item["quality"])+")"
        
        print traceback.format_exc()
    
def getIdLangueFromDB(database,langue):
    curseurDb=MySQLdb.cursors.DictCursor(database)
    curseurDb.execute("SELECT * FROM LANGUES WHERE langue=\"{langueName}\"".format(langueName=langue))
    row = curseurDb.fetchone()
    curseurDb.close()
    return row["id"]

def getIdServerTypeFromDB(database,serverType):
    curseurDb=MySQLdb.cursors.DictCursor(database)
    if DEBUG :
        print "SELECT * FROM SERVEURTYPE WHERE type=\"{servertype}\"".format(servertype=serverType)
    curseurDb.execute("SELECT * FROM SERVEURTYPE WHERE type=\"{servertype}\"".format(servertype=serverType))

    row = curseurDb.fetchone()
    print row
    curseurDb.close()
    return row["id"]

def addServerToDB(database,server):
    curseurDb=MySQLdb.cursors.DictCursor(database)
    
    try:

        curseurDb.execute("SELECT * FROM SERVEURS WHERE name=\"{serverName}\"".format(serverName=server["name"].encode("utf-8")))
        row =curseurDb.fetchone() 
        if DEBUG:
            print row
        if row != None:
            keyId=row["id"]
            if DEBUG:
                print keyId
        else:
            curseurDb.execute("SELECT MAX(id) FROM SERVEURS ")
            row =curseurDb.fetchone()
            if row["MAX(id)"] == None:
                maxIdItemsPicture=1
            else:
                if DEBUG:
                    print row
                maxIdItemsPicture=int(row[0])+1
            keyId=maxIdItemsPicture
            curseurDb.execute("""INSERT INTO SERVEURS VALUES(NULL,
                                                                     \"{serverName}\",
                                                                     {idLangue},
                                                                     {idType})
                                                                      """.format(serverName=server["name"].encode("utf-8"),
                                                                                 idLangue=getIdLangueFromDB(database,server["locale"]),
                                                                                 idType=getIdServerTypeFromDB(database,server["type"])
                                                                                 ))
            database.commit()
    except:
        print traceback.format_exc()
        return None
    return keyId
    
def getServer(serverName):
    if not os.path.exists("servers"):
        os.makedirs("servers")
    try:
        testfile=open("servers/servers.json","r")
        raw=json.load(testfile)
        testfile.close()
        
    except:
        raw=getDataFromUrl(WOW_API_URL+"realm/status")
        if raw != None:
            testfile=open("servers/servers.json","w")
            json.dump(raw,testfile)
            testfile.close()
        else:
            return None

    server=raw["realms"]
    for i in range(len(server)):
        if server[i]["name"] == serverName:
            return server[i]

    return None

def getItem(i):
    if not os.path.exists("items"):
        os.makedirs("items")
    try:
        testfile=open("items/item."+str(i)+".json","r")
        if DEBUG:
            print "items/item."+str(i)+".json"
        if testfile.readline() == "404":
            testfile.close()
            return None
        else:
            testfile.seek(0)
            return json.load(testfile)
    except:
        data= getDataFromUrl(WOW_API_URL+"item/"+str(i))
        savefile=open("items/item."+str(i)+".json","w")
        if data != None:
            json.dump(data,savefile)
            
        else:
            savefile.write("404")
        savefile.close()
        return data
        



def testAddPlayer(ranking):
    info,name,server=getLeader3V3(ranking)
    if(addPlayerToDB(db,info,name,server)!=None):
        db.commit()


def testAddItem(start,end):

    for i in range(start,end):
        item=getItem(i)
        if item != None:
            addItemToDB(db,item)
        if float(i-start)*float(1000)/float(end-start) %10 == 0:
            print str(float(i-start)*float(100)/float(end-start)) +" %"
        db.commit()

    

##generateWebSite()
# info,name,server=getLeader3V3(3)
# cur=db.cursor()
# if(addPlayerToDB(cur,info,name,server)!=None):

#     db.commit()
#     generateWebSite()
