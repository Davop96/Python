# List to store tasks
tasks = []

def show_menu():

	# Display the menu of options for the user.

	print("\nTask Manager")
	print("1. Add Task")
	print("2. View Tasks")
	print("3. Remove Task")
	print("4. Mark Task as Completed")
	print("5. Exit")

def add_task():

	# Prompt the user to enter a task description and add it to the tasks list.

	description = input("Enter the task description: ")
    
	# Create a task dictionary with description and completion status
	task = {"description": description, "completed": False}
	tasks.append(task)
	print("Task added successfully.")

def view_tasks():

	# Display all tasks with their current status (completed or pending).

	if not tasks:
		print("No tasks available.")
		return

	# Enumerate through the list of tasks and display them
	for index, task in enumerate(tasks):
		status = "Completed" if task["completed"] else "Pending"
		print(f"{index + 1}. {task['description']} - {status}")

def remove_task():

	# Prompt the user to enter the number of the task to remove and remove it from the tasks list.

	view_tasks()
	try:
		task_number = int(input("Enter the task number to remove: "))
		if 1 <= task_number <= len(tasks):
			removed_task = tasks.pop(task_number - 1)
			print(f"Task '{removed_task['description']}' removed successfully.")
		else:
			print("Invalid task number.")
	except ValueError:
		print("Invalid input. Please enter a number.")

def mark_task_completed():

	# Prompt the user to enter the number of the task to mark as completed.

	view_tasks()
	try:
		task_number = int(input("Enter the task number to mark as completed: "))
		if 1 <= task_number <= len(tasks):
			tasks[task_number - 1]["completed"] = True
			print(f"Task '{tasks[task_number - 1]['description']}' marked as completed.")
		else:
			print("Invalid task number.")
	except ValueError:
		print("Invalid input. Please enter a number.")

def main():

	# Main function to run the task manager. Displays the menu and handles user input.

	while True:
		show_menu()

		choice = input("Enter your choice: ")

		# Perform action based on user's choice
		if choice == '1':
			add_task()
		elif choice == '2':
			view_tasks()
		elif choice == '3':
			remove_task()
		elif choice == '4':
			mark_task_completed()
		elif choice == '5':
			print("Exiting...")
			break
		else:
			print("Invalid choice. Please select a valid option.")

# Entry point of the program
if __name__ == "__main__":
	main()
