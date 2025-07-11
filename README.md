🧠 Quickfingers - Speed Typing Test
⌨️ Terminal-based Typing Speed Game built with Python and curses
📌 Description
Quickfingers is a terminal-based application that allows users to test and improve their typing speed in real-time. It displays a random sentence from a list, tracks your typing accuracy, and calculates your Words Per Minute (WPM) as you type. After each line, you can choose to continue or exit.

This project is ideal for those looking to:

Build interactive terminal applications

Practice Python input handling and timing

Use the curses library effectively

🚀 Features
✅ Real-time WPM calculation

✅ Instant feedback (green for correct, red for incorrect characters)

✅ Loads random lines from text.txt

✅ Asks if user wants to continue after each line

✅ ESC key to quit instantly

✅ Color-coded UI with smooth terminal interaction

📂 How to Run
🖥 Works best on Linux/macOS terminal or Windows with Git Bash or Windows Terminal.

Install Python (if not installed):

bash
Copy
Edit
https://www.python.org/downloads/
Install windows-curses (Only for Windows users):

bash
Copy
Edit
pip install windows-curses
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/Quickfingers.git
cd Quickfingers
Create/Edit your text.txt with sentences:

txt
Copy
Edit
Practice makes perfect.
The quick brown fox jumps over the lazy dog.
Speed typing is fun and useful.
Run the Game:

bash
Copy
Edit
python Quickfingers.py
📸 Screenshot
pgsql
Copy
Edit
Welcome to the Speed Typing Test!
Press any key to begin!

The quick brown fox jumps over the lazy dog.
WPM: 52
Do you want to continue? (Y/N):
📦 Requirements
Python 3.6+

curses (built-in)

windows-curses (for Windows)

📁 File Structure
bash
Copy
Edit
Quickfingers/
│
├── Quickfingers.py      # Main game logic
├── text.txt             # Input file with sentences
└── README.md            # Project description
🧠 Concepts Used
Python curses for terminal UI

Non-blocking key input (nodelay)

Real-time input comparison and display

File handling and random selection

WPM formula based on typing time

✨ Future Improvements
Add difficulty levels

Store high scores

Track average WPM

Export results to a file

🤝 Contributing
Pull requests are welcome! Feel free to fork the repo, improve it, and submit a PR.

📜 License
This project is open-source and available under the MIT License.

