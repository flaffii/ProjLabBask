from flask import Flask, render_template, request
from math import exp, factorial
from db_connect import get_team_data  # Import the function from db_connect

app = Flask(__name__)

def getPoissionDistribution(lmb: int):
    List = []
    for i in range(0, 31):
        List.append((lmb ** i) * exp(-lmb) / factorial(i))
    return List

def calculateWinProc(List1: list, List2: list):
    winProc = []
    for i in range(1, len(List1)):
        winProc.append(round(List1[i] * sum(List2[0:i]), 4) * 100)
    return sum(winProc)

def makePredict(ATT1, DEF1, ATT2, DEF2, avg_goals):
    lmb1 = ATT1 * DEF2 * avg_goals
    lmb2 = ATT2 * DEF1 * avg_goals

    List1 = getPoissionDistribution(lmb1)
    List2 = getPoissionDistribution(lmb2)

    winProc1 = round(calculateWinProc(List1, List2), 2)
    winProc2 = round(calculateWinProc(List2, List1), 2)
    tie = round(100 - winProc1 - winProc2, 2)

    return winProc1, winProc2, tie

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data for team names
        team1 = request.form['team1']
        team2 = request.form['team2']
        avg_goals = float(request.form['avg_goals'])  
        
        # Fetch data for the specified teams from the database
        teams_data = get_team_data(team1, team2)
        
        if teams_data and len(teams_data) == 2:
            # Extract team data
            team1_data = teams_data[0]
            team2_data = teams_data[1]
            
            # Assign variables from database data for calculations
            ATT1 = team1_data['ATT_Rating']
            DEF1 = team1_data['DEF_Rating']
            ATT2 = team2_data['ATT_Rating']
            DEF2 = team2_data['DEF_Rating']
            

            # Calculate predictions
            winProc1, winProc2, tie = makePredict(ATT1, DEF1, ATT2, DEF2, avg_goals)
            
            return render_template('index.html', team1=team1, team2=team2, winProc1=winProc1, winProc2=winProc2, tie=tie)
        else:
            # Handle case where team data isn't found
            error_message = "One or both teams not found in the database."
            return render_template('index.html', error_message=error_message, winProc1=None, winProc2=None, tie=None)

    return render_template('index.html', winProc1=None, winProc2=None, tie=None)

if __name__ == '__main__':
    app.run()
