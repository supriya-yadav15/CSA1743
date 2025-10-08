% --- Facts ---
diet(diabetes, 'Eat more green vegetables, avoid sugar and white rice.').
diet(hypertension, 'Eat low-salt food, avoid oily and fried items.').
diet(obesity, 'Eat more fruits, drink water, avoid junk food.').
diet(anemia, 'Eat iron-rich food like spinach and liver.').
diet(heart_disease, 'Eat oats, vegetables, avoid red meat.').
diet(fever, 'Eat light food like soup, drink more water.').

% --- Rule ---
suggest_diet(Disease) :-
    diet(Disease, Advice),
    write('Suggested diet for '), write(Disease), write(':'), nl,
    write(Advice), nl.
