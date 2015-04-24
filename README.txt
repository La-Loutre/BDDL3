=== Projet BDD L3 ===

1)Création de la base de donnée(MySQL) :
CREATE DATABASE wowdb;
use wowdb;
source createtables.sql;


2) Réglages
-Ouvrir le fichier globals.py , modifier la ligne db=MySQLdb.connect(...)
pour y mettre le bon host , user et db . 
-Ajouter un fichier passwd.py contenant le mot de passe :
$ echo "p=Mon password" > passwd.py 

3) Lancement 
$ python demonstration.py

4)Website (nécessite un lancement au préalable)
$ chromium website/index.html

5)Clean-up:
$ rm -rf website/ items/ players/ servers/
