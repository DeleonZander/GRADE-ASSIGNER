#lab5
grade = int(input("What is your grade?:"))
if grade >= 101:
    print("Invalid Grade")
elif grade >=90:
    print("Grade A")
elif grade >=80:
    print("Grade B")
elif grade >=70:
    print("Grade C")
elif grade >=60:
    print("Grade D")
elif grade >=0:
    print("Grade F")
else:
    print("Invalid Grade")