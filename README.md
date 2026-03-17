# Python Quiz Game

A simple **command-line quiz game built in Python** that asks multiple-choice questions, checks user answers, and keeps track of the final score.

This project demonstrates basic Python concepts such as:

* Functions
* Lists and dictionaries
* Loops
* Conditional statements
* User input handling

It is ideal for **Python beginners learning programming fundamentals**.

---

# Features

* Multiple-choice quiz questions
* Automatic answer checking
* Score tracking
* Final results displayed at the end
* Clean and modular code structure

---

# Project Structure

Example structure of the project:

```
quiz-game-start/
│
├── main.py
├── question_model.py
├── data.py
├── quiz_brain.py
└── README.md
```

### File Descriptions

**main.py**

* Entry point of the program
* Runs the quiz loop

**question_model.py**

* Defines the `Question` class
* Stores question text and answer

**data.py**

* Contains the quiz question data
* Usually stored as a list of dictionaries

**quiz_brain.py**

* Handles quiz logic
* Tracks score
* Checks answers
* Moves to next question

---

# Example Question Format

Questions are typically stored like this:

```python
question_data = [
    {
        "text": "The sky is blue.",
        "answer": "True"
    },
    {
        "text": "2 + 2 = 5.",
        "answer": "False"
    }
]
```

---

# How the Game Works

1. Questions are loaded from the data file
2. Each question is converted into a `Question` object
3. The quiz asks questions one by one
4. User inputs **True** or **False**
5. The program checks the answer
6. The score updates
7. Final score is displayed at the end

---

# Example Gameplay

```
Q1: The sky is blue. (True/False)
True
Correct!

Q2: 2 + 2 = 5. (True/False)
False
Correct!

You completed the quiz.
Your final score: 2/2
```

---

# Requirements

You only need **Python installed**.

Recommended version:

```
Python 3.8+
```

No external libraries are required.

---

# How to Run

Clone the repository:

```
git clone https://github.com/yourusername/quiz-game-start.git
```

Navigate to the project folder:

```
cd quiz-game-start
```

Run the game:

```
python main.py
```

---

# Learning Objectives

This project helps beginners practice:

* Object-Oriented Programming
* Python modules
* Code organization
* Control flow
* User input handling

---

# Future Improvements

Possible upgrades:

* Add multiple-choice questions (A/B/C/D)
* Add timer for answering questions
* Save high scores
* GUI version using Tkinter
* Web version using Flask
* Randomized questions

---

# License

This project is open source and available under the MIT License.
