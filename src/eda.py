import matplotlib.pyplot as plt
import seaborn as sns

def plot_readmission(df):
    sns.countplot(x='readmitted', data=df)
    plt.title("Readmission Distribution")
    plt.savefig("visuals/readmission.png")
    plt.close()

def plot_age(df):
    plt.figure(figsize=(10,5))
    sns.histplot(df['age'], bins=10)
    plt.title("Age Distribution")
    plt.savefig("visuals/age.png")
    plt.close()

def correlation_heatmap(df):
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(), cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.savefig("visuals/heatmap.png")
    plt.close()
