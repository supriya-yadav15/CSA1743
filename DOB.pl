% Facts about people and their DOBs
dob(john, date(1990, 5, 1)).
dob(jane, date(1985, 12, 10)).
dob(bob,  date(1978, 2, 28)).
dob(sue,  date(1995, 8, 15)).
dob(tom,  date(2000, 4, 22)).

% Predicate to look up a person's DOB by name
lookup(Name, DOB) :-
    dob(Name, DOB).
