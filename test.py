import json
import MySQLdb
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
        cur.execute("CREATE TABLE ITEMS (`id` MEDIUMINT UNSIGNED NOT NULL,`classid` TINYINT UNSIGNED NOT NULL,`subclassid` TINYINT UNSIGNED NOT NULL,`name` varchar(50),`description` bool,`level` TINYINT UNSIGNED NOT NULL,PRIMARY KEY (id),`picture` MEDIUMINT UNSIGNED ) ")
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
        cur.execute("CREATE TABLE ITEMSPICTURES (`id` MEDIUMINT UNSIGNED NOT NULL,`name` varchar(30) , PRIMARY KEY(id,name))")
    except:
        print traceback.format_exc()

    
    ## Show results
    cur.execute("SELECT * FROM ITEMSUBCLASS")
    row=cur.fetchall()    
    print row


    ##Save results 
    db.commit()
    
    

WOW_API_URL="http://eu.battle.net/api/wow/"
LOCALS={"en":"?locale=en_GB","fr":"?locale=fr_FR"}
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
    return getDataFromUrl(WOW_API_URL+"character/"+serverName+"/"+playerName+field)
def getLeader3V3(ranking,moreInfo=True):
    assert(ranking>=1)
    # No trycatch 
    info = getDataFromUrl(WOW_API_URL+"leaderboard/3v3")["rows"][ranking-1]
    if moreInfo:
        return info,info["name"],info["realmName"]
    
def addItemToDB(database,item):
    curseurDb=database.cursor()
    try:
        print "SELECT id FROM ITEMSPICTURES WHERE name='"+item["icon"].encode("utf-8")+"'"
        curseurDb.execute("SELECT id FROM ITEMSPICTURES WHERE name='"+item["icon"].encode("utf-8")+"'")
    
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
    except:
        print traceback.format_exc()
        return None
    curseurDb.execute("INSERT INTO ITEMSPICTURES VALUES("+str(keyPicture)+",'"+item["icon"].encode("utf-8")+"')")

    
    description="true"
    if item["description"] == "":
        description="false"
    try:
        curseurDb.execute("INSERT INTO ITEMS VALUES("+str(item["id"])+","+str(item["itemClass"])+","+str(item["itemSubClass"])+",'"+item["name"].encode("utf-8")+"',"+description+","+str(item["itemLevel"])+","+str(keyPicture)+")")
    except:
        print traceback.format_exc()
    

def getItem(i):
    return getDataFromUrl(WOW_API_URL+"item/"+str(i))
        






