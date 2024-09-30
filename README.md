# Sistema Distribuído com Microserviços

Este projeto contém dois microserviços utilizando Flask e RabbitMQ para comunicação.

## Estrutura do Projeto

   #      microservice_1: Microserviço que recebe requisições para processar pagamentos.
   #      microservice_2: Microserviço que recebe notificações e envia mensagens para o RabbitMQ.

# Requisitos

- Docker
- Docker Compose

## Como Subir os Serviços

# 1 - Clone este repositório.
# 2 - Navegue até a pasta do projeto.
# 3 - Execute o comando:

   ```bash
   docker-compose up --build    (Esse comando irá construir as imagens Docker
      para os microserviços e iniciar todos os serviços definidos no docker-compose.yml.)
_____________________________________________________________________________________________

  #  Verificar se os Serviços Estão Funcionando
  #  Microserviço 1: Acesse http://localhost:5000/pagar.
  #  Microserviço 2: Acesse http://localhost:5001/notificar (não acessível diretamente, é um endpoint de notificação).
RabbitMQ: Acesse a interface de gerenciamento em http://localhost:15672 (usuário: guest, senha: guest).

