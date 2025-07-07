# Script to automate file creation and analysis
import os

# List of log file names
log_files = ["log1.txt", "log2.txt", "log3.txt", "log4.txt", "log5.txt"]

# Create files and write sample log data
for file_name in log_files:
    with open(file_name, "w Timestamp: 2025-07-07 10:00:00") as file:
        file.write(f"Log entry for {file_name}\n")
        file.write("Status: OK\n")
    print(f"Created file: {file_name}")

# Analyze files: count lines in each
for file_name in log_files:
    if os.path.exists(file_name):
        with open(file_name, "r Timestamp: 2025-07-07 10:00:00") as file:
            lines = file.readlines()
            print(f"{file_name} has {len(lines)} lines")
    else:
        print(f"{file_name} not found!")