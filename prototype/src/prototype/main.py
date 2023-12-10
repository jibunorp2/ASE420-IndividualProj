import datetime

import backend
import os
from dateutil import parser

os.system("clear")

ch = int(input("\t1. View What You Did\n\t2. Input What You Did\n\t3. QUIT \t\n>"))

while ch != 3:
    if ch == 1:
        os.system("clear")
        print("ID" + "\t" + "TASK" + "\t" + "\tDATE / TIME\t" + "\t\tTAG")
        for rows in backend.view():
            print(str(rows[0]) + "\t" + rows[1] + "\t\t" + rows[2] + "\t" + rows[3])
        ch = int(input("\t1. View What You Did\n\t2. Input What You Did\n\t3. QUIT \t\n>"))
    elif ch == 2:
        task = input("What did you do today?: ")
        askDate = parser.parse(input("Enter a Date: "))
        tag = input("Enter your TAG: ").upper()
        if len(task) != 0:
            backend.insertdata(task, askDate, tag)
            ch = int(input("\t1. View What You Did\n\t2. Input What You Did\n\t3. QUIT \t\n>"))
    else:
        print("Please Choose A Correct Input")
        ch = int(input("\t1. View What You Did\n\t2. Input What You Did\n\t3. QUIT \t\n>"))
else:
    print("Thank You For Using The Application!")
