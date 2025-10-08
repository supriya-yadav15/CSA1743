% --- Facts ---

% Gender information
female(pam).
female(liz).
female(ann).
female(pat).

male(tom).
male(bob).
male(jim).

% Parent relationships
parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(pam, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

% --- Rules ---

% Mother relation
mother(X, Y) :- 
    female(X), 
    parent(X, Y).

% Father relation
father(X, Y) :- 
    male(X), 
    parent(X, Y).

% Grandfather relation
grandfather(X, Y) :-
    male(X),
    parent(X, Z),
    parent(Z, Y).

% Grandmother relation
grandmother(X, Y) :-
    female(X),
    parent(X, Z),
    parent(Z, Y).

% Sister relation
sister(X, Y) :-
    female(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Brother relation
brother(X, Y) :-
    male(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
