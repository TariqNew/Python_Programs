number = input("Enter the number and I will tell you if its a prime or not: ")

if number.isdigit():
    number = int(number)

    if number > 1:
        for i in range(2, number):  # Start the loop from 2 to avoid unnecessary checks
            if (number % i) == 0:
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

else:
    print(f"{number} is not a digit number, please try again")