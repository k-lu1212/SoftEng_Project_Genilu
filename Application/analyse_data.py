import csv
from datetime import datetime
import sys


deltaDay_arg = int(sys.argv[1])
print deltaDay_arg
# deltaDay = 3 jours
deltaDay = datetime.strptime('2000-01-31', '%Y-%m-%d')-datetime.strptime('2000-01-'+str(31-deltaDay_arg), '%Y-%m-%d')
print deltaDay
data = []

#extraction des donnees du csv
with open('commits.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         if(row[1] != "name"):
             data.append(row)

#extraction de tous les utilisateurs
user = []
for d in data:
    if(d[1] not in user):
        user.append(d[1])

print user

#creation de la matrice user X user avec des 0
matriceUserInterraction = {}
for u in user:
    matriceUserInterraction[u] = {}
for u in user:
    for u2 in user:
        matriceUserInterraction[u][u2]=0

print matriceUserInterraction

for d1 in data:
    for d2 in data:
        if(d1!=d2 and d1[1]!=d2[1] and d1[4]==d2[4]):
            datetime_object2 = datetime.strptime(d2[2].split("T")[0], '%Y-%m-%d')
            datetime_object1 = datetime.strptime(d1[2].split("T")[0], '%Y-%m-%d')
            delta = max(datetime_object1,datetime_object2)-min(datetime_object1,datetime_object2)
            if(delta <= deltaDay):
                matriceUserInterraction[d1[1]][d2[1]] = matriceUserInterraction[d1[1]][d2[1]] + 1


print matriceUserInterraction
c = csv.writer(open("test.csv", "wb"))

#format_1 (matrice)
#c.writerow(matriceUserInterraction.keys())
#for m in matriceUserInterraction:
#    c.writerow(matriceUserInterraction[m].values())

#format_2
color = 1
c.writerow(["Commiter1","Commiter2","commits","color"])
for m1 in matriceUserInterraction:
    for m2 in matriceUserInterraction:
        c.writerow([m1,m2,matriceUserInterraction[m1][m2],color])

    color+=1
