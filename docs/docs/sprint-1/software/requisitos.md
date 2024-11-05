---
custom_edit_url: null
---

# Requisitos Funcionais

&emsp;Requisitos funcionais são as funcionalidades ou serviços específicos que um sistema de software deve realizar para atender às necessidades dos usuários ou aos objetivos do projeto. Eles descrevem as ações que o software deve ser capaz de executar, como, por exemplo, permitir que um usuário insira dados em um formulário, realize buscas, ou emita relatórios. Esses requisitos são fundamentais para definir o que o sistema deve fazer e são essenciais para garantir que o software cumpra suas finalidades. [1]

Em termos de aplicação prática, os requisitos funcionais são normalmente definidos durante a fase de elicitação no desenvolvimento de software. Eles servem como um guia para a equipe de desenvolvimento e são usados para validar se o sistema está funcionando conforme o esperado. Além disso, a clareza e a objetividade na definição desses requisitos são cruciais para evitar ambiguidades e garantir a qualidade do produto final. [1]

&emsp;Dessa maneira temos para esse projeto da Volkswagen os seguintes requisitos funcionais:

**RF01:** O modelo de predição desenvolvido deve se conectar ao sistema em Cloud, garantindo acesso contínuo e em tempo real aos dados necessários para as análises preditivas.

**RF02:** O sistema de predição deve disponibilizar uma interface de acesso por uma API, permitindo que os colaboradores da empresa enviem dados e utilizem as informações de saída para suas atividades.

**RF03:** O sistema de predição deve incluir dashboards interativos, facilitando a análise visual dos dados preditivos pelos colaboradores da Volkswagen, proporcionando uma interface intuitiva e amigável para que haja uma melhor compreensão dos dados de maneira rápida.

**RF04:** O sistema deve identificar a área específica onde ocorreu a falha exclusivamente no modelo de carro T-Cross da Volkswagen, categorizando-as em grupos para inspeções detalhadas e assegurando precisão e relevância nos resultados.


**RF05:** O sistema de predição deve fornecer o output para o modelo de carro T-Cross está apresentando falhas ou não.


# Requisitos não funcionais

&emsp;Os requisitos não funcionais representam as propriedades os quais o sistema deve possuir, tendo como enfoque garantir tecnicamente o funcionamento das funcionalidades adicionadas nos requisitos funcionais, descrevendo como serão feitas as funcionalidades. [2]

&emsp;Desta forma, os requisitos não funcionais relacionados ao projeto são:

**RNF01:** Cada previsão feita pelo sistema deve demorar menos que 5 (cinco) segundos para ser concluída e apresentada ao usuário.

**RNF02:** O sistema deve suportar no mínimo 50 previsões concomitantemente.

**RNF03:** O modelo deve possuir um recall (proporção entre verdadeiros positivos e o número de positivos encontrados) de no mínimo 95%.

**RNF04:** Assumindo que os mesmo dados de entreada sejam fornecidos para a API do sistema e o Dashboard, os resultados devem ser iguais.

**RNF05:** O tempo de resposta para uma requisição na API deve ser menor do que 7 (sete) segundos.

# Bibliografia:
[1] Requisitos funcionais e não funcionais: o que são? www.mestresdaweb.com.br. Disponível em: [https://www.mestresdaweb.com.br/tecnologias/requisitos-funcionais-e-nao-funcionais-o-que-sao](https://www.mestresdaweb.com.br/tecnologias/requisitos-funcionais-e-nao-funcionais-o-que-sao).

[2] Conceito: Requisitos Não-Funcionais https://www.trt9.jus.br/ . Disponível em [https://www.trt9.jus.br/pds/pdstrt9/guidances/concepts/supporting_requirements_B2C4D610.html](https://www.trt9.jus.br/pds/pdstrt9/guidances/concepts/supporting_requirements_B2C4D610.html)

‌