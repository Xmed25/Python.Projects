import numpy as np
print("Name                            Grade\n")
students=[]
grades=[]
with open(r"C:\Users\khate\Desktop\names.txt",'r') as names:
    for name in names:
        grade=np.random.random()*100
        students.append(name)
        grades.append(grade)
        print(f"{name.strip():15}:\t\t{grade:.2f}")

grades=np.array(grades)
print('=========================\n')
print(f"Average:{np.mean(grades):.2f}")
print(f"Highest Grade:{np.max(grades):.2f}")
print(f"Lowest Grade:{np.min(grades):.2f}\n")
print('++++++++++++++++++\n')
print(f"Number of students who has Excelent: {len(grades[grades>=90])}")
print(f"Number of students who has Very Good: {len(grades[(grades>=80) & (grades<90) ])}")
print(f"Number of students who has Good: {len(grades[(grades>=70) & (grades<80)])}")
print(f"Number of students who has Acceptable: {len(grades[(grades>=50) & (grades<70)])}")
print(f"Number of students who has Fail: {len(grades[grades<50])}\n")

passed=grades[grades>=50]
print(f"Number of Students who passed: {len(passed)}")
pass_rate=len(passed)/len(grades)*100
print(f"Pass Rate :{pass_rate:.2f}%")
highest_one=np.argmax(grades)
print(f"TOP 1 :{students[highest_one]}")
