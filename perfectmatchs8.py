
import networkx as nx

G = nx.Graph()
CAST = ['aasha', 'paige', 'amber', 'nour', 'basit', 'jonathan', 'brandon', 'remy', 'kai', 'danny', 'jasmine', 'jenna', 'kari', 'kylie', 'max', 'justin']

#### helper funcs ####

def filtered_nodes(id):
    filtered_nodes = [node for node, attrs in G.nodes(data=True) if isinstance(node, tuple) and node[1] == id]
    return filtered_nodes

def possible_matches_for(person):
    return list(filter(lambda tup: tup[0] == person or tup[1] == person, G.edges()))

def potential_matchings():
    # Find connected components in the bipartite graph
    components = list(nx.connected_components(G))

    # Find maximum matchings for each component
    all_matchings = []
    for comp in components:
        subgraph = G.subgraph(comp)
        matchings = nx.bipartite.maximum_matching(subgraph)
        all_matchings.extend(matchings)

    # Print all matchings
    for matching in all_matchings:
        print(matching)
    
    return all_matchings


# add nodes
for x in CAST:
    G.add_node((x, 0), bipartite=0)
    G.add_node((x, 1), bipartite=1)

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

# remove all the matches including people, except for their perfect match
MATCHED = [person for tuple in PERFECT_MATCH for person in tuple]

for (u, v) in G.edges():
    if (u, v) in PERFECT_MATCH or (v, u) in PERFECT_MATCH: 
        continue
    if u in MATCHED or v in MATCHED:
        G.remove_edge(u, v)

# print(G.edges())
# print(G.number_of_edges())

#### test ####
# print(possible_matches_for('justin'))
potential_matchings()