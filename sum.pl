% Program to find sum of integers from 1 to N

% Base case
sum(0, 0).

% Recursive case
sum(N, Result) :-
    N > 0,
    N1 is N - 1,
    sum(N1, Partial),
    Result is Partial + N.  