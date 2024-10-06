def get_score(option_1: str, option_2: str):
    """
    option_1: player 1's option
    option_2: player 2's option
    returns: integer value representing the game's status
            1 means player 1 won
            -1 means player 2 won
            0 means draw
    """
    if option_1 == "Rock":
        if option_2 == "Rock":
            return 0
        if option_2 == "Paper":
            return -1
        if option_2 == "Scissors":
            return 1
    if option_1 == "Paper":
        if option_2 == "Rock":
            return 1
        if option_2 == "Paper":
            return 0
        if option_2 == "Scissors":
            return -1   
    if option_1 == "Scissors":
            if option_2 == "Rock":
                return -1
            if option_2 == "Paper":
                return 1
            if option_2 == "Scissors":
                return 0