"""
M02 Lab - Case Study if else and while
This app will allow students names to be input into a system and then enter their GPA this will then sort and see if the student made honor roll or Dean's list
"""
last_name = input("Please enter the student's last name (to quit enter 'ZZZ')")
while last_name != 'ZZZ':
    first_name = input("Please enter the student's first name")
    gpa = float(input("Please enter the student's GPA"))
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List and Honor Roll")
    elif gpa >= 3.25 and gpa < 3.5:
        print(first_name, last_name, "has made Honor Roll")
    else:
        print(first_name, last_name, "has not made Honor Roll or the Dean's List")
    last_name = input("Please enter the student's last name (to quit enter 'ZZZ')")