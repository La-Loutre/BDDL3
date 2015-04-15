import json
import MySQLdb,MySQLdb.cursors
from passwd import *
import urllib2
import traceback
from loadfile import *

# db=MySQLdb.connect(host="dbserver",
#                    user="ldouriez",
#                    passwd=p,
#                    db="ldouriez"
#                    )

# cur = db.cursor()
# try:
#     cur.execute("CREATE TABLE ok3 (`ok` varchar(50))")
#     cur.execute("INSERT INTO ok3 VALUES('okok')")
#     cur.execute("SELECT * FROM ok3")
#     row=cur.fetchone()
#     print row
# except MySQLdb.Error,e:
#     print(e.args[0],e.args[1])
#     db.rollback()#9738 - 75136


# db.close()
db=MySQLdb.connect(host="localhost",user="louis",passwd=p,db="wowdb")
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
    
    

WOW_API_URL="http://eu.battle.net/api/wow/"
WOW_MEDIUM_IMG_API_URL="http://eu.media.blizzard.com/wow/icons/56/"
WOW_SMALL_IMG_API_URL="http://eu.media.blizzard.com/wow/icons/36/"
LOCALS={"en":"?locale=en_GB","fr":"?locale=fr_FR","None":""}
DEBUG=True
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
        print "INSERT INTO ITEMS VALUES("+str(item["id"])+","+str(item["itemClass"])+","+str(item["itemSubClass"])+",\""+item["name"].encode("utf-8")+"\","+description+","+str(item["itemLevel"])+","+str(keyPicture)+")"
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
    
def getTypes(typeid,subtypeid):
    cursor=MySQLdb.cursors.DictCursor(db)
    cursor.execute("SELECT name FROM ITEMCLASS WHERE id={id}".format(id=typeid))
    typeValue=cursor.fetchone()
    cursor.execute("SELECT * FROM ITEMSUBCLASS WHERE idClass={idClass} AND idSubClass={idSubClass}".format(idClass=typeid,idSubClass=subtypeid))
    subTypeValue=cursor.fetchone()
    cursor.close()
    if subTypeValue["completeName"]!="NULL":
        return typeValue["name"], subTypeValue["completeName"]
    else:
        return typeValue["name"], subTypeValue["name"]

def generatePlayerPage(row,filename):
    colors=["color:#B3B3B3",
            "color:#FFFFFF",
            "color:00FF26",
            "color:0D00FF",
            "color:BC00FF",
            "color:FF9E00",
            "color:FACD86"]
    
    newHtml=open(filename+".html","w")
    cursor=MySQLdb.cursors.DictCursor(db)
    cursorDb2=MySQLdb.cursors.DictCursor(db)
    items=row
    itemsList=[items["backId"],
               items["feetId"],
               items["finger1Id"],
               items["finger2Id"],
               items["chestId"],
               items["handsId"],
               items["legsId"],
               items["mainHandId"],
               items["neckId"],
               items["shoulderId"],
               items["trinket1Id"],
               items["trinket2Id"],
               items["waistId"],
               items["wristId"]]
    newHtml.write("<table style=\"background:#000000\"> "+
                      "<tr> <th style=\"color:#FFFFFF\">Nom</th>\n"+
                      "<th style=\"color:#FFFFFF\"> Image</th></tr>")    
    for i in range(len(itemsList)):
        cursor.execute("SELECT * FROM ITEMS WHERE id={id}".format(id=str(itemsList[i])))
        itemFound=cursor.fetchone()
        cursorDb2.execute("SELECT * FROM ITEMSPICTURES WHERE id="+str(itemFound["picture"]))
        row2=cursorDb2.fetchone()

        nomLien=itemFound["name"].decode(encoding="ascii",errors="ignore")
        nomLien=nomLien.replace(" ","")
        nomLien=nomLien.replace(":","")
        imgLink=WOW_MEDIUM_IMG_API_URL+row2["name"]+".jpg"
        newHtml.write("<tr><td><a style=\"{colorQuality}\" href={nomlien}.html>{nom}</a></td><td><img src={img} ></td><tr>".format(nom=itemFound["name"],nomlien=nomLien,img=imgLink,colorQuality=colors[itemFound["quality"]]))
    newHtml.write("</table>")

def generateItemPage(row,imgName,fileName):
    newHtml=open(fileName+".html","w")

    cursor=MySQLdb.cursors.DictCursor(db)
    cursor.execute("SELECT description FROM ITEMSDESCRIPTIONS WHERE id={idDesc}".format(idDesc=str(row["description"])))
    descriptionValue=cursor.fetchone()["description"]
    print str(row["classid"]) , str(row["subclassid"])
    typeValue,subTypeValue=getTypes(str(row["classid"]),str(row["subclassid"]))
    
    newHtml.write("<p>Nom : {nom} </p><p>Niveau : {niveau}</p><p>Description : {description}</p> <p>Type : {typee}</p><p>Sous-type : {subtype}</p><img src= {imgnom} > <p>".format(nom=row["name"],niveau=row["level"],description=descriptionValue,imgnom=imgName,typee=typeValue,subtype=subTypeValue))
    newHtml.close()
    cursor.close()
def generateWebSite():
    colors=["color:#B3B3B3",
            "color:#FFFFFF",
            "color:00FF26",
            "color:0D00FF",
            "color:BC00FF",
            "color:FF9E00",
            "color:FACD86"]
    cursorDb=MySQLdb.cursors.DictCursor(db)
    cursorDb2=MySQLdb.cursors.DictCursor(db)
    fichierHtml=open("sortie.html","w")
    fichierHtml.write("<table style=\"background:#000000\"> "+
                      "<tr> <th style=\"color:#FFFFFF\">Nom</th>\n"+
                      "<th style=\"color:#FFFFFF\"> Image</th></tr>")
    try:
        cursorDb.execute("SELECT * FROM ITEMS")
        for row in cursorDb:
           
            cursorDb2.execute("SELECT * FROM ITEMSPICTURES WHERE id="+str(row["picture"]))
            row2=cursorDb2.fetchone()
            nomLien=row["name"].decode(encoding="ascii",errors="ignore")
            nomLien=nomLien.replace(" ","")
            nomLien=nomLien.replace(":","")
            print nomLien
            imgLink=WOW_MEDIUM_IMG_API_URL+row2["name"]+".jpg"
            fichierHtml.write("<tr><td><a style=\"{colorQuality}\" href={nomlien}.html>{nom}</a></td><td><img src={img} ></td><tr>".format(nom=row["name"],nomlien=nomLien,img=imgLink,colorQuality=colors[row["quality"]]))
            generateItemPage(row,imgLink,nomLien)
        fichierHtml.write("</table>")
    except:
        print traceback.format_exc()

    try:
        cursorDb.execute("SELECT * FROM PLAYERS")
        for row in cursorDb:
            nomHtml=row["name"].decode(encoding="ascii",errors="ignore")
            nomHtml=nomHtml.replace(" ","")
            nomHtml=nomHtml.replace(":","")
            generatePlayerPage(row,nomHtml)
    except:
        print traceback.format_exc()
    fichierHtml.close()
##generateWebSite()
# info,name,server=getLeader3V3(3)
# cur=db.cursor()
# if(addPlayerToDB(cur,info,name,server)!=None):
#     db.commit()
#     generateWebSite()
