# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
What immediately stood out was the inconsistent ranges and attempts allowed for the difficulty ranges, the guesses allowed that were outside of the accepted range, and the incorrect hint. For the first bug I expected the ranges to increase as the difficulty increased and the attempts to decrease as the difficulty increased. For the guesses I expected an error to appear if a value fell outside of the high and low range. For the hint, I expected it to guide you closer to the number, but it kept guiding you incorrectly by telling you "go lower" or "go higher" in the wrong moments.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I utilized claude code for this project. One example of an AI suggestion that was correct was the suggestion that was made to modify the parse_guess function to validate if a value falls within the current range. It suggested that I include a check for if the value is less than low or greater than high. I validated this by running the game and checking with invalid inputs, as well as creating pytests. I received one incorrect suggestion where the AI indicated that the streamlit had a function named st.form() that basically batches all the widget changes and only submits when the form button is pressed. This function was supposed to fix a bug where the history does not append the most recently submitted guess, however after implementing this function the bug stayed the same. I verified this by running the game again and testing with verious inputs.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I came up with a set of test cases that I can test in both pytest and the actual game and confirmed the correct behavior. I ran the test for values outside of the allowed ranges manually and in pytest. It showed me that there are many edge cases that must be considered to confirm good logic design. AI mainly helped me understand why the issue was present and the different areas in which I could create a solution. After considering all the possible solutions, I went with the one I felt was the cleanest.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.