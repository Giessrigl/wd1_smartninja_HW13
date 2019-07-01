import random
import json
import datetime


class Result:
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date


# INPUT A ----------------------------------------------------------------------------------->


def play_game(level):
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    secret = random.randint(1, 10)
    attempts = 0
    wrong_guesses = []
    while True:
        guess = (input("guess the secret number (1-10):\n"))
        if guess.isdigit() is True:
            guess_int = int(guess)
            attempts += 1
            if guess_int == secret:
                # Save Everything into Text File ------------------------------------------------->
                score_list.append({"level": level, "attempts": attempts, "date": str(current_time), "name": str(name),
                                   "secret": str(secret), "wrong_guesses": wrong_guesses})
                with open("score_list.txt", "w") as score_file:
                    score_file.write(json.dumps(score_list))

                # Save Results into Text File ---------------------------------------------------->
                save_result = Result(score=attempts, player_name=name, date=current_time)
                with open("results.txt", "a") as result_file:
                    result_file.write(str(save_result.__dict__) + "\n")

                print("Congratulation! You win!")
                print("Attempts needed: " + str(attempts))
                break
            elif guess_int < secret:
                if level == "easy":
                    print("Wrong number! You need to go up!")
            elif guess_int > secret:
                if level == "easy":
                    print("Wrong number! You need to go down!")
            wrong_guesses.append(guess_int)
        else:
            print("Wrong input")
            continue
# INPUT B ------------------------------------------------------------------------------------>


def see_score():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
# LIST TOP SCORES OF EASY MODE -------------------------------------------------------------->
    print("Easy mode:")
    list_easy = [i for i in score_list if not (i['level'] == "hard")]
    score_list_easy = sorted(list_easy, key=lambda k: k["attempts"])[:3]
    for score_dict in score_list_easy:
        print("Top scores: " + (str(score_dict.get("attempts")) + " attempt(s), date: " + str(score_dict.get("date"))
                                + ", name: " + str(score_dict.get("name")) + ", number was: " +
                                str(score_dict.get("secret"))))

# LIST TOP SCORES OF HARD MODE ---------------------------------------------------------------->
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    print("Hard mode:")
    list_hard = [i for i in score_list if not (i['level'] == "easy")]
    score_list_hard = sorted(list_hard, key=lambda k: k["attempts"])[:3]
    for score_dict in score_list_hard:
        print("Top scores: " + (str(score_dict.get("attempts")) + " attempt(s), date: " + str(score_dict.get("date"))
                                + ", name: " + str(score_dict.get("name")) + ", number was: " + str(
                    score_dict.get("secret"))))

# INPUT D ------------------------------------------------------------------------------------->


def delete_score():
    with open("results.txt", "w") as result_file:
        result_file.write("")
    with open("score_list.txt", "w") as score_file:
        score_file.write("[]")
# ,,Start Screen ´´ --------------------------------------------------------------------------->


current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
name = str(input("What's your name? \n"))
print(current_time)

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, "
                      "C) delete the scores, or D) quit? \n")

    if selection.lower() == "a":
        while True:
            difficulty = input("Select Mode (easy/hard):\n")
            if difficulty.lower() == "easy":
                play_game(level="easy")
                break
            elif difficulty.lower() == "hard":
                play_game(level="hard")
                break
            else:
                print("Wrong input")
                continue

    elif selection.lower() == "b":
        see_score()

    elif selection.lower() == "c":
        delete_score()

    elif selection.lower() == "d":
        print("Goodbye " + str(name))
        break

    else:
        print("Wrong input")
        continue
