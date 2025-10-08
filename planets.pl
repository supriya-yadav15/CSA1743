planet(mercury, 1, terrestrial).
planet(venus,   2, terrestrial).
planet(earth,   3, terrestrial).
planet(mars,    4, terrestrial).
planet(jupiter, 5, gas_giant).
planet(saturn,  6, gas_giant).
planet(uranus,  7, ice_giant).
planet(neptune, 8, ice_giant).

planet_info(Name, Order, Type) :-
    planet(Name, Order, Type).

planets_of_type(Type, Name) :-
    planet(Name, _, Type).
