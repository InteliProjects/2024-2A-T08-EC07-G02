# Arquitetura do Sistema

A arquitetura do sistema foi projetada para atender aos requisitos de desempenho, segurança e escalabilidade. A seguir, detalhamos os principais componentes e suas interações.

![Architecture](/img/architecture.svg)

## Visão Geral dos Componentes

2. **Dashboard**:
    - Interface frontend desenvolvida em **Next.js**.
    - Responsável pela interação direta com o usuário.
    - Distribuída globalmente via **AWS CloudFront** para melhorar a velocidade e a experiência.
3. **Backend**:
    - Aplicação desenvolvida em **FastAPI**.
    - Processa a lógica de negócio e gerencia solicitações dos usuários.
    - Interage com os serviços de armazenamento.
4. **Armazenamento**:
    - **Banco de Dados**:
        - **PostgreSQL** gerenciado pelo **AWS RDS**.
        - Armazena dados estruturados e críticos da aplicação.
    - **Data Lake**:
        - Utiliza o **AWS S3** para armazenar grandes volumes de dados não estruturados ou semiestruturados.

## Infraestrutura na AWS

### AWS Cloud

Ambiente em nuvem que hospeda os recursos do sistema, aproveitando os serviços escaláveis e seguros da AWS.

### AWS VPC (Virtual Private Cloud)

-   Proporciona uma rede virtual isolada dentro da AWS.
-   **Sub-rede Privada**:
    -   Hospeda recursos não acessíveis diretamente da internet.
    -   Aumenta a segurança dos componentes internos.

### Grupos de Segurança (Security Groups)

-   Atuam como firewalls virtuais.
-   Controlam o tráfego de entrada e saída dos recursos AWS.
-   Protegem os serviços internos contra acessos não autorizados.

### Serviços Utilizados

-   **AWS CloudFront**:
    -   Serviço de CDN que entrega conteúdo rapidamente aos usuários globais.
    -   Distribui o **Dashboard** para melhorar a experiência do usuário.
-   **Amazon EC2 com Docker**:
    -   Executa o **Backend** em contêineres Docker.
    -   Oferece portabilidade e escalabilidade aos serviços.
-   **AWS RDS**:
    -   Serviço gerenciado para o banco de dados PostgreSQL.
    -   Simplifica o gerenciamento e manutenção do banco de dados.
-   **AWS S3**:
    -   Armazena dados não estruturados como um data lake.

## Fluxo de Interação entre os Componentes

1. O **Usuário** acessa o **Dashboard** via navegador.
2. O **Dashboard** comunica-se com o **Backend** para operações da aplicação.
3. O **Backend** interage com o **Banco de Dados** e o **Data Lake** para armazenar e recuperar dados.
4. Todos os componentes estão protegidos pelos **Grupos de Segurança** e executados dentro da **Sub-rede Privada** da **AWS VPC**.

## Benefícios da Arquitetura na AWS

-   **Escalabilidade**:
    -   Recursos ajustáveis conforme a demanda.
-   **Segurança**:
    -   Uso de sub-redes privadas e grupos de segurança protege dados e recursos.
-   **Desempenho**:
    -   Distribuição global de conteúdo com o **CloudFront**.
    -   Serviços otimizados da AWS melhoram a performance.
-   **Gerenciamento Simplificado**:
    -   Serviços gerenciados como o **RDS** reduzem a carga de manutenção.

## Diagrama da Arquitetura

_O diagrama da arquitetura foi criado utilizando o Eraser e ilustra visualmente a estrutura e a interação entre os componentes do sistema._

# Cloud Selecionada

Optamos pela **AWS (Amazon Web Services)** como provedora de nuvem pelos seguintes motivos:

-   **Programa AWS Academy**:
    -   Acesso a recursos e créditos por meio da parceria com a AWS Educate.
-   **Amplitude de Serviços**:
    -   Vasta gama de serviços que atendem às necessidades do projeto.
-   **Confiabilidade e Suporte**:
    -   Infraestrutura global garantindo alta disponibilidade e desempenho.
    -   Suporte e documentação abrangentes.
-   **Escalabilidade e Flexibilidade**:
    -   Recursos escaláveis que se adaptam ao crescimento do projeto sem comprometer a estabilidade.

Ao utilizar os serviços da AWS, construímos uma arquitetura robusta, segura e preparada para os desafios presentes e futuros do projeto.
