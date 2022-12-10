from random import shuffle

def lotto():
    i = 1
    user_numbers_list = []
    lotto_numbers = list(range(1,50))
    winning_numbers = []
    while i < 7:
        try:
            user_number = input(f"Please select {i} number, from 1 to 49: ")
            value = int(user_number)
            if value in range(1,50):
                if value in user_numbers_list:
                    print("Number already selected!")
                else:
                    user_numbers_list.append(value)
                    i += 1
            else:
                print("Number not in range!")
        except ValueError:
            try:
                value = float(user_number)
                print("Number must be Integer!")
            except ValueError:
                print("Not a number!")
    user_numbers_list.sort()
    print(f"Your numbers are :{user_numbers_list}")
    shuffle(lotto_numbers)
    next_number_to_append = 0
    while next_number_to_append <6:
        winning_numbers.append(lotto_numbers[next_number_to_append])
        next_number_to_append += 1
    winning_numbers.sort()
    print(f"Winning numbers are: {winning_numbers}")
    compare_numbers = sum(number in user_numbers_list for number in winning_numbers)
    if compare_numbers < 3:
        print(f"No luck this time, you only guessed {compare_numbers} numbers correctly.")
    else:
        print(f"Congratulations! You guessed {compare_numbers} numbers correctly!")

lotto()