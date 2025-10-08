

def minimax(state, is_ai):
    if state == 0:
        return -1 if is_ai else 1

    if is_ai:
        best = -10
        for move in [1,2,3]:
            if state - move >= 0:
                best = max(best, minimax(state - move, False))
        return best
    else:
        best = 10
        for move in [1,2,3]:
            if state - move >= 0:
                best = min(best, minimax(state - move, True))
        return best

def best_move(state):
    best_score = -10
    move_choice = 1
    for move in [1,2,3]:
        if state - move >= 0:
            score = minimax(state - move, False)
            if score > best_score:
                best_score = score
                move_choice = move
    return move_choice

state = 10
while state > 0:
    print(f"\nCurrent state: {state}")
    human = int(input("Your move (1,2,3): "))
    state -= human
    if state == 0:
        print("You lose! AI wins.")
        break
    ai = best_move(state)
    print(f"AI chooses: {ai}")
    state -= ai
    if state == 0:
        print("AI loses! You win.")
        break
