import json
    
def load_player():
    # Attempt to open player_save file
    try:
        with open("player_save.json") as file:
            player_data = json.load(file)
            # Ask if user would like to load the player
            load_player = input(f"Would you like to load player: {player_data}? (y/n): ")
            while True:
                if load_player.lower() == 'y':
                    # If yes, return the stored values
                    name = player_data["name"]
                    max_hitpoints = player_data["max-hitpoints"]
                    current_hp = player_data["current-hitpoints"]
                    player_class = player_data["class"]
                    return name, max_hitpoints, current_hp, player_class
                elif load_player.lower() == 'n':
                    # If no, return None and then ask the user which type of character they would like to create
                    return None
                else:
                    print("Please enter either y/n")
                    # Return error if no saved player file found and then ask to create a new character
    except Exception as e:
        print(f"Unable to load player data: {str(e)}")
        return None
    