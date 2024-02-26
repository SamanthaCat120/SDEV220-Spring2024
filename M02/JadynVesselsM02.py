"""
Name: Jadyn Vessels
File Name: M02 Lab Case Study
Description: Accepts student names and GPAs and test if the student qualifies 
            for either the Dean's List or the Honor Roll.
"""
            
##Variable to concatenate with output sentences based on GPA
honRoll = "has made it on the Honor Roll!"                 
deanHon = "has made on the Dean's List and the Honer Roll!"
none = "unfortunately did not make it on the Honor Roll or Dean's List."


lastName = input("Enter last name or enter 'ZZZ' to quit: ")
print()

while lastName != "ZZZ":
    firstName = input("Enter first name: ")
    gpa = float(input("\nEnter GPA: "))
    if gpa >= 3.25:
        if gpa >= 3.5:
            print(f"\nWith a {gpa} GPA, {firstName} {lastName} " + deanHon)
        else:
            print(f"\nWith a {gpa} GPA, {firstName} {lastName} " + honRoll)
    else:
        print(f"\nWith a {gpa} GPA, {firstName} {lastName} " + none)
    
    lastName = input("\nEnter last name or enter 'ZZZ' to quit: ")
