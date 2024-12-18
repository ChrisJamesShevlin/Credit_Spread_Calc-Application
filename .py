import tkinter as tk
from tkinter import messagebox

# Function to calculate max loss and max profit for a credit spread
def calculate():
    try:
        # Get user inputs
        short_strike = float(short_strike_entry.get())
        long_strike = float(long_strike_entry.get())
        premium_received = float(premium_received_entry.get())

        # Calculate max loss and max profit
        max_loss = (long_strike - short_strike) - premium_received
        max_profit = premium_received

        # Display results
        result_text.set(f"Maximum Loss: £{max_loss:.2f}\nMaximum Profit: £{max_profit:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Credit Spread Calculator")
root.geometry("400x300")
root.configure(bg="#1e1e2e")

# Result display variable
result_text = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Short Strike", bg="#1e1e2e", fg="white").grid(row=0, column=0, pady=5, padx=10, sticky="w")
short_strike_entry = tk.Entry(root, width=20)
short_strike_entry.grid(row=0, column=1, pady=5, padx=10)

tk.Label(root, text="Long Strike", bg="#1e1e2e", fg="white").grid(row=1, column=0, pady=5, padx=10, sticky="w")
long_strike_entry = tk.Entry(root, width=20)
long_strike_entry.grid(row=1, column=1, pady=5, padx=10)

tk.Label(root, text="Premium Received (£)", bg="#1e1e2e", fg="white").grid(row=2, column=0, pady=5, padx=10, sticky="w")
premium_received_entry = tk.Entry(root, width=20)
premium_received_entry.grid(row=2, column=1, pady=5, padx=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="#007acc", fg="white")
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, textvariable=result_text, bg="#1e1e2e", fg="white", font=("Helvetica", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
