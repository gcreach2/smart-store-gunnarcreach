# smart-store-gunnarcreach
# P1. Project Start & Planning
# Smart Store Data Preparation Project

This project is focused on essential data preparation techniques in Python, including setting up a Git-based project, creating a virtual environment, and working with data through libraries like Pandas.

## Project Setup Guide

Follow these steps to set up and configure your project environment on macOS.

### 1. Create a Virtual Environment for the Project

Start by creating a virtual environment using `python3`. This environment will isolate your project's dependencies.

```bash
python3 -m venv .venv

### 2. Activate the Virtual Environment

source .venv/bin/activate

### 3. Install Project Dependencies

python3 -m pip install --upgrade -r requirements.txt

### 4. Organize Project Files

Create utils/logger.py: In VS Code, make a folder called utils. Inside this folder, create a file named logger.py and add the starter code provided in the starter repository.

Create scripts/data_prep.py: In VS Code, create another folder called scripts. Inside this folder, create a file named data_prep.py and add the starter code provided in the starter repository.

### 5. Run the Data Preparation Script

python3 scripts/data_prep.py

### 6. Commit and Push Changes to GitHub

git add .
git commit -m "Add starter files"
git push -u origin main
