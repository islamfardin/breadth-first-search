# breadth-first-search
A breadth-first-search algorithm based off of this pseudocode
WIP


BFS(G, s)
for every vertex u in V[G]\{s} loop
  color[u]:=white;
  d[u]:=INF;
  Parent[u]:=NIL;
end{loop}

color[s]:=gray; d[s]:=0; Parent[s]=NIL;

Q:={};ENQUEUE(Q,s);

while Q!={} loop
  u = DEQUEUE(Q);
  for every v in Adj[u] loop
    if color[v]==white then
      color[v]:=gray;
      d[v]=d[u]+1:Parent[v]=u:
      ENQUEUE(Q,v);
     end{if}
    end{loop}
    color[u]=black;
  end{loop}
  end{BFS}

