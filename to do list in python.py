'''1.	To-Do List Application:
Create a command-line or web-based to-do list application where users can add, delete, and mark tasks as completed.

'''
class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return self.name + (" (completed)" if self.completed else "")


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))

    def delete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                break

    def mark_complete(self, name):
        for task in self.tasks:
            if task.name == name:
                task.complete()
                break

    def list_tasks(self):
        for task in self.tasks:
            print(task)


def main():
    todo = ToDoList()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Quit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            name = input("Enter the name of the task: ")
            todo.add_task(name)
        elif choice == "2":
            name = input("Enter the name of the task to delete: ")
            todo.delete_task(name)
        elif choice == "3":
            name = input("Enter the name of the task to mark as completed: ")
            todo.mark_complete(name)
        elif choice == "4":
            todo.list_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
