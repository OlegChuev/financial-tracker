import tkinter as tk

from .ui.main_window import MainWindow

# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
