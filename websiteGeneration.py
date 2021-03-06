# -*- coding:utf-8 -*-

import traceback
import json
import os 
import MySQLdb,MySQLdb.cursors
from httplib2 import iri2uri
from globals import *


COLORS={"gris":"color:#B3B3B3", 
        "blanc":"color:#FFFFFF",
        "noir":"color:000000",
        "vert":"color:00FF26", 
        "bleu":"color:0D00FF",
        "violet":"color:BC00FF",
        "orange":"color:FF9E00",
        "beige":"color:FACD86",
        "rouge":"color:#FF0000"
}
FRONT_PAGE_NAME="website/index.html"
PLAYERS_PAGE_NAME="players.html"
ITEMS_PAGE_NAME="items.html"
def generateFrontPage():
    if not os.path.exists("website"):
        os.makedirs("website")
    newHtml=open(FRONT_PAGE_NAME,"w")
    playersPage=generatePlayersPage()
    itemsPage=generateItemsPage()
    newHtml.write("""<p>
                        <a href=\"{playersPageTxt}\" >Players</a>
                     <p>
                     <p>
                        <a href=\"{itemsPageTxt}\" >Items</a>
                     <p>""".format( playersPageTxt=playersPage,
                                    itemsPageTxt=itemsPage))
    newHtml.close()
def generatePlayersPage():
    global db
    cursorDb=MySQLdb.cursors.DictCursor(db)
    cursorDb2=MySQLdb.cursors.DictCursor(db)
    newHtml=open("website/"+PLAYERS_PAGE_NAME,"w")
    newHtml.write("""<head><meta charset="utf-8"/></head>""")
    newHtml.write("""<table border=\"1\" style=\"background:#000000\"> 
                           <tr> 
                               <th style=\"color:#FFFFFF\"> 
                                     Nom
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Image
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Serveur
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Race
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Faction
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Classe
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Niveau
                               </th>

                           
                           </tr>""")    
    try:
        cursorDb.execute("SELECT * FROM PLAYERS")
        for row in cursorDb:
            ##Fetch serverName
            cursorDb2.execute("SELECT name FROM SERVEURS WHERE id={id}".format(id=row["serverId"]))
            serverName=(cursorDb2.fetchone())["name"]

            ##Fetch race name
            cursorDb2.execute("SELECT name FROM RACES WHERE id={id}".format(id=row["raceId"]))
            raceName=(cursorDb2.fetchone())["name"]

            ##Fetch Faction name
            cursorDb2.execute("SELECT name FROM FACTION WHERE id={id}".format(id=row["factionId"]))
            factionName=(cursorDb2.fetchone())["name"]

            ##Fetch class name
            cursorDb2.execute("SELECT name FROM CLASSES WHERE id={id}".format(id=row["classId"]))
            className=(cursorDb2.fetchone())["name"]


            nomHtml=iri2uri(row["name"])
            nomHtml=nomHtml.replace(" ","")
            nomHtml=nomHtml.replace(":","")
            newHtml.write(""" <tr> 
                                  <td>
                                    <a href=\"{url}\" style=\"{color}\" >{playerName} </a>
                                  </td>
                                  <td>
                                    <img src=\"{playerIconUrl}\" />
                                  </td>
                                  <td>
                                    <p style=\"{color}\" >{servername}   </p>
                                   </td>   
                                   <td>
                                    <p style=\"{color}\" >{racename}   </p>
                                   </td>     
                                   <td>
                                    <p style=\"{color}\" >{factionname}   </p>
                                   </td>     
                                   <td>
                                    <p style=\"{color}\" >{classname}   </p>
                                   </td>     
                                   <td>
                                    <p style=\"{color}\" >{level}   </p>
                                   </td>     
                                                                      
                                  
                              </tr>
                          """.format(url=nomHtml+".html",
                                     color=COLORS["blanc"],
                                     playerName=row["name"],
                                     playerIconUrl=WOW_PLAYER_MEDIUM_IMG_API_URL+row["thumbnail"],
                                     servername=serverName,
                                     racename=raceName,
                                     factionname=factionName,
                                     classname=className,
                                     level=str(row["level"])
                                     ))
            
            generatePlayerPage(row,nomHtml)
        
        newHtml.write("</table>")
        return PLAYERS_PAGE_NAME
    except:
        
        print traceback.format_exc()
        thread.sleep(10)
        
def generatePlayerPage(row,filename):

    newHtml=open("website/"+filename+".html","w")
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
    newHtml.write("""<head><meta charset="utf-8"/></head>""")
    newHtml.write("<table border=\"1\" style=\"background:#000000\"> "+
                      "<tr> <th style=\"color:#FFFFFF\">Nom</th>\n"+
                      "<th style=\"color:#FFFFFF\"> Image</th></tr>")    
    for i in range(len(itemsList)):
        newHtml.write(generateItemForTab(itemsList[i]))
    newHtml.write("</table>")


def generateItemForTab(itemId):
    colors=["color:#B3B3B3",
            "color:#FFFFFF",
            "color:00FF26",
            "color:0D00FF",
            "color:BC00FF",
            "color:FF9E00",
            "color:FACD86",
            "color:FACD86",
            "color:FACD86",
            "color:FACD86"
            
            ]
    cursor=MySQLdb.cursors.DictCursor(db)
    cursorDb2=MySQLdb.cursors.DictCursor(db)
    cursor.execute("SELECT * FROM ITEMS WHERE id={id}".format(id=str(itemId)))
    itemFound=cursor.fetchone()
    if itemFound == None:
        print str(itemId)
    cursorDb2.execute("SELECT * FROM ITEMSPICTURES WHERE id="+str(itemFound["picture"]))
    row2=cursorDb2.fetchone()
    nomLien=iri2uri(itemFound["name"])
    nomLien=nomLien.replace(" ","")
    nomLien=nomLien.replace(":","")
    imgLink=WOW_MEDIUM_IMG_API_URL+row2["name"]+".jpg"
    cursorDb2.close()
    cursor.close()
    return "<tr><td><a style=\"{colorQuality}\" href={nomlien}.html>{nom}</a></td><td><img src={img} ></td><tr>".format(nom=itemFound["name"],nomlien=nomLien,img=imgLink,colorQuality=colors[itemFound["quality"]])
    
def generateItemPage(row,imgName,fileName):
    colors=["color:#B3B3B3",
            "color:#FFFFFF",
            "color:00FF26",
            "color:0D00FF",
            "color:BC00FF",
            "color:FF9E00",
            "color:FACD86",
            "color:FACD86",
            "color:FACD86",
            "color:FACD86",
            "color:FACD86",

            ]
    newHtml=open("website/"+fileName+".html","w")
    color=COLORS["blanc"]
    cursor=MySQLdb.cursors.DictCursor(db)
    cursor.execute("SELECT description FROM ITEMSDESCRIPTIONS WHERE id={idDesc}".format(idDesc=str(row["description"])))
    descriptionValue=cursor.fetchone()["description"]
    if descriptionValue == "":
        descriptionValue="Pas de description"
    if DEBUG:
        print str(row["classid"]) , str(row["subclassid"])
    typeValue,subTypeValue=getTypes(str(row["classid"]),str(row["subclassid"]))
    newHtml.write("""<head><meta charset="utf-8"/></head>""")
    newHtml.write("""<table border=\"1\" style=\"background:#000000\"> 
                          <tr> 
                               <th style=\"color:#FFFFFF\"> 
                                     Nom
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Image
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Niveau
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Description
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Type
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Sous-type
                               </th><tr>""")

    newHtml.write( """ 
                                <tr>
                                 <td>
                                    <p style=\"{colorQuality}\">{itemName} </p>
                                  </td>
                                  <td>
                                    <img src=\"{imgnom}\" />
                                  </td>
                                  <td>
                                    <p style=\"{color}\" >{niveau}   </p>
                                   </td>   
                                   <td>
                                    <p style=\"{color}\" >{description}   </p>
                                   </td>     
                                   <td>
                                    <p style=\"{color}\" >{typee}   </p>
                                   </td>     
                                   <td>
                                    <p style=\"{color}\" >{subtype}   </p>
                                   </td>     
                                                                    
                              </tr>""".format(itemName=row["name"],niveau=row["level"],description=descriptionValue,imgnom=imgName,typee=typeValue,subtype=subTypeValue,color=color,colorQuality=colors[row["quality"]]))
    newHtml.write("""</table>""")
    if typeValue=="Weapon":
        generateWeaponStat(newHtml,row["id"])

    generateBonusStat(newHtml,row["id"])

    newHtml.close()
    cursor.close()


def generateWeaponStat(fichier,itemId):
    cursor=MySQLdb.cursors.DictCursor(db)
    cursor.execute("SELECT * FROM WEAPON WHERE id={id}".format(id=str(itemId)))
    weaponInfo=cursor.fetchone()
    fichier.write("""<table border=\"1\" style=\"background:#000000\"> 
                          <tr> 
                               <th style=\"color:#FFFFFF\"> 
                                     Damage Max
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Damage Min
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    DPS
                               </th>
                               <th style=\"color:#FFFFFF\"> 
                                    Vitesse d'attaque
                               </th><tr>""")
    fichier.write( """<tr>
                                 <td>
                                    <p style=\"{colorGreen}\">{dmgMax} </p>
                                  </td>
                                  <td>
                                    <p style=\"{colorRed}\" >{dmgMin}   </p>
                                   </td>   
                                   <td>
                                    <p style=\"{colorGreen}\" >{dps}   </p>
                                   </td>     
                                   <td>
                                    <p style=\"{colorBlue}\" >{weaponSpeed}   </p>
                                   </td>     
                                                                    
                              </tr></table>""".format(colorGreen=COLORS["vert"],
                                              colorBlue=COLORS["bleu"],
                                              colorRed=COLORS["rouge"],
                                              dmgMax=weaponInfo["damageMax"],
                                              dmgMin=weaponInfo["damageMin"],
                                              dps=weaponInfo["dps"],
                                              weaponSpeed=weaponInfo["weaponSpeed"]))
def generateBonusStat(fichier,itemId):
    cursor=MySQLdb.cursors.DictCursor(db)
    cursor2=MySQLdb.cursors.DictCursor(db)
    cursor.execute("SELECT * FROM ITEMSTAT WHERE id={id}".format(id=str(itemId)))
    row = cursor.fetchall()
    for i in range(0,len(row)):
        bonusStat=row[i]
        cursor2.execute("SELECT * FROM BONUSSTATS WHERE id={idStat}".format(idStat=str(bonusStat["stat"])))
        rowStatName=cursor2.fetchone()
        statName=rowStatName["description"]
        fichier.write("""<p style=\"{black}\">
                          <span style=\"{green}\">+{valueStat}</span>
                          {statName}
                         </p>""".format(black=COLORS["noir"],
                                        green=COLORS["vert"],
                                        valueStat=bonusStat["amount"],
                                        statName=statName))
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

def generateItemsPage():
    colors=["color:#B3B3B3",
            "color:#FFFFFF",
            "color:00FF26",
            "color:0D00FF",
            "color:BC00FF",
            "color:FF9E00",
            "color:FACD86",
            "color:FACD86",
            "color:FACD86",
            "color:FACD86",
            "color:FACD86",

            ]
    cursorDb=MySQLdb.cursors.DictCursor(db)
    cursorDb2=MySQLdb.cursors.DictCursor(db)
    fichierHtml=open("website/"+ITEMS_PAGE_NAME,"w")
    fichierHtml.write("""<head><meta charset="utf-8"/></head>""")
    fichierHtml.write("<table border=\"1\" style=\"background:#000000\"> "+
                      "<tr> <th style=\"color:#FFFFFF\">Nom</th>\n"+
                      "<th style=\"color:#FFFFFF\"> Image</th></tr>")
    try:
        cursorDb.execute("SELECT * FROM ITEMS")
        for row in cursorDb:
           
            cursorDb2.execute("SELECT * FROM ITEMSPICTURES WHERE id="+str(row["picture"]))
            row2=cursorDb2.fetchone()
            print row["name"]
            nomLien=iri2uri(row["name"])
            nomLien=nomLien.replace(" ","")
            nomLien=nomLien.replace(":","")
            nomLien=nomLien.replace("/","")
            
            if DEBUG:
                print nomLien
            imgLink=WOW_MEDIUM_IMG_API_URL+row2["name"]+".jpg"
            fichierHtml.write("<tr><td><a style=\"{colorQuality}\" href={nomlien}.html>{nom}</a></td><td><img src={img} ></td><tr>".format(nom=row["name"],nomlien=nomLien,img=imgLink,colorQuality=colors[row["quality"]]))
            generateItemPage(row,imgLink,nomLien)
        fichierHtml.write("</table>")
    except:
        print traceback.format_exc()


    fichierHtml.close()
    print ITEMS_PAGE_NAME
    return ITEMS_PAGE_NAME
