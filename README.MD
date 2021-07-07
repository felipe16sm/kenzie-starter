# Comando para instalação e incialização do projeto

```sh

docker-compose up

```

# Comandos para Carregar arquivo csv no banco de dados

<h2>Listar containers:</h2>

```sh

docker ps

```

<h2>Copie o id do container kenzie_starter_web e execute o seguinte comando:</h2>

```sh

sudo docker exec -it id_do_kenzie_starter_web /bin/bash

```

<h2>Execute o seguinte comando para carregar o arquivo Kickstarter.csv no banco de dados </h2>

```sh

./manage.py load_projects Kickstarter.csv

```

# Sobre o projeto

<p>Este projeto simula um sistema de consulta de uma plataforma de financiamento coletivo. O arquivo Kickstarter.csv possui centenas de milheres de registros e por isso demora para ser carregado no banco de dados. A grande quantidade de registros nesse projeto tem a finalidade de testar a eficiência do sistema de consultas ao banco de dados. </p>

<p>Algumas técnicas como indexação e paginação foram utilizadas para se reduzir o tempo de consulta das queries.</p>
