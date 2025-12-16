def player(prev_play, opponent_history=[]):
    # --- RESET STATE ON NEW GAME ---
    if prev_play == "":
        opponent_history.clear()  # <--- ADDED THIS LINE to reset the default list
        player.my_history = []
        player.play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }

    # Initialize attributes if they don't exist
    if not hasattr(player, "my_history"):
        player.my_history = []
    if not hasattr(player, "play_order"):
        player.play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }

    opponent_history.append(prev_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # Signatures
    quincy_p2_moves = ['', 'R', 'P', 'P', 'S', 'R', 'R', 'P', 'P', 'S', 'R']
    abbey_p2_moves = ['', 'P', 'P', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
    kris_p2_moves = ['', 'P', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
    mrugesh_p2_moves = ['', 'R', 'R', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']

    opp = 0

    # Identify Opponent
    if len(opponent_history) >= 11: 
        if opponent_history[:11] == quincy_p2_moves:
            opp = 1
        elif opponent_history[:11] == abbey_p2_moves:
            opp = 2
        elif opponent_history[:11] == kris_p2_moves:
            opp = 3
        elif opponent_history[:11] == mrugesh_p2_moves:
            opp = 4

    guess = "P" # Default starting move

    # --- STRATEGIES ---
    if opp == 1:
        # Quincy
        quincy = ['P', 'P', 'S', 'S', 'R']
        guess = quincy[((len(opponent_history)) % 5)]

    elif opp == 2:
        # Abbey
        if len(player.my_history) >= 2:
            last_two = "".join(player.my_history[-2:])
            if last_two in player.play_order:
                player.play_order[last_two] += 1

        my_last_play = player.my_history[-1] if player.my_history else "R"
        potential_plays = [
            my_last_play + "R",
            my_last_play + "P",
            my_last_play + "S",
        ]
        
        sub_order = {
            k: player.play_order[k]
            for k in potential_plays if k in player.play_order
        }
        
        prediction = "P"
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

        guess = ideal_response[ideal_response[prediction]]

    elif opp == 3:
        # Kris
        if len(player.my_history) > 0:
            guess = ideal_response[ideal_response[player.my_history[-1]]]
        else:
            guess = "P"

    elif opp == 4:
        # Mrugesh
        last_ten = player.my_history[-10:]
        most_frequent = "S"
        if len(last_ten) > 0:
            most_frequent = max(set(last_ten), key=last_ten.count)

        if most_frequent == '':
            most_frequent = "S"

        guess = ideal_response[ideal_response[most_frequent]]

    player.my_history.append(guess)
    return guess