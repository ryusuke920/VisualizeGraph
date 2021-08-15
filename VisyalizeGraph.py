from graphviz import Graph
from graphviz import Digraph

class VisualizeGraph:
    def __init__(self, Node: int, Edge: int, Indexed: int, graph_number: int) -> None:
        '頂点数, 辺の数, index指定'
        self.directed_graph = Digraph(format='pdf')
        self.undirected_graph = Graph(format='pdf')
        self.directed_graph.attr('node', shape='circle', color='blue')
        self.undirected_graph.attr('node', shape='circle', color='blue')
        self.directed_graph.attr('edge', shape='circle', color='blue')
        self.undirected_graph.attr('edge', shape='circle', color='blue')
        self.Node = Node
        self.Edge = Edge
        self.Indexed = Indexed
        self.graph = [[] for _ in range(Node)]
        self.graph_number = graph_number

    def DirectedDijkstraGraphWithWeight(self) -> None:
        '有向グラフ重み有り'
        for _ in range(self.Edge):
            u, v, weight = map(int,input().split())
            self.directed_graph.edge(f'{u+self.Indexed}', f'{v+self.Indexed}', label=f'{weight}')

    def DirectedDijkstraGraphWithoutWeight(self) -> None:
        '有向グラフ重み無し'
        for _ in range(self.Edge):
            u, v = map(int,input().split())
            self.directed_graph.edge(f'{u + self.Indexed}', f'{v + self.Indexed}')

    def UndirectedDijkstraGraphWithWeight(self) -> None:
        '無向グラフ重み有り'
        for _ in range(self.Edge):
            u, v, weight = map(int,input().split())
            self.undirected_graph.edge(f'{u + self.Indexed}', f'{v + self.Indexed}', label=f'{weight}')

    def UndirectedDijkstraGraphWithoutWeight(self) -> None:
        '無向グラフ重み無し'
        for _ in range(self.Edge):
            u, v = map(int,input().split())
            self.undirected_graph.edge(f'{u + self.Indexed}', f'{v + self.Indexed}')
    
    def ViewGraph(self) -> None:
        'グラフを描画する'
        if self.graph_number <= 2:
            self.directed_graph.view()
        elif self.graph_number >= 3:
            self.undirected_graph.view()


'''
indexedについて
0 -> 0-indexed
1 -> 1-indexed

graph_numberについて
1 -> 有向グラフ重み有り
2 -> 有向グラフ重み無し
3 -> 無向グラフ重み有り
4 -> 無向グラフ重み無し
'''
# 63-66行目のみ変更する
indexed = 0
graph_number = 4
Node = int(input()) # 頂点の数
Edge = Node - 1 # 辺の本数

VizGraph = VisualizeGraph(Node, Edge, indexed, graph_number) # インスタンスの生成

if graph_number == 1:
    VizGraph.DirectedDijkstraGraphWithWeight()
elif graph_number == 2:
    VizGraph.DirectedDijkstraGraphWithoutWeight()
elif graph_number == 3:
    VizGraph.UndirectedDijkstraGraphWithWeight()
elif graph_number == 4:
    VizGraph.UndirectedDijkstraGraphWithoutWeight()

VizGraph.ViewGraph()