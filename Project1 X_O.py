# Function choosing shura and tur number

def get_move(luah_mishak, Sahkan):
    valid_input = False

    while not valid_input:
        shura = int(input("Sahkan, enter shura number (0-2): "))
        tur = int(input("Sahkan, enter tur number (0-2): "))

        if shura in range(3) and tur in range(3):
            if luah_mishak[shura][tur] == "_":
                luah_mishak[shura][tur] = Sahkan
                valid_input = True
            else:
                print("That space is already occupied. Please choose another one.")
        else:
            print("shura and tur numbers must be between 0 and 2. Please enter valid numbers.")
    return luah_mishak

# check all shurot and turim

def check_win(luah_mishak):
    for shura in luah_mishak:
        if shura[0] == shura[1] == shura[2] != "_":
            return shura[0]

    for i in range(3):
        if luah_mishak[0][i] == luah_mishak[1][i] == luah_mishak[2][i] != "_":
            return luah_mishak[0][i]


    if luah_mishak[0][0] == luah_mishak[1][1] == luah_mishak[2][2] != "_":
        return luah_mishak[0][0]
    elif luah_mishak[0][2] == luah_mishak[1][1] == luah_mishak[2][0] != "_":
        return luah_mishak[0][2]

    # no winner
    return None

def check_tiko(luah_mishak):
    for shura in luah_mishak:
        if "_" in shura:
            return False
    return True

def print_luah_mishak(luah_mishak):
    for shura in luah_mishak:
        print(" ".join(shura))


# Welcome to the game and choosing name and symbol:

def new_game():
    luah_mishak = [["_","_","_"],["_","_","_"],["_","_","_"]]
    print("Welcome to the Roman's game X and O!")
    player1_name= input("Shalom Sahkan1, please enter your name: ")
    player1_symbol = input("Hi " + player1_name + ", please choose your symbol (X/O): ")

    while player1_symbol not in ["X", "O"]:
        player1_symbol = input("Invalid symbol, please choose X or O: ")

    player2_name = input("Shalom Sahkan2, please enter your name: ")
    player2_symbol = "O" if player1_symbol == "X" else "X"

    print(player1_name + " is " + player1_symbol + ", " + player2_name + " is " + player2_symbol)
    choosing_player = player1_name

    print(player1_name, "It's your turn to play! Good luck!")

    print("Starting new game...")
    print_luah_mishak(luah_mishak)


    while True:
        # player X's turn
        get_move(luah_mishak, "X",)
        print_luah_mishak(luah_mishak)
        winner = check_win(luah_mishak)
        if winner:
            print(f"Congratulations, {winner} wins!")
            break

        if check_tiko(luah_mishak):
            print("It's a tiko!")
            break

        # player O's turn
        get_move(luah_mishak, "O")
        print_luah_mishak(luah_mishak)

        winner = check_win(luah_mishak)
        if winner:
            print(f"Congratulations, {winner} wins!")
            break

        if check_tiko(luah_mishak):
            print("It's a tiko!")
            break

    new_game()

# start the game
new_game()


