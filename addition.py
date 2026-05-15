def get_number(prompt: str) -> float:
    return float(input(prompt))


def format_number(n: float) -> str:
    if n == int(n):
        return str(int(n))
    else:
        return str(n)


def add(a: float, b: float) -> float:
    return a + b


def main():
    try:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        result = add(num1, num2)
        print(f"Result: {format_number(num1)} + {format_number(num2)} = {format_number(result)}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
