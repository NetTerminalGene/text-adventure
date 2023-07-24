# The rooms of the game, their info, their items, and directional paths the player can take from them.
rooms = {
    'bedroom': {
        'info': "You're in the bedroom. The upper hallway is north.",
        'paths': {'north': 'upper hallway'}
    },
    'upper hallway': {
        'info': "You're in the upper hallway."
                " North is the bathroom, south is the bedroom, east is the office, "
                "and northwest is the lower hallway downstairs.",
        'paths': {'north': 'bathroom',
                  'south': 'bedroom',
                  'east': 'office',
                  'northwest': 'lower hallway'}
    },
    'bathroom': {
        'info': "You're in the bathroom. South is the upper hallway.",
        'paths': {'south': 'upper hallway'}
    },
    'office': {
        'info': "You're in the office. West is the upper hallway. ",
        'paths': {'west': 'upper hallway'},
    },
    'lower hallway': {
        'info': "You're in the lower hallway. North is the front door, south is the basement, east is the living room, "
                "west is the kitchen, and southwest is the upper hallway.",
        'paths': {'north': 'front door',
                  'south': 'basement',
                  'east': 'living room',
                  'west': 'kitchen',
                  'southwest': 'upper hallway'}
    },
    'front door': {
        'info': "The front door is locked by a keypad. "
                "You need a code. "
                "South is the lower hallway.",
        'paths': {'south': 'lower hallway'},
    },
    'kitchen': {
        'info': "You're in the kitchen. East is the lower hallway.",
        'paths': {'east': 'lower hallway'}
    },
    'living room': {
        'info': "You're in the living room. West is the lower hallway.",
        'paths': {'west': 'lower hallway'}
    },
    'basement': {
        'info': "You're in the basement. North is the lower hallway upstairs. "
                "To your right are two codes scratched into the wall: "
                "0451 and 1234. "
                "Maybe you could USE a CODE... but for what?",
        'paths': {'north': 'lower hallway'}
    },
}


# Starting room.
main_room = 'bedroom'


def quit_game():
    if ask in ['quit']:
        quit()


# User inputs something invalid, such as gibberish.
def invalid_input():
    print("I don't understand that.")


# User inputs a front door keypad code, leading to one of two endings.
def door_code():
    if ask in ['use code']:
        print("Knowing the two keypad codes, you stand at the front door. "
              "But which code is correct?")
        ask_two = input("Enter keypad code: ")
        if ask_two == "0451":
            print("The front door opens and you leave the house. \nGOOD END")
            exit()
        if ask_two == "1234":
            print("The house explodes and you die. \nBAD END")
            exit()
        else:
            print("That doesn't seem to work.")


while True:
    # Show the info of the current room.
    print(rooms[main_room]['info'])
    # What does the player want to do next?
    ask = input("Next action: ").lower()
    # Run door_code() function above.
    door_code()

    # Does the player want to go somewhere else?
    if ask in ['north', 'south', 'east', 'west', 'northwest', 'southwest']:
        # Is where the player wants to go valid?
        if ask in rooms[main_room]['paths']:
            # Change the room.
            main_room = rooms[main_room]['paths'][ask]
        else:
            # Where the player wants to go is invalid.
            print("Sorry, you can't go that way.")
    else:
        # Run invalid_input() function above.
        invalid_input()
    quit_game()
