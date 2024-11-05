# **Documentação de Testes**

## **Introdução**
Para garantir a qualidade do software desenvolvido, é necessário realizar testes que verifiquem se o sistema atende aos requisitos estabelecidos e se está livre de falhas. Os testes de software são fundamentais para identificar possíveis problemas e garantir que o sistema funcione corretamente em diferentes cenários. Este documento apresenta os casos de teste realizados no projeto da Volkswagen, com a finalidade de validar as funcionalidades desenvolvidas.

---

## **Escopo**
Com base nos [requisitos](../sprint-1/software/requisitos.md) do projeto, os testes cobrem as seguintes funcionalidades:
- Login na aplicação
- Envio de dados para o sistema através da API
- Funcionamento do dashboard interativo (visualização dos dados e identificação das falhas)
- Requisitos não funcionais (tempo de resposta, quantidade de previsões, precisão do modelo)

---

## **Ambiente de Teste**
- **Sistema Operacional**: Windows 10 e 11/ Ubuntu 22.04
- **Navegador**: Google Chrome 90+, Firefox 88+, Microsoft Edge 90+, Opera 76+.

---

## **Casos de Teste**

### **Caso de Teste 001 - Funcionamento do sistema de login**
- **Descrição**: Verificar se o sistema de login funciona corretamente, permitindo que o usuário acesse a aplicação.
- **Pré-condição**: O usuário deve estar cadastrado no sistema.
- **Passos**:
    1. Acessar a página de login, informando a URL da aplicação.
    2. Inserir o e-mail e a senha cadastrados.
    3. Clicar no botão "Entrar".
    4. Clicar no botão "Esqueci minha senha" caso não lembre da sua credencial.
- **Resultado Esperado**: O usuário é redirecionado para a página inicial da aplicação após o login bem-sucedido. O sistema deve permitir a recuperação de senha através do e-mail cadastrado.
- **Resultado Atual**: Após colocar o e-mail e senha, o usuário é redirecionado para a página inicial da aplicação. Porém, a recuperação de senha não está presente.

### **Caso de Teste 002 - Envio de dados para a plataforma**
- **Descrição**: Verificar se os dados enviados para a plataforma através da API são processados corretamente.
- **Pré-condição**: O usuário deve estar autenticado no sistema.
- **Passos**:
  1. Na página de dashboard, enviar os arquivos requisitados.
  2. Verificar se os dados são processados corretamente e exibidos no dashboard.
- **Resultado Esperado**: Os dados enviados são processados corretamente e exibidos no dashboard, permitindo a visualização das informações de forma clara e organizada.
- **Resultado Atual**: Após o envio dos arquivos, os dados são processados e exibidos no dashboard.

### **Caso de Teste 003 - Identificação de falhas no modelo de carro T-Cross**
- **Descrição**: Verificar se o sistema identifica corretamente as falhas no modelo de carro T-Cross.
- **Pré-condição**: O usuário deve estar autenticado no sistema e ter enviado os dados para a plataforma.
- **Passos**:
  1. Acessar a página de predição.
  2. Verificar se as falhas no modelo de carro T-Cross são exibidas corretamente.
- **Resultado Esperado**: O sistema deve identificar as falhas no modelo de carro T-Cross e categorizá-las em grupos para inspeções detalhadas.
- **Resultado Atual**: As falhas no modelo de carro T-Cross são identificadas e exibidas corretamente, permitindo a categorização em grupos para inspeções detalhadas.

### **Caso de Teste 004 - Requisitos não funcionais**
- **Descrição**: Verificar se os requisitos não funcionais do sistema são atendidos.
- **Pré-condição**: O sistema deve estar em funcionamento.
- **Passos**:
  1. Realizar 50 previsões concomitantemente.
  2. Verificar se o tempo de resposta para cada previsão é inferior a 5 segundos.
  3. Verificar se o modelo possui um recall de no mínimo 95%.
 
 - **Resultado Esperado**: O sistema deve suportar 50 previsões concomitantemente, com um tempo de resposta inferior a 5 segundos para cada previsão e um recall de no mínimo 95%.
    
  -  **Resultado Atual**: O sistema é capaz de suportar a realização de 50 previsões concomitantemente, com um tempo de resposta próximo de a 4 segundos para cada previsão e um recall de 96%.

---

Por fim, os testes realizados neste projeto da Volkswagen visam garantir a qualidade e a funcionalidade de todas as áreas críticas da aplicação, desde o login até o processamento de dados e predições. Cada caso de teste foi projetado para verificar o cumprimento dos requisitos funcionais e não funcionais, assegurando que o sistema atenda às expectativas de desempenho, precisão e usabilidade.