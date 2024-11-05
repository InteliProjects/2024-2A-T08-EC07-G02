# Docker

Segundo a AWS, o Docker é uma plataforma de estruturação em contêiner que você pode usar para empacotar software em contêineres e executá-los nas máquinas de destino. Os contêineres do Docker são executados em qualquer máquina ou máquina virtual em que o mecanismo do Docker esteja instalado. E eles são executados sem o conhecimento da arquitetura subjacente do sistema. O mecanismo Docker só funciona no sistema operacional Linux. Um contêiner do Docker é um contêiner feito usando a plataforma de estruturação em contêiner Docker; há também outras plataformas de estruturação em contêiner menos populares.[1]

## Containers

Um contêiner do Docker é um ambiente de runtime com todos os componentes necessários, como código, dependências e bibliotecas, necessários para executar o código da aplicação sem usar dependências da máquina host. Esse runtime de contêiner é executado no mecanismo em um servidor, máquina ou instância de nuvem. O mecanismo opera vários contêineres, dependendo dos atributos subjacentes disponíveis.[3]

### Funcionamento dos Containers

Os contêineres são possíveis por meio de isolamento de processos e recursos de virtualização incorporados no kernel do Linux. Esses recursos incluem grupos de controle (Cgroups) para alocar recursos entre processos e namespaces para restringir o acesso ou a visibilidade de um processo a outros recursos ou áreas do sistema.

Os contêineres permitem que múltiplos componentes de aplicações compartilhem os recursos de uma única instância do sistema operacional host. Esse compartilhamento é semelhante a como um hipervisor permite que várias Virtual Machines (VMs) compartilhem uma única unidade de processamento central (CPU) do servidor de hardware, memória e outros recursos.[2]

A tecnologia de contêineres oferece todas as funções e benefícios das Virtual Machines (VMs), incluindo isolamento de aplicações e escalabilidade econômica, além de outras vantagens significativas:

- **Menor peso**: ao contrário das VMs, os contêineres não carregam a carga de uma instância inteira de SO e hipervisor. Eles incluem apenas os processos e dependências do SO necessários para executar o código. Os tamanhos dos contêineres são medidos em megabytes (em vez de gigabytes para algumas VMs), fazem melhor uso da capacidade de hardware e têm tempos de inicialização mais rápidos.

- **Produtividade melhorada**: aplicações conteinerizadas podem ser escritas uma vez e executadas em qualquer lugar. Em comparação com as VMs, os contêineres são mais rápidos e fáceis de implementar, provisionar e reiniciar.

- **Maior eficiência**: com os contêineres, os desenvolvedores podem executar o mesmo número de cópias de uma aplicação no mesmo hardware do que ao usar VMs. Essa eficiência pode reduzir os gastos com a nuvem.

## Dockers utilizados no projeto

### Arquivo Dockerfile.dev

Este `Dockerfile.dev` é utilizado para criar uma imagem Docker leve e otimizada, configurada para o ambiente de desenvolvimento do projeto em Python. Ele utiliza a imagem base `python:3.10-slim`, uma versão reduzida do Python 3.10, ideal para minimizar o tamanho da imagem e acelerar o tempo de build, mantendo apenas o essencial para rodar a aplicação.

#### Passos do Dockerfile

1. **Definir a Imagem Base:**

   O primeiro passo do Dockerfile é definir a imagem base a partir da qual o container será construído. Neste caso, a imagem oficial `python:3.10-slim` é utilizada, que contém uma versão leve do Python.

   ```
   dockerfile
   FROM python:3.10-slim
   ```

2. **Criar e Definir o Diretório de Trabalho:**

    O comando WORKDIR /app cria e define o diretório de trabalho dentro do container, onde o código do projeto será armazenado e executado.
    WORKDIR/app

3. **Copiar Arquivos para o Container:**

    O comando COPY . . é responsável por copiar todos os arquivos e pastas do diretório atual, onde o Dockerfile está localizado, para o diretório de trabalho dentro do container (/app).
    ```
    COPY ..
    ```

4. **Instalação de Dependências:**

    O comando RUN pip install -r requirements.txt executa o instalador pip para garantir que todas as bibliotecas listadas no arquivo requirements.txt sejam instaladas dentro do ambiente do container.

    ```
    RUN pip install -r requirements.txt
    ```

#### Utilização do Dockerfile

##### Construir a Imagem Docker

Para construir a imagem Docker, utilize o seguinte comando:

```
docker build -f Dockerfile.dev -t nome_da_imagem_dev .
```

-f: Especifica qual arquivo Dockerfile deve ser utilizado (neste caso, Dockerfile.dev).
-t: Nomeia a imagem que será criada.

##### Executar Container
```
docker run -it --rm -v $(pwd):/app nome_da_imagem_dev
```
-it: Executa o container em modo interativo.
--rm: Garante que o container será removido automaticamente após ser finalizado.
-v $(pwd):/app: Mapeia o diretório atual do projeto para o diretório /app no container, permitindo que alterações feitas no código local sejam refletidas no container sem necessidade de reconstruir a imagem.

### Arquivo Dockerfile.duckdb

O `Dockerfile.duckdb` configura um ambiente Docker contendo o DuckDB, uma ferramenta de banco de dados leve, na sua versão CLI (Command Line Interface). A imagem base escolhida é o **Debian bullseye**, que oferece uma fundação estável e confiável para a execução do DuckDB.

#### 1. Imagem Base

O primeiro comando no Dockerfile é:
```dockerfile
FROM debian:bullseye
```

Essa escolha garante que o container terá um sistema operacional leve e seguro, ideal para rodar aplicativos como o DuckDB. O Debian é amplamente conhecido pela sua estabilidade, o que o torna uma escolha comum para ambientes de produção.

#### 2. Definição do Diretório de Trabalho

A seguir, o comando:
```
WORKDIR /database
```
define o diretório de trabalho como /database. Esse diretório será o local onde o DuckDB irá armazenar e acessar os dados. Caso o diretório não exista, ele será automaticamente criado.

#### 3. Atualização do Sistema e Instalação de Pacotes

Para garantir que o ambiente está atualizado e que as ferramentas necessárias estão instaladas, usamos o comando:
```
RUN apt-get update && apt-get install -y wget unzip && rm -rf /var/lib/apt/lists/*
```
Este comando realiza três tarefas:

    1. Atualiza o cache de pacotes do Debian.
    2. Instala os pacotes wget (para downloads) e unzip (para descompactar arquivos).
    3. Remove o cache de pacotes após a instalação, otimizando o tamanho final da imagem.

#### 4. Download e Instalação do DuckDB CLI

O DuckDB CLI é baixado diretamente do repositório oficial no GitHub. O comando utilizado é:
```
RUN wget https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip
```

Aqui, estamos baixando a versão 1.0.0 do binário. Após o download, o arquivo é descompactado e movido para o diretório /usr/local/bin:
```
RUN unzip duckdb_cli-linux-amd64.zip -d /usr/local/bin && rm duckdb_cli-linux-amd64.zip
```
Essa etapa garante que o DuckDB CLI esteja disponível no PATH do container, permitindo sua execução direta.

#### 5. Comando Padrão de Execução

O comando final do Dockerfile é o CMD, que define o comportamento padrão quando o container é iniciado:
```
CMD ["duckdb", "--version"]
```
Este comando executa o DuckDB e exibe a versão instalada, sendo uma verificação simples para garantir que tudo foi configurado corretamente.

### Arquivo docker-compose-db.yml

Este arquivo `docker-compose-db.yml` é utilizado para orquestrar o ambiente de banco de dados utilizando Docker Compose. Ele define dois serviços principais: um serviço PostgreSQL e um serviço DuckDB (atualmente desativado), permitindo a configuração e gerenciamento de bancos de dados em containers Docker de maneira eficiente e automatizada.

#### Serviço PostgreSQL

O serviço **PostgreSQL** é configurado utilizando a imagem oficial mais recente do banco de dados PostgreSQL (`postgres:latest`). Este container cria e configura um ambiente PostgreSQL pronto para uso. 

- O container é nomeado como `postgres` através do parâmetro `container_name: postgres`, facilitando a identificação e gerenciamento do container dentro do ambiente Docker.
  
- As portas do PostgreSQL são mapeadas entre o host e o container. A linha `ports: - '5432:5432'` garante que a porta padrão 5432 do PostgreSQL seja acessível tanto no host quanto no container, permitindo a conexão ao banco de dados a partir de aplicações externas ao container.

- Mapeamento de portas: A linha ports: - '5432:5432' mapeia a porta padrão 5432 do PostgreSQL entre o host e o container. Isso permite que aplicações externas ao container possam se conectar ao banco de dados PostgreSQL de forma transparente.


Configurações via variáveis de ambiente: O bloco environment define as principais configurações do banco de dados através de variáveis de ambiente:

- O bloco `environment` define variáveis de ambiente que configuram o banco de dados PostgreSQL. Estas variáveis são:
    - `POSTGRES_USER`: Define o nome de usuário do banco de dados como `postgres`.
    - `POSTGRES_PASSWORD`: Define a senha do banco de dados como `postgres`.
    - `POSTGRES_DB`: Cria um banco de dados inicial chamado `postgres` ao iniciar o container.

- Persistência de dados: Para garantir que os dados não sejam perdidos ao interromper ou remover o container, o volume `volumes: - ./.cache/postgres:/var/lib/postgresql/data` é utilizado. Esse volume monta o diretório `.cache/postgres` do sistema de arquivos do host no diretório `/var/lib/postgresql/data` dentro do container, garantindo a persistência dos dados do banco de dados.

### Arquivo docker-compose-dev.yml
O arquivo `docker-compose-dev.yml` é utilizado para configurar um ambiente de desenvolvimento completo para o projeto, utilizando Docker Compose para orquestrar os serviços de banco de dados PostgreSQL e o ambiente de desenvolvimento da aplicação. Ele permite que os desenvolvedores executem facilmente o projeto em containers isolados, garantindo consistência e eficiência no processo de desenvolvimento.

## Serviços

### 1. Serviço PostgreSQL

O serviço **PostgreSQL** neste arquivo estende a configuração definida no `docker-compose-db.yml`. Isso significa que o serviço PostgreSQL será configurado exatamente como definido naquele arquivo, reutilizando a imagem, as variáveis de ambiente e a configuração de volumes. A linha `extends: file: docker-compose-db.yml, service: postgres` é responsável por isso.

Essa abordagem evita duplicação de código e mantém a configuração do PostgreSQL separada do ambiente de desenvolvimento da aplicação, permitindo fácil manutenção e escalabilidade. Assim, o serviço de banco de dados está configurado da mesma forma que no ambiente de produção, garantindo consistência.

### 2. Serviço App

O serviço **app** é o coração do ambiente de desenvolvimento. Ele utiliza um `Dockerfile.dev` personalizado para construir a aplicação, que é definido na seção `build`. A propriedade `context: .` especifica que o contexto de construção é o diretório atual, e o `dockerfile: Dockerfile.dev` define o arquivo Docker específico que será usado para configurar o container.

O nome do container da aplicação é definido como `app` através de `container_name: app`. 

A linha `command: sh -c "prisma generate && prisma db push && pymon -c src/main.py"` executa uma série de comandos essenciais para preparar o ambiente de desenvolvimento. O `prisma generate` gera os clientes Prisma a partir do esquema definido, e o `prisma db push` sincroniza as alterações de esquema com o banco de dados. Em seguida, o `pymon` (um possível utilitário para monitorar mudanças no código) é iniciado com o arquivo principal `src/main.py`, garantindo que a aplicação seja executada e que alterações no código sejam detectadas automaticamente para recarregamento.

O mapeamento de portas, especificado por `ports: - '3333:3333'`, mapeia a porta 3333 do container para a porta 3333 do host. Isso significa que a aplicação estará acessível localmente na porta 3333.

O serviço também utiliza volumes, definidos como `volumes: - .:/app`, o que mapeia o diretório atual do projeto (no host) para o diretório `/app` dentro do container. Isso permite que as alterações no código local sejam refletidas imediatamente no ambiente do container, facilitando o processo de desenvolvimento.

### 3. Dependências e Variáveis de Ambiente

O serviço **app** depende do serviço PostgreSQL, conforme definido em `depends_on: - postgres`. Isso garante que o container do banco de dados seja iniciado antes do container da aplicação, evitando problemas de conexão durante o startup.

A variável de ambiente `DATABASE_URL` é configurada para apontar para o banco de dados PostgreSQL no container `postgres`, usando o formato: `postgres://postgres:postgres@postgres:5432/postgres`. Essa string de conexão é utilizada pela aplicação para se conectar ao banco de dados PostgreSQL.

## Referências

[1] *AMAZON WEB SERVICES.* The difference between Docker images and containers. Disponível em: [https://aws.amazon.com/pt/compare/the-difference-between-docker-images-and-containers/](https://aws.amazon.com/pt/compare/the-difference-between-docker-images-and-containers/). Acesso em: 10 set. 2024.

[2] *IBM.* Docker: definição e benefícios. Disponível em: [https://www.ibm.com/br-pt/topics/docker](https://www.ibm.com/br-pt/topics/docker). Acesso em: 10 set. 2024.

[3] *LOCAWEB.* O que é Docker e por que usar? Disponível em: [https://www.locaweb.com.br/blog/temas/codigo-aberto/o-que-e-docker-e-por-que-usar/](https://www.locaweb.com.br/blog/temas/codigo-aberto/o-que-e-docker-e-por-que-usar/). Acesso em: 10 set. 2024.
