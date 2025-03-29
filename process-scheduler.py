import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Scheduler")
        self.root.geometry("900x600")  # Enlarged window
        self.root.configure(bg="white")

        title_label = tk.Label(
            root,
            text="Process Scheduler",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="black"
        )
        title_label.pack(pady=10)

        frame = tk.Frame(root, bg="black")
        frame.pack(pady=10)

        headers = ["Process", "Arrival Time", "Burst Time", "Priority"]
        for i, header in enumerate(headers):
            tk.Label(frame, text=header, font=("Arial", 12, "bold"), fg="white", bg="black").grid(row=0, column=i, padx=5, pady=5)

        self.entries = []
        for i in range(5):  # For 5 processes
            tk.Label(frame, text=f"P{i+1}", font=("Arial", 12, "bold"), fg="white", bg="black").grid(row=i+1, column=0, padx=5, pady=5)
            row_entries = []
            for j in range(3):  # Arrival, Burst, Priority
                entry = tk.Entry(frame, width=10)
                entry.grid(row=i+1, column=j+1, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        tk.Label(frame, text="Algorithm:", font=("Arial", 12, "bold"), fg="white", bg="black").grid(row=6, column=0, pady=10)
        self.algo_var = ttk.Combobox(frame, values=["FCFS", "SJF", "Priority", "Round Robin"], width=10)
        self.algo_var.grid(row=6, column=1)
        self.algo_var.current(0)

        tk.Label(frame, text="Time Quantum:", font=("Arial", 12, "bold"), fg="white", bg="black").grid(row=6, column=2, pady=10)
        self.time_quantum_entry = tk.Entry(frame, width=5)
        self.time_quantum_entry.grid(row=6, column=3)

        button_frame = tk.Frame(root, bg="white")
        button_frame.pack(pady=10)

        run_button = tk.Button(button_frame, text="Run Scheduler", command=self.run_scheduler, font=("Arial", 12, "bold"), bg="green", fg="white")
        run_button.grid(row=0, column=0, padx=10)

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_entries, font=("Arial", 12, "bold"), bg="red", fg="white")
        clear_button.grid(row=0, column=1, padx=10)

        self.output_text = tk.Text(root, height=5, width=80, bg="black", fg="lime", font=("Arial", 16, "bold"))
        self.output_text.pack(pady=10)

        self.chart_frame = tk.Frame(root, bg="white")
        self.chart_frame.pack(pady=10)

    def clear_entries(self):
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)
        self.output_text.delete("1.0", tk.END)

    def run_scheduler(self):
        algorithm = self.algo_var.get()
        time_quantum = self.time_quantum_entry.get()
        
        processes = []
        for i, row in enumerate(self.entries):
            arrival = int(row[0].get() or 0)
            burst = int(row[1].get() or 0)
            priority = int(row[2].get() or 0)
            processes.append((f"P{i+1}", arrival, burst, priority))

        if algorithm == "FCFS":
            schedule = self.fcfs(processes)
        elif algorithm == "SJF":
            schedule = self.sjf(processes)
        elif algorithm == "Priority":
            schedule = self.priority_scheduling(processes)
        elif algorithm == "Round Robin":
            if not time_quantum.isdigit():
                self.output_text.insert(tk.END, "Invalid Time Quantum\n")
                return
            schedule = self.round_robin(processes, int(time_quantum))
        else:
            self.output_text.insert(tk.END, "Invalid Algorithm Selected\n")
            return

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "Scheduling Result:\n")
        self.output_text.insert(tk.END, "Scheduling completed\n")

        self.draw_gantt_chart(schedule)

    def draw_gantt_chart(self, schedule):
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(8, 2))
        start = 0
        for process, burst in schedule:
            ax.broken_barh([(start, burst)], (10, 5), facecolors='tab:blue')
            ax.text(start + burst/2, 12, process, ha='center', va='center', fontsize=12, color="white")
            start += burst

        ax.set_ylim(5, 20)
        ax.set_xlim(0, start)
        ax.set_xlabel("Time")
        ax.set_yticks([])
        ax.set_title("Gantt Chart")

        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def fcfs(self, processes):
        processes.sort(key=lambda x: x[1])  # Sort by arrival time
        return [(p[0], p[2]) for p in processes]

    def sjf(self, processes):
        processes.sort(key=lambda x: x[2])  # Sort by burst time
        return [(p[0], p[2]) for p in processes]

    def priority_scheduling(self, processes):
        processes.sort(key=lambda x: x[3])  # Sort by priority (lower is higher)
        return [(p[0], p[2]) for p in processes]

    def round_robin(self, processes, quantum):
        queue = processes[:]
        schedule = []
        time = 0
        while queue:
            process = queue.pop(0)
            if process[2] > quantum:
                schedule.append((process[0], quantum))
                queue.append((process[0], process[1], process[2] - quantum, process[3]))
            else:
                schedule.append((process[0], process[2]))
            time += quantum
        return schedule


if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()