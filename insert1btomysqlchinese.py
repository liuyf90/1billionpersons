import mysql.connector
import random
import csv
import datetime
import time

mydb = mysql.connector.connect(
  host="10.211.55.4",
  user="root",
  password="123456",
  database="test"
)

print(time.localtime())
f = open('./Chinese_Family_Name.csv','r')
reader=csv.reader(f)
family_names =[row[0] for row in reader]

f1 = open('./Chinese_Names_Corpus.csv','r')
reader1=csv.reader(f1)
names =[row[0] for row in reader1]


f2 = open('./earthquake.csv','r')
reader2=csv.reader(f2)
birthdays =[row[1] for row in reader2]


#print(firstNames)
#print(birthdays)
#print(len(result))

#insert 100million records
for n in range(1,100000001):
  nr = random.randrange(1, len(family_names))
  firstName=family_names[nr]
  
  lr = random.randrange(1, len(names))
  lastName=names[lr]
  

  br = random.randrange(1, len(birthdays))
  birthday=birthdays[br]
  mycursor = mydb.cursor()
  sql = "INSERT INTO personchinese (first_name,last_name,birthday) VALUES (%s, %s,%s)"
  val = (firstName,lastName,birthday);
  mycursor.execute(sql, val)
  #1million to commit please edit it for your need
  if (n%10000000==0):
    mydb.commit() 
f.close()
f1.close()
f2.close()

print(mycursor.rowcount, "record inserted.")

print(time.localtime())
