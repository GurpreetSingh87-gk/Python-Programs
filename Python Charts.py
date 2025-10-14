# Python Charts

# SDG 4 Chart:-
# ------------

'''
import matplotlib.pyplot as plt

# Target of SDG 4

target = [
    "Primary & Secondary Education",
    "Early Childhood Education",
    "Technical & Higher Education",
    "Skill Development",
    "Gender Quality in Education",
    "Literacy & Numeracy",
    "Sustainable Development & Citizenship",
]

# Hypothetical Progress Percentage (2024 estimates)

progress=[75, 68, 55, 60, 70, 65, 50]

# Creating the Bar Chart

fig, ax = plt.subplots(figsize=(10,6))
bars = ax.barh(target, progress, color='skyblue')

# Adding Data Lables

for bar in bars:
    width = bar.get_width()
    ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{width}%', va='center', fontsize=12)

# Formatting the Chart

ax.set_xlabel("Progress (%)", fontsize=14)
ax.set_xlim(0,100)
ax.set_title("Progress on SDG 4 Targets(2024 estimates)", fontsize=16)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Display the Chart

plt.gca().invert_yaxis()
plt.show()
'''
#--------------------------------------------------------------------------------------------------

# Pie Chart For Expense Distribution:-
# -----------------------------------
'''
import matplotlib.pyplot as plt

# Data

categories = ['Rent','Food','Transport','Entertainment','Savings']
expenses = [500, 200, 100, 50, 150]

# Create Pie Chart

plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title("Monthly Expense Disribution")
plt.show()
'''
#--------------------------------------------------------------------------------------------------

# Bar Chart For Exam Scores:-
# --------------------------
'''
import matplotlib.pyplot as plt

students = ['Alice', 'Bob', 'Charlie', 'David', 'Garrison']
scores = [85, 92, 78, 90,65]

plt.bar(students, scores, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Exam Scores")
plt.show()
'''
#--------------------------------------------------------------------------------------------------

# Random Dic Roller:-
# ------------------
'''
import random

while True:
    input("Press Enter to roll the dice...")
    print("🎲 You rolled:", random.randint(1, 6))
'''
#--------------------------------------------------------------------------------------------------

# Simple To Do List App:-
# ---------------------
'''
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def show_tasks():
    print("Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    action = input("Enter (add/show/exit): ").lower()
    if action == "add":
        task = input("Enter task: ")
        add_task(task)
    elif action == "show":
        show_tasks()
    elif action == "exit":
        break
'''





    
