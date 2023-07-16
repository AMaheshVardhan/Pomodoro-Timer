# Pomodoro-Timer🍅

This is a simple Pomodoro Timer implemented using Python and the tkinter library. The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. The intervals are known as "pomodoros."
## How it works
The main window displays the title "Pomodoro," and an image of a tomato which represents a typical pomodoro timer.

There are three constants defined for the different time intervals used in the Pomodoro Technique:

WORK_MIN: The length of a work session in minutes (default is 25 minutes).
SHORT_BREAK_MIN: The length of a short break in minutes (default is 5 minutes).
LONG_BREAK_MIN: The length of a long break in minutes (default is 20 minutes).
The timer keeps track of the number of completed work sessions using the reps variable.

The start_timer() function handles the timing and switching between work sessions and breaks. It sets the appropriate countdown duration and label based on the current session.

The count_down() function is responsible for updating the timer's display in the format "mm:ss" and scheduling the next countdown tick using window.after().

When the timer reaches 00:00 for a work session or a break, the count_down() function calls start_timer() to begin the next session or break.

The "Start" button triggers the start_timer() function when clicked, initiating the Pomodoro Technique. The "Reset" button allows the user to stop the current session and reset the timer to its initial state.

During work sessions, the timer's title displays "Work" in red (RED), during short breaks it displays "Break" in pink (PINK), and during long breaks it displays "Break" in green (GREEN).

As the work sessions are completed, checkmarks (✓) are displayed at the bottom to indicate the number of completed work sessions.

## Usage

Ensure you have Python and the tkinter library installed on your system.

Save the script in a file named pomodoro.py.

Make sure to have an image named tomato.png in the same directory as the script. The image is used as a visual representation of the timer.

Run the script using a Python interpreter.

The main window of the Pomodoro Timer will appear.

Click the "Start" button to begin the Pomodoro Technique. The timer will switch between work sessions and breaks automatically.

To stop and reset the timer, click the "Reset" button.

You can repeat the process as needed for improved productivity and time management.

Enjoy using the Pomodoro Timer to boost your productivity and manage your time effectively! Happy working!

## Contribution
Feel free to contribute to this project on GitHub: [Pomodoro-Timer](https://github.com/mahesh-vardhan/Pomodoro-Timer)

If you find any issues or have suggestions for improvement, please create an issue or pull request. Your contributions are highly appreciated!
