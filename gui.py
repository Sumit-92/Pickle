import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests

def submit_data():
    float1 = entry1.get()
    float2 = entry2.get()
    float3 = entry3.get()
    float4 = entry4.get() 

    try:
        float1 = float(float1)
        float2 = float(float2)
        float3 = float(float3)
        float4 = float(float4)
    except ValueError:
        messagebox.showerror("Invalid Input", "Float values must be numeric.")
        return

    # data = {
    #     # 'string1': string1,
    #     # 'string2': string2,
    #     # 'string3': string3,
    #     'float1': float1,
    #     'float2': float2,
    #     'float3': float3,
    #     'float4': float4
    # }

    data = {
    'data': [[float1, float2, float3, float4]]
     } 

    try:
        response = requests.post('http://localhost:5000/predict', json=data)
        result = response.json()

        result_text.config(text=f"Result: {result}")
    except requests.exceptions.RequestException:
        messagebox.showerror("Connection Error", "Failed to connect to the server.")

# Create the main application window
app = tk.Tk()
app.title("Python GUI")
app.geometry("400x250")

# Style the widgets using a ttk theme
style = ttk.Style(app)
style.theme_use("clam")  # Choose the "clam" theme, you can try other themes as well


# Form inputs
label1 = tk.Label(app, text="Float 1:")
entry1 = tk.Entry(app)
label2 = tk.Label(app, text="Float 2:")
entry2 = tk.Entry(app)
label3 = tk.Label(app, text="Float 3:")
entry3 = tk.Entry(app)
label4 = tk.Label(app, text="Float 4:")
entry4 = tk.Entry(app)


# Submit button
submit_button = tk.Button(app, text="Submit", command=submit_data)

# Result label
result_text = tk.Label(app, text="Result: ")

# Grid layout
label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
label3.grid(row=2, column=0, padx=5, pady=5)
entry3.grid(row=2, column=1, padx=5, pady=5)
label4.grid(row=3, column=0, padx=5, pady=5)
entry4.grid(row=3, column=1, padx=5, pady=5)


submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)
result_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
