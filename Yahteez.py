import random


class Yahtzee:
    def __init__(self):
        self.upper_total = self.upper_bonus = self.lower_total = self.grand_total = self.upper_total_with_bonus = ""
        self.score = ["" for x in range(0, 13)]

    def score_board(self):
        if self.is_game_complete():
            self.finalize_score()

        print(f'\n{"=" * 59}'
              f'\n|{"Yahtzee Score Card":^57s}|'
              f'\n{"=" * 59}'
              f'\n|{"Option":^6s}|{" Upper Section":15s}|{" Scoring":25s}|{"Game":^8s}|'
              f'\n|{"1":^6s}|{" Aces":15s}|{" Count & add only Aces":25s}|{str(self.score[0]):^8s}|'
              f'\n|{"2":^6s}|{" Two":15s}|{" Count & add only Twos":25s}|{str(self.score[1]):^8s}|'
              f'\n|{"3":^6s}|{" Three":15s}|{" Count & add only Threes":25s}|{str(self.score[2]):^8s}|'
              f'\n|{"4":^6s}|{" Four":15s}|{" Count & add only Fours":25s}|{str(self.score[3]):^8s}|'
              f'\n|{"5":^6s}|{" Five":15s}|{" Count & add only Fives":25s}|{str(self.score[4]):^8s}|'
              f'\n|{"6":^6s}|{" Six":15s}|{" Count & add only Sixes":25s}|{str(self.score[5]):^8s}|'
              f'\n|{"":^6s}|{" Total Score":15s}|{"--->":^25s}|{str(self.upper_total):^8s}|'
              f'\n|{"":^6s}|{" Bonus":15s}|{"Score 35":^25s}|{str(self.upper_bonus):^8s}|'
              f'\n|{"":^6s}|{" Total of Upper":15s}|{"--->":^25s}|{str(self.upper_total_with_bonus):^8s}|'

              f'\n|{"_" * 57}|'
              f'\n|{"":^6s}|{" Lower Section":50s}|'

              f'\n|{"7":^6s}|{" 3 of a kind":15s}|{" Add total of all dice":25s}|{str(self.score[6]):^8s}|'
              f'\n|{"8":^6s}|{" 4 of a kind":15s}|{" Add total of all dice":25s}|{str(self.score[7]):^8s}|'
              f'\n|{"9":^6s}|{" Full House":15s}|{" Score 25":25s}|{str(self.score[8]):^8s}|'
              f'\n|{"10":^6s}|{" Sequence of 4":15s}|{" Score 30":25s}|{str(self.score[9]):^8s}|'
              f'\n|{"11":^6s}|{" Sequence of 5":15s}|{" Score 40":25s}|{str(self.score[10]):^8s}|'
              f'\n|{"12":^6s}|{" 5 of a kind":15s}|{" Score 50":25s}|{str(self.score[11]):^8s}|'
              f'\n|{"13":^6s}|{" Chance":15s}|{" All total of 5 dices":25s}|{str(self.score[12]):^8s}|'

              f'\n|{"_" * 57}|'
              f'\n|{"":^6s}|{" Total of lower":15s}|{"--->":^25s}|{str(self.lower_total):^8s}|'
              f'\n|{"":^6s}|{" Total of upper":15s}|{"--->":^25s}|{str(self.upper_total):^8s}|'
              f'\n|{"":^6s}|{" Grand Total":15s}|{"--->":^25s}|{str(self.grand_total):^8s}|'
              f'\n{"=" * 59}'
              )

    def finalize_score(self):
        self.upper_total = 0
        for x in range(0, 6):
            self.upper_total = self.score[x] + self.upper_total

        if self.upper_total >= 63:
            self.upper_bonus = 35
        else:
            self.upper_bonus = 0

        self.upper_total_with_bonus = self.upper_total + self.upper_bonus

        self.lower_total = 0
        for x in range(6, 13):
            self.lower_total = self.score[x] + self.lower_total

        self.grand_total = self.lower_total + self.upper_total_with_bonus

    def is_game_complete(self):
        for each in self.score:
            if each == "":
                return False
        return True

    def roll_dices(self, dices):
        rolls = []
        for x in range(0, dices):
            rolls.append(random.randint(1, 6))
        return rolls

    def play_game(self):
        while not self.is_game_complete():
            dices = 5
            kept = []
            round_ongoing = True
            for x in range(0, 3):
                if dices > 0 and round_ongoing:

                    print(f'{"#" * 59}'
                          f"\nRolling...{x + 1}"
                          f"\nRolling {dices} dices")
                    rolled = self.roll_dices(dices)

                    if x == 0:
                        print("Best Move Here.")

                    not_valid = True
                    while not_valid:
                        print(f'{"Kept:":20s} {kept}')
                        print(f'{"Rolled:":20s} {rolled}')
                        keep_dices = input("Select dices to keep from kept and rolled: ").strip().split()
                        dices_selectable = rolled + kept

                        if len(keep_dices) < 1:
                            not_valid = False

                        else:
                            for each in keep_dices:
                                try:
                                    if int(each) in dices_selectable:
                                        dices_selectable.remove(int(each))
                                        not_valid = False
                                    else:
                                        not_valid = True
                                        print("You don't have these options.")
                                        break
                                except:
                                    print("Invalid Entry!!!")

                    kept = []
                    for each in keep_dices:
                        kept.append(int(each))

                    print(f'{"Dices Kept:":20s} {kept}')
                    print(f'{"Dices To re-roll:":20s} {dices_selectable}')
                    dices = 5 - len(kept)

                    if dices < 0:
                        break

                    while True:
                        if x < 2:
                            print(f'{"Will re-roll: ":20s} {dices}')
                            choice = input("Enter 'R/r' to roll or 'S/s' to score: ")
                            if choice.lower() == 'r':
                                break
                            elif choice.lower() == 's':
                                self.score_board()
                                self.update_score(dices_selectable + kept)
                                self.score_board()
                                round_ongoing = False
                                break
                            else:
                                print("Invalid choice, please try again.")
                        else:
                            self.score_board()
                            self.update_score(dices_selectable + kept)
                            self.score_board()
                            break
            print("Scored...")

    def update_score(self, dices):
        while True:

            choice = input("Choose a valid option: ")
            if self.is_valid_option(choice):

                for x in range(0, 6):
                    if int(choice) == x + 1:
                        self.score[x] = 0
                        for each in dices:
                            if each == x + 1:
                                self.score[x] = self.score[x] + each
                        return

                if choice == "7":
                    total_of_3 = 0
                    for each in dices:
                        if dices.count(each) == 3:
                            for each_dice in dices:
                                total_of_3 = each_dice + total_of_3
                            self.score[6] = total_of_3
                            return
                        else:
                            self.score[6] = 0

                if choice == "8":
                    total_of_4 = 0
                    for each in dices:
                        if dices.count(each) == 4:
                            for each_dice in dices:
                                total_of_4 = total_of_4 + each_dice
                            self.score[7] = total_of_4
                            return
                        else:
                            self.score[7] = 0

                if choice == "9":
                    for each in dices:
                        if dices.count(each) == 3:
                            for each_dice in dices:
                                if dices.count(each_dice) == 2 and each_dice != each:
                                    self.score[8] = 25
                                    return
                        else:
                            self.score[8] = 0

                if choice == "10":
                    if all(x in dices for x in [1, 2, 3, 4]) or all(
                            x in dices for x in [2, 3, 4, 5]) or all(
                        x in dices for x in [3, 4, 5, 6]
                    ):
                        self.score[9] = 30
                    else:
                        self.score[9] = 0

                if choice == "11":
                    if all(x in dices for x in [1, 2, 3, 4, 5]) or all(
                            x in dices for x in [2, 3, 4, 5, 6]):
                        self.score[10] = 40
                    else:
                        self.score[10] = 0

                if choice == "12":
                    if dices.count(dices[0]) == 5:
                        self.score[11] = 50
                    else:
                        self.score[11] = 0

                if choice == "13":
                    total = 0
                    for each in dices:
                        total = each + total
                    self.score[12] = total

                break
            else:
                print("Invalid choice.")

    def is_valid_option(self, choice):
        if choice.isnumeric() and 1 <= int(choice) <= 13 and self.score[int(choice) - 1] == "":
            return True
        else:
            return False


if __name__ == '__main__':
    Yahtzee().play_game()