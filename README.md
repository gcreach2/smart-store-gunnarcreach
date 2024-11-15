# smart-store-gunnarcreach
# P1. Project Start & Planning
# Smart Store Data Preparation Project

# Smart Store - GunnarCreach
## P1. Project Start & Planning

## Smart Store Data Preparation Project

This project is focused on essential data preparation techniques in Python, including setting up a Git-based project, creating a virtual environment, and working with data through libraries like Pandas.

### Project Setup Guide



```bash
# 1. Create a Virtual Environment for the Project
python3 -m venv .venv

# 2. Activate the Virtual Environment
source .venv/bin/activate  # For macOS/Linux
# On Windows: .\.venv\Scripts\activate

# 3. Install Project Dependencies
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade -r requirements.txt

# 4. Organize Project Files
# Create utils/logger.py: In VS Code, create a folder named 'utils'.
# Inside this folder, create a file named 'logger.py' and add the starter code from the starter repository.
# Create scripts/data_prep.py: In VS Code, create another folder named 'scripts'.
# Inside this folder, create a file named 'data_prep.py' and add the starter code from the starter repository.

# 5. Set Up the SQLite Database
# Use scripts/create_dw.py to define and initialize your data warehouse schema.
python3 scripts/create_dw.py

# 6. Clean and Prepare the Data
# Use the reusable DataScrubber class and data preparation scripts.
python3 scripts/data_prep.py

# 7. Run Unit Tests for Data Cleaning
# Validate data cleaning methods with the test suite.
PYTHONPATH=. python3 tests/test_data_scrubber.py

# 8. Commit and Push Changes to GitHub
git add .
git commit -m "Add completed project files"
git push -u origin main

smart-store-gunnarcreach/
├── .venv/                     # Virtual environment
├── data/
│   ├── raw/                   # Raw data files
│   ├── prepared/              # Cleaned and prepared data files
│   ├── dw/                    # SQLite database storage
├── scripts/
│   ├── create_dw.py           # Database schema setup
│   ├── data_prep.py           # Data preparation script
│   ├── data_scrubber.py       # DataScrubber class for cleaning
├── tests/
│   ├── test_data_scrubber.py  # Unit tests for DataScrubber
├── utils/
│   ├── logger.py              # Logger utility
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to exclude from Git
