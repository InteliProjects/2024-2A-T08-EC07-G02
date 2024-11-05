# Datalake
Segundo a AWS um Datalake é um repositório centralizado que permite armazenar todos os seus dados estruturados e não estruturados em qualquer escala. Você pode armazenar seus dados como estão, sem precisar primeiro estruturá-los e executar diferentes tipos de análise, desde painéis e visualizações até processamento de big data, análise em tempo real e machine learning para orientar melhores decisões. [1]

Nesse sentido, o Datalake adota o conceito de “schema on read”, o que significa que a estruturação dos dados ocorre apenas quando são lidos, conforme a necessidade. Assim, essa abordagem permite uma ingestão mais rápida e facilita a exploração e análise dos dados, adaptando-os conforme a interpretação necessária no momento da leitura. [2]

Nessa perspectiva, este projeto não implementará um Datalake para o armazenamento dos dados. Isso ocorre porque os dados tratados na implementação deste projeto já estão em um estado filtrado, uma vez que a Volkswagen forneceu dados de qualidade e previamente definidos, com certo refinamento. No entanto, caso a solução deste projeto exigisse a captação direta de todos os ciclos da fabricação dos carros, com os dados em seu formato bruto, haveria a necessidade de implementar um Datalake e, em seguida, filtrar os dados necessários.

Assim, uma opção de implementação do Datalake neste projeto é o arquivo Docker `docker-compose-db.yml`, que será responsável pelo armazenamento dos modelos utilizados na execução do projeto. 

[1] O que é um data lake? — Introdução aos data lakes e análises — AWS. Amazon Web Services, Inc. Disponível em: [https://aws.amazon.com/pt/what-is/data-lake/](https://aws.amazon.com/pt/what-is/data-lake/). Acesso em: 8 set. 2024.

[2] ALURA. Data Lake: conceitos, vantagens e desafios. Alura. Disponível em: [https://www.alura.com.br/artigos/data-lake-conceitos-vantagens-desafios?srsltid=AfmBOoosPYrOaZq-Yj7MQSAEgy1kwcJyubGGodxgZVDIvi-XyWuMRjzf](https://www.alura.com.br/artigos/data-lake-conceitos-vantagens-desafios?srsltid=AfmBOoosPYrOaZq-Yj7MQSAEgy1kwcJyubGGodxgZVDIvi-XyWuMRjzf). Acesso em: 8 set. 2024.

‌
‌