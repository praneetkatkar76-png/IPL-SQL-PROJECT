IPL Data Analysis Project

Project Overview

This project analyzes IPL (Indian Premier League) match data using Python, SQLite, Pandas, and Matplotlib. The objective is to perform SQL-based analysis and visualize important insights from IPL matches.

Technologies Used

- Python
- SQLite
- Pandas
- Matplotlib
- VS Code

Dataset Information

The dataset contains the following fields:

- Match ID
- Season
- Team 1
- Team 2
- Toss Winner
- Match Winner
- Player of the Match
- Venue

Analysis Performed

SQL Queries

1. Display first 10 matches
2. Most winning teams
3. Top Players of the Match
4. Toss impact analysis
5. Venue analysis
6. Season-wise winners
7. Toss winners count
8. Teams winning after losing toss
9. Team participation count
10. Matches per season
11. Unique teams count
12. Venue-wise winning teams

Data Visualizations

- Most Winning Teams (Bar Chart)
- Top Players of the Match (Bar Chart)
- Toss Impact Analysis (Pie Chart)
- Venue Analysis (Bar Chart)

Key Insights

- CSK and MI are among the most successful teams in the dataset.
- Winning the toss has a noticeable impact on match outcomes.
- Certain venues host more IPL matches than others.
- Player of the Match awards highlight important individual performances.
- Team participation and venue trends provide useful IPL insights.

Project Structure

IPL-SQL-PROJECT/

├── analysis.py

├── matches.csv

├── ipl.db

├── README.md

└── Screenshots/

  ├── Most_Winning_teams.png

  ├── Top_Players.png

  ├── Toss_impact.png

  └── Venue_analysis.png

How to Run the Project

1. Install required libraries:

pip install pandas matplotlib

2. Open the project in VS Code.

3. Run the script:

python analysis.py

4. View query results in the terminal and charts in separate windows.

Future Enhancements

- Interactive dashboard using Streamlit
- Larger IPL dataset
- Advanced statistical analysis
- Additional visualizations and filters

Author

Praneet Katkar

B.Sc. Information Technology
