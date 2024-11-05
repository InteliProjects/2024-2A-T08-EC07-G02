# Processo ETL (Extract Load Transform)

Nesta quarta sprint o processo de dados e confecção dos mesmos continuou sendo trabalhado com os mesmos da sprint anterior. Assim, nessa sprint foi aplicada um novo processo de ETL em cima deles para que haja um fluxo das diferentes fontes, extração deles e transformação para os dados que serão utilizados no projeto.
Sendo assim, para saber mais sobre a sprint anterior (sprint 3) acesse
: [https://github.com/Inteli-College/2024-2A-T08-EC07-G02/tree/main/docs/docs/sprint-3/software](https://github.com/Inteli-College/2024-2A-T08-EC07-G02/tree/main/docs/docs/sprint-3/software)

## Conceito

O processo ETL, sigla para Extract, Transform, Load, é um conjunto de procedimentos utilizado para integrar, transformar e carregar dados de diferentes fontes em um sistema de armazenamento centralizado, como um data warehouse. Este processo é amplamente utilizado em ambientes de business intelligence (BI), data warehousing e data analytics para consolidar e preparar dados de forma eficiente para análise. Ele é dividido em três etapas principais:

1. **Extração (Extract):**
   A fase de extração envolve a coleta de dados brutos de várias fontes heterogêneas, como bancos de dados relacionais, sistemas ERP, arquivos CSV, APIs web, entre outros. O objetivo é obter todos os dados relevantes, independentemente do formato ou da estrutura, e trazê-los para um ambiente onde possam ser processados. Essa etapa é crítica, pois a qualidade dos dados extraídos impacta diretamente as fases subsequentes. As principais técnicas de extração incluem a captura completa dos dados, a extração incremental (apenas as alterações desde a última extração) e a replicação em tempo real.

2. **Transformação (Transform):**
   Na transformação, os dados extraídos são processados para atender às necessidades de análise. Isso inclui tarefas como limpeza de dados, onde inconsistências e duplicatas são removidas; padronização, que garante que os dados estejam em um formato uniforme; agregação, que resume informações em métricas específicas; e integração, que combina dados de diferentes fontes em uma visão única e coerente. Além disso, a transformação pode envolver cálculos complexos, mudanças de tipos de dados e aplicação de regras de negócios específicas. Esta etapa é fundamental para garantir que os dados sejam precisos, consistentes e adequados para análises aprofundadas.

3. **Carga (Load):**
   A etapa final do processo ETL é a carga dos dados transformados em um sistema de destino, geralmente um data warehouse ou um banco de dados analítico. A carga pode ser realizada de várias maneiras, dependendo dos requisitos de negócio e da frequência de atualização necessária. Pode ser feita de forma completa, substituindo todos os dados antigos, ou incremental, adicionando apenas os novos dados ou atualizando os existentes. A carga eficiente e sem falhas é crucial para garantir que o sistema de destino esteja sempre atualizado e pronto para suportar as análises desejadas.

## Utilização no projeto

No contexto do projeto, o processo ETL é fundamental, pois garante que todos os dados necessários para avaliação do modelo de machine learning sejam moldados de forma a garantir a sua melhor performance. A seguir, são descritas as etapas com mais detalhes:

1. **Extração (Extract):**
   A extração de dados no projeto, em sua maioria, é realizada a partir de arquivos XLSX (Excel), CSV ou PARQUET, fornecidos pela Volkswagen. São três tabelas principais, _STATUS_, _RESULTS_ e _FAILURES_, que contêm informações padronizadas sobre os testes realizados em cada veículo. A extração é feita de forma manual, baixando os arquivos diretamente do e-mail ou do sistema de compartilhamento de arquivos da Volkswagen.

2. **Transformação (Transform):**
   A fase de transformação é a mais importante para o projeto, pois é nela que os dados são preparados para treinamento do modelo de machine learning. Nesta etapa, os dados são colocados no dashboard da solução, onde são processados e transformados através do [_Backend_](../../sprint-2/software/api.md) da aplicação. A transformação envolve a limpeza dos dados, a remoção de valores nulos, a padronização de formatos, a normalização de dados, a criação de novas features e a seleção das variáveis mais relevantes para o modelo. Além disso, a transformação inclui a divisão dos dados em conjuntos de treino e teste, sendo que todo esse processo é automatizado e realizado de forma transparente para o usuário, garantindo a qualidade e a consistência dos dados.

3. **Carga (Load):**
   Por último, a etapa de carga envolve o armazenamento dos dados transformados em um data lake. Porém, como foi explicado na seção de [Data Lake](../../sprint-3/software/dataLake.md), o projeto não implementará está feature. Assim, os dados transformados são armazenados temporariamente no dashboard da solução, onde são utilizados para treinamento do modelo. A carga dos dados é realizada de forma eficiente e segura, garantindo a integridade e a disponibilidade dos dados para análises futuras.

## Conclusão

O processo ETL desempenha um papel fundamental no projeto, garantindo que os dados sejam coletados, transformados e carregados de forma eficiente e confiável. Através das etapas de extração, transformação e carga, os dados são preparados para treinamento do modelo de machine learning, permitindo que a solução entregue resultados precisos e confiáveis. Assim, o ETL é uma peça-chave na jornada de transformação digital da Volkswagen, contribuindo para a tomada de decisões mais assertivas e o desenvolvimento de soluções inovadoras e sustentáveis.