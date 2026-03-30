def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    counter = {"R": "P", "P": "S", "S": "R"}

    if len(opponent_history) < 5:
        return "R"

    # -------- Pattern (length 3) --------
    pattern = "".join(opponent_history[-3:])
    patterns = {}

    for i in range(len(opponent_history) - 3):
        seq = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i+3]

        if seq not in patterns:
            patterns[seq] = []
        patterns[seq].append(next_move)

    predicted = None
    if pattern in patterns:
        predicted = max(set(patterns[pattern]), key=patterns[pattern].count)

    # -------- Recent frequency --------
    recent = opponent_history[-12:]
    counts = {"R": 0, "P": 0, "S": 0}

    for move in recent:
        counts[move] += 1

    freq_pred = max(counts, key=counts.get)

    # 🔥 FINAL FIX: dynamic decision
    if predicted and patterns[pattern].count(predicted) > 1:
        final_pred = predicted
    else:
        final_pred = freq_pred

    return counter[final_pred]