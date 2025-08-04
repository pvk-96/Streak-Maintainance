#!/bin/bash

TODO_FILE="$HOME/todo.txt"

show_help() {
    echo "Simple Todo List"
    echo "Usage:"
    echo "  $0 add \"Task\"    # Add new task"
    echo "  $0 list           # Show all tasks"
    echo "  $0 done N         # Mark task N as done (remove)"
    echo "  $0 clear          # Remove all tasks"
}

add_task() {
    echo "$1" >> "$TODO_FILE"
    echo "Added: $1"
}

list_tasks() {
    if [[ ! -s "$TODO_FILE" ]]; then
        echo "No tasks found!"
        return
    fi
    nl -w2 -s'. ' "$TODO_FILE"
}

remove_task() {
    sed -i "${1}d" "$TODO_FILE"
    echo "Removed task $1"
}

clear_tasks() {
    > "$TODO_FILE"
    echo "All tasks cleared."
}

case "$1" in
    add)
        shift
        add_task "$*"
        ;;
    list)
        list_tasks
        ;;
    done)
        remove_task "$2"
        ;;
    clear)
        clear_tasks
        ;;
    *)
        show_help
        ;;
esac
