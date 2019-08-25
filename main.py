from copy import deepcopy

COMPUTER_SYMBOL = "C"
EMPTY_SYMBOL = " "
GRID_SIZE = 3
LOSS_SCORE = -10
PLAYER_SYMBOL = "P"
POSITION_CHOICES = ["1", "2"]
WIN_SCORE = 10

class Game(object):

    def __init__(self):
        self.grid = [[EMPTY_SYMBOL for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.turn_order = None

    def play(self):
        """
        This function is the only public function of this class and it handles all gameplay logic
        """
        self._ask_user_position()
        self._display_grid()
        turn_order_index = 0
        move_function = self.turn_order[turn_order_index % 2]
        while move_function():
            self._display_grid()
            turn_order_index += 1
            move_function = self.turn_order[turn_order_index % 2]
        print ("The game is over!")
        self._display_grid()

    def _ask_user_position(self):
        user_position_input = raw_input("@player: press 1 to go first, 2 to go second: ")
        while user_position_input not in POSITION_CHOICES:
            user_position_input = raw_input("@player: ERROR (BAD INPUT) press 1 to go first, 2 to go second: ")

        self.turn_order = [self._computer_turn, self._player_turn]
        if user_position_input == "1":
            self.turn_order = [self._player_turn, self._computer_turn]

    def _character_match(self, list_of_characters):
        if all(char == PLAYER_SYMBOL for char in list_of_characters):
            return PLAYER_SYMBOL
        if all(char == COMPUTER_SYMBOL for char in list_of_characters):
            return COMPUTER_SYMBOL
        return EMPTY_SYMBOL

    def _computer_turn(self):
        best_move_index = None
        best_move_score = -float("inf")
        for row, col in self._get_available_indices(self.grid):
            minimax_grid = deepcopy(self.grid)
            minimax_grid[row][col] = COMPUTER_SYMBOL
            score = self._minimax(minimax_grid, 0, False)
            if score > best_move_score:
                best_move_index = (row, col)
                best_move_score = score
            minimax_grid[row][col] = EMPTY_SYMBOL
        optimal_row, optimal_col = best_move_index
        self.grid[optimal_row][optimal_col] = COMPUTER_SYMBOL
        print ("@computer has selected their move")
        game_over_bool, winner = self._game_over(self.grid)
        return not game_over_bool

    def _display_grid(self):
        for idx, row in enumerate(self.grid):
            print ("|".join(row))
            if idx == GRID_SIZE - 1:
                break
            print ("-----")
        print ("\n")

    def _game_over(self, grid):
        for row in grid:
            matching_char = self._character_match(row)
            if matching_char != EMPTY_SYMBOL:
                return True, matching_char
        for column in zip(*grid):
            matching_char = self._character_match(column)
            if matching_char != EMPTY_SYMBOL:
                return True, matching_char
        primary_diagonal = [grid[idx][idx] for idx in range(GRID_SIZE)]
        matching_char = self._character_match(primary_diagonal)
        if matching_char != EMPTY_SYMBOL:
            return True, matching_char
        secondary_diagonal = [grid[idx][GRID_SIZE - 1 - idx] for idx in range(GRID_SIZE)]
        matching_char = self._character_match(secondary_diagonal)
        if matching_char != EMPTY_SYMBOL:
            return True, matching_char
        # The game is over if there are no empty spots left
        empty_spots = False
        for row in grid:
            if " " in row:
                empty_spots = True
        if not empty_spots:
            return True, EMPTY_SYMBOL
        return False, None

    def _get_available_indices(self, grid):
        available_indices = []
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] == EMPTY_SYMBOL:
                    available_indices.append((row, col))
        return available_indices

    def _minimax(self, grid, depth, max_player):
        game_over_bool, winner = self._game_over(grid)
        if game_over_bool:
            if winner == PLAYER_SYMBOL:
                return LOSS_SCORE + depth
            elif winner == COMPUTER_SYMBOL:
                return WIN_SCORE - depth
            return 0

        if max_player:
            best_score = -float("inf")
            for row, col in self._get_available_indices(grid):
                grid[row][col] = COMPUTER_SYMBOL
                score = self._minimax(grid, depth + 1, False)
                best_score = max(score, best_score)
                grid[row][col] = EMPTY_SYMBOL
            return best_score
        best_score = float("inf")
        for row, col in self._get_available_indices(grid):
            grid[row][col] = PLAYER_SYMBOL
            score = self._minimax(grid, depth + 1, True)
            best_score = min(score, best_score)
            grid[row][col] = EMPTY_SYMBOL
        return best_score

    def _player_turn(self):
        grid_choices = [str(num) for num in range(0, GRID_SIZE)]
        player_row = raw_input("@player: pick row (zero indexed) for your turn: ")
        player_column = raw_input("@player: pick column (zero indexed) for your turn: ")
        while (
            player_row not in grid_choices
            or player_column not in grid_choices
            or self.grid[int(player_row)][int(player_column)] != " "
        ):
            player_row = raw_input("@player: ERROR (BAD INPUT) pick row (zero indexed) for your turn: ")
            player_column = raw_input("@player: ERROR (BAD INPUT) pick column (zero indexed) for your turn: ")
        self.grid[int(player_row)][int(player_column)] = "P"
        game_over_bool, winner = self._game_over(self.grid)
        return not game_over_bool


game = Game()
game.play()