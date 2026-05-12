# Notas de Aula: Lógica de Programação
**Disciplina:** Lógica de Programação  
**Linguagens:** C++ e Python

---

## 1. Introdução à Lógica
A lógica de programação é a organização de instruções para que um computador execute uma tarefa. Independentemente da linguagem, os conceitos de algoritmos permanecem os mesmos.

---

## 2. Variáveis e Tipos de Dados
As variáveis armazenam informações. C++ é **fortemente tipada** (exige declarar o tipo), enquanto Python é **dinamicamente tipada**.

### Exemplo em C++
```cpp
int idade = 20;
float altura = 1.75;
string nome = "Ana";
bool programador = true;
```

### Exemplo em Python
```python
idade = 20
altura = 1.75
nome = "Ana"
programador = True
```

---

## 3. Estruturas Condicionais (IF/ELSE)
Tomada de decisão baseada em condições lógicas.


| Linguagem | Sintaxe Básica |
| :--- | :--- |
| **C++** | `if (idade >= 18) { cout << "Maior"; }` |
| **Python** | `if idade >= 18: print("Maior")` |

---

## 4. Estruturas de Repetição (Loops)
Utilizadas para repetir tarefas enquanto uma condição for verdadeira.

### Loop "For" em C++
```cpp
for(int i = 0; i < 5; i++) {
    cout << i << endl;
}
```

### Loop "For" em Python
```python
for i in range(5):
    print(i)
```

---

## 5. Comparativo: C++ vs Python

*   **C++:**
    *   Sintaxe mais rígida (usa `;` e `{}`).
    *   Mais próximo do hardware (mais rápido).
    *   Exige compilação.
*   **Python:**
    *   Sintaxe limpa e próxima do inglês.
    *   Usa **identação** (espaços) para organizar blocos de código.
    *   Linguagem interpretada.

---


```
