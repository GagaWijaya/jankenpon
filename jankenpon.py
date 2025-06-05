# Nama: Moh.Rangga Wijaya Fadilah
# NPM: 227006416144



import random  # Import the random module to let the computer pick moves randomly

# Class to represent a move (rock, paper, or scissors)
class Move:

    options = ['rock', 'paper', 'scissors']  # Valid move options

    def __init__(self):
        self.choice = None  # Initialize choice to None

    # Set the player's move if it is a valid option
    def set_choice(self, choice):
        if choice in Move.options:
            self.choice = choice
        else:
            raise ValueError("Invalid move choice.")

    # Randomly select a move (for computer)
    def random_choice(self):
        self.choice = random.choice(Move.options)

    # Get the current move choice
    def get_choice(self):
        return self.choice

# Class to represent a player (human or computer)
class Player:
    def __init__(self, is_human=True):
        self.is_human = is_human  # Determine if the player is human
        self.move = Move()        # Each player has their own Move instance
        self.counter = 5         # Each player starts with a counter of 10

    # Increase the counter by 1 (when the player loses)
    def increment_counter(self):
        self.counter += 1

    # Decrease the counter by 1 (when the player wins)
    def decrement_counter(self):
        if self.counter > 0:
            self.counter -= 1

    # Allow the player to make a move
    def make_move(self):
        if self.is_human:
            # Ask the human player for input
            choice = input("Choose rock, paper, or scissors: ").lower()
            while choice not in Move.options:
                print("Invalid input. Try again.")
                choice = input("Choose rock, paper, or scissors: ").lower()
            self.move.set_choice(choice)
        else:
            # Let the computer randomly pick a move
            self.move.random_choice()

    # Return the move made by the player
    def get_move(self):
        return self.move.get_choice()

# Class to control the overall game logic
class JankenGame:
    def __init__(self):
        self.human = Player(is_human=True)      # Create a human player
        self.computer = Player(is_human=False)  # Create a computer player
        self.round = 1                          # Start from round 1

    # Determine the winner of the round based on both choices
    def determine_winner(self, human_choice, computer_choice):
        if human_choice == computer_choice:
            return "tie"
        elif (human_choice == 'rock' and computer_choice == 'scissors') or \
             (human_choice == 'scissors' and computer_choice == 'paper') or \
             (human_choice == 'paper' and computer_choice == 'rock'):
            return "human"
        else:
            return "computer"

    # Logic for playing one round of the game
    def play_round(self):
        print(f"\n🔁 Round {self.round}")
        input("Press Enter to play the round...")  # Pause until player is ready

        self.human.make_move()     # Get the human player's move
        self.computer.make_move()  # Get the computer's move

        human_move = self.human.get_move()
        computer_move = self.computer.get_move()

        # Show both players' moves
        print(f"You chose: {human_move}")
        print(f"Computer chose: {computer_move}")

        # Determine the winner of the round
        winner = self.determine_winner(human_move, computer_move)

        # Update counters based on result
        if winner == "tie":
            print("⚖️ It's a tie! No counter changes.")
        elif winner == "human":
            print("✅ You win this round!")
            self.human.decrement_counter()
            self.computer.increment_counter()
        else:
            print("❌ Computer wins this round!")
            self.computer.decrement_counter()
            self.human.increment_counter()

        # Display current counters
        print(f"Counter → You: {self.human.counter} | Computer: {self.computer.counter}")
        self.round += 1  # Increment the round number

    # Method to run the full game
    def play(self):
        print("👋 Welcome to the Japanese Suit Game (Janken)!")
        print("The first to reach counter = 0 wins!\n")

        # Continue playing until one player's counter reaches 0
        while self.human.counter > 0 and self.computer.counter > 0:
            self.play_round()

        # Show final result
        print("\n🏁 Game Over!")
        if self.human.counter == 0:
            print("🎉 Congratulations! You won the game!")
        else:
            print("💻 The computer won the game. Better luck next time!")

# Start the game if this file is executed
if __name__ == "__main__":
    game = JankenGame()
    game.play()
