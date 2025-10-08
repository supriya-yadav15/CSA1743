% --- Facts: diseases and symptoms ---
disease(flu, [fever, cough, headache, fatigue]).
disease(cold, [cough, sneezing, runny_nose]).
disease(malaria, [fever, headache, chills, sweating]).
disease(chickenpox, [fever, rash, fatigue, headache]).

% --- Rule: Diagnose disease based on symptoms ---
diagnose(Symptoms, Disease) :-
    disease(Disease, DiseaseSymptoms),
    subset(Symptoms, DiseaseSymptoms).

% --- Helper: Check if all symptoms match ---
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).
