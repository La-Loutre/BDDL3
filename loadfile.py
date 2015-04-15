def loadcommand(fichier):
    line = fichier.readline()
    if line == "\n":
        return False
    if line == "":
        return None
    paragraphe = line
    while len(line)>=2 and line[len(line)-2] != ";":
        line=fichier.readline()
        paragraphe += line
    if len(line)<2 :
        return None
    return paragraphe

def loadfile(cur, filename):
    fichier = open(filename)
    para=loadcommand(fichier)
    while para != None:
        if para != False:
            try:
                cur.execute(para)
            except:
                print para
                return None
        para=loadcommand(fichier)

        

# from test import *        
# cur = db.cursor()
# loadfile(cur, "tmp")
# db.commit()
