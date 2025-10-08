Sdef evaluate(state):
    return -1 if state == 0 else 0

def game_over(state):
    return state == 0

def alpha_beta(state, depth, alpha, beta, is_ai):
    if depth == 0 or game_over(state):
        return evaluate(state)
    if is_ai:
        best = -999
        for move in [1,2,3]:
            if state - move >= 0:
                score = alpha_beta(state - move, depth-1, alpha, beta, False)
                best = max(best, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best
    else:
        best = 999
        for move in [1,2,3]:
            if state - move >= 0:
                score = alpha_beta(state - move, depth-1, alpha, beta, True)
                best = min(best, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best

def best_move(state):
    best_score = -999
    move_choice = 1
    for move in [1,2,3]:
        if state - move >= 0:
            score = alpha_beta(state - move, 10, -999, 999, False)
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
