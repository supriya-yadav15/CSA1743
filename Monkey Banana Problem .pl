% --- Monkey Banana Problem ---

% State representation: state(MonkeyPosition, BoxPosition, HasBanana)

% Initial State
initial(state(at_door, at_window, no)).

% Goal State
goal(state(_, _, yes)).

% --- Actions ---
move(state(at_door, Box, no), walk, state(at_window, Box, no)).
move(state(at_window, Box, no), push_box, state(at_banana, at_banana, no)).
move(state(at_banana, at_banana, no), climb_box, state(on_box, at_banana, no)).
move(state(on_box, at_banana, no), grab_banana, state(on_box, at_banana, yes)).

% --- Solution Rule ---
can_get_banana(State) :-
    goal(State),
    write('Monkey has the banana!'), nl.

can_get_banana(State) :-
    move(State, Action, NextState),
    write('Monkey performs: '), write(Action), nl,
    can_get_banana(NextState).

% --- To Start the Process ---
start :-
    initial(State),
    can_get_banana(State).
