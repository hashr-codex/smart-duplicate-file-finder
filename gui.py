import tkinter as tk
from tkinter import filedialog, messagebox

from duplicate_finder.cleaner import find_duplicates


root = tk.Tk()
root.title("Smart Duplicate File Finder")
root.geometry("600x400")

selected_folder = ""

def choose_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    folder_label.config(text=f"Folder: {selected_folder}")

def choose_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    folder_label.config(text=f"Folder: {selected_folder}")

def scan_duplicates():
    if not selected_folder:
        messagebox.showwarning("Error", "Please select a folder first.")
        return

    duplicates = find_duplicates(selected_folder)

    result_box.delete(1.0, tk.END)

    if not duplicates:
        result_box.insert(tk.END, " NO duplicates found. Hooray!")
        return
    
    for hash_value, files in duplicates.items():
        result_box.insert(tk.END, f"\nDuplicates group:\n")
        for file in files:
            result_box.insert(tk.END, f"{file}\n")

title = tk.Label(root, text="Smart Duplicate File Finder", font=("Arial", 16))
title.pack(pady=10)

folder_label = tk.Label(root, text="No folder selected", font=("Arial", 12))
folder_label.pack()

choose_button = tk.Button(root, text="Choose Folder", command=choose_folder)
choose_button.pack(pady=5)

scan_button = tk.Button(root, text="Scan for Duplicates", command=scan_duplicates)
scan_button.pack(pady=5)

result_box = tk.Text(root, wrap=tk.WORD, width=70, height=15)
result_box.pack(pady=10)

root.mainloop()
