def main():
    # Prompt the user for input
    size = int(input("Enter the size of the pattern: "))

    # Validate input
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Draw the pattern
    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line
        row += 1

# Execute the main function
if __name__ == "__main__":
    main()
