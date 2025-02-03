from pkg.Field import Field

class Board:
    street_data = [
        ("Start", "ST", 0, 0),
        ("Kottbusser Tor", "KT", 5, 4),
        ("Wittenau", "WT", 10, 6),
        ("Event 1", "E1", 0, 0),
        ("Alt-Tegel", "AT", 15, 10),
        ("Tempelhofer Feld", "TF", 20, 12),
        ("Prison", "PR", 0, 0),
        ("Friedrichstraße", "FS", 25, 14),
        ("Museumsinsel", "MI", 30, 16),
        ("Event 2", "E2", 0, 0),
        ("Brandenburger Tor", "BT", 35, 18),
        ("Kurfürstendamm", "KD", 40, 20)
    ]

    board_fields = []

    def __init__(self, playerA, playerB):
        self.playerA = playerA
        self.playerB = playerB
        self.__initialize_fields()
    
    # Private method to initialize all board_fields.
    def __initialize_fields(self):
        for street in Board.street_data:
            new_field = Field(street[0], street[1], street[2], street[3])
            # To do: Add dynamic player icons
            if street[0] == "Start":
                new_field.player_present = f"{self.playerA.icon}{self.playerB.icon}"
                
            Board.board_fields.append(new_field) 
        print("\nAll board fields were added.\n")

    # Private method to assemble the current board status
    def __assemble_board(self):
        visuals = []
        for field in self.board_fields:
            visual = field.state()
            visuals.append(visual)
        
        spacer_field = Field.spacer_field()

        # Combine fields 1-4 line by line to get first board row 
        board_row_1 = ""
        for i in range(len(visuals[0])):  # Loop through each of the 5 field lines
            board_row_1 += visuals[0][i] + "       " + visuals[1][i] + "       " + visuals[2][i] + "       " + visuals[3][i] + "\n"

        # Combine fields 1-4 line by line to get first board row 
        board_row_2 = ""
        for i in range(len(visuals[11])): 
            board_row_2 += visuals[11][i] + "       " + spacer_field[i] + "       " + spacer_field[i] + "       " + visuals[4][i] + "\n"

        # Combine fields 1-4 line by line to get first board row 
        board_row_3 = ""
        for i in range(len(visuals[10])):  # Loop through each of the 5 field lines
            board_row_3 += visuals[10][i] + "       " + spacer_field[i] + "       " + spacer_field[i] + "       " + visuals[5][i] + "\n"

        # Combine fields 1-4 line by line to get first board row 
        board_row_4 = ""
        for i in range(len(visuals[9])):  # Loop through each of the 5 field lines
            board_row_4 += visuals[9][i] + "       " + visuals[8][i] + "       " + visuals[7][i] + "       " + visuals[6][i] + "\n"

        return board_row_1 + board_row_2 + board_row_3 + board_row_4

    def show_board(self):
        print("\n=== Current Board ===\n")
        print(self.__assemble_board())
    
    def move_player(self, player, number):
        crossed_start = False
        current_position = player.position
        player_icon = player.icon

        # Find the current field of the player
        # enumerate() to be able to access index too, inside for loop data is [1, field]
        for data in enumerate(Board.board_fields):
            if data[1].name == current_position:
                current_field = data[1]
                current_index = data[0]
        
        target_index = current_index + number
        if target_index > 11:
            target_index = target_index - 11 - 1 # If traget_index is 12, it should actually continue at 0
            crossed_start = True

        target_field = Board.board_fields[target_index]
        
        # Remove player icon from current field
        if len(current_field.player_present) == 1:
            current_field.player_present = current_field.player_present.replace(player_icon,"  ")
        elif len(current_field.player_present) == 2:
            current_field.player_present = current_field.player_present.replace(player_icon,"")

        # Move player to new field and update position in player instance
        if target_field.player_present == "  ":
            target_field.player_present = player_icon
        else:
            target_field.player_present += player_icon

        player.position = target_field.name

        move_info = [target_field, crossed_start]

        return move_info







