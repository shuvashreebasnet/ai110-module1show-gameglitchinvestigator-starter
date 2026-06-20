# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
There was a drop down tab titled Developer Debug Info that contained attempt, score and difficulty data. There was also a text box and 2 buttons Submit Guess and New Game, and a checkbox to show hint.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  When I pressed Enter, the guess did not submit, even though the text box indicates to press Enter to submit. 
  When I clicked New Game after getting the correct answer, I was unable to interact with either button and could not submit my guess. The winning label also stayed on the screen.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Click Submit | To get a hint that gives accurate information about the answer | Hint that is opposite of the direction that the player should guess to find the number | none |
| Click Submit | The score to lead to 0 | Score became a negative number | none |
| Click New Game | Attempts to restore back to 7 | Attempts was set to 8 | none |
| Click New Game | History to be reset | History from former game stayed | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
GitHub Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Input: I found that when I guessed a number higher than the secret number, the game told me to gold higher. And it told me to go lower when I did the opposite. Explain why that bug it occuring in my code

AI Suggestion: When guess > secret (your guess is too high), the function returns "Go HIGHER!" — but you should actually go LOWER. When guess < secret (your guess is too low), the function returns "Go LOWER!" — but you should actually go HIGHER......To fix the emoji messages, swap them: if guess > secret, return "Too High", "📉 Go LOWER!" else return "Too Low", "📈 Go HIGHER!". On even-numbered attempts, the secret becomes a string. Then when comparing an integer guess to a string secret, string comparison gets used (lexicographically), which doesn't work correctly for numbers. This adds another layer of glitchiness to the game. The identification and suggestion were both correct. The status labels ("Too High" / "Too Low") are correct, but the hint messages are backwards.
*When I asked to create a commit message of a summary to the changes made:
Fix game logic bugs: reversed hint messages and type mismatch on even attempts

- Swap emoji hint messages in check_guess() to correctly guide players (📉 "Go LOWER" when guess too high, 📈 "Go HIGHER" when guess too low)
- Prevent secret number from being converted to string on even attempts, which caused incorrect comparisons
- Resolves issue where players received opposite directional hints and unpredictable behavior on alternating attempts

Verification: I asked AI to make the changes and add a comment next to each bug they fixed. I also asked AI to generate a pytest for the bug fixes (that I still need to test) and asked AI to generate a commit statment.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
