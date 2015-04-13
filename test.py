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
        print traceback.format_exc()
        return None

def getLeader3V3(ranking):
    assert(ranking>=1)
    return getDataFromUrl("http://eu.battle.net/api/wow/leaderboard/3v3?locale=fr_FR")["rows"][ranking-1]
    


def getItem(i):
    return getDataFromUrl("http://eu.battle.net/api/wow/item/"+str(i))
        





