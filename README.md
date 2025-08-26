
# Basketball Shot Analytics Project

This is a simple data analytics project written in Python that analyzes basketball shot data from a CSV file.
It calculates field goal percentage (FG%) overall, by distance, and by location, and produces charts.

## Files included:
- analyze_shots.py — main Python script
- shots_sample.csv — sample data of basketball shots
- requirements.txt — Python libraries needed
- .gitignore — ignores temporary files
- README.md — this file

## How to run:
1. Install Python 3.11+
2. Open a terminal (Command Prompt on Windows)
3. Navigate to the project folder:
   ```
   cd "C:\Users\Mohamed\Basketball Shot Chart"
   ```
4. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
5. Install requirements:
   ```
   pip install -r requirements.txt
   ```
6. Run the script:
   ```
   python analyze_shots.py
   ```

This will generate:
- summary_overall.txt
- summary_by_distance.csv
- summary_by_location.csv
- fg_by_distance.png
- fg_by_location.png

Upload this project to GitHub as your first portfolio project.
