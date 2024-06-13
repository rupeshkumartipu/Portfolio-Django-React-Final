import os
import subprocess
0
# Directory where your command files are located
commands_dir = 'portfolio_app/management/commands'

# List all the files in the commands directory
command_files = os.listdir(commands_dir)

# Loop through each file
for command_file in command_files:
    # Skip __pycache__ directory
    if command_file == '__pycache__':
        continue

    # Get the command name by removing the '.py' extension
    command_name = command_file[:-3]

    # Run the command
    result = subprocess.run(['python', 'manage.py', command_name], capture_output=True, text=True)
    print(f'Running {command_name}...')
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
