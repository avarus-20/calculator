while True:  # бесконечный цикл
    try:
        num_1 = int(input("Enter the first number : "))
        num_2 = int(input("Enter the first number :"))

        operation = input("Choose an operation (+,-,*,/):").lower()

        if operation == "exit":
            print("Program closed.")
            break

        if operation == "+":
            print(num_1 + num_2)

        elif operation == "-":
            print(num_1 - num_2)

        elif operation == "*":
            print(num_1 * num_2)

        elif operation == "/":

            if num_2 != 0:  # / 0
                print(num_1 / num_2)
            else:
                print("Division by 0 is not allowed")

        elif operation == "**":
            print(num_1**num_2)
        elif operation == "%":
            print(num_1 % num_2)

        else:
            print("Error! Enter a valid operation (+,-,*,/):")

    except ValueError:  # Ловим ошибку
        print("Error! Invalid number")
