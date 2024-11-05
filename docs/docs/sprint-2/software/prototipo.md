# Prototipagem da Aplicação

Após a elaboração do wireframe, que permitiu visualizar as funcionalidades da aplicação, o grupo avançou para o próximo passo no desenvolvimento da interface gráfica: o mockup, que se trata da criação de um protótipo de alta fidelidade. Este mockup é a melhor forma de visualizar o design da aplicação sem a necessidade de desenvolver o frontend.

## Imagem 1 do Mockup - tela de login
![Login](/img/wireframe-login.png)

A tela de login é projetada para uma autenticação segura e eficaz, facilitando também a identificação do usuário que acessa a aplicação. No topo, o logo do grupo é bem visível, acompanhado de campos para inserir "Usuário" e "Senha", além de um botão "Entrar". Esta organização promove uma navegação intuitiva e direta, proporcionando uma experiência de uso fluida e livre de distrações. O design mantém a simplicidade, com adição de detalhes visuais como um logo mais proeminente e um esquema de cores distintas, reforçando a identidade visual da aplicação.

## Imagem 2 do Mockup - dashboard
![Dashboard](/img/wireframe-dash.png)

A tela do dashboard é projetada para uma visualização clara dos dados. No topo, o logo do grupo se alinha à identidade visual da aplicação. A disposição inclui vários espaços para gráficos, cada um com seu próprio título para facilitar a identificação rápida do conteúdo. O layout organizado promove uma navegação intuitiva, permitindo aos usuários acessar informações essenciais de maneira rápida.

## Imagem 3 do Mockup - tela com input para pesquisa
![Input](/img/wireframe-input.png)

Esta tela é projetada para a entrada de KNR, permitindo ao usuário enviar informações específicas para o modelo de predição defalhas. No topo, o título clarifica a função da página, mantendo a consistência visual com o logo ao lado esquerdo. Há um campo de entrada rotulado para inserir o número de identificação do veículo (KNR), acompanhado por um botão "Enviar" para submeter a informação. A parte inferior da tela apresenta linhas horizontais, destinadas à exibição de opções de KNR para envio.

## Imagem 4 do Mockup - tela de feedback: falha encontrada
![Falha](/img/wireframe-falha.png)

Tela de feedback projetada para indicar falhas identificadas em um veículo após a análise pelo KNR. No topo, o título "Feedback" e um ícone de "X" vermelho anunciam a detecção de problemas. "FALHAS ENCONTRADAS" reforça a mensagem logo abaixo. Cada retângulo apresenta a etapa de produção onde a falha ocorreu e uma descrição do problema, proporcionando clareza sobre a natureza das falhas detectadas. As falhas são categorizadas por cor em retângulos: amarelo para falhas não funcionais, como problemas na pintura, e vermelho para falhas que afetam a funcionalidade do carro. 

## Imagem 5 do Mockup - tela de feedback: nenhum falha encontrada
![Okay](/img/wireframe-ok.png)

Tela de feedback positivo informa que não foram detectadas falhas no veículo após a análise do KNR. No topo, o título "Feedback" é seguido por um ícone de marca de verificação verde, simbolizando que o veículo está em conformidade. A seção "Identificador de falhas" na parte inferior está vazia, indicando que não há problemas a reportar.

# Jornada de Usuário na Aplicação

A jornada do usuário foi projetada para garantir uma experiência intuitiva e eficiente em cada etapa de interação com a aplicação. Cada ponto da jornada foi planejada para facilitar o uso, minimizar frustrações e garantir que as informações necessárias estejam acessíveis de maneira rápida e clara para os funcionários da Volkswagen.

## 1. Acesso à Aplicação

O primeiro contato do usuário com a aplicação ocorre na **tela de login**. Ao acessar o sistema, o usuário é direcionado para uma interface limpa e objetiva. Nessa tela, ele insere seu **usuário** e **senha**, visualizando claramente os campos de preenchimento e o botão "Entrar".

- **Objetivo**: Autenticar o usuário para garantir acesso seguro às funcionalidades.
- **Ação**: O usuário insere as credenciais e clica em "Entrar".
- **Resultado esperado**: O usuário é redirecionado ao dashboard após a validação.

## 2. Visualização de Dados no Dashboard

Após a autenticação, o usuário é levado à tela de **dashboard**, onde pode visualizar informações importantes de maneira clara e organizada. Gráficos são apresentados em seções, cada um com um título descritivo que permite a rápida identificação do conteúdo. Essa visualização ajuda o usuário a monitorar os principais indicadores e a tomar decisões informadas.

- **Objetivo**: Fornecer uma visão geral dos dados em um layout intuitivo.
- **Ação**: O usuário visualiza os gráficos e acessa as informações que deseja.
- **Resultado esperado**: O usuário consegue navegar facilmente pelos dados e entender o panorama geral do sistema.

## 3. Inserção de Dados no Sistema

Para utilizar as funcionalidades de predição de falhas, o usuário acessa a **tela de input de pesquisa**. Nessa etapa, ele insere o **KNR** (Número de Identificação do Veículo) no campo de entrada e clica no botão "Enviar". Essa interação permite ao sistema realizar a análise de falhas com base nas informações inseridas.

- **Objetivo**: Permitir a inserção de KNR para análise pelo modelo preditivo.
- **Ação**: O usuário insere o KNR e submete a informação.
- **Resultado esperado**: O sistema processa o KNR e redireciona o usuário para a próxima etapa, que é a tela de feedback.

## 4. Feedback - Falha Encontrada

Se forem detectadas falhas no veículo após a análise, o usuário é levado para a **tela de feedback com falhas encontradas**. Nessa tela, ele vê as falhas reportadas, categorizadas de acordo com a quantidade. Cada falha é descrita com informações sobre a etapa da produção em que ocorreu, permitindo que o usuário entenda a natureza do problema e a ação necessária.

- **Objetivo**: Informar o usuário sobre as falhas encontradas no veículo.
- **Ação**: O usuário visualiza as falhas, compreendendo a extensão dos problemas.
- **Resultado esperado**: O usuário tem clareza sobre as falhas.

## 5. Feedback - Nenhuma Falha Encontrada

Caso não sejam detectadas falhas no veículo, o usuário é redirecionado para a **tela de feedback sem falhas**. Nessa etapa, ele visualiza uma mensagem confirmando que o veículo está em conformidade, com o ícone de marca de verificação verde no topo, sinalizando o sucesso da análise.

- **Objetivo**: Informar o usuário que não foram encontradas falhas no veículo.
- **Ação**: O usuário visualiza a confirmação de que o veículo está em conformidade.
- **Resultado esperado**: O usuário tem a confirmação de que o veículo está livre de problemas e pode prosseguir com segurança.
