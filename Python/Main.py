import os
import subprocess
import signal
import sys


# Function to start a subprocess for Main.py in a directory
def start_main_py(directory):
    main_script_path = os.path.join(directory, "Main.py")
    process = subprocess.Popen(["python3", main_script_path])
    return process


# Signal handler for termination
def signal_handler(sig, frame):
    print("\nStopping processes...")
    for process in running_processes:
        process.terminate()
    sys.exit(0)


# Register signal handler for termination signals
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Determine the path to the Clients directory
current_file_path = os.path.abspath(__file__)
# Replace "Python" with "Clients" in the path
clients_directory = os.path.join(
    os.path.dirname(current_file_path).replace("Python", "Clients")
)

# List all directories in the Clients directory
directories = [
    os.path.join(clients_directory, name)
    for name in os.listdir(clients_directory)
    if os.path.isdir(os.path.join(clients_directory, name))
]

# List to keep track of running processes
running_processes = []

# Start Main.py in each directory
for directory in directories:
    process = start_main_py(directory)
    running_processes.append(process)
    print(f"Started process for {directory} (PID: {process.pid})")

# Wait for processes to finish
for process in running_processes:
    process.wait()
