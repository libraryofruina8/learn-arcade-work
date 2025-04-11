# defining the room class

class Room:

    def __init__(self, description, north, east, south, west):
        # attributes for the rooms
        self.description = ""
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0

def main():
    # empty list meant to hold the rooms later
    room_list = []
    done = False
    room_0 = Room("It's a dark and stormy night, but you've found shelter in a seemingly uninhabited mansion. You're standing in the entrance hall and the door behind you has somehow locked. The only way forward is north.",
                1,
                None,
                None,
                None)

    room_list.append(room_0)

    room_1 = Room("Seems you've entered the main hall. A large staircase stands in the middle, but for some reason it's blocked off by chains. Your only options are the doors on the east and west sides of the room. ",
                None,
                3,
                0,
                2)

    room_list.append(room_1)

    room_2 = Room("This must be the dining room. A table sits alone in the center of the room with no guests to entertain. It doesn't seem like there's a way forward from here, best to turn back.",
                None,
                1,
                None,
                None)

    room_list.append(room_2)

    room_3 = Room("A completely empty room. Who knows what it was meant for? Regardless, the only way forward is north.",
                4,
                None,
                None,
                1)

    room_list.append(room_3)

    room_4 = Room("A long hallway stretches out before you, a door in every direction. Which will you decide to go through?",
                7                ,
                6,
                3,
                5)

    room_list.append(room_4)

    room_5 = Room("Looks to be a young boy's bedroom, toys strewn across the floor. You think you hear a breeze coming from the closet to the west.",
                None,
                4,
                None,
                8)

    room_list.append(room_5)

    room_6 = Room("Looks to be a young girl's bedroom. A vanity sits close to the door you entered from. Nothing of interest here, better turn back.",
                None,
                None,
                None,
                4)

    room_list.append(room_6)

    room_7 = Room("Likely the master bedroom. A bed fit for a king sits in the middle of the large room. Nothing of interest here, better turn back.",
                None,
                None,
                4,
                None)

    room_list.append(room_7)

    room_8 = Room("The closet was actually an entrance to a back porch! How odd. No matter, the rain has stopped and you've escaped the mansion. Lucky you! Though I suppose you could always turn back and investigate any rooms you may have missed.",
                None,
                5,
                None,
                None)

    room_list.append(room_8)

    # starting room
    current_room = room_list[0]

    while not done:
        # room 0
        if current_room == room_list[0]:
            print()
            print(room_list[0].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

        # room 1
        if current_room == room_list[1]:
            print()
            print(room_list[1].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

        # room 2
        if current_room == room_list[2]:
            print()
            print(room_list[2].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

        # room 3
        if current_room == room_list[3]:
            print()
            print(room_list[3].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

        # room 4
        if current_room == room_list[4]:
            print()
            print(room_list[4].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

        # room 5
        if current_room == room_list[5]:
            print()
            print(room_list[5].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

        # room 6
        if current_room == room_list[6]:
            print()
            print(room_list[6].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

        # room 7
        if current_room == room_list[7]:
            print()
            print(room_list[7].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

        if current_room == room_list[8]:
            print()
            print(room_list[8].description)
            user_choice = input("Which way would you like to go? Please enter the first letter of the direction you wish to travel. ")
            if user_choice.lower() == "N" or user_choice.lower() == "n":
                if current_room.north is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.north]
            elif user_choice.lower() == "S" or user_choice.lower() == "s":
                if current_room.south is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.south]
            elif user_choice.lower() == "E" or user_choice.lower() == "e":
                if current_room.east is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.east]
            elif user_choice.lower() == "W" or user_choice.lower() == "w":
                if current_room.west is None:
                    print("Try a different direction.")
                else:
                    current_room = room_list[current_room.west]
            else:
                print("Error.")

main()