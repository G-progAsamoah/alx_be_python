def main():
    # Prompt the user for input
    number = int(input("Enter a number to see its multiplication table: "))

    # Generate and print the multiplication table
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

# Execute the main function
if __name__ == "__main__":
    main()
