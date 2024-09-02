# https://docs.python.org/3/library/pickle.html

'''Usar por sua propria conta e risco

        Eu evito ensinar! :)
'''

import pickle

# Criar objeto
obj = dict(nome='Raphael', idade=40, sexo='M')

# Salvar objeto
with open('objeto.pkl', 'wb') as f:
    pickle.dump(obj, f)

# Carregar objeto
with open('objeto.pkl', 'rb') as f:
    obj = pickle.load(f)
    print(obj)