"""
Author: Samantha Lopez
Last updated: 01/28/2024
Python program to determine if a student qualifies for the Dean's list or Honor roll
"""

def honorRoll():
    while True:
        lname = input("Enter student's last name (or type 'ZZZ' to quit): ")

        #checks to see if user wants to quit
        if lname == "ZZZ":
            break

        fname = input("Enter student's first name: ")

        gpa = float(input("Enter student's GPA: "))
       
        if gpa >= 3.5:
           print(f"Congratulations, {fname} {lname} made the Dean's List!")

        elif 3.25 < gpa < 3.5:
            print(f"Congratulations, {fname} {lname} made the Honor Roll!")

        else:
            print(f"Keep working!{fname} {lname} You're almost there!")

if __name__ == "__main__":
    honorRoll()
