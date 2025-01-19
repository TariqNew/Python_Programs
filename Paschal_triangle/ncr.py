from math import factorial

def printPascal(height):
    for i in range(height):
        # Add spaces for left alignment
        for j in range(height - i + 1):
            print(" ", end="")

        for j in range(i + 1):
            # Calculate the binomial coefficient
            value = factorial(i) // (factorial(j) * factorial(i - j))
            print(f"{value:3}", end=" ")  # Use fixed-width formatting for alignment

        # Move to the next line
        print()


# Given height
height = 5
# Pass the height as a parameter to the printPascal function
printPascal(height)
