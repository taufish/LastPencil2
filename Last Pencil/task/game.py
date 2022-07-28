import random

print("How many pencils do you want to use?")
while True:
    try:
        start_pencils = int(input())
        if start_pencils <= 0:
            print("The number of pencils should be positive")
        else:
            break
    except ValueError:
        print("The number of pencils should be numeric")

players = ["John", "Jack"]
print("Who will be the first (John, Jack)")
while True:
    current_player = input()
    if current_player in players:
        break
    else:
        print("Choose between 'John' and 'Jack'")

while start_pencils > 0:
    print("|" * start_pencils)
    print(current_player + "'s turn:")
    while True:
        if current_player == "John":
            try:
                take = int(input())
                if 3 >= take > 0:
                    if start_pencils - take < 0:
                        print("Too many pencils were taken")
                    else:
                        start_pencils -= take
                        current_player = "Jack"
                        break
                elif take > 3 or take <= 0:
                    print("Possible values: '1', '2' or '3'")
            except ValueError:
                print("Possible values: '1', '2' or '3'")
        elif current_player == "Jack":
            losing = []
            x = range(1, start_pencils + 1, 4)
            for n in x:
                losing.append(n)
            if start_pencils in losing:
                if start_pencils == 1:
                    jacks_pencils = 1
                else:
                    jacks_pencils = random.randint(1, 3)
            else:
                step1_losing = start_pencils // 4
                try:
                    losing_position = losing[step1_losing]
                except IndexError:
                    losing_position = losing[-1]
                jacks_pencils = start_pencils - losing_position
            start_pencils -= jacks_pencils
            print(jacks_pencils)
            current_player = "John"
            break

print(current_player + " wins!")
