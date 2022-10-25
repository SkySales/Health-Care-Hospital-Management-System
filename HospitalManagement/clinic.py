from colorama import Fore
import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="healthcare"
)

def PatientNeeds():
  os.system('cls')
  print(Fore.GREEN + '##########################################################################')
  print(Fore.GREEN + '#                          CHOOSE YOUR NEEDS                             #')
  print(Fore.GREEN + '##########################################################################')

  print("""
    1.Patient Sick 
    2.Patient Blood Check
    3.Patient Pregnancy Test
    4.Patient Vision Eye Check
    5.Patient Bone Fracture or Sprain
  """)

def CRM():
  os.system('cls')
  PatientNeeds()
  name = input(Fore.MAGENTA + 'Enter Name: ')
  email = input(Fore.MAGENTA + 'Enter Personal Email: ')
  phone = input(Fore.MAGENTA + 'Enter Personal Phone No.: ')
  needs = int(input(Fore.MAGENTA + 'Chooose Your Needs 1-5: '))
  message = input(Fore.MAGENTA + 'Enter any message for the Doctors: ')

  if needs == 1:
    query = "INSERT INTO hospital (name, email, phone, needs, message) VALUES (" \
            "'" + name + "', '" + email + "', '" + phone + "', 'Patient Sick', '" + message + "')"
    cur = mydb.cursor()
    cur.execute(query)
    mydb.commit()
    cur.close()
    print(Fore.CYAN + "Information Successfully Send To The Clinic Admin/Staff")
  elif needs == 2:
    query = "INSERT INTO hospital (name, email, phone, needs, message) VALUES (" \
            "'" + name + "', '" + email + "', '" + phone + "', 'Patient Blood Check', '" + message + "')"
    cur = mydb.cursor()
    cur.execute(query)
    mydb.commit()
    cur.close()
    print(Fore.CYAN + "Information Successfully Send To The Clinic Admin/Staff")
  elif needs == 3:
    query = "INSERT INTO hospital (name, email, phone, needs, message) VALUES (" \
            "'" + name + "', '" + email + "', '" + phone + "', 'Patient Pregnancy Test', '" + message + "')"
    cur = mydb.cursor()
    cur.execute(query)
    mydb.commit()
    cur.close()
    print(Fore.CYAN + "Information Successfully Send To The Clinic Admin/Staff")
  elif needs == 4:
    query = "INSERT INTO hospital (name, email, phone, needs, message) VALUES (" \
            "'" + name + "', '" + email + "', '" + phone + "', 'Patient Vision Eye Check', '" + message + "')"
    cur = mydb.cursor()
    cur.execute(query)
    mydb.commit()
    cur.close()
    print(Fore.CYAN + "Information Successfully Send To The Clinic Admin/Staff")
  elif needs == 5:
    query = "INSERT INTO hospital (name, email, phone, needs, message) VALUES (" \
            "'" + name + "', '" + email + "', '" + phone + "', 'Patient Bone Fracture or Sprain', '" + message + "')"
    cur = mydb.cursor()
    cur.execute(query)
    mydb.commit()
    cur.close()
    print(Fore.CYAN + "Information Successfully Send To The Clinic Admin/Staff")

  close = input("Enter [C] to close: ")
  if close == "c" or close == "C":
    HealthAssist()

def ViewData():
  os.system('cls')
  print(Fore.GREEN + '##########################################################################')
  print(Fore.GREEN + '#                      ADMIN VIEW DATA FUNCTION                          #')
  print(Fore.GREEN + '##########################################################################')
  cursor = mydb.cursor()
  cursor.execute("SELECT * FROM hospital")
  result = cursor.fetchall()
  for x in result:
    print(x)

  close = input("Enter [C] to close: ")
  if close == "c" or close == "C":
    AdminPage()

def Deletedata():
  os.system('cls')
  print(Fore.GREEN + '##########################################################################')
  print(Fore.GREEN + '#                      ADMIN DELETE DATA FUNCTION                        #')
  print(Fore.GREEN + '##########################################################################')
  pid = input(Fore.CYAN + "Enter Patient ID: ")
  mycursor = mydb.cursor()
  sql = "DELETE FROM hospital WHERE pid = '" + pid + "' "
  mycursor.execute(sql)
  mydb.commit()
  print(mycursor.rowcount, Fore.CYAN + "record(s) deleted")

  close = input(Fore.CYAN + "Enter [C] to close: ")
  if close == "c" or close == "C":
    AdminPage()

def AdminPage():
  os.system('cls')
  print("""
  A. View Data
  B. Delete Data
  C. Back To Main Page  
  
  """)
  cmd = input(Fore.CYAN + "Choose [A] - [C]: ")
  if cmd == "a" or cmd == "A":
    ViewData()
  elif cmd == "b" or cmd == "B":
    Deletedata()
  elif cmd == "c" or cmd == "C":
    HealthAssist()

def StaffSection():
  os.system('cls')
  print(Fore.GREEN + '##########################################################################')
  print(Fore.GREEN + '#              ADMIN/STAFF HEALTH CARE/HOSPITAL MANAGEMENT               #')
  print(Fore.GREEN + '#            Admin/Staff can View & Delete Data of the system            #')
  print(Fore.GREEN + '##########################################################################')

  login = input(Fore.CYAN + "Enter ID: ")
  if login == "admin" or login == "Admin":
    AdminPage()
  else:
    print(Fore.CYAN + "Incorrect ID")
    HealthAssist()


def HealthAssist():
  os.system('cls')
  print(Fore.GREEN + '##########################################################################')
  print(Fore.GREEN + '#              WELCOME TO HEALTH CARE/HOSPITAL MANAGEMENT                #')
  print(Fore.GREEN + '#         Clinic/Hospital Health Care and Consultation Support           #')
  print(Fore.GREEN + '##########################################################################')
  comm = input(Fore.CYAN + "Enter CRM for Customer Support/Enter Staff for Admin/Staff Page: ")

  if comm == "crm" or comm == "CRM":
    CRM()
  elif comm == "staff" or comm == "Staff":
    StaffSection()
  else:
    print("Enter the correct keyword")

HealthAssist()