from flask import Flask, request                                 # Importa as classes Flask e request da biblioteca Flask para criar uma aplicação web.
import pika                                                      # Importa a biblioteca json para manipulação de dados em formato JSON.
import json                                                      # Importa a biblioteca json para manipulação de dados em formato JSON.

app = Flask(__name__)                                            # Cria uma instância da aplicação Flask.

@app.route('/notificar', methods=['POST'])                       # Define um endpoint '/notificar' que aceita requisições POST.
def notificar():                                                 # Define a função que será chamada quando uma requisição for feita para o endpoint '/notificar'.
    data = request.json                                          # Recebe os dados da requisição em formato JSON e os armazena na variável 'data'.
     
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))         # Estabelece uma conexão com o RabbitMQ, usando o nome do serviço 'rabbitmq' definido no Docker Compose.
    channel = connection.channel()                               # Cria um canal de comunicação com o RabbitMQ.
    channel.queue_declare(queue='notificacoes')                  # Declara uma fila chamada notificacoes. Se a fila já existir, essa chamada não fará nada.
    channel.basic_publish(exchange='', routing_key='notificacoes', body=json.dumps(data))          # Publica a mensagem (dados) na fila 'notificacoes', convertendo os dados para formato JSON.
    connection.close()                                           # Fecha a conexão com o RabbitMQ após o envio da mensagem.
    return {'status': 'Mensagem enviada'}, 200                   # Retorna um dicionário com o status Mensagem enviada e um código de status 200 (OK).

if __name__ == '__main__':                                       # Verifica se este arquivo está sendo executado diretamente.
    app.run(host='0.0.0.0',port=8081)                           # Inicia o servidor Flask, tornando a aplicação acessível em todas as interfaces de rede na porta 8081.
