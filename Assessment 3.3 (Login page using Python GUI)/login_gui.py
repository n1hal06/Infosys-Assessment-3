import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("300x180")
        self.root.resizable(False, False)
        tk.Label(root, text="Username:").pack(pady=(20, 0))
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        tk.Label(root, text="Password:").pack(pady=(10, 0))
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()
        tk.Button(root, text="Login", command=self.check_login).pack(pady=15)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "nihal" and password == "200506":
            messagebox.showinfo("Login Success", "Welcome, admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

