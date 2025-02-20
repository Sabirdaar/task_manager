# Task Manager CLI

A simple command-line interface (CLI) task manager built with Python. This application allows users to add, list, complete, and delete tasks using a JSON file for storage.

## Features
- Add new tasks
- List all tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage using a JSON file

## Installation
1. Ensure you have Python installed (Python 3.10+ recommended for `match-case` support).
2. Clone this repository or download the script.
3. Open a terminal and navigate to the project directory.

## Usage
Run the script using:
```sh
python task_manager.py
```

### Menu Options:
- **1**: Add a new task
- **2**: List all tasks
- **3**: Mark a task as completed
- **4**: Delete a task
- **5**: Exit the program

## JSON Storage
Tasks are stored in `tasks.json` with the following structure:
```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "completed": false
    }
]
```

## Requirements
No external dependencies—this project uses Python's built-in libraries.

## Notes
- If `tasks.json` does not exist, it will be created automatically.
- Each task is assigned a unique ID based on the highest existing ID.

## Future Improvements
- Add a due date for tasks
- Implement a search feature
- Enhance UI with color-coded output

## License
This project is open-source and available under the MIT License.

