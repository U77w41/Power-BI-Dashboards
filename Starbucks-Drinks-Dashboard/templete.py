import os

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directories needed
dirs = [
    os.path.join(current_dir, "Data"),
    os.path.join(current_dir, "Previews"),
    os.path.join(current_dir, "Scripts"),
]

# Create the directories and write a .gitkeep file inside each directory (to allow committing empty directories to git)
for dir in dirs:
    os.makedirs(dir, exist_ok=True)
    with open(os.path.join(dir, ".gitkeep"), "w") as f:
        pass

# Files to be created
files = [
    os.path.join(current_dir, 'Documentation.md')
]

for file_ in files:
    with open(file_, "w") as f:
        pass
