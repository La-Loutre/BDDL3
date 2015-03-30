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

def getLeader3V3(ranking):
    try:
        fichier=urllib2.urlopen("http://eu.battle.net/api/wow/leaderboard/3v3")
        data=json.load(fichier)
        try:
            print "Rank = "+str(ranking)
            print "Name = "+str(data["rows"][ranking]["name"])
            print "Servername ="+str(data["rows"][ranking]["realmName"])
        except :
            print "Erreur json parsing"
    except :
        print "Impossible de retrouver la liste"


def getItem(i):

    try:
        fichier=urllib2.urlopen("http://us.battle.net/api/wow/item/"+str(i))
        data=json.load(fichier)
        print "ID ="+str(data["id"])
        print "Buyprice ="+str(data["buyPrice"])
        print "\n"
    except :
        print "404 id ="+str(i)+"\n"
        





