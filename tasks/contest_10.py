def knight_vs_king(knight_position, king_position):
    knight_position = knight_position[0], (ord(knight_position[1]) - 60)
    king_position = king_position[0], (ord(king_position[1]) - 60)
    distance = pow(knight_position[0] - king_position[0], 2) + pow(knight_position[1] - king_position[1], 2)
    if distance == 5:
        return "Knight"
    elif distance == 2 or distance == 1:
        return "King"
    else:
        return "None"


print(knight_vs_king([7, "A"], [8, "A"]))
