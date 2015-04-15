import json
import MySQLdb,MySQLdb.cursors
from passwd import *
import urllib2
import traceback

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
    

    ## Create items table (empty)
    try:
        cur.execute("CREATE TABLE ITEMS (`id` MEDIUMINT UNSIGNED NOT NULL,`classid` TINYINT UNSIGNED NOT NULL,`subclassid` TINYINT UNSIGNED NOT NULL,`name` varchar(100),`description` MEDIUMINT,`level` TINYINT UNSIGNED NOT NULL,PRIMARY KEY (id),`picture` MEDIUMINT UNSIGNED ) ")
    except:
        print traceback.format_exc()
    

    ## Create itemclass table and fill it 
    try:
        cur.execute("CREATE TABLE ITEMCLASS (`id` TINYINT UNSIGNED NOT NULL,`name` varchar(30),PRIMARY KEY(id))")
    except:
        print traceback.format_exc()
       

    fichierItemClass=open("itemClass.txt","r")
    line=fichierItemClass.readline()
    while line != "":
        splitedLine=line.split(",",1)
        line=fichierItemClass.readline()
        print splitedLine[0],splitedLine[1]
        cur.execute("INSERT INTO ITEMCLASS VALUES("+splitedLine[0]+",'"+splitedLine[1].split("\n")[0]+"')")

    fichierItemClass.close()

    ## Create itemsubclass table and fill it
    fichierItemSubClass=open("itemSubClass.txt","r")
    try:
        cur.execute("CREATE TABLE ITEMSUBCLASS (`idClass` TINYINT UNSIGNED NOT NULL,`idSubClass` TINYINT UNSIGNED NOT NULL, `name` varchar(30) ,`completeName` varchar(30),PRIMARY KEY(idClass,idSubClass)) ")
    except:
        print traceback.format_exc()
       
    line=fichierItemSubClass.readline()
    while line != "":
        splitedLine = line.split(",")
        cur.execute("INSERT INTO ITEMSUBCLASS VALUES("+splitedLine[0]+","+splitedLine[1]+",'"+splitedLine[2]+"','"+splitedLine[3].split("\n")[0]+"')")
        line=fichierItemSubClass.readline()

    fichierItemSubClass.close()

    
    ## Create ITEMSPICTURES table (empty)
    try:
        cur.execute("CREATE TABLE ITEMSPICTURES (`id` MEDIUMINT UNSIGNED NOT NULL,`name` varchar(100) , PRIMARY KEY(id,name))")
    except:
        print traceback.format_exc()

    ## Create ITEMSDESCRIPTION table (empty)
    try:
        cur.execute("CREATE TABLE ITEMSDESCRIPTIONS (`id` MEDIUMINT UNSIGNED NOT NULL,`description` varchar(100) , PRIMARY KEY(id,description))")
    except:
        print traceback.format_exc()

    ## Create PLAYERS table (empty)
    try:
        cur.execute("CREATE TABLE PLAYERS (`name` varchar(50),`server` varchar(50),`genderId` TINYINT UNSIGNED, `factionId` TINYINT UNSIGNED,`raceId` TINYINT,`level` TINYINT UNSIGNED,`thumbnail` varchar(100),`backId` MEDIUMINT,`chestID` MEDIUMINT UNSIGNED,`feetId` MEDIUMINT UNSIGNED,`finger1Id` MEDIUMINT UNSIGNED,`finger2Id` MEDIUMINT UNSIGNED,`handsId` MEDIUMINT UNSIGNED,`legsId` MEDIUMINT UNSIGNED,`mainHandId` MEDIUMINT UNSIGNED,`neckId` MEDIUMINT UNSIGNED,`shoulderId` MEDIUMINT UNSIGNED,`trinket1Id` MEDIUMINT UNSIGNED,`trinket2Id` MEDIUMINT UNSIGNED,`waistId` MEDIUMINT UNSIGNED,`wristId` MEDIUMINT UNSIGNED)")
    ## Show results
    except:
        print traceback.format_exc()
    cur.execute("SELECT * FROM ITEMSUBCLASS")
    row=cur.fetchall()    
    print row


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

def addPlayerToDB(curseurDb,infoPlayer,playerName,serverName):
    itemsProfile=getPlayerProfile(serverName,playerName,"?fields=items")
    try:
        curseurDb.execute("INSERT INTO PLAYERS VALUES(\"{playerNamee}\",\"{serverNamee}\",{genderId},{factionId},{raceId},{level},\"{thumbnail}\",{backId},{chestId},{feetId},{finger1Id},{finger2Id},{handsId},{legsId},{mainHandId},{neckId},{shoulderId},{trinket1Id},{trinket2Id},{waistId},{wristId})".format(playerNamee=playerName,serverNamee=serverName,genderId=str(infoPlayer["genderId"]),factionId=str(infoPlayer["factionId"]),raceId=str(infoPlayer["raceId"]),level=str(itemsProfile["level"]),thumbnail=itemsProfile["thumbnail"],backId=str(itemsProfile["items"]["back"]["id"]),chestId=str(itemsProfile["items"]["chest"]["id"]),feetId=str(itemsProfile["items"]["feet"]["id"]),finger1Id=str(itemsProfile["items"]["finger1"]["id"]),finger2Id=str(itemsProfile["items"]["finger2"]["id"]),handsId=str(itemsProfile["items"]["hands"]["id"]),legsId=str(itemsProfile["items"]["legs"]["id"]),mainHandId=str(itemsProfile["items"]["mainHand"]["id"]),neckId=str(itemsProfile["items"]["neck"]["id"]),shoulderId=str(itemsProfile["items"]["shoulder"]["id"]),trinket1Id=str(itemsProfile["items"]["trinket1"]["id"]),trinket2Id=str(itemsProfile["items"]["trinket2"]["id"]),waistId=str(itemsProfile["items"]["waist"]["id"]),wristId=str(itemsProfile["items"]["wrist"]["id"])))
        return True
    except :
        print traceback.format_exc()
        print itemsProfile
        print "INSERT INTO PLAYERS VALUES(\"{playerNamee}\",\"{serverNamee}\",{genderId},{factionId},{raceId},{level},\"{thumbnail}\",{backId},{chestId},{feetId},{finger1Id},{finger2Id},{handsId},{legsId},{mainHandId},{neckId},{shoulderId},{trinket1Id},{trinket2Id},{waistId},{wristId}".format(playerNamee=playerName,serverNamee=serverName,genderId=str(infoPlayer["genderId"]),factionId=str(infoPlayer["factionId"]),raceId=str(infoPlayer["raceId"]),level=str(itemsProfile["level"]),thumbnail=itemsProfile["thumbnail"],backId=str(itemsProfile["items"]["back"]["id"]),chestId=str(itemsProfile["items"]["chest"]["id"]),feetId=str(itemsProfile["items"]["feet"]["id"]),finger1Id=str(itemsProfile["items"]["finger1"]["id"]),finger2Id=str(itemsProfile["items"]["finger2"]["id"]),handsId=str(itemsProfile["items"]["hands"]["id"]),legsId=str(itemsProfile["items"]["legs"]["id"]),mainHandId=str(itemsProfile["items"]["mainHand"]["id"]),neckId=str(itemsProfile["items"]["neck"]["id"]),shoulderId=str(itemsProfile["items"]["shoulder"]["id"]),trinket1Id=str(itemsProfile["items"]["trinket1"]["id"]),trinket2Id=str(itemsProfile["items"]["trinket2"]["id"]),waistId=str(itemsProfile["items"]["waist"]["id"]),wristId=str(itemsProfile["items"]["wrist"]["id"]))
        return None
    
    
def addItemToDB(curseurDb,item):

    keyPicture=addItemPicture(curseurDb,item)
    if keyPicture == None:
        return None

    
    keyDescription=addItemDescription(curseurDb,item)
    if keyDescription == None:
        return None

    try:        
        curseurDb.execute("INSERT INTO ITEMS VALUES("+str(item["id"])+","+str(item["itemClass"])+","+str(item["itemSubClass"])+",\""+item["name"].encode("utf-8")+"\","+str(keyDescription)+","+str(item["itemLevel"])+","+str(keyPicture)+")")

    except:
        print "INSERT INTO ITEMS VALUES("+str(item["id"])+","+str(item["itemClass"])+","+str(item["itemSubClass"])+",\""+item["name"].encode("utf-8")+"\","+description+","+str(item["itemLevel"])+","+str(keyPicture)+")"
        print traceback.format_exc()
    

def getItem(i):
    return getDataFromUrl(WOW_API_URL+"item/"+str(i))
        




def testAddItem(start,end):
    cursorDb=db.cursor()
    for i in range(start,end):
        item=getItem(i)
        if item != None:
            addItemToDB(cursorDb,item)
        db.commit()
    
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
    cursorDb=MySQLdb.cursors.DictCursor(db)
    cursorDb2=MySQLdb.cursors.DictCursor(db)
    fichierHtml=open("sortie.html","w")
    fichierHtml.write("<table> "+
                      "<tr> <th>Nom</th>\n"+
                      "<th>Image</th></tr>")
    try:
        cursorDb.execute("SELECT * FROM ITEMS")
        for row in cursorDb:
           
            cursorDb2.execute("SELECT name FROM ITEMSPICTURES WHERE id="+str(row["picture"]))
            row2=cursorDb2.fetchone()
            nomLien=row["name"].decode(encoding="ascii",errors="ignore")
            nomLien=nomLien.replace(" ","")
            print nomLien
            imgLink=WOW_MEDIUM_IMG_API_URL+row2["name"]+".jpg"
            fichierHtml.write("<tr><td><a href={nomlien}.html>{nom}</a></td><td><img src={img} ></td><tr>".format(nom=row["name"],nomlien=nomLien,img=imgLink))
            generateItemPage(row,imgLink,nomLien)
        fichierHtml.write("</table>")
    except:
        print traceback.format_exc()
    fichierHtml.close()
##generateWebSite()
info,name,server=getLeader3V3(3)
cur=db.cursor()
if(addPlayerToDB(cur,info,name,server)!=None):
    db.commit()
