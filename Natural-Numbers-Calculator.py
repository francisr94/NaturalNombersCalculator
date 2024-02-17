def calculate_sum_of_natural_numbers(n):
    # Calculate the sum of the first n natural numbers using the formula
    sum_natural_numbers = (n * (n + 1)) // 2

    return sum_natural_numbers


def main():
    # Prompt the user for input
    n = int(input("Enter the value of n: "))

    # Calculate and print the sum
    sum_natural_numbers = calculate_sum_of_natural_numbers(n)
    print(f"The sum of the first {n} natural numbers is: {sum_natural_numbers}")


if __name__ == "__main__":
    main()
