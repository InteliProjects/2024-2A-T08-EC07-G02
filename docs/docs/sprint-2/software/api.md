# API

As APIs (Application Programming Interfaces) podem ser pensadas como intermediárias que facilitam a comunicação entre diferentes softwares. Elas estabelecem um conjunto de regras e protocolos que determinam como esses sistemas devem interagir entre si, garantindo que a troca de informações ocorra de forma segura e eficiente. Com isso, as APIs permitem que um software solicite dados ou acesse funcionalidades de outro software, sem precisar conhecer detalhes internos da sua implementação, o que promove a modularidade e o encapsulamento das aplicações. [1]

A reutilização de serviços existentes por meio de APIs pode reduzir significativamente o tempo de desenvolvimento e os custos associados, além de aumentar a flexibilidade e a escalabilidade dos sistemas. Além disso, as APIs permitem a integração de diferentes tecnologias, facilitando a inovação contínua e a adaptação de sistemas para atender a novas demandas de negócios.

Durante a segunda Sprint, foram implementadas as seguintes rotas no sistema, utilizando o framework FastAPI, que é conhecido por sua performance e facilidade de uso. Essas rotas desempenham papéis importantes no fluxo de dados entre o frontend e o backend:

- `@api_keys_router.get("/api/keys")`: Rota responsável por obter os dados enviados pelos formulários do campus, processando-os no backend para utilização posterior. Essa rota é essencial para garantir que os dados corretos sejam recuperados e estejam disponíveis para outras partes do sistema.

- `@api_keys_router.post("/api/keys")`: Esta rota captura os dados fornecidos pelos usuários no formulário e, em seguida, envia o "KNR" obtido para o banco de dados. Essa operação é fundamental para a persistência de dados, permitindo que as informações sejam armazenadas e consultadas futuramente.

- `@api_keys_router.get("/health")`: Rota que verifica o status do sistema, validando se os processos de recebimento ou postagem das informações estão ocorrendo corretamente. Uma rota de "health check" como essa é importante para monitorar a integridade do sistema, garantindo que o mesmo esteja funcionando conforme esperado.

Essas rotas podem ser melhor visualizadas e testadas através da documentação automática gerada pelo FastAPI, acessível localmente no endereço: `localhost:3333/docs`. Essa documentação interativa permite que os desenvolvedores explorem e testem as funcionalidades das rotas de maneira intuitiva, acelerando o processo de desenvolvimento e integração.

# Bibliografia:

[1] O que é API? Guia de APIs para iniciantes. Redhat.com. Disponível em: [https://www.redhat.com/pt-br/topics/api/what-are-application-programming-interfaces](https://www.redhat.com/pt-br/topics/api/what-are-application-programming-interfaces). Acesso em: 20 ago. 2024.


‌