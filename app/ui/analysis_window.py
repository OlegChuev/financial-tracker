import tkinter as tk
from tkinter import ttk, messagebox, filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ..constants import PLOT_WINDOW_SIZE
from ..plotter import Plotter

class AnalysisWindow:
    def __init__(self, master, transactions):
        self.top = tk.Toplevel(master)
        self.top.title("Expense Analysis")
        self.top.geometry(PLOT_WINDOW_SIZE)
        self.top.grab_set()

        plot_frame = ttk.Frame(self.top, padding="20")
        plot_frame.pack(fill="both", expand=True)

        notebook = ttk.Notebook(plot_frame)
        notebook.pack(fill="both", expand=True)

        months = Plotter.get_months(transactions)
        if not months:
            messagebox.showinfo("Info", "No expenses to analyze.")
            self.top.destroy()
            return

        self._plot_figures = {}
        self._months = months
        self._notebook = notebook

        for month in months:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=month)
            fig = Plotter.plot_expenses_for_month(transactions, month)
            if fig:
                canvas = FigureCanvasTkAgg(fig, master=tab)
                canvas.draw()
                canvas.get_tk_widget().pack(fill="both", expand=True)
                self._plot_figures[month] = fig
            else:
                ttk.Label(tab, text="No data for this month").pack(padx=20, pady=20)

        save_btn = ttk.Button(plot_frame, text="Save Chart as Image", command=self.save_chart)
        save_btn.pack(pady=10, anchor="e")

    def save_chart(self):
        idx = self._notebook.index(self._notebook.select())
        month = self._months[idx]
        fig = self._plot_figures.get(month)
        if not fig:
            messagebox.showerror("Error", "No chart to save for this month.")
            return
        file_path = fd.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("All Files", "*.*")],
            title="Save Chart As..."
        )
        if file_path:
            fig.savefig(file_path)
            messagebox.showinfo("Success", f"Chart saved to {file_path}") 