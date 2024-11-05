# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2024/06/logo-inteli-3-768x420-1.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# _Presgen_
Repositório do grupo _**Presgen**_

## Descrição do Projeto
O projeto se baseia na criação de uma solução com modelo preditivo para indicar ao inspetor de veículos o tipo de inspeção que deverá ser realizada em um automóvel. A solução será desenvolvida em Python ou JavaScript, para facilitar a integração com o sistema de inspeção. O modelo preditivo será treinado com base em uma lista de parâmetros e deverá ser calibrado mensalmente com os novos dados de produção. Espera-se que o modelo tenha uma assertividade acima de 95% para que seja possível sua utilização. O desenvolvimento do projeto será realizado pelo analista de sistemas da fábrica, que irá adaptar o processo e utilizar o resultado do algoritmo de uma forma visual, para que o motorista inspetor consiga saber que tipo de inspeção ele deverá realizar naquele veículo.

## Objetivos do Projeto
- Aumentar a assertividade e eficiência na inspeção de veículos;
- Facilitar o uso e integração com o ambiente de produção da Volkswagen;sd
- Reduzir custos operacionais e tempo de inspeção.

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/cec%C3%ADlia-alonso-gon%C3%A7alves-3aa4bb271/">Cecilia Gonçalves</a>
- <a href="https://www.linkedin.com/in/eduardo-henrique-dos-santos/">Eduardo Santos</a>
- <a href="https://www.linkedin.com/in/gabriel-gallo-m-coutinho-443809232/">Gabriel Gallo</a>
- <a href="https://www.linkedin.com/in/gabrielle-mitoso/">Gabrielle Mitoso</a>
- <a href="https://www.linkedin.com/in/guilherme-ferreira-linhares-8638411a1/">Guilherme Linhares</a>
- <a href="https://www.linkedin.com/in/vinicioslugli/">Vinicios Lugli</a>

## 👩‍🏫 Professores:
### Orientador
- <a href="https://www.linkedin.com/in/murilo-zanini-de-carvalho-0980415b/">Murilo Zanini</a>
### Instrutores
- <a href="https://www.linkedin.com/in/geraldo-magela-severino-vasconcelos-22b1b220/">Geraldo Magela</a>
- <a href="https://www.linkedin.com/in/gui-cestari/">Guilherme Cestari</a>
- <a href="https://www.linkedin.com/in/lisane-valdo/">Lisane Valdo</a> 
- <a href="https://www.linkedin.com/in/monica-anastassiu-d-sc-2568522/">Mônica Anastassiu</a>
- <a href="https://www.linkedin.com/in/rafaelmatsuyama/">Rafael Matsuyama</a> 
- <a href="https://www.linkedin.com/in/ricardo-jos%C3%A9-missori/">Ricardo Missori</a>

## Estrutura de Pastas
```bash
.github
docs
   ├── sprint-1
   ├── sprint-2
   ├── sprint-3 
   ├── sprint-4
   ├── sprint-5
   └── intro.md
src
   ├── backend
   ├── frontend
static
.gitignore
README.md
sidebars.js
model
   ├── FALHAS.csv
   ├── RESULTADOS_02.csv
   ├── RESULTADOS_02MERGED.csv
   ├── RESULTADOS_04.csv
   ├── RESULT_MERGED.csv
   └── STATUS_PREDICTIONS.csv
.gitignore
README.md

````

## Guia de instrução 

Para executar o projeto, siga os passos abaixo:
1. Clone esse repositório e abra ele com o Visual Studio Code.

2. Agora execute o comando para iniciar o frontend: `npm install` para instalar as dependências e `npm run dev` para inciar. 

3. Acesse o diretório do código: Navegue até a pasta `src/backend`.

4. Agora no terminal integrado do Visual Studio Code envie `docker-compose up --build` para inicalizar o backend e o banco de dados.


*OBS*: Para facilitar o entendimento do processo de treinamento e da escolha do modelo, temos dois arquivos: `src/model/Treino_modelo.ipynb` e `src/model/BATCHES.py`

## Documentação

Para acessar a nossa documentação, clique [aqui](https://inteli-college.github.io/2024-2A-T08-EC07-G02/)!

## 📋 Licença/License

<div xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
    <a property="dct:title" rel="cc:attributionURL" href="https://github.com/Inteli-College/2024-2A-T08-EC07-G02/">
        Presgen
    </a>
    <span>
        by
    </span>
    <span property="cc:attributionName">
        <a href="https://www.inteli.edu.br/">Inteli</a>,
        <a href="https://www.linkedin.com/in/cec%C3%ADlia-alonso-gon%C3%A7alves-3aa4bb271/">Cecília Gonçalves</a>,
        <a href="https://www.linkedin.com/in/eduardo-henrique-dos-santos/">Eduardo Santos</a>,
        <a href="https://www.linkedin.com/in/gabriel-gallo-m-coutinho-443809232/">Gabriel Gallo</a>,
        <a href="https://www.linkedin.com/in/gabrielle-mitoso/">Gabrielle Mitoso</a>,
        <a href="https://www.linkedin.com/in/guilherme-ferreira-linhares-8638411a1/">Guilherme Linhares</a>,
        <a href="https://www.linkedin.com/in/vinicioslugli/">Vinicios Lugli</a>
    </span> 
    <span>
        is licensed under
    </span>
    <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">
        Creative Commons Attribution 4.0 International
        <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="Creative Commons">
        <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt="Attribution">
    </a>
</div>

## 🗃 Histórico de lançamento

- 1.1.0 - 05/08/2024
  - Início do Projeto

- 1.1.1 - 19/08/2024
  - Definição do escopo do projeto;
  - Experiência do Usuário;
  - Economia Circular;
  - Primeiro modelo preditivo.

- 1.1.2 - 02/09/2024
  - Alterar filtros na exploração de dados;
  - Melhoria de acurácia e recall dos modelos;
  - Testes de novas configurações de modelos;
  - Criação da nossa primeira API para acesso ao modelo.

- 1.2.0 - 16/09/2024
  - Otimização do modelo;
  - Solução dockerizada;
  - Implementação de Datalake.

- 1.2.1 - 30/09/2024
  - Processo de ETL (Extract, Transform, Load);
  - Refinamento do modelo;
  - Pipeline de treinamento com a integração do modelo;
  - Dashboard para visualização dos dados.

- 1.2.2 - 07/10/2024
  - Docker e Datalake em nuvem;
  - Refinamento do front-end;
  - Finalização da integração.
