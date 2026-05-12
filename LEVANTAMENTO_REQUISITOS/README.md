# Notas de Aula: Levantamento de Requisitos
**Disciplina:** Engenharia de Software / Análise de Sistemas  
**Tópico:** Requisitos Funcionais (RF) e Não Funcionais (RNF)

---

## 1. O que é o Levantamento de Requisitos?
É a fase do projeto onde se define **o que** o sistema deve fazer. É a base para o desenvolvimento, testes e aceitação do cliente.

### Principais Técnicas de Levantamento:
*   **Entrevistas:** Conversas diretas com stakeholders.
*   **Questionários:** Coleta de dados em larga escala.
*   **Brainstorming:** Geração de ideias em grupo.
*   **Observação (Shadowing):** Observar o usuário em seu ambiente de trabalho.
*   **Prototipagem:** Criar telas básicas para validar ideias.

---

## 2. Requisitos Funcionais (RF)
Descrevem as **funções** e serviços que o sistema deve fornecer. Estão ligados diretamente ao comportamento e às tarefas do usuário.

**Exemplos:**
*   **RF01:** O sistema deve permitir que o usuário recupere sua senha via e-mail.
*   **RF02:** O sistema deve emitir um relatório mensal de vendas em formato PDF.
*   **RF03:** O usuário deve ser capaz de buscar produtos por categoria ou preço.

---

## 3. Requisitos Não Funcionais (RNF)
Descrevem as **qualidades** ou restrições do sistema. Eles não dizem o que o sistema faz, mas **como** ele faz (desempenho, segurança, usabilidade).

### Categorias Comuns:
*   **Usabilidade:** Facilidade de aprendizado e uso.
*   **Desempenho:** Tempo de resposta e consumo de memória.
*   **Segurança:** Criptografia de dados e níveis de acesso.
*   **Disponibilidade:** O tempo que o sistema deve ficar no ar (ex: 99.9%).

**Exemplos:**
*   **RNF01:** O sistema deve responder a qualquer consulta em menos de 2 segundos.
*   **RNF02:** O sistema deve ser compatível com os navegadores Chrome e Firefox.
*   **RNF03:** Todas as senhas devem ser armazenadas utilizando criptografia SHA-256.

---

## 4. Diferença Prática (Resumo)


| Característica | Requisito Funcional | Requisito Não Funcional |
| :--- | :--- | :--- |
| **Foco** | O que o sistema faz. | Como o sistema funciona. |
| **Origem** | Necessidade do negócio/usuário. | Restrição técnica ou de qualidade. |
| **Exemplo** | "Fazer login". | "Login deve ser seguro". |

---

## Exercício de Fixação
Identifique se os itens abaixo são RF ou RNF:
1. O sistema deve processar 100 transações por segundo. ( )
2. O sistema deve permitir o cadastro de novos clientes. ( )
3. A interface deve ser adaptável para dispositivos móveis (Responsivo). ( )
