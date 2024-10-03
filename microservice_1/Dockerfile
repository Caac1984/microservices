FROM python:3.9
   # Define a imagem base como Python 3.9. Esta imagem já contém o interpretador Python e suas bibliotecas essenciais.
WORKDIR /app
   # Define o diretório de trabalho dentro do container como /app. Todos os comandos subsequentes serão executados neste diretório.
COPY requerimentos.txt .
   # Copia o arquivo 'requerimentos.txt' do diretório local para o diretório de trabalho (/app) no container.
RUN pip install -r requerimentos.txt
   # Executa o comando 'pip install' para instalar todas as dependências listadas em 'requerimentos.txt'.
COPY app.py .
   # Copia o arquivo 'app.py' do diretório local para o diretório de trabalho (/app) no container.
CMD ["python", "app.py"]
   # Define o comando padrão a ser executado quando o container for iniciado: executa o script 'app.py' com o interpretador Python.
