
import networkx as nx
# import matplotlib.pyplot as plt

G = nx.Graph()
CAST = ['aasha', 'paige', 'amber', 'nour', 'basit', 'jonathan', 'brandon', 'remy', 'kai', 'danny', 'jasmine', 'jenna', 'kari', 'kylie', 'max', 'justin']

#### helper funcs ####

def filtered_nodes(id):
    filtered_nodes = [node for node, attrs in G.nodes(data=True) if isinstance(node, tuple) and node[1] == id]
    return filtered_nodes

# def find_all_matchings(graph):
#     matchings = []
#     for nodeset in nx.bipartite.matching.minimum_weight_full_matching(graph):
#         matching = [(u, v) for u, v, _ in nodeset]
#         matchings.append(matching)
#     return matchings

# add nodes
for x in CAST:
    G.add_node((x, 0))
    G.add_node((x, 1))

# add edges
for (u, i) in filtered_nodes(0):
        for (v, j) in filtered_nodes(1):
            if u == v: # don't add edge between someone and themself
                continue
            G.add_edge(u, v)

#### SPOILERS ####
# remove confirmed truth booth no-matches
TRUTH_BOOTH_NO_MATCH = [
    ('justin', 'nour'),
    ('brandon', 'remy'),
    ('kai', 'jenna'),
    ('jenna', 'danny'),
    ('kari', 'kylie'),
]

BLACKOUT_NO_MATCH = [
    ('kylie', 'jenna'),
    ('nour', 'amber'),
    ('jonathan', 'justin'),
    ('max', 'brandon'),
    ('remy', 'basit'),
    ('kari', 'danny'),
    ('paige', 'jasmine'),
    ('aasha', 'kai')
]

G.remove_edges_from(TRUTH_BOOTH_NO_MATCH)
G.remove_edges_from(BLACKOUT_NO_MATCH)

# TODO: add perfect matches
PERFECT_MATCH = [
    ('brandon', 'aasha'),
    ('basit', 'jonathan')
]

print(G.edges())
print(G.number_of_edges())

# remove all the matches including people
MATCHED = [person for tuple in PERFECT_MATCH for person in tuple]

for (u, v) in G.edges():
    if (u, v) in PERFECT_MATCH or (v, u) in PERFECT_MATCH:
        continue
    if u in MATCHED or v in MATCHED:
        G.remove_edge(u, v)

print(G.edges())
print(G.number_of_edges())