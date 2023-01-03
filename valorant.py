import tkinter as tk
import matplotlib.pyplot as plt


def calculate_hours():
    # Get the user's responses to the survey questions
    hours_per_week = int(hours_per_week_entry.get())
    hours_per_day = int(hours_per_day_entry.get())
    game_mode = game_mode_entry.get()

    # Calculate the total number of hours spent playing Valorant
    total_hours = hours_per_week * 7 + hours_per_day

    # Create a pie chart showing the breakdown of hours spent by game mode
    labels = ["Valorant", "Other"]
    sizes = [total_hours, 168 - total_hours]
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title(f"Hours spent on Valorant vs other games (favorite mode: {game_mode})")
    plt.show()


# Create the main window
window = tk.Tk()
window.title("Valorant Survey")

# Create the labels and entries for the survey questions
hours_per_week_label = tk.Label(
    text="How many hours per week do you spend playing Valorant?"
)
hours_per_week_entry = tk.Entry()
hours_per_day_label = tk.Label(
    text="How many hours per day do you spend playing Valorant?"
)
hours_per_day_entry = tk.Entry()
game_mode_label = tk.Label(text="What is your favorite Valorant game mode?")
game_mode_entry = tk.Entry()

# Create the button to submit the survey responses
submit_button = tk.Button(text="Submit", command=calculate_hours)

# Place the widgets in the window
hours_per_week_label.pack()
hours_per_week_entry.pack()
hours_per_day_label.pack()
hours_per_day_entry.pack()
game_mode_label.pack()
game_mode_entry.pack()
submit_button.pack()

# Run the main loop
window.mainloop()
