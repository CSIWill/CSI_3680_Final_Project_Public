import tkinter as tk
from tkinter import messagebox, filedialog
import keygen


def browse_file1():
    global file_path1
    file_path1 = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    selected_file_label1.config(text=f"Selected File: {file_path1}")
    return file_path1

def browse_file2():
    global file_path2
    file_path2 = filedialog.askopenfilename(filetypes=[("Key Text File", "*.txt"), ("All files", "*.*")])
    selected_file_label2.config(text=f"Selected File: {file_path2}")
    return file_path2

def browse_file3():
    global file_path3
    file_path3 = filedialog.askopenfilename(filetypes=[("Ciphertext File", "*.txt"), ("All files", "*.*")])
    selected_file_label3.config(text=f"Selected File: {file_path3}")
    return file_path3

def browse_file4():
    global file_path4
    file_path4 = filedialog.askopenfilename(filetypes=[("Key Text File", "*.txt"), ("All files", "*.*")])
    selected_file_label4.config(text=f"Selected File: {file_path4}")
    return file_path4

def initialize_key():
    try:
        keygen.generate_key(user_input_entry.get())
        messagebox.showinfo("Generate Keys", "Keys have been generated, encrypt with your private key and send your public key")
    except:
        messagebox.showerror("Unable to Generate Keys","Error: Unable to generate key with provided e, consider using the default value of 65537")
    
def encrypt_file():
    try:
        global file_path1, file_path2
        encryptFile = file_path1
        keyFile = file_path2
        keygen.encrypt_file(encryptFile, keyFile)
        messagebox.showinfo("Encrypt File", "File has been encrypted")
    except:
        messagebox.showerror("Unable to Encrypt File", "Error: Unable to encrypt file, please try again")
def decrypt_file():
    try:
        global file_path3, file_path4
        decryptFile = file_path3
        keyFile = file_path4
        keygen.decrypt_file(decryptFile, keyFile)
        messagebox.showinfo("Decrypt File", "File has been decrypted")
    except:
        messagebox.showerror("Unable to Decrypt File", "Error: Unable to decrypt file, please try again")
# global
file_path1 = ""
file_path2 = ""
file_path3 = ""
file_path4 = ""


# Create the main window
root = tk.Tk()
root.title("RSA Encryption -- William Eng")

root.geometry("1024x768")

# generate keys
user_input_entry_label = tk.Label(root, text="Please input a number for e, or press enter to use the default value 65537.  If you want a random e, enter 0")
user_input_entry_label.pack(pady=10)
user_input_entry = tk.Entry(root, width=10)
user_input_entry.pack(pady=5)
generateKeyButton = tk.Button(root, text="Generate Keys", command=initialize_key)
generateKeyButton.pack(pady=10)

center_frame = tk.Frame(root)
center_frame.pack(expand=True)

# encrypt file with your private key
frame1 = tk.Frame(center_frame)
frame1.pack(side=tk.LEFT, padx=10, pady=10)

encryptionLabel = tk.Label(frame1, text="Encryption")
encryptionLabel.pack(padx=10, pady=10)
selected_file_label1 = tk.Label(frame1, text="Selected File to Encrypt: None")
selected_file_label1.pack(padx=10, pady=10)
browse_button1 = tk.Button(frame1, text="Browse", command=browse_file1)
browse_button1.pack(padx=10, pady=10)

selected_file_label2 = tk.Label(frame1, text="Selected Key File: None")
selected_file_label2.pack(padx=10, pady=10)
browse_button2 = tk.Button(frame1, text="Browse", command=browse_file2)
browse_button2.pack(padx=10, pady=10)

encrypt_file_label = tk.Label(frame1, text="Encrypt File")
encrypt_file_label.pack(padx=10, pady=10)
encrypt_button = tk.Button(frame1, text="Submit", command=encrypt_file)
encrypt_button.pack(padx=10, pady=10)

# decrypt file with your public key
frame2 = tk.Frame(center_frame)
frame2.pack(side=tk.LEFT, padx=10, pady=10)

decryptionLabel = tk.Label(frame2, text="Decryption")
decryptionLabel.pack(padx=10, pady=10)
selected_file_label3 = tk.Label(frame2, text="Selected File to Decrypt: None")
selected_file_label3.pack(padx=10, pady=10)
browse_button3 = tk.Button(frame2, text="Browse", command=browse_file3)
browse_button3.pack(padx=10, pady=10)

selected_file_label4 = tk.Label(frame2, text="Selected Key File: None")
selected_file_label4.pack(padx=10, pady=10)
browse_button4 = tk.Button(frame2, text="Browse", command=browse_file4)
browse_button4.pack(padx=10, pady=10)

decrypt_file_label = tk.Label(frame2, text="Decrypt File")
decrypt_file_label.pack(padx=10, pady=10)
decrypt_button = tk.Button(frame2, text="Submit", command=decrypt_file)
decrypt_button.pack(padx=10, pady=10)




# Run the Tkinter event loop
root.mainloop()