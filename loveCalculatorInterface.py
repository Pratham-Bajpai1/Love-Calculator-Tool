import tkinter as tk
from tkinter import messagebox, ttk
from loveCalculatorbackend import calculate_love_percentage

class LoveCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Love Calculator 💖')
        self.root.geometry('500x700')
        self.root.config(bg='#ffcccb')

        self.past_results = []

        self.create_widgets()

    def create_widgets(self):
        # Create a canvas and a vertical scrollbar linked to this canvas
        self.canvas = tk.Canvas(self.root, bg='#ffcccb')
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style="My.TFrame")

        # Configure the scrollbar and canvas
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Heading
        self.heading_label = tk.Label(self.scrollable_frame, text='Love Calculator - How much is he/she into you?', font=("Helvetica", 18, 'bold'), bg='#ffcccb', fg='#e6005c')
        self.heading_label.pack(pady=20)

        # Name 1 Input
        self.name1_label = tk.Label(self.scrollable_frame, text="Enter Your Name:", font=("Helvetica", 14), bg='#ffcccb')
        self.name1_label.pack(pady=5)
        self.name1_entry = tk.Entry(self.scrollable_frame, font=("Helvetica", 14), width=30)
        self.name1_entry.pack(pady=5)

        # Name 2 Input
        self.name2_label = tk.Label(self.scrollable_frame, text="Enter Your Partner's Name:", font=("Helvetica", 14), bg='#ffcccb')
        self.name2_label.pack(pady=5)
        self.name2_entry = tk.Entry(self.scrollable_frame, font=("Helvetica", 14), width=30)
        self.name2_entry.pack(pady=5)

        # Calculate Button
        self.calculate_button = tk.Button(self.scrollable_frame, text="Calculate", font=("Helvetica", 14), command=self.calculate_love, bg='#ff6699', fg='#ffffff', activebackground='#ff3366')
        self.calculate_button.pack(pady=20)

        # Result Label
        self.result_label = tk.Label(self.scrollable_frame, text='Love Percentage between both of You:', font=("Helvetica", 14), bg='#ffcccb')
        self.result_label.pack(pady=5)

        # Result Display
        self.result_display = tk.Label(self.scrollable_frame, text='', font=("Helvetica", 18, 'bold'), bg='#ffcccb', fg='#ff1a75')
        self.result_display.pack(pady=5)

        # Message Display
        self.message_display = tk.Label(self.scrollable_frame, text='', font=("Helvetica", 14), bg='#ffcccb', fg='#ff1a75')
        self.message_display.pack(pady=5)

        # Save Button
        self.save_button = tk.Button(self.scrollable_frame, text="Save Result", font=("Helvetica", 14), command=self.save_result, bg='#ff6699', fg='#ffffff', activebackground='#ff3366')
        self.save_button.pack(pady=10)

        # Share Button
        self.share_button = tk.Button(self.scrollable_frame, text="Share Result", font=("Helvetica", 14), command=self.share_result, bg='#ff6699', fg='#ffffff', activebackground='#ff3366')
        self.share_button.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(self.scrollable_frame, text="Reset", font=("Helvetica", 14), command=self.reset_fields, bg='#ff6699', fg='#ffffff', activebackground='#ff3366')
        self.reset_button.pack(pady=10)

        # Create a frame for past results
        self.past_results_frame = tk.Frame(self.root, bg='#ffcccb')
        self.past_results_frame.pack(fill="both", expand=True)

        # Past Results Label
        self.past_results_label = tk.Label(self.past_results_frame, text='Past Results:', font=("Helvetica", 14), bg='#ffcccb')
        self.past_results_label.pack(pady=5)

        # Past Results Display
        self.past_results_display = tk.Text(self.past_results_frame, height=10, font=("Helvetica", 12), bg='#ffe6e6', fg='#000000')
        self.past_results_display.pack(pady=5)
        self.past_results_display.config(state=tk.DISABLED)

        # Footer
        self.footer_label = tk.Label(self.root, text="© Made by Pratham Bajpai", font=("Helvetica", 10), bg='#ffcccb', fg='#e6005c')
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def calculate_love(self):
        name1 = self.name1_entry.get()
        name2 = self.name2_entry.get()
        if name1.strip() and name2.strip():
            self.animate_calculation(name1, name2)
        else:
            messagebox.showerror("Error", "Please enter both names to calculate the love percentage.")

    def animate_calculation(self, name1, name2):
        def update_label(percentage):
            self.result_display.config(text=f"{percentage}%")
        
        self.result_display.config(text="")
        for i in range(10, 101, 10):
            self.root.after(i * 10, lambda i=i: update_label(i))
        self.root.after(1000, lambda: self.show_final_result(name1, name2))

    def show_final_result(self, name1, name2):
        love_percentage, message = calculate_love_percentage(name1, name2)
        self.result_display.config(text=f"{love_percentage}%")
        self.message_display.config(text=message)

    def save_result(self):
        name1 = self.name1_entry.get()
        name2 = self.name2_entry.get()
        result = self.result_display.cget("text")
        message = self.message_display.cget("text")
        if name1.strip() and name2.strip() and result:
            entry = f"{name1} ❤ {name2}: {result} - {message}"
            self.past_results.append(entry)
            self.update_past_results()
        else:
            messagebox.showerror("Error", "No result to save.")

    def update_past_results(self):
        self.past_results_display.config(state=tk.NORMAL)
        self.past_results_display.delete(1.0, tk.END)
        for result in self.past_results:
            self.past_results_display.insert(tk.END, result + '\n')
        self.past_results_display.config(state=tk.DISABLED)

    def share_result(self):
        result = self.result_display.cget("text")
        message = self.message_display.cget("text")
        if result:
            messagebox.showinfo("Share", f"Share this result: {result} - {message}")
        else:
            messagebox.showerror("Error", "No result to share.")

    def reset_fields(self):
        self.name1_entry.delete(0, tk.END)
        self.name2_entry.delete(0, tk.END)
        self.result_display.config(text="")
        self.message_display.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoveCalculatorApp(root)
    root.mainloop()

    
