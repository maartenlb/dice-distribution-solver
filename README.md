# Dice Distribution Solver

A Python tool to find the top 5 dice combinations matching a target mean and optional standard deviation. Perfect for probability modeling and tabletop games. Supports custom dice inputs and comes with a GUI for ease of use.

## Features

- **Target Distribution Matching**: Finds dice combinations that match a target mean and optional standard deviation.
- **Custom Dice Input**: Supports custom dice types (e.g., d4, d6, d8, d10, d12, d20, d100).
- **Efficient BFS Algorithm**: Uses BFS to explore dice combinations efficiently.
- **Readable Output**: Displays dice combinations in a clean format like `1d6, 2d20`.
- **GUI Integration**: Comes with a graphical user interface for easy input and visualization.
- **Executable Available**: Download and run the [`.exe`](https://github.com/maartenlb/dice-distribution-solver/blob/main/dist/gui.exe) file for a hassle-free experience.

## Installation

### Option 1: Run from Source

1. Clone the repository:
   ```
   git clone https://github.com/maartenlb/dice-distribution-solver.git
   cd dice-distribution-solver
   ```

2. Run the script:
    ```
    python dice_distribution.py
    ```
2. Or, if you have a GUI:
    ```
    python gui.py
    ```

### Option 2: Download and Run the Executable
1. Download the [.exe](https://github.com/maartenlb/dice-distribution-solver/blob/main/dist/gui.exe) file from the dist folder in the repository.
2. Double-click the .exe file to launch the application.

## Usage
Command-Line Interface
You can run the script directly from the command line:
```
python dice_distribution.py --mean 75 --std_dev 30 --dice 6 20 100
```
