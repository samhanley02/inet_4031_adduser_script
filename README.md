# INET4031 Add Users Script and User List

## Program Description

This program is meant to make adding users to a system fast, and easy. Instead of typing each users information into the terminal one-by-one, you can instead feed it a formatted file containing information like name, passwords, groups, and other important information. This helps to reduce errors, increase efficiency, and make the job overall easier.

## Program User Operation

This program takes in a formated file and will automatically add users to the system based on the contents of said file.

This section should start off with a paragraph description, then have subsections for the following:

### Input File Format
The input file is formatted as follows: '(username):(password):(Lastname):(Firstname):(Group1, optional(, Group2, etc.))
Each new user must be on a new line.
If the user needs to skip a line in the input file, simply place a '#' in front of the line
If the user does NOT want a new user added to any groups, in the (group1) section place a '-'

### Command Excuction
In order to run the code, you must first edit the file permissions
Using chmod, type the following command: chmod 764 "create-users.py"
This sets the file permissions to executable.
Now to run the program, use the following command: ./create-users.py < create-users.input

### "Dry Run"
If the user would like to do a "dry run" (run the program to ensure no bugs are present and no system changes are made)
First edit the create-users.py file using vi or nano. Comment out any lines containing os.systen(cmd). There are a total of three and they are located on lines 41, 48, and 55.
After this change is made, you can run the program to ensure no errors occur. In order to run the program for real, simply remove the comments on those same lines.
