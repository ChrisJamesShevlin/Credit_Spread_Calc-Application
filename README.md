# Credit Spread Calculator

This is a Python-based graphical application for calculating the **maximum loss** and **maximum profit** of an options credit spread. The tool is built using the `tkinter` library and provides an easy-to-use interface for entering strike prices and premium received.

## Features
- **User-Friendly Interface:** Simple input fields for entering the short strike, long strike, and premium received.
- **Accurate Calculations:** Computes the maximum profit and maximum loss based on the inputs provided.
- **Quick Results:** Displays the calculated values in a clear, easy-to-read format.

## Requirements
- Python 3.7 or later
- `tkinter` (included with most Python installations)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/credit-spread-calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd credit-spread-calculator
   ```
3. Run the application:
   ```bash
   python credit_spread_calculator.py
   ```

## Usage
1. Enter the **Short Strike** price in the corresponding input field.
2. Enter the **Long Strike** price in the corresponding input field.
3. Enter the **Premium Received (£)** in the corresponding input field.
4. Click the **Calculate** button to see:
   - **Maximum Loss**
   - **Maximum Profit**

## Formulae Used
- **Maximum Loss:**
  ```
  Maximum Loss = (Long Strike - Short Strike) - Premium Received
  ```
- **Maximum Profit:**
  ```
  Maximum Profit = Premium Received
  ```

## Example
For a credit spread with:
- **Short Strike:** 100
- **Long Strike:** 105
- **Premium Received:** 2.50

The calculator will display:
- **Maximum Loss:** 2.50
- **Maximum Profit:** 2.50



## Contributing
Feel free to submit pull requests or open issues if you find any bugs or have suggestions for improvements.



