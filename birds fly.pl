% Facts: birds that can fly
can_fly(eagle).
can_fly(parrot).
can_fly(sparrow).

% Facts: birds that cannot fly
cannot_fly(ostrich).
cannot_fly(penguin).
cannot_fly(kiwi).

% Rule: check if a bird can fly
bird_flight(Bird, 'can fly') :-
    can_fly(Bird).

bird_flight(Bird, 'cannot fly') :-
    cannot_fly(Bird).
