from flask import Flask, render_template, request
from db_connect import get_team_data
from math import exp, factorial

app = Flask(__name__)

# Poisson distribution
def getPoissionDistribution(lmb: int):
    List = []
    for i in range(0, 100):
        List.append((lmb ** i) * exp(-lmb) / factorial(i))
    return List

# Calculates team's win percentage
def calculateWinProc(List1: list, List2: list):
    winProc = []
    for i in range(1, len(List1)):
        winProc.append(round(List1[i] * sum(List2[0:i - 1]), 4) * 100)
    return sum(winProc)

# Calculating win percentage of teams and percentage of tie
def makePredict(ATT1, DEF1, ATT2, DEF2):
    avg_goals = 0.537256562
    lmb1 = ATT1 * DEF2 * avg_goals
    lmb2 = ATT2 * DEF1 * avg_goals

    List1 = getPoissionDistribution(lmb1)
    List2 = getPoissionDistribution(lmb2)

    winProc1 = round(calculateWinProc(List1, List2), 2)
    winProc2 = round(calculateWinProc(List2, List1), 2)
    #tie = round(100 - winProc1 - winProc2, 5)

    return winProc1, winProc2

# Retrieve team data from database
def findData(Komanda1, Komanda2):
    team_data = get_team_data(Komanda1, Komanda2)
    if team_data and len(team_data) == 2:
        ATT1, DEF1 = float(team_data[0]['ATT_Rating']), float(team_data[0]['DEF_Rating'])
        ATT2, DEF2 = float(team_data[1]['ATT_Rating']), float(team_data[1]['DEF_Rating'])
        return ATT1, DEF1, ATT2, DEF2
    else:
        raise ValueError("Unable to retrieve team data.")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        team1 = request.form.get("first_team")
        team2 = request.form.get("second_team")
        if team1 and team2:
            try:
                ATT1, DEF1, ATT2, DEF2 = findData(team1, team2)
                win1, win2 = makePredict(ATT1, DEF1, ATT2, DEF2)
                return render_template("index.html", first_team=team1, second_team=team2, winProc1=win1, winProc2=win2)
            except ValueError as e:
                return render_template("index.html", error=str(e))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
