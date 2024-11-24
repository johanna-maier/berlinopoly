class Field:
    def __init__(self, name, short_name, price, rent):
        self.name = name
        self.short_name = short_name
        self.player_present = "  "
        self.price = price
        self.rent = rent
        self.rent_w_house = rent * 2

        if short_name in ["ST", "E1", "E2", "PR"]:
           self.owner = "city property"
           self.house = "--"
        else:
           self.owner = "for sale"
           self.house = "  "


    def state(self):
        n = self.short_name
        h = self.house
        o = self.player_present
        if o == "  ":
            field = [
                f" ______ ",
                f"|  {n}  |",
                f"|  {h}  |",
                f"|  {o}  |",
                f" ‾‾‾‾‾‾ "
            ]
        elif len(o) == 2: # Case for 2 icons next to each other
            field = [
                f" ______ ",
                f"|  {n}  |",
                f"|  {h}  |",
                f"| {o} |",
                f" ‾‾‾‾‾‾ "
            ]
        else:
            field = [
                f" ______ ",
                f"|  {n}  |",
                f"|  {h}  |",
                f"|  {o}  |",
                f" ‾‾‾‾‾‾ "
            ]

        return field
    
    @staticmethod # Call with Field.spacer_field()
    def spacer_field():                
        return [
            f"        ",
            f"        ",
            f"        ",
            f"        ",
            f"        "
        ]
        
