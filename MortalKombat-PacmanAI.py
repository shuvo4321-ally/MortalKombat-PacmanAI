import random
import time


# Node class definition for game decision tree
class Node:
    def __init__(self, depth, is_maximizing_player, alpha, beta):
        self.depth = depth
        self.is_maximizing_player = is_maximizing_player
        self.alpha = alpha
        self.beta = beta
        self.children = []
        self.utility = None

    # Generate children nodes (simulate game states)
    def generate_children(self):
        if self.depth > 0:
            for _ in range(2):  # Simulate a binary branching factor
                child = Node(self.depth - 1, not self.is_maximizing_player, self.alpha, self.beta)
                child.generate_children()
                self.children.append(child)
        else:
            # Leaf nodes are assigned random utility values
            self.utility = random.choice([-1, 1])

    # Perform alpha-beta pruning and return the utility value
    def alpha_beta_pruning(self):
        if self.depth == 0:
            # At a leaf node, return its utility value
            return self.utility
        if self.is_maximizing_player:
            max_eval = float('-inf')
            for child in self.children:
                eval = child.alpha_beta_pruning()
                max_eval = max(max_eval, eval)
                self.alpha = max(self.alpha, eval)
                if self.beta <= self.alpha:
                    break  # Prune
            return max_eval
        else:
            min_eval = float('inf')
            for child in self.children:
                eval = child.alpha_beta_pruning()
                min_eval = min(min_eval, eval)
                self.beta = min(self.beta, eval)
                if self.beta <= self.alpha:
                    break  # Prune
            return min_eval


# Simulate a 3-round battle using alpha-beta decision-making
def simulate_battle(starting_player):
    current_player = starting_player
    rounds = []

    for round_number in range(1, 4):  # Simulate 3 rounds
        # Generate the decision tree root with depth 5
        root = Node(depth=5, is_maximizing_player=(current_player == 1), alpha=float('-inf'), beta=float('inf'))
        root.generate_children()
        result = root.alpha_beta_pruning()

        if result == -1:
            winner = "Scorpion"
        else:
            winner = "Sub-Zero"
        rounds.append(winner)

        # Alternate the starting player for fairness in the next round
        current_player = 1 - current_player

    # Calculate the overall winner of the battle
    scorpion_wins = rounds.count("Scorpion")
    sub_zero_wins = rounds.count("Sub-Zero")

    if scorpion_wins > sub_zero_wins:
        game_winner = "Scorpion"
    else:
        game_winner = "Sub-Zero"

    return game_winner, rounds


# Seed the random number generator for variability
random.seed(time.time())

# Input starting player
starting_player = int(input("Enter starting player (0 for Scorpion, 1 for Sub-Zero): "))

# Simulate the battle and determine the overall winner
game_winner, rounds = simulate_battle(starting_player)

# Output the results
print(f"Game Winner: {game_winner}")
print(f"Total Rounds Played: 3")
for i, round_winner in enumerate(rounds, start=1):
    print(f"Winner of Round {i}: {round_winner}")
#PART 2
class PacmanNode:
    def __init__(self, depth, is_maximizing_player, alpha, beta, values=None):
        self.depth = depth
        self.is_maximizing_player = is_maximizing_player
        self.alpha = alpha
        self.beta = beta
        self.values = values
        self.children = []

    def generate_children(self):
        if self.depth == 0:
            return
        num_children = len(self.values) // 2  # Split children equally
        for i in range(2):
            child_values = self.values[i * num_children: (i + 1) * num_children]
            child = PacmanNode(
                self.depth - 1, not self.is_maximizing_player, self.alpha, self.beta, child_values
            )
            self.children.append(child)
            child.generate_children()

    def alpha_beta_pruning(self):
        if self.depth == 0:
            # Return the leaf node value if it's a leaf
            return sum(self.values)

        if self.is_maximizing_player:
            value = float('-inf')
            for child in self.children:
                value = max(value, child.alpha_beta_pruning())
                self.alpha = max(self.alpha, value)
                if self.beta <= self.alpha:
                    break
            return value
        else:
            value = float('inf')
            for child in self.children:
                value = min(value, child.alpha_beta_pruning())
                self.beta = min(self.beta, value)
                if self.beta <= self.alpha:
                    break
            return value


def pacman_game(c):
    # Define the leaf values for minimax comparison
    leaf_values = [3, 6, 2, 3, 7, 1, 2, 0]

    # Generate the game tree without dark magic
    root_without_magic = PacmanNode(
        depth=3,
        is_maximizing_player=True,
        alpha=float('-inf'),
        beta=float('inf'),
        values=leaf_values,
    )
    root_without_magic.generate_children()

    # Perform alpha-beta pruning for decision-making without dark magic
    value_without_magic = root_without_magic.alpha_beta_pruning()

    # Simulate dark magic decision paths manually
    left_subtree_value = leaf_values[1] - c  # Left subtree with dark magic
    right_subtree_value = leaf_values[4] - c  # Right subtree with dark magic

    # Determine the better path with magic
    if left_subtree_value >= right_subtree_value:
        best_value_with_magic = left_subtree_value
        best_path_with_magic = "Left"
    else:
        best_value_with_magic = right_subtree_value
        best_path_with_magic = "Right"

    # Compare the two strategies
    if best_value_with_magic > value_without_magic:
        return f"Using dark magic is advantageous. Best path: {best_path_with_magic}, Value: {best_value_with_magic}"
    else:
        return f"Not using dark magic is better. Value: {value_without_magic}"


# Example test cases
print(pacman_game(5))  # Test with a cost of 5
print(pacman_game(2))  # Test with a cost of 2
