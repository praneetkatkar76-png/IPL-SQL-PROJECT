import pandas as pd
import sqlite3

# Step 1: Load dataset
df = pd.read_csv("matches.csv")

# Step 2: Create SQLite database
conn = sqlite3.connect("ipl.db")

import pandas as pd
import sqlite3

conn = sqlite3.connect("ipl.db")

print("\n================ IPL DATA ANALYSIS ================\n")

# 1. Show first 10 rows
print("📊 First 10 Matches:")
query1 = "SELECT * FROM matches LIMIT 10"
df1 = pd.read_sql(query1, conn)
print(df1)

# 2. Most winning teams
print("\n🏆 Most Winning Teams:")
query2 = """
SELECT winner, COUNT(*) AS total_wins
FROM matches
GROUP BY winner
ORDER BY total_wins DESC
"""
df2 = pd.read_sql(query2, conn)
print(df2)

# 3. Top players of match
print("\n🌟 Top Players of Match:")
query3 = """
SELECT player_of_match, COUNT(*) AS awards
FROM matches
GROUP BY player_of_match
ORDER BY awards DESC
"""
df3 = pd.read_sql(query3, conn)
print(df3)

# 4. Toss impact analysis
print("\n🪙 Toss Impact:")
query4 = """
SELECT
CASE
WHEN toss_winner = winner THEN 'Won after Toss'
ELSE 'Lost after Toss'
END AS toss_result,
COUNT(*) AS matches
FROM matches
GROUP BY toss_result
"""
df4 = pd.read_sql(query4, conn)
print(df4)

# 5. Venue analysis
print("\n🏟️ Venue Analysis:")
query5 = """
SELECT venue, COUNT(*) AS matches_played
FROM matches
GROUP BY venue
ORDER BY matches_played DESC
"""
df5 = pd.read_sql(query5, conn)
print(df5)

# 6. Season-wise Winners
print("\n📅 Season-wise Winners:")
query6 = """
SELECT season, winner
FROM matches
ORDER BY season
"""
print(pd.read_sql(query6, conn))

# 7. Toss Winners Count
print("\n🪙 Toss Winners Count:")
query7 = """
SELECT toss_winner, COUNT(*) AS toss_wins
FROM matches
GROUP BY toss_winner
ORDER BY toss_wins DESC
"""
print(pd.read_sql(query7, conn))

# 8. Teams Winning After Losing Toss
print("\n🔥 Teams Winning After Losing Toss:")
query8 = """
SELECT winner, COUNT(*) AS wins_after_losing_toss
FROM matches
WHERE toss_winner != winner
GROUP BY winner
ORDER BY wins_after_losing_toss DESC
"""
print(pd.read_sql(query8, conn))

# 9. Team Participation Count
print("\n🏏 Team Participation Count:")
query9 = """
SELECT team, COUNT(*) AS matches_played
FROM (
    SELECT team1 AS team FROM matches
    UNION ALL
    SELECT team2 AS team FROM matches
)
GROUP BY team
ORDER BY matches_played DESC
"""
print(pd.read_sql(query9, conn))

# 10. Matches Per Season
print("\n📊 Matches Per Season:")
query10 = """
SELECT season, COUNT(*) AS total_matches
FROM matches
GROUP BY season
ORDER BY season
"""
print(pd.read_sql(query10, conn))

# 11. Unique Teams Count
print("\n👥 Total Unique Teams:")
query11 = """
SELECT COUNT(DISTINCT team) AS total_teams
FROM (
    SELECT team1 AS team FROM matches
    UNION
    SELECT team2 AS team FROM matches
)
"""
print(pd.read_sql(query11, conn))

# 12. Venue-wise Winning Teams
print("\n🏟️ Venue-wise Winning Teams:")
query12 = """
SELECT venue, winner, COUNT(*) AS wins
FROM matches
GROUP BY venue, winner
ORDER BY wins DESC
"""
print(pd.read_sql(query12, conn))

import matplotlib.pyplot as plt

# Chart 1 - Most Winning Teams
df2.plot(
    x='winner',
    y='total_wins',
    kind='bar',
    title='Most Winning Teams'
)
plt.tight_layout()
plt.show()

# Chart 2 - Top Players of the Match
df3.plot(
    x='player_of_match',
    y='awards',
    kind='bar',
    title='Top Players of the Match'
)
plt.tight_layout()
plt.show()

# Chart 3 - Toss Impact
df4.plot(
    y='matches',
    kind='pie',
    labels=df4['toss_result'],
    autopct='%1.1f%%',
    title='Toss Impact Analysis'
)
plt.ylabel('')
plt.tight_layout()
plt.show()

# Chart 4 - Matches Played by Venue
df5.plot(
    x='venue',
    y='matches_played',
    kind='bar',
    title='Matches Played by Venue'
)
plt.tight_layout()
plt.show()

print("\n================ END OF REPORT ================\n")

