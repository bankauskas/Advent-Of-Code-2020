import re
import networkx as nx

dt = open('input.txt').read()
stopwords = re.compile('(bags\.|bag\.|bags|bag)')
pattern = re.compile('(\d+)\s([a-z]*\s?[a-z]*)')


def clean_data(dt, stopwords):
    return stopwords.sub("", dt).splitlines()


def extract_nodes_from_str(pattern, ls):
    return [pattern.match(i.strip()).groups() for i in ls]


def build_directed_Graph(dt):
    G = nx.DiGraph()

    for raw in dt:
        if 'no other' in raw:
            x, y = raw.split('contain')
            G.add_node(x.strip())
        else:
            k, v = raw.split('contain')  
            v = extract_nodes_from_str(pattern, v.split(','))
            for i in v:
                G.add_weighted_edges_from([(k.strip(), i[1].strip(), int(i[0].strip()))])  
    return G


# list(G.nodes)
counter = 0
extracted_noodes = set()
completed_nodes = set()

dt = clean_data(dt, stopwords)
G = build_directed_Graph(dt)
    
for edge in G.in_edges('shiny gold'):
    extracted_noodes.add(edge[0])


def extract_edges():   
        for node in extracted_noodes.copy():
            if node not in completed_nodes:
                for edge in G.in_edges(node):
                    extracted_noodes.add(edge[0])
                completed_nodes.add(node) 

while extracted_noodes != completed_nodes:
    extract_edges()
        
if __name__ == '__main__':
    print(len(extracted_noodes)) 
