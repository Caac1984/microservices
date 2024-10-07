# Sistema Distribuído com Microserviços

Este projeto contém dois microserviços utilizando Flask e RabbitMQ para comunicação.

## Estrutura do Projeto

   #      microservico_1: Microserviço que recebe requisições para processar pagamentos.
   #      microservico_2: Microserviço que recebe notificações e envia mensagens para o RabbitMQ.

- Docker
- Docker Compose

## Como Subir os Serviços

# 1 - Clone este repositório.
       git clone
       cd microservices
# 2 - Navegue até a pasta do projeto.
# 3 - Execute o comando:

```bash
docker-compose up --build    (Esse comando irá construir as imagens Docker
para os microserviços e iniciar todos os serviços definidos no docker-compose.yml.)
_____________________________________________________________________________________________

  #  Verificar se os Serviços Estão Funcionando
  #  Microserviço 1: Acesse http://localhost:8080/pagar
  #  Microserviço 2: Acesse http://localhost:8081/notificar
RabbitMQ: Acesse a interface de gerenciamento em http://localhost:15672 (usuário: guest, admin, senha: guest, 123)

# A combinação de microsserviços Python e Docker permite um desenvolvimento simples, ágil, uma implantação mais eficiente e a capacidade de lidar com cargas variáveis.