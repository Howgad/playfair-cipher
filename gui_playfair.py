import tkinter as tk
from playfair import playfair_cipher

def run_cipher():
    text = entry_text.get()
    key = entry_key.get()
    mode = var_mode.get()
    result = playfair_cipher(text, key, mode)
    output_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Playfair Cipher")
root.geometry("400x250")

tk.Label(root, text="Enter Text:").pack()
entry_text = tk.Entry(root, width=40)
entry_text.pack()

tk.Label(root, text="Enter Key:").pack()
entry_key = tk.Entry(root, width=40)
entry_key.pack()

var_mode = tk.StringVar(value='encrypt')
tk.Radiobutton(root, text="Encrypt", variable=var_mode, value='encrypt').pack()
tk.Radiobutton(root, text="Decrypt", variable=var_mode, value='decrypt').pack()

tk.Button(root, text="Run", command=run_cipher).pack(pady=10)

output_label = tk.Label(root, text="Result: ", font=("Arial", 12))
output_label.pack()

root.mainloop()