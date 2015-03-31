import json
import MySQLdb
from passwd import *
import urllib2

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

def getDataFromUrl(url):
    try:
        jsonFile=urllib2.urlopen(url)
        data=json.load(jsonFile)
        return data
    except :
        return None

def getLeader3V3(ranking):
    assert(ranking>=1)
    return getDataFromUrl("http://eu.battle.net/api/wow/leaderboard/3v3")["rows"][ranking-1]
    


def getItem(i):
    return getDataFromUrl("http://us.battle.net/api/wow/item/"+str(i))
        





