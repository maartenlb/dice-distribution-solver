# Dice Distribution Solver

A Python tool to find the top 5 dice combinations matching a target mean and optional standard deviation. Perfect for probability modeling and tabletop games. Supports custom dice inputs and comes with a GUI for ease of use.

## Features

- **Target Distribution Matching**: Finds dice combinations that match a target mean and optional standard deviation.
- **Custom Dice Input**: Supports custom dice types (d5, d17, d53, d506, etc).
- **Efficient BFS Algorithm**: Uses BFS to explore dice combinations efficiently.
- **Readable Output**: Displays dice combinations in a clean format like `1d6, 2d20`.
- **GUI Integration**: Comes with a graphical user interface for easy input and visualization.
- **Executable Available**: Download and run the [`.exe`](https://github.com/maartenlb/dice-distribution-solver/blob/main/dist/gui.exe) file.

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
### Command-Line Interface
You can run the script directly from the command line:
```
python dice_distribution.py --mean 75 --std_dev 30 --dice 6 20 100
```
Would give the following output:

```
dice 6 20 100
Target Mean: 75.0
Target Standard Deviation: 30.0
Allowed Dice: [6, 20, 100]
Pre-calculated Expected Values: {6: 3.5, 20: 10.5, 100: 50.5}

Top 5 Matches:
Match 1: DiceState(dice=1d6, 2d20, 1d100, mean=75.00, std_dev=30.04), Distance=0.04, Num Dice=4
Match 2: DiceState(dice=4d6, 1d20, 1d100, mean=75.00, std_dev=29.63), Distance=0.37, Num Dice=6
Match 3: DiceState(dice=7d6, 1d100, mean=75.00, std_dev=29.22), Distance=0.78, Num Dice=8
Match 4: DiceState(dice=2d20, 1d100, mean=71.50, std_dev=30.00), Distance=3.50, Num Dice=3
Match 5: DiceState(dice=2d6, 2d20, 1d100, mean=78.50, std_dev=30.09), Distance=3.59, Num Dice=5
```

Arguments
--mean: The target mean of the distribution (required).

--std_dev: The target standard deviation of the distribution (optional).

--dice: List of allowed dice (default: 4 6 8 10 12 20 100).

### GUI
If you're using a GUI, you can input the mean, optional standard deviation, allowed dice and custom dice directly through the interface.

## How It Works
Pre-calculated Expected Values:
   * The script calculates the expected value (mean) for each allowed die using the formula: (die / 2) + 0.5.

BFS Algorithm:

   * The script uses BFS to explore dice combinations, starting from an empty state and adding one die at a time.
   * Keeps track of the top 5 matches based on their distance to the target mean and standard deviation.
   * Each state is represented as a dictionary of dice counts (e.g., {6: 1, 20: 2, 100: 1}), and a set is used to avoid exploring duplicate states.

Output Formatting:
   * The dice combinations are displayed in a readable format like 1d6, 2d20.

## Future Work
I would like to add the option for a flat modifier option to the script and GUI, as that is currently missing. Right now if you have a flat modifier of +30 and want to attain a distribution with a mean of 70, you should subtract the flat modifier from the target mean (so 70 - 30 = 40). This also works for negative flat modifiers (70 - -30 = 100).
