from flask import Flask, request         # Importa as classes Flask e request da biblioteca Flask.
import requests                          # Importa a biblioteca requests para fazer requisições HTTP.

app = Flask(Pagamento_teste_)                    # Cria uma instância da aplicação Flask.

@app.route('/pagar', methods=['POST'])   # Define um endpoint '/pagar' que aceita requisições POST.
def pagar():                             # Define a função que será chamada quando uma requisição for feita para o endpoint '/pagar

    data = request.json                  # Recebe os dados da requisição em formato JSON e os armazena na variável 'data'.
    response = requests.post('http://microservico_2:8081/notificar', json=data)    # Faz uma requisição POST para o Microserviço 2, enviando os dados recebidos.
    return response.json(), response.status_code                                   # Retorna a resposta do Microserviço 2, incluindo o corpo da resposta em formato JSON e o status da resposta.

if __name__ == '__main__':               # Verifica se este arquivo está sendo executado diretamente.
    app.run(host='0.0.0.0', port=8080)   # Inicia o servidor Flask, tornando a aplicação acessível em todas as interfaces de rede na porta 8080.
