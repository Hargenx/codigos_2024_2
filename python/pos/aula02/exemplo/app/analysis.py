import pandas as pd
import matplotlib.pyplot as plt

class Analysis:
    def __init__(self, data):
        self.data = data

    def survival_rate(self):
        return self.data['Survived'].mean()

    def plot_age_distribution(self):
        fig, ax = plt.subplots()
        ax.hist(self.data['Age'], bins=20, color='skyblue', edgecolor='black')
        ax.set_title('Distribuição de Idade')
        ax.set_xlabel('Idade')
        ax.set_ylabel('Frequência')
        return fig
