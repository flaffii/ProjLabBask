from flask import Flask, render_template, request
from math import exp, factorial

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
        # Retrieve form data
        ATT1 = float(request.form['ATT1'])
        DEF1 = float(request.form['DEF1'])
        ATT2 = float(request.form['ATT2'])
        DEF2 = float(request.form['DEF2'])
        avg_goals = float(request.form['avg_goals'])
        
        # Calculate predictions
        winProc1, winProc2, tie = makePredict(ATT1, DEF1, ATT2, DEF2, avg_goals)
        
        return render_template('index.html', winProc1=winProc1, winProc2=winProc2, tie=tie)

    return render_template('index.html', winProc1=None, winProc2=None, tie=None)

if __name__ == '__main__':
    app.run()
