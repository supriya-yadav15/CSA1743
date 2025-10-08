% --- Facts ---
fact(sunny).
fact(warm).

% --- Rules ---
rule(go_outside, [sunny, warm]).
rule(play_football, [go_outside, warm]).
rule(swim, [sunny, warm]).

% --- Backward Chaining Inference ---
infer(Goal) :-
    fact(Goal).  % Goal is a known fact

infer(Goal) :-
    rule(Goal, Preconditions),
    satisfy(Preconditions).

% --- Helper: Satisfy all conditions ---
satisfy([]).
satisfy([H|T]) :-
    infer(H),
    satisfy(T).
