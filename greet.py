# Simple script to greet a user and check system status
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to AI Ops.")

# Simulate a system check
disk_space = 20  # Example disk space in GB
if disk_space > 30:
    print("System status: Disk space is sufficient.")
else:
    print("Warning: Low disk space!")
    