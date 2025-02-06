import argparse
import math
from collections import deque, defaultdict

# Argparse Setup
def setup_argparse():
    parser = argparse.ArgumentParser(description="Find dice combinations that match a target distribution.")
    parser.add_argument("--mean", type=float, required=True, help="The target mean of the distribution.")
    parser.add_argument("--std_dev", type=float, default=None, help="The target standard deviation of the distribution (optional).")
    parser.add_argument("--dice", nargs="+", type=int, default=[4, 6, 8, 10, 12, 20, 100],
                        help="List of allowed dice (default: 4 6 8 10 12 20 100).")
    return parser.parse_args()

# Pre-calculate Expected Values
def calculate_expected_values(allowed_dice):
    """Pre-calculate the expected value (mean) for each allowed die."""
    return {die: (die / 2) + 0.5 for die in allowed_dice}

# DiceState Class
class DiceState:
    def __init__(self, dice_counts, expected_values):
        self.dice_counts = dice_counts
        self.expected_values = expected_values
        self.mean = self.calculate_mean()
        self.std_dev = self.calculate_std_dev()

    def calculate_mean(self):
        """Calculate the mean of the dice state by summing the expected values."""
        return sum(count * self.expected_values[die] for die, count in self.dice_counts.items())

    def calculate_std_dev(self):
        """Calculate the standard deviation of the dice state."""
        # Variance of a single die is (d^2 - 1) / 12
        variance = sum(count * (die ** 2 - 1) / 12 for die, count in self.dice_counts.items())
        return math.sqrt(variance)

    def __repr__(self):
        """Format the dice counts as a string like '1d6, 2d20'."""
        dice_str = ", ".join(f"{count}d{die}" for die, count in sorted(self.dice_counts.items()))
        return f"DiceState(dice={dice_str}, mean={self.mean:.2f}, std_dev={self.std_dev:.2f})"

# BFS Function
def bfs_top_matches(target_mean, target_std_dev, expected_values):
    """Perform BFS to find the top 5 dice states that match the target mean and standard deviation."""
    # List to store the top 5 matches
    top_matches = []
    # Deque to explore states
    queue = deque()
    # Set to track seen states
    seen_states = set()

    # Start with an empty dice state
    initial_state = DiceState(defaultdict(int), expected_values)
    queue.append(initial_state)
    seen_states.add(frozenset(initial_state.dice_counts.items()))

    while queue:
        current_state = queue.popleft()

        # Calculate the total distance to the target
        total_distance = abs(current_state.mean - target_mean)
        if target_std_dev is not None:
            total_distance += abs(current_state.std_dev - target_std_dev)

        # If the current state is better than the worst in the top 5, add it
        if len(top_matches) < 5 or total_distance < top_matches[-1][0]:
            top_matches.append((total_distance, sum(current_state.dice_counts.values()), current_state))
            # Sort the top matches by distance and number of dice
            top_matches.sort(key=lambda x: (x[0], x[1]))
            # Keep only the top 5 matches
            if len(top_matches) > 5:
                top_matches.pop()

        # Explore further by adding one die of each type
        for die in expected_values:
            new_dice_counts = current_state.dice_counts.copy()
            new_dice_counts[die] += 1
            new_state = DiceState(new_dice_counts, expected_values)
            new_distance = abs(new_state.mean - target_mean)
            if target_std_dev is not None:
                new_distance += abs(new_state.std_dev - target_std_dev)

            # Only add to the queue if the new state could potentially improve the top 5
            if len(top_matches) < 5 or new_distance < top_matches[-1][0]:
                # Check if the new state is worth exploring
                if (new_state.mean < target_mean or
                    (target_std_dev is not None and new_state.std_dev < target_std_dev)):
                    # If the new state is below the target values, it can still be improved
                    state_key = frozenset(new_state.dice_counts.items())
                    if state_key not in seen_states:
                        seen_states.add(state_key)
                        queue.append(new_state)
                elif new_distance <= top_matches[-1][0]:
                    # If the new state is above the target values but still better than the worst in the top 5, explore it
                    state_key = frozenset(new_state.dice_counts.items())
                    if state_key not in seen_states:
                        seen_states.add(state_key)
                        queue.append(new_state)

    return top_matches

# Function to integrate with GUI
def find_optimal_dice(target_mean, target_std_dev, allowed_dice):
    # Pre-calculate expected values for all allowed dice
    expected_values = calculate_expected_values(allowed_dice)

    # Perform BFS to find the top 5 matches
    top_matches = bfs_top_matches(target_mean, target_std_dev, expected_values)

    return top_matches


# Main Function
def main():
    args = setup_argparse()
    target_mean = args.mean
    target_std_dev = args.std_dev
    allowed_dice = args.dice

    # Pre-calculate expected values for all allowed dice
    expected_values = calculate_expected_values(allowed_dice)

    print(f"Target Mean: {target_mean}")
    if target_std_dev is not None:
        print(f"Target Standard Deviation: {target_std_dev}")
    print(f"Allowed Dice: {allowed_dice}")
    print(f"Pre-calculated Expected Values: {expected_values}")

    # Perform BFS to find the top 5 matches
    top_matches = bfs_top_matches(target_mean, target_std_dev, expected_values)

    if top_matches:
        print("\nTop 5 Matches:")
        for i, (distance, num_dice, state) in enumerate(top_matches, 1):
            print(f"Match {i}: {state}, Distance={distance:.2f}, Num Dice={num_dice}")
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()