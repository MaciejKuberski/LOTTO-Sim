from random import shuffle

def lotto():
    i = 1
    user_numbers_list = []
    while i < 7:
        try:
            user_number = input(f"Please select {i} number, from 1 to 49")
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
lotto()