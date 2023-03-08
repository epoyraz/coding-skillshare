import tkinter as tk

def find_zodiac_sign(day, month):
    # Check if the input is valid
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 11:
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    else:
        astro_sign = 'Invalid input'

    return astro_sign

def calculate_zodiac_sign():
    # Get user input
    day = int(day_entry.get())
    month = int(month_entry.get())

    # Find the zodiac sign
    zodiac_sign = find_zodiac_sign(day, month)

    # Update the result label
    result_label.config(text="Your zodiac sign is " + zodiac_sign)

# Create the main window
window = tk.Tk()
window.title("Zodiac Sign Calculator")

# Create the input labels and entry widgets
day_label = tk.Label(window, text="Enter your birth day (1-31): ")
day_label.pack()
day_entry = tk.Entry(window)
day_entry.pack()

month_label = tk.Label(window, text="Enter your birth month (1-12): ")
month_label.pack()
month_entry = tk.Entry(window)
month_entry.pack()

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_zodiac_sign)
calculate_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main event loop
window.mainloop()
