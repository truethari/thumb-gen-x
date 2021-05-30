import tkinter as tk

from .gui import GUI

def main():
    root = tk.Tk()
    root.title("Thumb-Gen-X")
    root.geometry("1000x500")
    root.configure(bg="White")
    root.resizable(0,0)
    root.minsize(1000, 500)
    root.maxsize(1000, 500)
    GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
