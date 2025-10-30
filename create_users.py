#!/usr/bin/python3

# INET4031
# Sam Hanley
# 10/29/25
# 10/30/25

#import os: Allows the program to edit files, retrieve system info etc.
#import re: Helps in dealing with strings & expressions
#import sys: Imports system module, helps with command liine arguments and io streams
import os
import re
import sys

def main():
    for line in sys.stdin:

        #This is looking line by line for the '#' symbol. It is looking for this character figure what is a comment so it can skip it
        match = re.match("^#",line)

        #Splits the line by the ':' character because that is what is used to separate entries in files like passwd
        fields = line.strip().split(':')

        #This if statement ignores any lines that are exactly 5 fields long or lines with comments
        if match or len(fields) != 5:
            continue

        #These three lines all relate to the passwd file because the file format is username:password:groups
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This is where all of the user data is stores (name, room, phone numbers etc.) So splitting it by ',' gives words of data
        groups = fields[4].split(',')

        #This shows what user we are creating the account for based on the gathered information from the passwd file
        print("==> Creating account for %s..." % (username))
        #The variable cmd will now contain the entire adduser command for the gathered user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        os.system(cmd)

        #This print statement ensures we know what user we are creating the account for.
        print("==> Setting the password for %s..." % (username))
        #This creates a shell command to set the users password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        os.system(cmd)

        for group in groups:
            #Checks if the group is not a placeholder, if it is a placeholder, no group is added, if it is a real group, the user is assigned to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                os.system(cmd)

if __name__ == '__main__':
    main()
