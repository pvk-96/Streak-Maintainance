#!/bin/bash

# Thresholds (in %)
CPU_LIMIT=50
MEM_LIMIT=30

echo "🔍 Checking for processes using more than $CPU_LIMIT% CPU or $MEM_LIMIT% Memory..."

# Get processes over limits
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | \
awk -v cpu="$CPU_LIMIT" -v mem="$MEM_LIMIT" 'NR>1 && ($4>mem || $5>cpu) {print $0}'

echo
read -p "Enter PID to kill (or press Enter to skip): " PID

if [[ -n "$PID" ]]; then
    if kill -9 "$PID" 2>/dev/null; then
        echo "✅ Process $PID killed."
    else
        echo "❌ Failed to kill process $PID."
    fi
else
    echo "No process killed."
fi
