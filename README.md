
# 📮 Problema do Carteiro Chinês (Dígrafo Euleriano)

modelagem e resolução do Problema do Carteiro Chinês em um **dígrafo ponderado**, utilizando conceitos de teoria dos grafos e a implementação do **método de Hierholzer** com apoio da biblioteca `algs4`.

---

## 🎥 Apresentação

🔗 Assista à apresentação do trabalho aqui: 

---

## 📌 Sobre o Projeto

Este projeto resolve uma instância do **Problema do Carteiro Chinês**, cujo objetivo é encontrar um **percurso fechado de menor custo** que percorra todas as arestas de um grafo ao menos uma vez.

O problema foi modelado como um **dígrafo ponderado**, onde:

* **Vértices** → representam locais/interseções
* **Arestas direcionadas** → representam ruas
* **Pesos** → representam o custo/distância de cada rua

A solução foi dividida em duas etapas:

1. **Eulerização manual** do grafo (fora do código)
2. Implementação do **algoritmo de Hierholzer** para encontrar o circuito euleriano

---

## 🎯 Objetivos

* Modelar um **dígrafo ponderado**
* Calcular **grau de entrada e saída**
* Verificar se o grafo é **euleriano**
* Aplicar o **método de Hierholzer**
* Determinar um **circuito euleriano**
* Calcular o **custo total do percurso**

---

## 🧩 Estrutura do Projeto

```text
t3-pcc/
├── dados/
│   └── entrada_eulerizada.txt     # Grafo já balanceado (entrada principal)
├── src/
│   └── main.py                    # Implementação completa
└── README.md                      # Documentação do projeto
```

---

## 🧭 Modelagem do Grafo

O grafo é representado utilizando a classe:

* `EdgeWeightedDigraph` → dígrafo com pesos
* `DirectedEdge` → arestas direcionadas com peso

Como os vértices são representados por letras (`a, b, c...`), foi necessário realizar um mapeamento:

| Vértice | Índice |
| ------- | ------ |
| a       | 0      |
| b       | 1      |
| c       | 2      |
| d       | 3      |
| e       | 4      |
| f       | 5      |

---

## ⚖️ Graus dos Vértices

O programa calcula:

* **grau de entrada (indegree)**
* **grau de saída (outdegree)**

Um grafo é euleriano quando:

```
indegree(v) = outdegree(v), ∀ v
```

---

## 🔄 Algoritmo Utilizado

### 🔹 Método de Hierholzer

Utilizado para encontrar um **circuito euleriano**.

Passos principais:

1. Escolher um vértice inicial
2. Percorrer arestas não utilizadas
3. Quando não houver mais arestas → retroceder
4. Construir o circuito final

---

## 💰 Cálculo do Custo

Como o grafo já está **eulerizado**, cada aresta é percorrida exatamente uma vez.

Logo:

```
custo total = soma dos pesos das arestas
```

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone 
```

2. Acesse a pasta:

```bash
cd t3-pcc/src
```

3. Execute o programa:

```bash
python main.py
```

---

## 📄 Formato da Entrada

Arquivo `entrada_eulerizada.txt`:

```text
V
E
v w peso
v w peso
...
```

Exemplo:

```text
6
13
a c 20
a b 10
b e 10
...
```

---

## 📤 Saída Esperada

O programa imprime:

* graus dos vértices
* verificação de grafo euleriano
* circuito euleriano
* custo total

Exemplo:

```text
GRAUS
a -> entrada: 2, saída: 2
...

Grafo é euleriano

CIRCUITO
a -> b -> e -> ...

CUSTO TOTAL
XXX
```

---

## 🧠 Decisões de Implementação

* Uso da biblioteca **algs4** para representar grafos ponderados
* Mapeamento manual de vértices simbólicos → índices numéricos
* Implementação própria do algoritmo de **Hierholzer**
* Separação entre estrutura do grafo e lógica do algoritmo

---

## ❓ Perguntas Respondidas

* O grafo é euleriano?
* Quais são os graus de cada vértice?
* Qual é o circuito euleriano encontrado?
* Qual é o custo total do percurso?

---

## 📚 Referência

* Sedgewick & Wayne — *Algorithms, 4th Edition*
* Biblioteca `algs4`
* Problema do Carteiro Chinês
* Método de Hierholzer


