% Tower of Hanoi simple program

hanoi(1, A, C, _) :-
    write('Move disk from '), write(A),
    write(' to '), write(C), nl.

hanoi(N, A, C, B) :-
    N > 1,
    M is N - 1,
    hanoi(M, A, B, C),
    write('Move disk from '), write(A),
    write(' to '), write(C), nl,
    hanoi(M, B, C, A).
