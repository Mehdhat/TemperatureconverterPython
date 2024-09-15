from tkinter import *
from tkinter import messagebox

class TemperatureConverter:
    def __init__(self, tempconverter):
        self.tempconverter = tempconverter
        tempconverter.title("Temperature Converter")
        tempconverter.geometry("300x230")
        tempconverter.resizable(0, 0)
        tempconverter.configure(bg="#2E2E2E")  # Dark background for the main window

        # Set the icon for the window
        tempconverter.iconbitmap(r'C:\Users\Admin\Downloads\pythonProject1\125.ico')  # Update this path to your .ico file

        # Input field for temperature
        self.temp_input_label = Label(tempconverter, text="Enter Temperature:", bg="#2E2E2E", fg="white", font=("Helvetica", 14))
        self.temp_input_label.pack(pady=10)

        self.temp_input = Entry(tempconverter, width=10, font=("Helvetica", 14), bg="#4B4B4B", fg="white", insertbackground='white')
        self.temp_input.pack(pady=5)

        # Convert to Celsius Button
        self.to_celsius_button = Button(tempconverter, text="Convert to Celsius", command=self.convert_to_celsius, font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#45A049")
        self.to_celsius_button.pack(pady=5)

        # Convert to Fahrenheit Button
        self.to_fahrenheit_button = Button(tempconverter, text="Convert to Fahrenheit", command=self.convert_to_fahrenheit, font=("Helvetica", 12), bg="#F44336", fg="white", activebackground="#D32F2F")
        self.to_fahrenheit_button.pack(pady=5)

        # Label to display the result
        self.result_label = Label(tempconverter, text="", bg="#2E2E2E", fg="white", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

    def convert_to_celsius(self):
        try:
            fahrenheit = float(self.temp_input.get())
            celsius = (fahrenheit - 32) * 5.0 / 9.0
            self.result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number.")

    def convert_to_fahrenheit(self):
        try:
            celsius = float(self.temp_input.get())
            fahrenheit = (celsius * 9.0 / 5.0) + 32
            self.result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = Tk()
    temp_converter = TemperatureConverter(root)
    root.mainloop()

