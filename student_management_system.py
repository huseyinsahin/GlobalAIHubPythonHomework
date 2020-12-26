'''
    GlobalAIHub - Project
    Huseyin SAHIN
    huseyinsahn@gmail.com
'''

student_list = ["Huseyin Sahin","Ziya Ozsoy","Ertugrul Kalkan", "Burak Akincioglu"]
courses = ["Assembly", "Python", "Java", "Haskell", "Pascal", "Swift", "Matlab"]

def calculateGrade():

    grades = {"Midterm":0,"Final":0,"Project":0}
                
    midterm = int(input("\nEnter your midterm grade: "))
    grades["Midterm"] = midterm
    final = int(input("Enter your final grade: "))
    grades["Final"] = final
    project = int(input("Enter your project grade: "))
    grades["Project"] = project

    result = midterm * 0.3 + final * 0.5 + project * 0.2

    return result

def selectCourse():

    courses_input = input("\nWhat courses would you like to take?: ")
    course_list = list(courses_input.split(","))

    if len(course_list) >= 3 and len(course_list) <= 5:

        for i in course_list:
            if i not in courses:
                print(f"There is no course named {i} in the system.")
            
        course = input("Enter one of the courses you took to see your grade: ")

        if course in course_list:
                
            grade = calculateGrade()
                
            if grade >= 90:
                return print(f"\nYour {course} grade is AA, passed.")
            elif grade >= 70 and grade < 90:
                return print(f"\nYour {course} grade is BB, passed.")
            elif grade >= 50 and grade < 70:
                return print(f"\nYour {course} grade is CC, passed.")
            elif grade >= 30 and grade < 50:
                return print(f"\nYour {course} grade is DD, passed.")
            else:
                return print(f"\nYour {course} grade is FF, failure.")
                        
        elif course not in course_list and course in courses:
            return print(f"\nYou can't take this {course}!!!")
            
        else:
            return print(f"\nThere is no lesson {course} in the student management system.")
    else:
        return print("\nYou must take at least 3 and at most 5 courses.You failed in class.")
    
for i in range(3):
    
    name = input("Please enter your name: ")
    surname = input("Please enter your surname: ")
    
    student_name_surname = name + " " + surname
    
    if student_name_surname in student_list:
        
        print("\nWelcome to the student management system {}".format(student_name_surname))
        selectCourse()
        break

    if i <= 1: 
        print("Could not login to the system!!\n")
        
    else:   
        print("Please try again later!!")