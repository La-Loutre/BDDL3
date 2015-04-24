import MySQLdb
from passwd import *
db=MySQLdb.connect(host="localhost",user="louis",passwd=p,db="wowdb")
WOW_API_URL="http://eu.battle.net/api/wow/"
WOW_MEDIUM_IMG_API_URL="http://eu.media.blizzard.com/wow/icons/56/"
WOW_SMALL_IMG_API_URL="http://eu.media.blizzard.com/wow/icons/36/"
WOW_PLAYER_MEDIUM_IMG_API_URL="http://eu.battle.net/static-render/eu/"
LOCALS={"en":"?locale=en_GB","fr":"?locale=fr_FR","None":""}
DEBUG=False
