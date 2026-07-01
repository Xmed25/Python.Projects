# 🧠Project 1: Student Grades Analyzer
# Concept:

# A program that generates random grades for students and then analyzes them.

# Requirements:
# Generate grades for 30 students.
# Calculate:
# Average
# Highest grade
# Lowest grade
# Number of students who passed (≥ 50)
# Pass rate




import numpy as np
print("Name                            Grade\n")
grades=[]
with open(r"C:\Users\khate\Desktop\names.txt",'r') as names:
    for name in names:
        grade=np.random.random()*100
        grades.append(grade)
        print(f"{name.strip():15}:\t\t{grade:.2f}")

grades=np.array(grades)
print('=========================\n')
print(f"Average:{np.mean(grades):.2f}")
print(f"Highest Grade:{np.max(grades):.2f}")
print(f"Lowest Grade:{np.min(grades):.2f}\n")
passed=grades[grades>=50]
print(f"Number of Students who passed: {len(passed)}")
pass_rate=len(passed)/len(grades)*100
print(f"Pass Rate :{pass_rate:.2f}%")