import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        return self.data

    def preprocess_data(self):
        # Exemplo de pré-processamento
        self.data = self.data.copy()
        self.data['Age'] = self.data['Age'].fillna(self.data['Age'].mean())
        self.data['Fare'] = self.data['Fare'].fillna(self.data['Fare'].mean())
        self.data = self.data.dropna(subset=['Embarked'])
        return self.data
