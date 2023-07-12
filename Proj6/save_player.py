import json
def save_player(name, max_hitpoints, current_hp, player_class):
    # Data to be written
    savefile = {
        "name": name,
        "max-hitpoints": max_hitpoints,
        "current-hitpoints": current_hp,
        "class": player_class
    }

    # Serializing json
    json_object = json.dumps(savefile, indent=4)

    # Writing to sample.json
    with open("player_save.json", "w") as outfile:
        outfile.write(json_object)
        