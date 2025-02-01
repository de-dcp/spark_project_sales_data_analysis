import tkinter as tk
from tkinter import messagebox
import time
import threading


# Function to show a pop-up reminder
def show_reminder():
    # Create a simple Tkinter pop-up window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    root.attributes("-topmost", True)

    # Create a pop-up window with a reminder message
    messagebox.showinfo("Break Reminder", "Time to take a break! Stretch your legs and relax your eyes.")
    root.quit()


# Function to run the timer and show reminders every 30 minutes
def start_timer():
    while True:
        time.sleep(1200)  # 30 minutes in seconds
        show_reminder()  # Show the Tkinter pop-up


# Main function to start the timer in a background thread
def run():
    # Start the background thread to remind every 30 minutes
    threading.Thread(target=start_timer, daemon=True).start()

    # Keep the script running
    while True:
        time.sleep(1)


if __name__ == "__main__":
    run()
