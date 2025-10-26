# High-Precision e Calculator

## Overview

The High-Precision e Calculator is a tool designed to compute the mathematical constant *e* (Euler's number) to a high degree of precision. This project implements efficient algorithms to calculate *e* with arbitrary precision, suitable for scientific and educational purposes.

## Features

- Calculates the constant *e* to a user-specified number of decimal places.
- Supports arbitrary precision arithmetic.
- Efficient and optimized for performance.
- Easy-to-use command-line interface.

## Installation

To use the High-Precision e Calculator, clone the repository and install any required dependencies:

```bash
git clone https://github.com/yourusername/high-precision-e-calculator.git
cd high-precision-e-calculator
pip install -r requirements.txt
```

## Usage

Run the calculator from the command line by specifying the number of decimal places:

```bash
python e_calculator.py --precision 100
```

This command computes *e* to 100 decimal places.

## Example Output

```
e = 2.71828182845904523536028747135266249775724709369995...
```

## How It Works

The calculator uses the following methods:

- **Series Expansion:** Calculates *e* using the infinite sum of 1/n! for n=0 to infinity.
- **Arbitrary Precision Arithmetic:** Utilizes Python's `decimal` module to handle high-precision calculations.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for bug fixes, improvements, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [your.email@example.com](mailto:your.email@example.com).
