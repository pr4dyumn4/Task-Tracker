# Task-Tracker

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Requirements
The application should:

- Run from the command line.
- Accept user actions and inputs as arguments.
- Store tasks in a JSON file.

### Features
The user should be able to:

- Add, Update, and Delete tasks.
- Mark a task as in progress or done.
- List all tasks.
- List tasks based on their status:
  - Tasks that are done.
  - Tasks that are not done.
  - Tasks that are in progress.

### Constraints
- Use positional arguments in the command line to accept user inputs.
- Use a JSON file to store the tasks in the current directory.
- The JSON file should be created if it does not exist.
- Use the native file system module of your programming language to interact with the JSON file.
- Do not use any external libraries or frameworks to build this project.
- Handle errors and edge cases gracefully.

## Commands and Usage
Below are examples of the commands and their usage:

### Adding a New Task
```bash
python main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Updating a Task
```bash
python main.py update 1 "Buy groceries and cook dinner"
# Output: Task 1 updated successfully
```

### Deleting a Task
```bash
python main.py delete 1
# Output: Task 1 deleted successfully
```

### Marking Tasks as In Progress or Done
```bash
python main.py mark-in-progress 1
# Output: Task 1 marked as in progress

python main.py mark-done 1
# Output: Task 1 marked as done
```

### Listing All Tasks
```bash
python main.py list
# Output:
# 1: Buy groceries (todo)
# 2: Complete project (in-progress)
```

### Listing Tasks by Status
#### Todo Tasks
```bash
python main.py list todo
# Output:
# 1: Buy groceries (todo)
```

#### In Progress Tasks
```bash
python main.py list in-progress
# Output:
# 2: Complete project (in-progress)
```

#### Done Tasks
```bash
python main.py list done
# Output:
# 3: Submit report (done)
```

## Task Properties
Each task will have the following properties:

- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

### JSON Structure Example
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2024-12-28T10:00:00",
    "updatedAt": "2024-12-28T10:00:00"
  }
]
```

## Getting Started

### Prerequisites
- Python installed on your system.

### Steps
1. Clone the repository.
2. Navigate to the project directory.
3. Run the following commands as per your requirement.

### Example Usage
```bash
python main.py add "Complete coding assignment"
python main.py list
python main.py mark-done 1
```

## Notes
- Ensure the `tasks.json` file is in the same directory as the `main.py` script.
- The script will create the `tasks.json` file if it does not exist.
- Project: https://roadmap.sh/projects/task-tracker

Happy coding!
