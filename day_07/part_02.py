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

dt = clean_data(dt, stopwords)
G = build_directed_Graph(dt)


def sum_of_bags(node='shiny gold'):
    c=0 
  
    edges=G.out_edges(node)

    if len(edges) > 0:

        for _, sub_node in edges:
            value = G.get_edge_data(_,sub_node)['weight']
            c+=value+value*count(sub_node)

    return c

if __name__ == '__main__':
    print(sum_of_bags())