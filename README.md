# Process Scheduling Application

This project is a process scheduling application that implements various scheduling algorithms including First-Come, First-Serve (FCFS), Shortest Job First (SJF), Priority Scheduling, and Round Robin. The application features a graphical user interface (GUI) built with Tkinter, allowing users to input process details and visualize the scheduling results through a Gantt chart generated using Matplotlib.

## Features

- **FCFS Scheduling**: Processes are scheduled in the order they arrive.
- **SJF Scheduling**: Processes with the shortest burst time are scheduled first.
- **Priority Scheduling**: Processes are scheduled based on priority (lower values indicate higher priority).
- **Round Robin Scheduling**: Each process is assigned a fixed time slice (quantum) in a cyclic order.

## Installation

To run this project, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This project requires the following Python packages:

- Tkinter (usually included with Python)
- Matplotlib

You can install Matplotlib using pip:

```
pip install matplotlib
```

## Usage

1. Clone the repository to your local machine:

   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```
   cd process-scheduling
   ```

3. Run the application:

   ```
   python src/script.py
   ```

4. Input the process details (arrival time, burst time, and priority) in the provided fields.
5. Select the desired scheduling algorithm from the dropdown menu.
6. For Round Robin, specify the time quantum.
7. Click on "Run Scheduler" to see the scheduling results and the Gantt chart.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

