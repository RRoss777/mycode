#!/usr/bin/python3

loginfail = 0

#keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    
    for line in kfile:

        if "- - - - -] Authorization failed" in line:
            loginfail += 1

print("The number of failed log in attempts is", loginfail)
#keystone_file.close()
