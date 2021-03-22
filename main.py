import csv

f = open("legislator.csv")
legislator = csv.reader(f)
l = list(legislator)

gender=[]

for row in l:
  gender.append(row[3])

gender = set(gender[1:])
print(gender)

#GESTION DES ERREURS Exploration du dataset.
#exploration du dataset doit nous permettre de voir les tendances, les erreur et manquement et des valeur non ccoherente
#ici nous avons une liste de personnage politique avec leur parti.

#explorons les differends parti politique

party =[]

for row in l:
  party.append(row[6])

party = set(party[1:])
print(party)

#{'', 'National Greenbacker', 'Crawford Republican', 'Free Soil', 'Progressive Republican', 'Federalist', 'Conservative', 'Free Silver', 'Ind. Democrat', 'Law and Order', 'Populist', 'Silver Republican', 'American', 'Nullifier', 'Progressive', 'Pro-Administration', 'Ind. Republican-Democrat', 'Unconditional Unionist', 'Republican-Conservative', 'Socialist', 'Ind. Republican', 'Popular Democrat', 'American Labor', 'Democratic and Union Labor', 'Democratic Republican', 'Nonpartisan', 'Independent Democrat', 'Farmer-Labor', 'Anti Jackson', 'Union Democrat', 'Adams', 'Democrat-Liberal', 'Jackson Republican', 'Jackson', 'New Progressive', 'Union', 'Independent', 'Liberty', 'Democrat', 'Constitutional Unionist', 'Anti-Jacksonian', 'Readjuster Democrat', 'Readjuster', 'Anti Jacksonian', 'Prohibitionist', 'Coalitionist', 'Anti-Lecompton Democrat', 'Ind. Whig', 'Conservative Republican', 'Liberal Republican', 'Unknown', 'Jacksonian', 'Republican', 'Unionist', 'States Rights', 'Anti-Administration', 'Whig', 'Union Labor', 'Anti Masonic', 'Adams Democrat'}

#GESTION DES ERREURS
#Valeurs manquantes
#Je remplace les valeurs manquante par aucun parti
for row in l:
  if row[6] == "":
    row[6] = "no party"

party =[]

for row in l:
  party.append(row[6])

party = set(party[1:])
print(party)

#Valeurs manquantes 2
# remplacer les genre manquant par M car il y a une tendance majoritairement masculine dans la liste.

for row in l:
  if row[3] == "":
    row[3] = "M"

gender =[]

for row in l:
  gender.append(row[3])

gender = set(gender[1:])
print(gender)

#Analyse des années de naissance
#recupere les annee de naissance :
birth_year =[]

for row in l:
  list_row = []
  list_row.append(row[2])
  for x in list_row:
    list_row= x.split("-")
    birth_year.append(list_row[0])

birth_year = set(birth_year)
print(birth_year)


# un code encore mieux avec moins de code
birth_years2 = []

for row in l:
  birthday = row[2]
  parts = birthday.split("-")
  birth_years2.append(parts[0])

birth_years2 = set(birth_years2)
print(birth_years2)

