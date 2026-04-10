from algs4.edge_weighted_digraph import EdgeWeightedDigraph
from algs4.directed_edge import DirectedEdge

def build_symbol_table(filename):
    st = {}
    keys = []
    
    with open(filename) as f:
        f.readline()  # pula V
        f.readline()  # pula E

        for line in f:
            v, w, _ = line.split()
            
            for x in (v, w):
                if x not in st:
                    st[x] = len(st)
                    keys.append(x)

    return st, keys


def build_graph(filename, st):
    G = EdgeWeightedDigraph(len(st))

    with open(filename) as f:
        f.readline()
        f.readline()

        for line in f:
            v, w, weight = line.split()
            v_id = st[v]
            w_id = st[w]
            weight = float(weight)

            G.add_edge(DirectedEdge(v_id, w_id, weight))

    return G

def calculate_degrees(G, keys):
    indegree = [0] * G.V
    outdegree = [0] * G.V

    for v in range(G.V):
        for e in G.adj[v]:
            w = e.w
            outdegree[v] += 1
            indegree[w] += 1

    return indegree, outdegree

def hierholzer(G):
    adj = {v: list(G.adj[v]) for v in range(G.V)}

    stack = []
    circuit = []

    current = next(v for v in range(G.V) if adj[v])
    stack.append(current)

    while stack:
        if adj[current]:
            stack.append(current)
            edge = adj[current].pop()
            current = edge.w
        else:
            circuit.append(current)
            current = stack.pop()

    return circuit[::-1]

def calculate_cost(G):
    cost = 0
    for v in range(G.V):
        for e in G.adj[v]:
            cost += e.weight
    return cost

def main():
    filename = "entrada_eulerizada.txt"

    st, keys = build_symbol_table(filename)
    G = build_graph(filename, st)

    indegree, outdegree = calculate_degrees(G, keys)

    print(" GRAUS ")
    for i in range(G.V):
        print(f"{keys[i]} -> entrada: {indegree[i]}, saída: {outdegree[i]}")

    # verifica
    for i in range(G.V):
        if indegree[i] != outdegree[i]:
            print("\n NÃO é euleriano")
            return

    print("\n Grafo é euleriano")

    circuit = hierholzer(G)

    print("\n CIRCUITO ")
    print(" -> ".join(keys[v] for v in circuit))

    cost = calculate_cost(G)

    print("\n CUSTO TOTAL ")
    print(cost)

main()
