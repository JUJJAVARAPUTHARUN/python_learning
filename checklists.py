# Daily Task Organizer

# Step 1: Create checklist
checklist = []
completed_tasks = []
incomplete_tasks = []

num = int(input("How many tasks do you want to add to today's checklist? "))

for i in range(num):
    task = input(f"Enter task {i+1}: ")
    checklist.append(task)

print("\n--- End of Day Review ---")
for task in checklist:
    status = input(f"Did you complete '{task}'? (yes/no): ").strip().lower()
    if status == "yes":
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

# Final Output
print("\n✅ Completed Tasks:")
for t in completed_tasks:
    print(f" - {t}")

print("\n❌ Incomplete Tasks:")
for t in incomplete_tasks:
    print(f" - {t}")
