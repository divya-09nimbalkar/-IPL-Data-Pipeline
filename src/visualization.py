import matplotlib.pyplot as plt
import seaborn as sns

def plot_runs(df):
    plt.figure(figsize=(8,5))
    plt.bar(df["team1"], df["runs_team1"], label="Team1 Runs")
    plt.bar(df["team2"], df["runs_team2"], label="Team2 Runs")
    plt.xticks(rotation=45)
    plt.title("Runs by Teams")
    plt.ylabel("Runs")
    plt.legend()
    plt.show()

def plot_winners(df):
    plt.figure(figsize=(6,4))
    sns.countplot(x="winner", data=df)
    plt.title("Match Winners")
    plt.show()
