# 📝 Simple Bash To-Do List

A minimalist command-line to-do list manager written in Bash. Quickly add, view, and remove tasks directly from your terminal. Your tasks are stored in a convenient `todo.txt` file in your home directory.

## ✨ Features

- Add new tasks  
- List all tasks with line numbers  
- Mark tasks as done (removes from the list)  
- Clear all tasks  
- No dependencies except Bash (works on any standard Linux system)  

## 📦 Installation

Download or copy the `todo.sh` script to your preferred location.

Make it executable:

```bash
chmod +x todo.sh
````

(Optional) Move to a directory in your `$PATH` for system-wide usage, e.g.:

```bash
sudo mv todo.sh /usr/local/bin/todo
```

## 🚀 Usage

```bash
./todo.sh add "Your task here"      # Add a new task
./todo.sh list                      # Display all tasks
./todo.sh done N                    # Mark task number N as done (removes it)
./todo.sh clear                     # Remove all tasks
./todo.sh                           # Show help/usage instructions
```

### Examples

**Add a new task:**

```bash
./todo.sh add "Buy groceries"
```

**View all tasks:**

```bash
./todo.sh list
```

**Mark the second task as done:**

```bash
./todo.sh done 2
```

**Clear all tasks:**

```bash
./todo.sh clear
```

**Get help:**

```bash
./todo.sh
```

## 📁 Notes

* All tasks are stored in `~/todo.txt`.
* Feel free to extend this script with more features such as deadlines, priorities, or notifications!

---

## 📎 GitHub Repository

[https://github.com/pvk-96/bash-todo](https://github.com/pvk-96/Streak-Maintainance/Bash/To-do)

## 📫 Contact

Email: [praneethvarmak96@gmail.com](mailto:praneethvarmakopperla@gmail.com)
GitHub: [@pvk-96](https://github.com/pvk-96)

```
```
