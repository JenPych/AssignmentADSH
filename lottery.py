import random

# game1 = megamillions 1-70 and 1- 25
# game2 = powerball ball 1-69 and 1-26

while True:
    game1 = ["megamillion", "mega", "megamillions", "m", "mm", "mega million"]
    game2 = ["power", "powerball", "power ball", "p", "pb"]

    def lottery_number(end1):
        result = []

        for i in range(5):
            new = random.randint(1, end1)
            result.append(new)

        return result


    def mega_power(end2):
        mp = []

        for x in range(1):
            ball = random.randint(1, end2)
            mp.append(ball)

        return mp


    playing: str = input("Are you playing MegaMillions or Powerball?: ").lower()

    if playing in game1:
        end_1 = 71
        end_2 = 26
        print(f"Lottery number: {lottery_number(end_1)} and MegaMillion number is {mega_power(end_2)}")
        break

    elif playing in game2:
        end_1 = 70
        end_2 = 27
        print(f"Lottery number: {lottery_number(end_1)} and Powerball number is {mega_power(end_2)}")
        break

    else:
        print("Enter correct game!")
        continue