% --- Facts ---
fact(sunny).
fact(warm).

% --- Rules ---
rule(go_outside, [sunny, warm]).
rule(play_football, [go_outside, warm]).
rule(swim, [sunny, warm]).

% --- Forward Chaining Inference ---
infer(Goal) :-
    fact(Goal).  % If the goal is already a fact

infer(Goal) :-
    rule(Goal, Preconditions),
    all_facts(Preconditions),
    assertz(fact(Goal)).

% --- Helper: Check if all preconditions are facts ---
all_facts([]).
all_facts([H|T]) :-
    fact(H),
    all_facts(T).
