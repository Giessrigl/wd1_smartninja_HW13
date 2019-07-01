class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)
kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586, yellow_cards=95, red_cards=11)
messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

ask = input("Do you want to add a Player? (Y/N): ")
while True:
    if ask.lower() == "y":
        ask_game = input("Football or Basketball? (F/B): ")

        player_first_name = input("Enter the player´s first name: ")
        player_last_name = input("Enter the player´s last name: ")
        player_height_cm = input("Enter player height (cm): ")
        player_weight_kg = input("Enter player weight (kg): ")

        if ask_game.upper() == "F":

            player_goals = input("Enter the player´s goals: ")
            player_yellow_cards = input("Enter the player´s yellow cards: ")
            player_red_cards = input("Enter the player´s red cards: ")

            random_player = FootballPlayer(first_name=player_first_name, last_name=player_last_name, height_cm=player_height_cm, weight_kg=player_weight_kg, goals=player_goals, yellow_cards=player_yellow_cards, red_cards=player_red_cards)

            with open("footballplayers.txt", "a") as f:
                f.write(str(random_player.__dict__) + "\n")

            ask_2 = input("Do you want to add another Player? (Y/N): ")
            if ask_2.upper() == "N":
                break

        elif ask_game.upper() == "B":
            player_points = input("Enter the player´s points: ")
            player_rebounds = input("Enter the player´s rebounds: ")
            player_assists = input("Enter the player´s assists: ")

            random_player = BasketballPlayer(first_name=player_first_name, last_name=player_last_name, height_cm=player_height_cm, weight_kg=player_weight_kg, points=player_points, rebounds=player_rebounds, assists=player_assists)

            with open("basketballplayers.txt", "a") as b:
                b.write(str(random_player.__dict__) + "\n")

            ask_2 = input("Do you want to add another Player? (Y/N): ")
            if ask_2.upper() == "N":
                break
        else:
            continue

    else:
        break

