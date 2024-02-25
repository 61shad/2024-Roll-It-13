# checks users enter yes (y) or no (n)
def yes_no (question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "N":
            return "no"
        else:
            print("You didn't choose a valid response.")

# main routine goes here
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"you chose {want_instructions}")

