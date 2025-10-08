% --- Facts: fruits and their colors ---
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(watermelon, green).

% --- Match a fruit with its color ---
match_fruit_color(Fruit, Color) :-
    fruit(Fruit, Color).

% --- Find all fruits with a certain color ---
% Using backtracking and findall
fruits_with_color(Color, FruitList) :-
    findall(Fruit, match_fruit_color(Fruit, Color), FruitList).
