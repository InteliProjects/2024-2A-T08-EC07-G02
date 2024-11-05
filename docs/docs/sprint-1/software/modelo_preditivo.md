# Modelo Preditivo para manutenção preditiva

&emsp;Um **modelo preditivo para manutenção preditiva** é um sistema que utiliza dados históricos e em tempo real, algoritmos de aprendizado de máquina e técnicas estatísticas para prever quando um equipamento ou sistema está prestes a falhar. Ele é composto por várias etapas, começando pela **coleta de dados** que pode ser feita através de sensores que monitoram condições operacionais como temperatura, vibração, pressão e etc. Esses dados são então analisados e limpos para remover inconsistências, permitindo a construção de um modelo preditivo. <a href="#bibliografia">[[1]](#bibliografia)</a>

&emsp;O modelo é criado utilizando algoritmos de machine learning, como redes neurais e regressão, que são treinados com dados históricos e validados com novos dados. Uma vez implementado, o modelo é integrado em sistemas de monitoramento em tempo real, gerando alertas quando há uma alta probabilidade de falha iminente. Isso permite que a manutenção seja realizada de forma preventiva, minimizando o tempo de inatividade não planejado e os custos associados. <a href="#bibliografia">[[1]](#bibliografia)</a>

&emsp;Modelos preditivos são amplamente aplicados em indústrias como automotiva, manufatura, energia e aeronáutica, onde ajudam a prever falhas em motores, equipamentos de produção, redes de distribuição e sistemas críticos de aeronaves. Os benefícios incluem a redução de tempo de inatividade, economia de custos, aumento da vida útil dos equipamentos e melhoria da segurança.<a href="#bibliografia">[[1]](#bibliografia)</a>

&emsp;Entretanto, a qualidade dos dados é crucial, e a implementação desses modelos pode ser complexa e custosa. Ainda assim, a manutenção preditiva é uma ferramenta essencial para a eficiência operacional e a confiabilidade dos sistemas, sendo uma estratégia cada vez mais adotada na manutenção moderna. <a href="#bibliografia">[[1]](#bibliografia)</a>

&emsp; Com essa descrição do que seria um modelo preditivo focado para manutenção preditiva, este projeto conta nesta primeria sprint com dois modelos que foram desenvolvidos para predizer carros com possíveis falhas. Assim os modelos esoclhidos foram:

## Datasets
Atualmente o projeto conta com quatro datasets com dados diferentes dados de diferentes fontes. Os datasets são:

- Conjunto de dados de `FALHAS`, no qual contém informações sobre falhas em veículos, como o modelo, cor, motor, estação, local, falha e data da falha.
- Relatório de `STATUS`, no qual contém informações sobre o status de veículos, como o KNR, data e status. A coluna de status possui informações sobre a localização da carroceria, ou seja, ela é automaticamente mapeada pelos sensores de trilhos durante no processo de produção.
- Conjunto de relatórios de `RESULTADOS`, no qual contém informações sobre os resultados de máquinas, como o KNR, nome, ID, status, unidade, valor ID, valor e data. Os dados de resultados são divididos em três grupos: máquinas, parafusamento e eletrônicos:
	- Máquinas: resultados de fluidos, regulagem de freio e teste de pedal, indexados pelo ID `1`.
	- Parafusamento: torques e ângulos dos apertos realizados, indexados pelo ID `2`.
	- Eletrônicos: testes de componentes elétricos e eletrônicos, indexados pelo ID `718`.

	Indicados pela coluna `ID`.

	No qual resultados com `status` `10` são considerados `OK`(Dentro das medidas) e resultados com status `13` são considerados `NOK`(Fora das medidas).

	As colunas `UNIT`, `VALUE ID` e `VALUE` são utilizadas para identificar o tipo de valor, o sub resultado e o valor resultante daquele aperto, respectivamente, assim é possível identificar o tipo de resultado obtido.
- Tabela de `PREDICT_VW_M7_EC` é uma tabela de testes fornecida pela Volkswagen, que contém informações _compiladas_ de todas as outras tabelas, com intúito de ser utilizada diretamente no treinamento do modelo, pelo o que foi fornecido de informação, essa tabela tem a mesma estrutura que a utilizada em meios de automações em produção de algumas montadoras da Volkswagen. Atualmente essa tabela serve apenas para escopo de exemplo e não é utilizada no treinamento do modelo já que não possui informações suficientes para tal (É composta por apenas 4 meses de dados).

## Modelos

Será utilizado como base para a seleção de modelos de treino a tabela exemplo fornecida `PREDICT_VW_M7_EC`, pois ela fornece uma **base de preparação de dados** pré-selecionado. O foco inicial será na criação de um **modelo de predição binário** que preverá se um carro apresentará falhas ou não com base nos dados históricos disponíveis. Especificamente, a coluna `FALHAS_ROD` será utilizada como variável alvo (target), onde **o objetivo é prever se haverá ou não falhas no veículo durante da rodagem**. Para modelos futuros, será realizado a criação de um modelo de classificação multiclasse para prever o tipo de falha que um veículo pode apresentar durante o teste de rodagem.

### Overview do Dataset em relação ao Modelo
O dataset fornecido contém diversas colunas que registram informações sobre o veículo, como tempos de montagem, medições de torque, ângulos, números de falhas em diferentes zonas de produção, entre outros. A coluna alvo para a predição binária é `FALHAS_ROD`, que indica se houve (1) ou não (0) falhas relacionadas à rodagem do veículo.

### Modelos de Predição

Para abordar a tarefa de predição, foram mapeados os seguintes modelos de aprendizado de máquina que fazem sentido para o escopo do projeto:

#### Random Forest
- O _Random Forest_ é um modelo de ensemble (conjunto) que combina várias _Decision Tree_ para melhorar a robustez e a precisão da predição, ele **funciona agregando os resultados de múltiplas _Decision Tree_**, o que reduz a variância e melhora a generalização do modelo. Tende a ser mais preciso do que uma única árvore de decisão, especialmente em **conjuntos de dados complexos e com muitas variáveis**, como no caso da tabela de exemplo `PREDICT_VW_M7_EC` que contém cerca de `80` _features_. Ele também oferece **resistência ao overfitting e fornece uma medida da importância das variáveis**, o que pode ser útil para identificar quais fatores são mais influentes na previsão de falhas nos veículos antes da rodagem. <a href="#bibliografia">[[2]](#bibliografia)</a>

#### Gradient Boosting Machines (GBM)
-  O _GBM_ é outro método de ensemble (conjunto) que **cria um modelo preditivo forte a partir de modelos preditivos fracos, adicionando _Decision Tree_ em sequência**, **cada nova árvore corrige os erros cometidos pelas árvores anteriores**. Oferece uma alta precisão e é particularmente **eficaz em capturar interações complexas entre as variáveis**. É ideal para datasets com muitas características e pode fornecer previsões muito precisas, embora a **custo de maior complexidade computacional**, ou seja, maior tempo de treinamento. Em relação a tabela de exemplo `PREDICT_VW_M7_EC`, o _GBM_ pode ser **útil para capturar as relações complexas entre as variáveis que não podem ser identificadas por visualmente em gráficos de dispersão ou correlação**. <a href="#bibliografia">[[3]](#bibliografia)</a>

#### Support Vector Machine (SVM)
-  O _SVM_ é um modelo de classificação que busca encontrar o hiperplano que melhor separa as classes (no caso binário, falhas e não falhas) no espaço de características, é **especialmente eficaz em espaços de alta dimensionalidade e pode utilizar diferentes tipos de kernel para capturar relações complexas entre as variáveis**. O SVM é **útil quando as classes são não-linearmente separáveis** (não podem ser separadas por uma linha reta). Ele é **robusto a _outliers_** e pode fornecer **boas predições em conjuntos de dados com muitas _features_**, como é o caso do dataset fornecido de exemplo. <a href="#bibliografia">[[4]](#bibliografia)</a>

### Conclusão da pesquisa
Para um primeiro modelo, o _Gradient Boosting Machines (GBM)_ é recomendado devido à sua alta precisão e capacidade de capturar interações complexas entre as variáveis. O _Random Forest_ também é uma boa opção, pois oferece resistência ao _overfitting_ e fornece uma medida da importância das variáveis. O _Support Vector Machine (SVM)_ é uma alternativa robusta para conjuntos de dados com muitas variáveis e classes não-linearmente separáveis.

## Métricas de Avaliação

Para avaliar a eficácia dos modelos de predição, serão utilizadas as seguintes métricas:

- **Acurácia**: A acurácia mede a proporção de previsões corretas feitas pelo modelo. É uma métrica geral que indica a qualidade geral do modelo.
	- (Acurácia = (Verdadeiros Positivos + Verdadeiros Negativos) / Total de Instâncias) <a href="#bibliografia">[[5]](#bibliografia)</a>
- **Recall**: O _recall_ mede a proporção de instâncias positivas que foram corretamente identificadas pelo modelo. É útil quando o custo de um falso negativo é alto.
	- (_recall_ = verdadeiros positivos / (verdadeiros positivos + falsos negativos)) <a href="#bibliografia">[[5]](#bibliografia)</a>
- **F1-Score**: O _F1-Score_ é a média harmônica da precisão e do _recall_. É uma métrica útil para equilibrar a precisão e o _recall_.
	- (_F1-Score_ = 2 * (Precisão * _recall_) / (Precisão + _recall_)) <a href="#bibliografia">[[5]](#bibliografia)</a>

## Resultados

Serão apresentados os resultados dos modelos de predição desenvolvidos, incluindo a acurácia, _recall_ e _F1-Score_ obtidos para cada modelo.

### Modelo Gradient Boosting Machines (GBM)

Resultado do modelo de predição utilizando o algoritmo _Gradient Boosting Machines (GBM)_:

- **Acurácia**: 0.997
- **_Recall_**: 1.00
- **_F1-Score_**: 1.00

O modelo em sí foi utilizado sem customizações nos hiperparâmetros, pelo resultado obtido, atualmente nosso _dataset_ sofre de um problema de _Overfitting_, onde o modelo está muito ajustado para os dados de treino, mas não generaliza bem para novos dados. Para melhorar a performance do modelo, será necessário ajustar os hiperparâmetros, como a profundidade máxima das árvores, a taxa de aprendizado e o número de árvores no _GBM_ e alteração nas _features_ utilizadas no treinamento, para evitar que o modelo se ajuste demais aos dados de treino e tenha uma performance melhor na predição de novos dados. <a href="#bibliografia">[[6]](#bibliografia)</a>


### Modelo Support Vector Machine (SVM)

Resultado do modelo de predição utilizando o algoritmo _Support Vector Machine (SVM)_:

- **Acurácia**: 0.997
- **_Recall_**: 1.00
- **_F1-Score_**: 1.00

Obtendo um resultado semelhante ao _GBM_, o modelo _SVM_ também sofre de _Overfitting_, onde o modelo está muito ajustado para os dados de treino, mas não generaliza bem para novos dados. Isso reforça a necessidade de ajustar os hiperparâmetros do modelo e as _features_ utilizadas no treinamento para melhorar a performance do modelo na predição de novos dados. <a href="#bibliografia">[[6]](#bibliografia)</a>

### Conclusão

Mesmo com o problema de _Overfitting_, os modelos _Gradient Boosting Machines (GBM)_ e _Support Vector Machine (SVM)_ ainda são modelos promissores para a predição no nosso ambiente de dados, assim, no próximo sprint, será necessário refatorar toda estrutura de nosso _dataset_ e criar novas estratégias para evitar o _Overfitting_ e melhorar a performance dos modelos. <a href="#bibliografia">[[6]](#bibliografia)</a>

## Bibliografia:

[1] SANTOS. Manutenção preditiva: o que é? Veja 8 técnicas principais. Abecom Rolamentos SKF. Disponível em: [https://www.abecom.com.br/o-que-e-manutencao-preditiva/](https://www.abecom.com.br/o-que-e-manutencao-preditiva/). Acesso em: 10 ago. 2024.

[2] SCIKIT-LEARN. Decision Trees. Disponível em: [https://scikit-learn.org/stable/modules/tree.html](https://scikit-learn.org/stable/modules/tree.html). Acesso em: 13 ago. 2024.

[3] SCIKIT-LEARN. Ensemble Methods. Disponível em: [https://scikit-learn.org/stable/modules/ensemble.html](https://scikit-learn.org/stable/modules/ensemble.html). Acesso em: 13 ago. 2024.

[4] SCIKIT-LEARN. Support Vector Machines. Disponível em: [https://scikit-learn.org/stable/modules/svm.html](https://scikit-learn.org/stable/modules/svm.html). Acesso em: 14 ago. 2024.

[5] SCIKIT-LEARN. Model Evaluation. Disponível em: [https://scikit-learn.org/stable/modules/model_evaluation.html](https://scikit-learn.org/stable/modules/model_evaluation.html). Acesso em: 14 ago. 2024.

[6] SCIKIT-LEARN. Underfitting vs. Overfitting. Disponível em: [https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html). Acesso em: 14 ago. 2024.

