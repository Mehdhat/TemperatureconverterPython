# Temperature Converter Application

## Overview

This is a simple temperature converter application built using Python's Tkinter library. The application allows users to convert temperatures between Fahrenheit and Celsius. It features a dark-themed interface with input fields and buttons to perform the conversions.

## Features

- **Convert to Celsius**: Convert a temperature from Fahrenheit to Celsius.
- **Convert to Fahrenheit**: Convert a temperature from Celsius to Fahrenheit.
- **Result Display**: Shows the conversion result.

## Installation

1. Ensure you have Python installed on your system.
2. Tkinter should be included with your Python installation, but make sure it's available.

## Usage

1. Save the provided code into a file named `temperature_converter.py`.
2. Place an icon file named `125.ico` in the same directory or update the path in the code to your .ico file.
3. Run the script using Python:

    ```bash
    python temperature_converter.py
    ```

4. A window will open with the temperature converter application.

## Code Details

- **Window Title**: "Temperature Converter"
- **Window Size**: 300x230 pixels
- **Background Color**: Dark grey (#2E2E2E)
- **Input Field**:
  - Font: Helvetica, 14
  - Background: Dark grey (#4B4B4B)
  - Foreground: White
- **Convert to Celsius Button**:
  - Color: Green (#4CAF50)
  - Font: Helvetica, 12
- **Convert to Fahrenheit Button**:
  - Color: Red (#F44336)
  - Font: Helvetica, 12
- **Result Label**:
  - Font: Helvetica, 14
  - Background: Dark grey (#2E2E2E)
  - Foreground: White

## Icon

The application uses an icon file for the window. Make sure to update the path to the correct location of your `.ico` file in the script:

```python
tempconverter.iconbitmap(r'C:\Users\Admin\Downloads\pythonProject1\125.ico')
