
import networkx as nx

G = nx.Graph()
CAST = ['aasha', 'paige', 'amber', 'nour', 'basit', 'jonathan', 'brandon', 'remy', 'kai', 'danny', 'jasmine', 'jenna', 'kari', 'kylie', 'max', 'justin']
CAST_COPY = list(map(lambda x: x + '1' , CAST))

# helper funcs

def generate_edges_for_couple(x, y):
    return [[x, y+'1'], [x+'1', y]]

def print_edges_without_dupes():
    edges_without_dupes = []
    for (x,y) in G.edges():
        if y[len(y)-1] == '1' and (y[:-1], x+'1') not in edges_without_dupes:
            print((x,y))
            edges_without_dupes.append((x,y))
            
    print(len(edges_without_dupes))
    return edges_without_dupes

# add nodes
G.add_nodes_from(CAST, bipartite=0)
G.add_nodes_from(CAST_COPY, bipartite=1)

# add edges
for u in CAST:
    for v in CAST_COPY:
        if (u == v[:-1]): # don't include edge between someone and themself
            continue
        G.add_edge(u, v)

#### SPOILERS ####
# remove confirmed truth booth no-matches
TRUTH_BOOTH_NO_MATCH = [
    ['justin', 'nour'],
    ['brandon', 'remy'],
    ['kai', 'jenna'],
    ['jenna', 'danny'],
    ['kari', 'kylie'],
]

BLACKOUT_NO_MATCH = [
    ['kylie', 'jenna'],
    ['nour', 'amber'],
    ['jonathan', 'justin'],
    ['max', 'brandon'],
    ['remy', 'basit'],
    ['kari', 'danny'],
    ['paige', 'jasmine'],
    ['aasha', 'kai']
]

for [x,y] in TRUTH_BOOTH_NO_MATCH:
    G.remove_edges_from(generate_edges_for_couple(x, y))

for [x,y] in BLACKOUT_NO_MATCH:
    G.remove_edges_from(generate_edges_for_couple(x, y))

# TODO: add perfect matches
PERFECT_MATCH = [
    ['brandon', 'aasha'],
    ['basit', 'jonathan']
]

# test
print_edges_without_dupes()
