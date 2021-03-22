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

