import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def convert_area(value, from_unit, to_unit):
    area_units = {
        'acre': 4046.86,
        'hectare': 10000,
        'square meter': 1,
        'square foot': 0.092903,
        'square inch': 0.00064516,
        'square centimeter': 0.0001
    }
    return value * area_units[from_unit] / area_units[to_unit]

def convert_length(value, from_unit, to_unit):
    length_units = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34,
        'nautical mile': 1852,
        'mil': 0.0000254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    return value

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'liter': 0.001,
        'milliliter': 0.000001,
        'cubic centimeter': 0.000001,
        'cubic meter': 1,
        'cubic foot': 0.0283168,
        'cubic inch': 1.63871e-05
    }
    return value * volume_units[from_unit] / volume_units[to_unit]

def convert_mass(value, from_unit, to_unit):
    mass_units = {
        'pound': 0.453592,
        'ounce': 0.0283495,
        'kilogram': 1,
        'gram': 0.001
    }
    return value * mass_units[from_unit] / mass_units[to_unit]

def convert_data(value, from_unit, to_unit):
    data_units = {
        'bit': 0.125,
        'byte': 1,
        'kilobyte': 1024,
        'megabyte': 1024 ** 2,
        'kibibyte': 1024,
        'mebibyte': 1024 ** 2,
        'gigabyte': 1024 ** 3,
        'gibibyte': 1024 ** 3,
        'terabyte': 1024 ** 4,
        'tebibyte': 1024 ** 4
    }
    return value * data_units[from_unit] / data_units[to_unit]

def convert_speed(value, from_unit, to_unit):
    speed_units = {
        'meter per hour': 1 / 3600,
        'meter per second': 1,
        'kilometer per second': 1000,
        'kilometer per hour': 1000 / 3600,
        'inch per second': 0.0254,
        'inch per hour': 0.0254 / 3600,
        'foot per second': 0.3048,
        'foot per hour': 0.3048 / 3600,
        'mile per second': 1609.34,
        'mile per hour': 1609.34 / 3600,
        'knot': 0.514444
    }
    return value * speed_units[from_unit] / speed_units[to_unit]

def convert_time(value, from_unit, to_unit):
    time_units = {
        'millisecond': 0.001,
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800
    }
    return value * time_units[from_unit] / time_units[to_unit]

# Tkinter GUI
def convert_units():
    try:
        value = float(entry_value.get())
        from_unit = from_unit_combobox.get()
        to_unit = to_unit_combobox.get()
        category = category_combobox.get()

        if category == "Area":
            result = convert_area(value, from_unit, to_unit)
        elif category == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif category == "Volume":
            result = convert_volume(value, from_unit, to_unit)
        elif category == "Mass":
            result = convert_mass(value, from_unit, to_unit)
        elif category == "Data":
            result = convert_data(value, from_unit, to_unit)
        elif category == "Speed":
            result = convert_speed(value, from_unit, to_unit)
        elif category == "Time":
            result = convert_time(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid category")

        label_result.config(text=f"Result: {result} {to_unit}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def update_units(event):
    category = category_combobox.get()
    units = {
        "Area": ["acre", "hectare", "square meter", "square foot", "square inch", "square centimeter"],
        "Length": ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile", "nautical mile", "mil"],
        "Temperature": ["celsius", "fahrenheit", "kelvin"],
        "Volume": ["liter", "milliliter", "cubic centimeter", "cubic meter", "cubic foot", "cubic inch"],
        "Mass": ["pound", "ounce", "kilogram", "gram"],
        "Data": ["bit", "byte", "kilobyte", "megabyte", "kibibyte", "mebibyte", "gigabyte", "gibibyte", "terabyte", "tebibyte"],
        "Speed": ["meter per hour", "meter per second", "kilometer per second", "kilometer per hour", "inch per second", "inch per hour", "foot per second", "foot per hour", "mile per second", "mile per hour", "knot"],
        "Time": ["millisecond", "second", "minute", "hour", "day", "week"]
    }
    from_unit_combobox['values'] = units[category]
    to_unit_combobox['values'] = units[category]

app = tk.Tk()
app.title("Unit Converter")

tk.Label(app, text="Value:").grid(row=0, column=0, padx=10, pady=10)
entry_value = tk.Entry(app)
entry_value.grid(row=0, column=1, padx=10, pady=10)

tk.Label(app, text="Category:").grid(row=1, column=0, padx=10, pady=10)
category_combobox = ttk.Combobox(app, values=["Area", "Length", "Temperature", "Volume", "Mass", "Data", "Speed", "Time"])
category_combobox.grid(row=1, column=1, padx=10, pady=10)
category_combobox.bind("<<ComboboxSelected>>", update_units)

tk.Label(app, text="From Unit:").grid(row=2, column=0, padx=10, pady=10)
from_unit_combobox = ttk.Combobox(app)
from_unit_combobox.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="To Unit:").grid(row=3, column=0, padx=10, pady=10)
to_unit_combobox = ttk.Combobox(app)
to_unit_combobox.grid(row=3, column=1, padx=10, pady=10)

tk.Button(app, text="Convert", command=convert_units).grid(row=4, column=0, columnspan=2, pady=10)
label_result = tk.Label(app, text="Result: ")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
