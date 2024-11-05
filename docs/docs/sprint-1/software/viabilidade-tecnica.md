# Estudo de Viabilidade Técnica

O estudo de viabilidade técnica proporciona uma análise geral que além de determinar se o projeto é tecnicamente viável, avalia as tecnologias envolvidas e procura determinar possíveis desafios que podem surgir ao longo do desenvolvimento. Esse estudo ajuda a garantir de que o projeto poderá ser entregue e cumpra o escopo definido com qualidade. 

## Tecnologias e Ferramentas 
### Modelos de Aprendizado de Máquina (SVM e Gradient Boosting)
Esses modelos foram escolhidos devido à sua eficácia em tarefas de predição e classificação, pontos principais para identificação de falhas durante a inspeção dos veículos. O SVM (Support Vector Machine) é comumumente utilizado para lidar com dados de alta dimensionalidade, previnindo contra outliers e aumentando a capacidade de maximizar a margem de seperação entre classes, objetos cruciais para alcançar alta precisão. Por outro lado, o Gradient Boosting é um modelo que combina diversos modelos mais fracos formando um modelo poderoso, que otimiza continuamente a precisão e permitindo a captura de padrões. Ambos são boas opções no contexto do projeto, garantindo uma solução eficiente e adaptável às necessidades do cliente.

### Python
- **Pandas**: biblioteca em Python usado para manipulação e análise dos dados;
- **NumPy**: biblioteca em Python usada para computação numérica e transformação dos dados;
- **Matplotlib**: ferramenta que permite criar gráficos que ajudam a identificar padrões.

## Dados

### Exploração dos Dados

Para a tabela *FALHAS*, a primeira etapa foi a leitura da base de dados, onde a tabela foi carregada em um DataFrame para análise. Em seguida, realizou-se uma visualização da estrutura do DataFrame, identificando sua forma (número de linhas e colunas) e as colunas disponíveis, permintindo a maior compreensão dos dados em questão. Foram identificados os tipos de dados presentes em cada coluna para garantir que todas as variáveis estavam no formato correto para a análise. Ao analisar os dados, verificou-se a quantidade de valores nulos em cada coluna e optou-se pela exclusão dos registros com dados faltantes, resultando na remoção de 1862 registros da tabela, o que melhorou a integridade dos dados para o processo de modelagem.

O próximo passo foi filtrar a tabela para focar apenas nos modelos de veículos T-Cross, que são o modelo de interesse. Isso envolveu a identificação de todas as ocorrências desse modelo e a exclusão de dados relativos a outros modelos. Além disso, eliminou-se colunas que não eram relevantes para a análise, como a coluna Modelo (tendo em vista que nesse momento todos os registros se referiam ao T-Cross) e a coluna Data, que não era necessária para esse modelo preditivo.Para assegurar a consistência dos dados, as descrições das falhas foram padronizadas, convertendo todos os textos para letras maiúsculas. Após essa padronização, fez-se uma nova visualização para garantir que todas as falhas foram uniformizadas. Em sequência, identificou-se e elimou-se registros duplicados, garantindo que cada falha registrada na base de dados fosse única e representativa.

Já na tabela *RESULTADOS*, o primeiro passo foi a leitura da tabela e identificar a presença de colunas que não tinham utilidade para a essa análise.  As coluna foram removidas. Em seguida, realizou-se uma contagem das ocorrências do KNR em cada coluna, o que ajudou a entender a distribuição e a frequência desse parâmetro nas diferentes categorias de resultados. 

Por fim, após a limpeza e padronização de ambas as tabelas *FALHAS* e *RESULTADOS*, seguiu-se com a combinação dessas duas tabelas. Essa junção foi necessária para integrar as informações de falhas e resultados, permitindo que o modelo preditivo fosse treinado com um conjunto de dados completo, que reflete as falhas identificadas e os resultados observados no processo.

### Normalização

Após a combinação das tabelas FALHAS e RESULTADOS, o passo seguinte foi a normalização dos dados. Esse processo é crucial para assegurar que todas as variáveis sejam tratadas de forma uniforme no modelo preditivo, evitando que características com valores em diferentes escalas influenciem indevidamente a modelagem.

Optou-se por adotar a técnica de normalização min-max, que ajusta os valores de cada variável para um intervalo que vai de 0 a 1. Como resultado, todos os dados passaram a estar na mesma faixa, o que facilita o treinamento do modelo e melhora o desempenho do algoritmo de machine learning. A normalização min-max é especialmente vantajosa em modelos como o SVM, como o que está sendo utilizado.

## Custo e Tempo
### Orçamento
O projeto pode incorrer em despesas consideráveis, dependendo da complexidade, da infraestrutura exigida e das integrações com sistemas já existentes.
### Tempo de Execução
A implementação total pode demorar diversos meses, englobando o desenvolvimento, os testes, as adaptações e as certificações exigidas.

## Riscos e Desafios
### Overfitting 
Existe a possibilidade de que o modelo se adapte de forma excessiva aos dados de treinamento, o que pode prejudicar sua habilidade de generalizar para novos dados e alcançar a precisão almejada de 95%.

### Manutenção e Atualização
É necessário realizar ajustes periódicos no modelo para garantir sua exatidão. Problemas na atualização ou cuidados com o equipamento podem resultar na redução do desempenho, gerando aumento na complexidade e nos gastos operacionais.

# Bibliografia:
Arrumar
- MODELOS DE PREDIÇÃO SVM. **Medium**. Disponível em: https://medium.com/turing-talks/turing-talks-12-classifica%C3%A7%C3%A3o-por-svm-f4598094a3f1
- GRADIENT BOOSTING CLASSIFIER. **Scikit Learn**. Disponível em: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html
