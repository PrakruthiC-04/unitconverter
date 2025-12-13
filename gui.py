import subprocess
import tkinter as tk
from tkinter import ttk
import os

conversion_codes={
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

def perform_conversion_via_files(value,conversion_code):
    try:
        with open("input_txt","w") as f:
            f.write(f"{conversion_code} {value}\n")
    except Exception as e:
        return f"Python I/O Error: {e}"
    
    try:
        subprocess.run(['./converter_exe'], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return f"C Runtime Error: {e.stderr.decode()}"
    except FileNotFoundError:
        return "Error: converter_exe not found."

    try:
        with open("output_txt", "r") as f:
            result = f.read().strip()
            os.remove("input_txt")
            os.remove("output_txt")
            
            return result
    except FileNotFoundError:
        return "Error: C program failed to produce output_txt."

class ConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Unit Converter (C Logic)")
        
        main_frame = ttk.Frame(root, padding="10 10 10 10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(main_frame, text="Value to Convert:").grid(column=1, row=1, sticky=tk.W)
        self.input_entry = ttk.Entry(main_frame, width=20)
        self.input_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
        
        ttk.Label(main_frame, text="Select Conversion:").grid(column=1, row=2, sticky=tk.W)
        
        self.dropdown_variable = tk.StringVar(root)
        self.dropdown_variable.set(list(conversion_codes.keys())[0]) 
        
        self.conversion_menu = ttk.Combobox(main_frame, 
                                            textvariable=self.dropdown_variable, 
                                            values=list(conversion_codes.keys()),
                                            state='readonly', 
                                            width=30)
        self.conversion_menu.grid(column=2, row=2, sticky=(tk.W, tk.E))

        self.convert_button = ttk.Button(main_frame, text="CONVERT", 
                                         command=self.run_conversion)
        self.convert_button.grid(column=1, row=3, columnspan=2, pady=10) 
        self.result_label = ttk.Label(main_frame, text="Result:")
        self.result_label.grid(column=1, row=4, sticky=tk.W)
        
        self.output_display = ttk.Label(main_frame, text="---", font='Arial 12 bold')
        self.output_display.grid(column=2, row=4, sticky=(tk.W, tk.E))

    def run_conversion(self):
        selected_name = self.dropdown_variable.get() 
        code = conversion_codes[selected_name] 
        value = self.input_entry.get() 
        final_result = perform_conversion_via_files(value, code)
        self.output_display.config(text=final_result)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()