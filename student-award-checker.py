# Raven Blessinger - SDEV220
# Student Award Checker App = student-award-checker.py
# This app checks if a student qualifies for the Dean's List or Honor Roll based on their GPA.

print("🎉 Let's check if your student qualifies for an award! 🎉")
print()

while True:
    
    print("Enter 'ZZZ' for the student's last name to quit.")
    print('-' * 50)
    print()
    
    student_last_name = input("Enter your student's last name: ")
    
    if student_last_name.upper() == "ZZZ":
        quit_prompt = input("Are you sure you want to quit? (y/n): ")
        
        if quit_prompt.lower() == "y":
            print("Goodbye!")
            break
    
    else:
        student_first_name = input("Enter your student's first name: ")
        student_gpa = float(input("Enter your student's GPA: "))
        print()
        
        if student_gpa >= 3.5:
            print('+' * 50)
            print(f"{student_first_name} {student_last_name} has a GPA of {student_gpa}.")
            print(f"Congrats! 🎉 They have made the Dean's List!")
            print('+' * 50)
            print()
        elif student_gpa >= 3.25:
            print('+' * 50)
            print(f"{student_first_name} {student_last_name} has a GPA of {student_gpa}.")
            print(f"Way to go! 🙌 They have made the Honor Roll!")
            print('+' * 50)
            print()
        else:
            print('+' * 50)
            print(f"{student_first_name} {student_last_name} has a GPA of {student_gpa}.")
            print("While they don't qualify for an award, encourage them to keep up the good work!")
            print('+' * 50)
            print()

        

      