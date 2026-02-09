import os
import tkinter as tk

from tkinter import filedialog, messagebox

from duplicate_finder.cleaner import find_duplicates


root = tk.Tk()
root.title("Smart Duplicate File Finder")
root.geometry("600x400")
root.configure(bg="#121212")

selected_folder = ""
duplicate_files = []

def choose_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    folder_label.config(text=f"Folder: {selected_folder}")

def choose_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    folder_label.config(text=f"Folder: {selected_folder}")

def scan_duplicates():
    global duplicate_files
    duplicate_files = []

    if not selected_folder:
        messagebox.showerror("Error", "Please select a folder first!")
        return

    duplicates = find_duplicates(selected_folder)
    result_list.delete(0, tk.END)

    if not duplicates:
        result_list.insert(tk.END, " NO duplicates found")
        return
    
    for hash_value, files in duplicates.items():
        for f in files[1:]:
            duplicate_files.append(f)
            result_list.insert(tk.END, f)

def delete_selected():
    selected = result_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "No files selected for deletion!")
        return
    
    for index in reversed(selected):
        file_path = duplicate_files[index]
        try:
            os.remove(file_path)
            result_list.delete(index)
            duplicate_files.pop(index)
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete {file_to_delete}: {str(e)}")


title = tk.Label(root, text="Smart Duplicate File Finder", font=("Arial", 16), bg="#121212", fg="lime")
title.pack(pady=10)

folder_label = tk.Label(root, text="No folder selected", font=("Arial", 12), fg="cyan", bg="#121212")
folder_label.pack()

btn_folder = tk.Button(root, text="Choose Folder", command=choose_folder, bg="black", fg="lime")
btn_folder.pack(pady=5)

btn_scan = tk.Button(root, text="Scan for Duplicates", command=scan_duplicates, bg="black", fg="lime")
btn_scan.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Selected", command=delete_selected, bg="red", fg="white")
btn_delete.pack(pady=5)

result_list = tk.Listbox(root,selectmode=tk.MULTIPLE, width=80, height=15, bg="black", fg="white")
result_list.pack(pady=10)


root.mainloop()
