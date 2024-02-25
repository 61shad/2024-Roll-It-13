
# check that user enter an integer
# that is more than 13

def int_checker():


    while True:
        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input("Enter an integer: "))

            # check that number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine goes here
target_score = int_checker()
print(target_score)