#!/usr/bin/python3
#### Student Name: Hamza Mohamed
#### Program Name: INET Assignment 9
#### Program Creation Date: 12/12/24
#### Program Last Updated Date: 12/12/24

#what are these imports being used for?
# os is used to interact with operating system, re provides regular expressions, and sys talks to the system run time environment
import os
import re
import sys

def main():
    for line in sys.stdin:

        #this "regular expression" is searching for the presence of a character - what is it and why?
        # it searching for regular expressions
        match = re.match("^#",line)

        #what is this field doing?
        # it removes any blank space and # stores elements
        fields = line.strip().split(':')

        #what would an appropriate comment be for describing what this IF statement is checking for?
        # a good comment explains the if statement
        #what happens if the IF statement evaluates to true?
        # then it would be followed up with true
        #how does this IF statement rely on what happened in the prior two lines of code? The match and fields lines.
        # if statements rely on what happens before because it is dependant
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        #print cmd
        os.system(cmd)
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)

        for group in groups:
            #what is this if statement looking for?
            # it ensures the user got added to the group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
