% --- Graph Edges ---
edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(e, g).

% --- Heuristic Values ---
h(a, 10).
h(b, 8).
h(c, 5).
h(d, 7).
h(e, 3).
h(f, 6).
h(g, 0).   % goal node

% --- Best First Search ---
best_first(Start, Goal, Path) :-
    bfs([[Start]], Goal, Path).

bfs([[Goal | Rest] | _], Goal, Path) :-
    reverse([Goal | Rest], Path).

bfs([[Node | Rest] | Others], Goal, Path) :-
    findall([Next, Node | Rest],
            (edge(Node, Next), \+ member(Next, [Node | Rest])),
            Children),
    sort_paths(Children, NewPaths),
    append(Others, NewPaths, AllPaths),
    bfs(AllPaths, Goal, Path).

% --- Sort nodes by heuristic value ---
sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_cost, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_cost([Node | _], Cost) :- h(Node, Cost).
