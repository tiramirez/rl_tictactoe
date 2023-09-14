from random import randint

class tictactoe:
    def __init__(self):
        self.grid = [' ' for i in range(9)]
        self.turn = 'X'
        self.keep_playing = True
        self.score = {'X':0,'O':0}

    def change_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
        print(f"Now it is {self.turn} turn to play")
    
    def check_winner(self):
        candidates = [[0,1,2],[3,4,5],[6,7,8],
                      [0,3,6],[1,4,7],[2,5,8],
                      [0,4,8],[2,4,6]]
        for i in candidates:
            if self.grid[i[0]] == self.turn and self.grid[i[1]] == self.turn and self.grid[i[2]] == self.turn:
                print("=================")
                print("    GAME OVER    ")
                print(f" THE WINNER IS {self.turn}")
                print("=================")
                self.keep_playing = False
        if self.keep_playing:
            self.change_turn()

    def print_board(self):
        # print(self.grid)
        print("\n\n {0} : {1} : {2} |\n---+---+---|\n {3} : {4} : {5} |\n---+---+---|\n {6} : {7} : {8} |\n===========#\n\n".format(*self.grid))

    def player_move(self):
        try:
            tile_number = int(input("Please enter tile number: ").rstrip())
            if tile_number < 1 or tile_number > 9:
                self.player_move()
        except:
            self.player_move()

        if self.grid[tile_number-1] == ' ':
            self.grid[tile_number-1] = self.turn
            self.print_board()
            self.check_winner()

        else:
            print("That tile is already taken")
            self.player_move()


    def two_player(self):
        print("\n\n 1 : 2 : 3 |\n---+---+---|\n 4 : 5 : 6 |\n---+---+---|\n 7 : 8 : 9 |")
        # print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")
        print('='*11+'#\n\n')

        while self.keep_playing:
            self.player_move()
    
    def cpu_move(self):
        try:
            tile_number = randint(1,9)
            if tile_number < 1 or tile_number > 9:
                self.cpu_move()
        except:
            self.cpu_move()

        if self.grid[tile_number-1] == ' ':
            self.grid[tile_number-1] = self.turn
            self.print_board()
            self.check_winner()
        else:
            # print("That tile is already taken")
            self.cpu_move()

    def one_player(self):
        print("\n\n 1 | 2 | 3 U\n---+---+---U\n 4 | 5 | 6 U\n---+---+---U\n 7 | 8 | 9 U")
        print('='*11+'#\n\n')
        while self.keep_playing:
            self.player_move()
            self.cpu_move()

    def select_mode(self):
        try:
            game_mode = int(input("Select mode\n1) Two Player\n2) Single Player (random)"))
            if game_mode < 1 or game_mode > 2:
                self.select_mode()
        except:
            self.select_mode()

        if game_mode == 1:
            self.two_player()
        elif game_mode == 2:
            self.one_player()




if __name__ == "__main__":
    game = tictactoe()
    game.select_mode()
