import csv #Import de CSV, librairie native de python

### 1 - Load the data from the nat2021 file you have downloaded

file = open('nat2021.csv') #Ouverture du fichier de donnees

csvreader = csv.reader(file) #Lecture du fichier CSV

header = next(csvreader) # Extraction des en tetes du fichier CSV

rows = []

for row in csvreader: # Boucle d'extraction des donnees
    rows.append(row)

headers = header[0].split(';') # Extraction des en-tetes dans une liste

data = []

#   Boucle de tri des donnees dans des tableau associatif comme 
#   l'exemple suivant : {'nombre' : 1500, 'annee' : 2012, 'sexe' : 1 'prenom' : 'Alain'}

for row in rows:
    aRow = row[0].split(';')
    aData = {}
    for i in range(0, len(headers), 1):         # Boucle de parcours de la taille du tableau d'en tetes
        aData[headers[i]] = aRow[i]                 # Ajout de la donnee N dans le tableau associatif a la case N ; Iteration de N+1 jusqu'a ce que N+1 == taille du tableau de headers
    data.append(aData)                          # Ajout du tableau associatif dans une liste

#print(data[0])
# Ligne du dessus a decommenter pour avoir un exemple d'un tableau associatif

### 2 - Create a function to count the number of firstnames used by less than 100 persons from 1900 to this date

def countUsedByLessThan(number = 100):
    allData = []
    count = 0
    lastName = data[0]['prenom']
    for aData in data:
        newName = aData['prenom']
        if(newName == lastName):                                        # Detection de changement de nom dans le parcours
            count += int(aData['nombre'])
        else:
            allData.append([lastName, count])                           # Si le nom change, on ajoute la valeur [prenom, nombre] a la liste
            count = int(aData['nombre'])
            
        lastName = aData['prenom']
    

    lessThanHundred = []

    for anArray in allData:                                             # Si le nombre est superieur au nombre en parametre on ajoute le prenom
        if(anArray[1] < number):
            lessThanHundred.append(anArray)
            
    return len(lessThanHundred)                                         # Retour de la taille de la liste

#print(countUsedByLessThan())

### 3 - Create a function to count the number of persons for a specified firstname since 1900 and for a specific year

def countNumberForName(name, year = False):
    count = 0
    for aData in data:
        if(aData['prenom'] == name and (str(year) == aData['annee'])):  # Si le prenom en parametre == le prenom parcouru AND (l'annee renseignee == l'annee parcourue)
            count += int(aData['nombre'])
        elif(aData['prenom'] == name and (year == False)):              # Si le prenom en parametre == le prenom parcouru AND l'annee n'est pas renseignee en parametre
            count += int(aData['nombre'])
    return count                                                        # Retour du compte

#print(countNumberForName('ANNE-EMMANUELLE', 1977))

###  4 - Create a function to list the X first firstname for year Y (X and Y being argument of the function)

def countFirstNameOfYear(number, year):
    nameList = []
    firstsName = []
    for aData in data:
        if(aData['annee'] == str(year)):                                    # Si l'annee parcourue correspond a l'annee en parametre
            nameList.append((aData['prenom'], int(aData['nombre'])))        # Ajout du tuple (prenom, nombre)
    
    nameSorted = sorted(nameList, key=lambda nom: nom[1], reverse= True)    # Tri decroissant de la liste des prenoms sur le nombre
    for i in range(0, number):                                            # Parcours des {number} premiers prenoms 
        firstsName.append(nameSorted[i][0])                                     # Ajout des prenoms dans la liste
    return firstsName

#print(countFirstNameOfYear(6, 1951))


### 5 - Create a function to count the number of unique firstnanes per year from 1900 and for the whole

def countUniqueFirstnames():
    allData = []
    count = 0
    lastName = data[0]['prenom']
    for aData in data:
        newName = aData['prenom']
        if(newName == lastName):                                        # Detection de changement de nom dans le parcours
            count += int(aData['nombre'])
        else:
            allData.append([lastName, count])                           # Si le nom change, on ajoute la valeur [prenom, nombre] a la liste
            count = int(aData['nombre'])
            
        lastName = aData['prenom']
    

    usedByOne = []

    for anArray in allData:                                             # Si le nombre est inferieur a 1 on ajoute le prenom
        if(anArray[1] < 2):
            usedByOne.append(anArray)
            
    return len(usedByOne)     

#print(countUniqueFirstnames())

# Enonce 5
"""

def countUniqueFirstnames():
    count = 0

    for aData in data:
        if(int(aData['nombre']) == 1):
            count += 1

    return count

"""


### 6 - Compute the ratio of girls over boys per year from 1900
def compute():

    print('Girls over boys per years : \n')

    listYears = []

    dico = {'girl' : {}, 'boy' : {}}

    for aData in data:
        if (int(aData['sexe']) == 2):                                       # Verification du sexe
            if aData['annee'] not in dico['girl']:                              # Si la case annee n'existe pas dans le tableau girls
                dico['girl'][aData['annee']] = (int(aData['nombre']))               # On cree la variable
            else:                                                               # Sinon
                dico['girl'][aData['annee']] += (int(aData['nombre']))              # Si la case existe on ajoute la valeur a la valeur existante
        
        elif (int(aData['sexe']) == 1):                                     # Verification du sexe
            if aData['annee'] not in dico['boy']:                               # Si la case annee n'existe pas dans le tableau girls
                dico['boy'][aData['annee']] = (int(aData['nombre']))                # On cree la variable
            else :                                                              # Sinon
                dico['boy'][aData['annee']] += (int(aData['nombre']))               # Si la case existe on ajoute la valeur a la valeur existante
    
    for aYear in sorted(dico['girl']):                                          # Parcours dans la liste ordonnee
        if aYear in dico['boy']:
            print(aYear+' : '+str(round(float(dico['girl'][aYear]) / float(dico['boy'][aYear]), 2))) # Impression du rapport femme / homme sur toutes les annees
        
#compute()

### 7 - Find the list of firstnames that have remained among the 200 most popular in the whole period

def countMost():

    lastName = data[0]['prenom']
    count = 0
    allData = []
    firstsName = []

    for aData in data:
        newName = aData['prenom']
        if(newName == lastName):
            count += int(aData['nombre'])
        else:
            allData.append([lastName, count])
            count = int(aData['nombre'])
            
        lastName = aData['prenom']

    allData = sorted(allData, key=lambda number: number[1], reverse= True)      # Tri de la liste des prenoms en decroissant sur le nombre
    for i in range(0, 199):                                                     # Parcours des 200 premiers prenoms tries pr ordre decroissant
        firstsName.append(allData[i][0])                                            # Ajout dans une liste
    return firstsName

#print(countMost())


### 8 - Which firstname with at least 50 births per year has had the strongest compound annual growth rate in the last 10 years 

def biggerGrowth():
    lastName = data[0]['prenom']
    count = 0
    allNames = []
    mostName = ''
    mostTcac = 0.0
    firstsName = []
    temoin = True
    compteur = 0
    underFifty = False
    lastSex = data[0]['sexe']

    for aData in data:
        newName = aData['prenom']
        if newName != lastName:
            if(underFifty == False):                                    # Si aucun occurence du prenom a ete en dessous de 50 pour chacune des annees
                allNames.append(str(lastName)+str(lastSex))                 # On ajoute la concatenation {prenom} + {sexe} dans la liste
            temoin = True                                               # On reinitialise les variables 
            count = int(aData['nombre'])
            compteur = 0
            underFifty = False
        if(temoin):                                                     # Si le prenom n'a jamais ete en dessous de 50
            if(int(aData['nombre']) < 50):
                temoin = False
                underFifty = True
            elif(newName == lastName):                                  # Sinon si le prenom parcouru est le meme qu'a l'occurence precedente
                if(compteur == 0):                                      # Si c'est la premiere occurence sur ce prenom
                    count = int(aData['nombre'])                            # On initialise la valeur du compteur
                else: count += int(aData['nombre'])                     # Sinon on ajoute a la valeur existante
        lastName = aData['prenom']
        lastSex = aData['sexe']
        compteur += 1

    dicoNames = {}
    count = 0
    for aData in data:
        ## Si la concatenation {prenom} + {sexe} de l'objet parcouru est presente dans la liste cree au dessus
        ## Ainsi que l'annee parcourue est soit egale a (anneeCourante - 10) ou (annee courante)
        if (aData['prenom']+aData['sexe'] in allNames) and ((aData['annee'] == '2011') or ('2021' == aData['annee'])):
            count += 1
            if count%2 == 1 :                                                                       # Determine si on a passe l'annee 2011 ou 2021
                dicoNames[aData['prenom']] = int(aData['nombre'])                                   # Si {annee} == 2011 on initialise la variable count dans le tableau avec pour index le prenom
            else : dicoNames[aData['prenom']] = (dicoNames[aData['prenom']], int(aData['nombre']))  # Si {annee} == 2021 on remplace la valeur de la variable par le tuple ({valeur pour 2011}, {valeur pour 2021})

    for aName in dicoNames:
        tcac = (pow((float(dicoNames[aName][1])/float(dicoNames[aName][0])), (0.1))-1) * 100        # Formule de calcul du taux de croissance annuel compose
        if tcac > mostTcac :                                                                        # Si le TCAC est plus grand que le plus grand enregistre 
            mostName = aName                                                                            # On garde le prenom en memoire
            mostTcac = tcac                                                                             # On garde le TCAC en memoire
    print(mostTcac, mostName)

#biggerGrowth()
