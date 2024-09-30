import tkinter as tk
from random import choice


# Function to decide the winner and update score
def decide_winner(player_choice):
    global player_score, computer_score

    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(options)

    # Update choices display
    player_choice_label.config(text=f"Player chose: {player_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a tie!"
        result_label.config(fg="black")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
            (player_choice == 'Paper' and computer_choice == 'Rock') or \
            (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        player_score += 1
        result_label.config(fg="white")
    else:
        result = "You lose!"
        computer_score += 1
        result_label.config(fg="red")

    result_label.config(text=result)

    # Update scores
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")


# Function to handle button clicks
def play(choice):
    decide_winner(choice)


# Function to reset the game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_score_label.config(text="Player Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    result_label.config(text="")
    player_choice_label.config(text="Player chose: ")
    computer_choice_label.config(text="Computer chose: ")


# Gradient background function
def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        r = int(int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * (i / height))
        g = int(int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * (i / height))
        b = int(int(color1[5:], 16) + (int(color2[5:], 16) - int(color1[5:], 16)) * (i / height))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)


# Setting up the GUI
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x600")

# Create a canvas for gradient background
canvas = tk.Canvas(root, width=450, height=600)
canvas.pack(fill="both", expand=True)

# Apply a gradient from top to bottom
create_gradient(canvas, 450, 600, "#3498DB", "#1ABC9C")

# Global variables for score
player_score = 0
computer_score = 0

# Create a frame to place widgets on top of the gradient background
frame = tk.Frame(root, bg="#34495E", bd=2, relief="ridge")
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

# Heading label
heading_label = tk.Label(frame, text="Rock Paper Scissors", font=("Helvetica", 24, "bold"), bg="#34495E", fg="white")
heading_label.pack(pady=20)

# Create a frame for the scoreboard
score_frame = tk.Frame(frame, bg="#2C3E50", bd=2, relief="groove")
score_frame.pack(pady=10, padx=10, fill="x")

# Create labels for displaying player and computer choices
player_choice_label = tk.Label(score_frame, text="Player chose: ", font=("Helvetica", 14), bg="#2C3E50", fg="white")
player_choice_label.grid(row=0, column=0, padx=10, pady=10)

computer_choice_label = tk.Label(score_frame, text="Computer chose: ", font=("Helvetica", 14), bg="#2C3E50", fg="white")
computer_choice_label.grid(row=0, column=1, padx=10, pady=10)

# Create labels for scores
player_score_label = tk.Label(score_frame, text="Player Score: 0", font=("Helvetica", 14), bg="#2C3E50", fg="white")
player_score_label.grid(row=1, column=0, padx=10, pady=10)

computer_score_label = tk.Label(score_frame, text="Computer Score: 0", font=("Helvetica", 14), bg="#2C3E50", fg="white")
computer_score_label.grid(row=1, column=1, padx=10, pady=10)

# Create label to display result
result_label = tk.Label(frame, text="", font=("Helvetica", 16, "bold"), bg="#34495E", fg="white")
result_label.pack(pady=20)


# Button styling functions
def on_enter(e):
    e.widget.config(bg="#1ABC9C")


def on_leave(e):
    e.widget.config(bg="#3498DB")


# Create buttons for Rock, Paper, and Scissors with styling
button_frame = tk.Frame(frame, bg="#34495E")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=15, height=2, font=("Helvetica", 14), bg="#3498DB", fg="white",
                        bd=0, command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=15, height=2, font=("Helvetica", 14), bg="#3498DB",
                         fg="white", bd=0, command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=15, height=2, font=("Helvetica", 14), bg="#3498DB",
                            fg="white", bd=0, command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Add hover effect for buttons
for button in [rock_button, paper_button, scissors_button]:
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Reset button to reset scores
reset_button = tk.Button(frame, text="Reset Game", width=20, height=2, font=("Helvetica", 12), bg="#E74C3C", fg="white",
                         command=reset_game)
reset_button.pack(pady=20)

# Running the application
root.mainloop()
