# Mind Reader game

import random

higher_range = random.randint(5, 9)
lower_range = higher_range - 4
number_count = 12
array_numbers = ""
number_list = []

# Character input to start
keep_going = ""
print("\033[44;43m Welcome to the Mind Reader. Prepare to be *mind* blown. \033[m\n\nPush any letter/number"
      " key then <enter> to begin.")
while keep_going == "":
    keep_going = input("")

# Generating grid of numbers
for item in range(1, number_count + 1):
    number = str(random.randint(lower_range, higher_range)) + str(random.randint(lower_range, higher_range)) + \
             str(random.randint(lower_range, higher_range)) + str(random.randint(lower_range, higher_range))
    number_list.append(number)

# Print Grid and (sort then) print list

print()
print(number_list)
number_list.sort()

# Character input to confirm choosing number
keep_going_2 = ""
print("\nChoose a number from the list above.\n"
      "Memorise it really well\n"
      "Write it down if you wish.\n\n"
      "\033[1mDone? Push any key then <enter>\033[0m")
while keep_going_2 == "":
    keep_going_2 = input("")

print("\nStudy the following grid.\n\n")

eliminative_list = []
answer = ""
loop_times = 0
user_number = ""
while user_number == "":
    # Set up values for mixed grid
    mixed_grid_1 = ""
    random_partition_1 = random.randint(9, 15)
    random_partition_2 = random.randint(17, 23)
    random_partition_3 = random.randint(25, 31)
    random_partition_4 = random.randint(33, 39)
    random_partition_5 = random.randint(41, 47)
    random_partition_6 = random.randint(49, 55)
    VAR1 = 8
    VAR2 = 0
    if loop_times == 0:
        VAR2 = 0
    elif loop_times == 1:
        if answer[0].lower() == "y":
            VAR2 = 0
        elif answer[0].lower() == "n":
            VAR2 = 6
    elif loop_times == 2:
        if answer[0].lower() == "y":
            if VAR2 == 0:
                VAR2 = 0
            elif VAR2 == 6:
                VAR2 = 6
        elif answer[0].lower() == "n":
            if VAR2 == 0:
                VAR2 = 3
            elif VAR2 == 6:
                VAR2 = 9

    # Generate 7 by 8 grid of random 4-digit numbers containing the first 6 values of the sorted array ^^^
    for item in range(1, 57):
        fake_number = str(random.randint(1, 9)) + str(random.randint(1, 9)) + \
                 str(random.randint(1, 9)) + str(random.randint(1, 9))
        while fake_number == number_list[0] or fake_number == number_list[1] or fake_number == number_list[2] or \
                fake_number == number_list[3] or fake_number == number_list[4] or fake_number == number_list[5]:
            fake_number = str(random.randint(1, 9)) + str(random.randint(1, 9)) + \
                          str(random.randint(1, 9)) + str(random.randint(1, 9))
        if item == 1:
            mixed_grid_1 = " | " + fake_number
        elif item > 1:
            if loop_times == 0:
                if item == VAR1 or item == (VAR1*2) or item == (VAR1*3) or item == (VAR1*4) or \
                        item == (VAR1*5) or item == (VAR1*6) or item == (VAR1*7):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number + " |\n"
                elif item < VAR1:
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_1:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2]
                elif item < (VAR1*2):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_2:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2 + 1]
                elif item < (VAR1*3):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_3:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2 + 2]
                elif item < (VAR1*4):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_4:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2 + 3]
                elif item < (VAR1*5):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_5:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2 + 4]
                elif item < (VAR1*6):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_6:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2 + 5]
                elif item < (VAR1*7):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                else:
                    print("Unexpected error")
            elif loop_times == 1:
                if item == VAR1 or item == (VAR1 * 2) or item == (VAR1 * 3) or item == (VAR1 * 4) or \
                        item == (VAR1 * 5) or item == (VAR1 * 6) or item == (VAR1 * 7):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number + " |\n"
                elif item < VAR1:
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_1:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2]
                elif item < (VAR1 * 2):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_2:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2 + 1]
                elif item < (VAR1 * 3):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_3:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2 + 2]
                elif item < (VAR1 * 4):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item < (VAR1 * 5):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item < (VAR1 * 6):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item < (VAR1 * 7):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
            elif loop_times == 2:
                if item == VAR1 or item == (VAR1 * 2) or item == (VAR1 * 3) or item == (VAR1 * 4) or \
                        item == (VAR1 * 5) or item == (VAR1 * 6) or item == (VAR1 * 7):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number + " |\n"
                elif item < VAR1:
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_1:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2]
                elif item < (VAR1 * 2):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item == random_partition_2:
                    mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2 + 1]
                elif item < (VAR1 * 3):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item < (VAR1 * 4):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item < (VAR1 * 5):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item < (VAR1 * 6):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif item < (VAR1 * 7):
                    mixed_grid_1 = mixed_grid_1 + " | " + fake_number
            elif loop_times == 3:
                if answer[0].lower() == "y":
                    if item == VAR1 or item == (VAR1 * 2) or item == (VAR1 * 3) or item == (VAR1 * 4) or \
                            item == (VAR1 * 5) or item == (VAR1 * 6) or item == (VAR1 * 7):
                        mixed_grid_1 = mixed_grid_1 + " | " + fake_number + " |\n"
                    elif item < VAR1:
                        mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                    elif item == random_partition_1:
                        mixed_grid_1 = mixed_grid_1 + " | " + number_list[VAR2]
                    elif item < (VAR1 * 2):
                        mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                    elif item < (VAR1 * 3):
                        mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                    elif item < (VAR1 * 4):
                        mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                    elif item < (VAR1 * 5):
                        mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                    elif item < (VAR1 * 6):
                        mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                    elif item < (VAR1 * 7):
                        mixed_grid_1 = mixed_grid_1 + " | " + fake_number
                elif answer[0].lower() == "n":
                    user_number = number_list[VAR2 + 2]
                    break
            elif loop_times == 4:
                if answer[0].lower() == "y":
                    user_number = number_list[VAR2]
                    break
                elif answer[0].lower() == "n":
                    user_number = number_list[VAR2 + 1]
                    break
        else:
            print("Unexpected error")

    if user_number == "":
        print("\033[1m" + mixed_grid_1 + "\033[0m")

        # Check if number is included in the grid (half of 'unstatused' list values)
        answer = input("Is your number anywhere to be seen above? \n")
        while answer.lower() != "y" and answer.lower() != "yes" and answer.lower() != "no" and answer.lower() != "n" \
                and answer.lower() != "nah" and answer.lower() != "yeah" and answer.lower() != "yea" and \
                answer.lower() != "nope" and answer.lower() != "na" and answer.lower() != "yep" and answer.lower() != \
                "yup" and answer.lower() != "ye":
            answer = input("Sorry I missed that. Is your number in the preceding grid? ")

    loop_times += 1

print("\n\n\n\033[44;42mWell, well, well. If you answered all the questions correctly, the Mind Reader will work "
      "exactly\033[m\n\033[44;42mas advertised. Are you ready to be surprised?\033[m\n\nDoesn't matter! \033[44;41m"
      " Your number is: {} \033[m".format(user_number))

print("\nThank you for using this program. Please leave a positive comment if you enjoyed or some constructive "
      "feedback if you didn't enjoy it so much")
