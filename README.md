# Falcon - Simple Calculator

A simple Python calculator application that performs basic arithmetic operations.

## Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with zero-division handling)
- User-friendly command-line interface

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/awasthiste1/Falcon.git
cd Falcon
```

2. No external dependencies required! This is a pure Python project.

## Usage

Run the calculator:
```bash
python calculator.py
```

### Example Session
```
==================================================
         SIMPLE CALCULATOR
==================================================
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
==================================================

Enter choice (1/2/3/4/5): 1
Enter first number: 10
Enter second number: 5

10.0 + 5.0 = 15.0
```

## File Structure

```
Falcon/
├── calculator.py          # Main calculator application
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies (if any)
└── .gitignore           # Git ignore file
```

## How It Works

The calculator provides four basic arithmetic operations:

1. **Add**: Adds two numbers and returns the sum
2. **Subtract**: Subtracts the second number from the first
3. **Multiply**: Multiplies two numbers together
4. **Divide**: Divides the first number by the second (handles division by zero)

## Error Handling

- **Division by Zero**: Returns an error message instead of crashing
- **Invalid Input**: Prompts the user to enter valid numeric values

## Author

Created by awasthiste1

## License

This project is open source and available under the MIT License.
