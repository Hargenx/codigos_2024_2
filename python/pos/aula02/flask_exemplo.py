from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home() -> str:
    '''

    Retorna uma mensagem de boas-vindas.

    args:
        None
    
    return: 
        uma mensagem de boas-vindas

    '''
    return jsonify(message="Oi mamãe e papai!")

if __name__ == '__main__':
    app.run(debug=True)
