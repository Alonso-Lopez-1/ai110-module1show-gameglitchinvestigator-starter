# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose:** A number guessing game where the player tries to guess a randomly chosen secret number, receiving higher/lower hints until they guess correctly.

- [x] **Detail which bugs you found:**
  1. The secret number reset on every button click because it wasn't stored in `session_state`.
  2. Invalid guesses still counted as an attempt because the increment wasn't inside the valid-guess block.
  3. The secret was converted to a string before comparison, so guesses never matched.

- [x] **Explain what fixes you applied:**
  1. Initialized the secret once using `if "secret" not in st.session_state`, so it persists across reruns.
  2. Moved `attempts += 1` inside the `else` block so only valid guesses consume an attempt.
  3. Removed the `str()` conversion and compared `guess_int` directly to the integer secret.


## 📸 Demo

- [ ] [![Alt text]("C:\Users\19092\Pictures\Screenshots\Screenshot 2026-03-14 222002.png")
]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
