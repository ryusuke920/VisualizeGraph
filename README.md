# VisualizeGraph
A tool for visualizing graph problems.

## How to use

**1. Install the library**  

Installation of Graphviz
```
$ brew install graphviz
```
Installation of Wrapper
```
$ pip install graphviz
```

**2. Initial setting (Settings on lines 63-66)**  

**indexed**
|indexed|setting|
|:--:|:--:|
|0-indexed|0|
|1-indexed|1|

**graph_number**
|Graph type|graph_numnber|
|:--:|:--:|
|directed graph with weight|1|
|directed graph without weight|2|
|undirected graph with weight|3|
|undirected graph without weight|4|

**Node**  
The number of vertex  

**Edge**  
The number of edge  

**setting example**
```python
63  indexed = 0
64  graph_number = 2
65  Node = int(input()) # 頂点の数
66  Edge = Node - 1 # 辺の本数
```

## Image diagram
|type 1|type 2|type 3|type 4|
|---|---|---|---|
|<img width="410" alt="スクリーンショット 2021-08-15 18 56 32" src="https://user-images.githubusercontent.com/66785066/129474683-6f2f2d80-47d9-4326-abb5-b016b7e542c7.png">|<img width="303" alt="スクリーンショット 2021-08-15 18 57 03" src="https://user-images.githubusercontent.com/66785066/129474688-ea1a2a0f-dfc8-4bd6-a222-8a1d9891057f.png">|<img width="410" alt="スクリーンショット 2021-08-15 18 56 01" src="https://user-images.githubusercontent.com/66785066/129474682-ee38c858-133b-49a6-ac9a-00baffbed3c8.png">|<img width="302" alt="スクリーンショット 2021-08-15 18 54 17" src="https://user-images.githubusercontent.com/66785066/129474677-af5c70b0-f7bf-4cd5-8398-b7d5d5b31014.png">|

## Contact
If you have any questions, please use an issue.
