import subprocess
import tkinter as tk
from tkinter import ttk
import os
import time

basic_codes={
    "1-Centimetre to Metre":1,
    "2-Metre to Centimetre":2,
    "3-Metre to Kilometre":3,
    "4-Kilometre to Metre":4,
    "5-Inch to Centimetre":5,
    "6-Centimetre to Inch":6,
    "7-Gram to Kilogram":7,
    "8-Kilogram to Gram":8,
    "9-Second to Hour":9,
    "10-Hour to Second":10,
    "11-Hour to Day":11,
    "12-Day to Hour":12,
    "13-Celsius to Fahrenheit":13,
    "14-Fahrenheit to Celsius":14,
    "15-Celsius to Kelvin":15,
    "16-Kelvin to Celsius":16,
    "17-Litre to Millilitre":17,
    "18-Millilitre to Litre":18
}

complex_codes={
    "19-Joule to Calorie":19,
    "20-Calorie to Joule":20,
    "21-Pascal to Bar":21,
    "22-Bar to Pascal":22,
    "23-Pascal to psi":23,
    "24-psi to pascal":24,
    "25-Torr to Pascal":25,
    "26-Pascal to Torr":26,
    "27-m/s to kmph":27,
    "28-kmph to m/s":28,
    "29-Mile/s to kmph":29,
    "30-kmph to Mile/s":30,
    "31-g/cubic cm to Kg/cubic m":31,
    "32-Kg/cubic m to g/cubic cm":32,
    "33-Horsepower to Watt":33,
    "34-Watt to Horsepower":34,
    "35-Megabyte/s to Megabit/s":35,
    "36-Megabit/s to Megabyte/s":36,
    "37-Mg/dL to mmol/L":37,
    "38-mmol/L to Mg/dL":38,
    "39-gold purity(%)":39,
    "40-knot to kmph":40,
    "41-kmph to knot":41
}

def perform_conversion_via_files(value,conversion_code):
    try:
        with open("input_txt","w") as f:
            f.write(f"{conversion_code} {value}\n")
    except Exception as e:
        return f"Python I/O Error: {e}"
    
    try:
        result = subprocess.run(['./converter_exe.exe'], check=False, capture_output=True, timeout=5)
        if result.returncode != 0:
            stderr_output = result.stderr.decode().strip()
            return f"C Runtime Error (Code {result.returncode}): {stderr_output}"

    except subprocess.TimeoutExpired:
        return "C Runtime Error: Program timed out."
    except FileNotFoundError:
        return "Error: converter_exe.exe not found."

    try:
        with open("output_txt", "r") as f:
            result = f.read().strip()
        os.remove("input_txt")
        max_retries = 10
        for i in range(max_retries):
            try:
                os.remove("output_txt")
                break 
            except PermissionError:
                if i < max_retries - 1:
                    time.sleep(0.05) 
                else:
                    raise 

        return result
    except FileNotFoundError:
        return "Error: C program failed to produce output_txt."
    except PermissionError as e:
        return f"Final File Lock Error: {e}"

class ConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Advanced Unit Converter")
        root.geometry("600x550") 
        
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
        ttk.Label(main_frame, text="Value to Convert:").grid(column=1, row=1, sticky=tk.W, pady=10)
        self.input_entry = ttk.Entry(main_frame, width=25)
        self.input_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        
        ttk.Label(main_frame, text="Basic Conversions:").grid(column=1, row=2, sticky=tk.W, pady=5)
        self.basic_var = tk.StringVar()
        self.basic_menu = ttk.Combobox(main_frame, 
                                        textvariable=self.basic_var, 
                                        values=list(basic_codes.keys()),
                                        state='readonly', 
                                        width=40)
        self.basic_menu.grid(column=2, row=2, sticky=(tk.W, tk.E))
        self.basic_menu.bind("<<ComboboxSelected>>", lambda e: self.complex_var.set(""))

        ttk.Label(main_frame, text="Complex Conversions:").grid(column=1, row=3, sticky=tk.W, pady=5)
        self.complex_var = tk.StringVar()
        self.complex_menu = ttk.Combobox(main_frame, 
                                          textvariable=self.complex_var, 
                                          values=list(complex_codes.keys()),
                                          state='readonly', 
                                          width=40)
        self.complex_menu.grid(column=2, row=3, sticky=(tk.W, tk.E))
        self.complex_menu.bind("<<ComboboxSelected>>", lambda e: self.basic_var.set(""))

        self.convert_button = ttk.Button(main_frame, text="CONVERT", 
                                         command=self.run_conversion)
        self.convert_button.grid(column=1, row=4, columnspan=2, pady=25) 

        self.result_label = ttk.Label(main_frame, text="Result:", font='Arial 10')
        self.result_label.grid(column=1, row=5, sticky=tk.W)
        
        self.output_display = ttk.Label(main_frame, text="---", font='Arial 14 bold', foreground="blue")
        self.output_display.grid(column=2, row=5, sticky=(tk.W, tk.E))

    def run_conversion(self):
        basic_choice = self.basic_var.get()
        complex_choice = self.complex_var.get()
        
        if basic_choice:
            code = basic_codes[basic_choice]
        elif complex_choice:
            code = complex_codes[complex_choice]
        else:
            self.output_display.config(text="Select a unit!", foreground="red")
            return

        value = self.input_entry.get()
        try:
            float(value)
        except ValueError:
            self.output_display.config(text="Invalid Number", foreground="red")
            return

        final_result = perform_conversion_via_files(value, code)
        self.output_display.config(text=final_result, foreground="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()