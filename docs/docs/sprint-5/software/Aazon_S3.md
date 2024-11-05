# AWS - S3

O **Amazon S3 (Simple Storage Service)** é um serviço de armazenamento em nuvem oferecido pela Amazon Web Services (AWS) que proporciona uma solução escalável, segura e durável para gerenciar grandes volumes de dados. Este serviço é amplamente adotado por empresas e desenvolvedores para armazenar e recuperar dados de maneira eficiente, a qualquer momento e de qualquer lugar na web. O S3 organiza os dados em objetos, que são compostos pelas informações propriamente ditas, metadados e uma chave única para identificação. [1]

Uma das principais vantagens do S3 é sua escalabilidade automática, que permite que o armazenamento se ajuste conforme as necessidades do usuário, sem a necessidade de intervenção manual. Além disso, o serviço garante alta disponibilidade e durabilidade, com os dados sendo replicados automaticamente em múltiplas zonas de disponibilidade. Isso assegura que as informações permaneçam acessíveis e protegidas contra falhas. [1]

A segurança é outro aspecto crucial, com suporte para criptografia de dados, tanto em trânsito quanto em repouso, além de um controle de acesso granular e integração com o AWS Identity and Access Management (IAM). [1]

No contexto do projeto, está sendo utilizado o plano da AWS Academy para explorar os recursos do S3. Embora existam algumas limitações associadas a esse plano, ele atende adequadamente a todos os requisitos do projeto. No bucket do S3, os valores gerados pelo modelo estão sendo armazenados, permitindo que os usuários acessem os dados a qualquer momento e visualizem quais carros apresentam problemas.

Nesse sentido, para esse projeto na parte da AWS o usuário necessita ir no arquivo `.env.example` que está localizado em `src/backend` e mudar as seguintes variáveis com suas credenciais da AWS:

```
SERVICE_NAME= ''
AWS_ACCESS_KEY_ID= ''
AWS_SECRET_ACCESS_KEY= ''
REGION= ''
```

Por fim, o S3 adota um modelo de cobrança baseado no uso, com preços determinados pela quantidade de dados armazenados, transferência de dados e operações realizadas. Esse serviço é versátil e pode ser aplicado em diversos casos, como backup, recuperação de dados, armazenamento de arquivos para aplicativos web, distribuição de conteúdo e armazenamento de dados para análises e Big Data. [1]



[1] Demo: Getting started with Amazon S3 (Demonstração: conceitos básicos do Amazon S3) (7:37). Amazon Web Services, Inc. Disponível em: [https://aws.amazon.com/pt/s3/getting-started/#:~:text=O%20Amazon%20Simple%20Storage%20Service,de%20qualquer%20lugar%20na%20Web.](https://aws.amazon.com/pt/s3/getting-started/#:~:text=O%20Amazon%20Simple%20Storage%20Service,de%20qualquer%20lugar%20na%20Web.). Acesso em: 6 out. 2024.

‌
