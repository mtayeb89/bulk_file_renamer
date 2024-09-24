import os
import tkinter as tk
from tkinter import filedialog, messagebox


# Function to rename files
def bulk_rename(directory, prefix, start_num=1, extension=None):
    """
    Renames all files in the specified directory with a given prefix and optional file extension.

    Parameters:
    - directory (str): The directory where the files are located.
    - prefix (str): The prefix for the new file names.
    - start_num (int): The starting number for renaming (default is 1).
    - extension (str, optional): The file extension to filter by (e.g., ".txt"). If None, all files are renamed.
    """
    try:
        files = os.listdir(directory)

        # Filter files by extension if provided
        if extension:
            files = [f for f in files if f.endswith(extension)]

        if not files:
            messagebox.showinfo("No Files Found", f"No files found in {directory} with the extension '{extension}'")
            return

        # Rename the files
        for index, filename in enumerate(files, start=start_num):
            file_path = os.path.join(directory, filename)

            # Extract file extension
            file_extension = os.path.splitext(filename)[1]

            # Build new file name
            new_name = f"{prefix}_{index}{file_extension}"
            new_file_path = os.path.join(directory, new_name)

            # Rename the file
            os.rename(file_path, new_file_path)

        messagebox.showinfo("Success", f"Files successfully renamed in {directory}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to select directory
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)


# Function to trigger renaming process
def start_renaming():
    directory = directory_entry.get()
    prefix = prefix_entry.get()
    start_num = start_num_entry.get()
    extension = extension_entry.get()

    if not directory or not os.path.isdir(directory):
        messagebox.showerror("Error", "Please select a valid directory.")
        return

    if not prefix:
        messagebox.showerror("Error", "Please enter a prefix.")
        return

    try:
        start_num = int(start_num)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid starting number.")
        return

    bulk_rename(directory, prefix, start_num, extension if extension else None)


# Create the Tkinter interface
root = tk.Tk()
root.title("Bulk File Renamer")

# Directory selection
tk.Label(root, text="Select Directory:").grid(row=0, column=0, padx=10, pady=5)
directory_entry = tk.Entry(root, width=40)
directory_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_directory).grid(row=0, column=2, padx=10, pady=5)

# Prefix input
tk.Label(root, text="File Prefix:").grid(row=1, column=0, padx=10, pady=5)
prefix_entry = tk.Entry(root, width=40)
prefix_entry.grid(row=1, column=1, padx=10, pady=5)

# Starting number input
tk.Label(root, text="Starting Number:").grid(row=2, column=0, padx=10, pady=5)
start_num_entry = tk.Entry(root, width=40)
start_num_entry.grid(row=2, column=1, padx=10, pady=5)

# Extension input (optional)
tk.Label(root, text="File Extension (Optional):").grid(row=3, column=0, padx=10, pady=5)
extension_entry = tk.Entry(root, width=40)
extension_entry.grid(row=3, column=1, padx=10, pady=5)

# Rename button
tk.Button(root, text="Rename Files", command=start_renaming).grid(row=4, column=1, padx=10, pady=20)

# Run the application
root.mainloop()
