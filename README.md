# Natural Language Calculator

#### Video Demo:  <https://www.youtube.com/watch?v=FZ3ahccp4t4>

#### Description:
> ⚠️ *The following description was generated with the assistance of AI (ChatGPT) to help clearly communicate the project’s purpose. All code and implementation are my own.*


This project is a natural language-based calculator built using Python. The idea is simple: instead of typing mathematical expressions like `5 + 2 * 3`, the user can input a phrase like “what is five plus two times three,” and the program will parse the language, extract the intent, and return the correct numerical result while respecting order of operations.

It is designed to be interactive, beginner-friendly, and capable of parsing spoken-style math queries. The project makes use of basic natural language processing techniques to convert word-based numbers into integers, identify arithmetic operations, and compute results accordingly.

This project was developed as the final project for CS50’s Introduction to Programming with Python. It includes parsing logic, natural language token handling, and operator precedence.

---

### How It Works

1. **Text Input**: The user provides a natural language question like:
   _"What is fifty two divided by two plus one?"_

2. **Parsing**:
   The `parse_input` function uses the `spaCy` NLP library to tokenize the input sentence and filter out irrelevant words. It only keeps math-related keywords and number-like tokens.

3. **Combining Number Words**:
   Sometimes numbers are written across multiple words (e.g., "twenty five"). The `combine_number_words` function uses recursion to group adjacent number words into a single string, like `"twenty five"`.

4. **Conversion to Integers**:
   The `convert` function uses the `word2number` library to convert number words into actual integers (`25`, `3`, etc.).

5. **Evaluation**:
   The `evaluate` function walks through the list of numbers and operations, and performs arithmetic in proper order:
   - Multiplication and division come first.
   - Then addition and subtraction.
   - Python’s `operator` module is used to map string operations (like `"plus"`) to actual math functions.

---

### File Overview

- `project.py`:
  - Contains all of the program logic.
  - Includes five main functions:
    - `main()` — handles user interaction.
    - `parse_input()` — filters relevant tokens using spaCy.
    - `combine_number_words()` — recursively groups number words.
    - `convert()` — converts strings like `"twenty"` into `20`.
    - `evaluate()` — processes the expression based on operator precedence.

- `test_project.py`:
  - Includes unit tests for each function using `pytest`.
  - Covers edge cases like single-word numbers, multiple operations, and operator ordering.

---

### Design Decisions

One major design choice was to avoid complex grammar parsing and instead rely on token filtering and recursive number grouping. This made the logic simpler and easier to test. I also handled operator precedence manually using two passes: first for multiplication/division, then for addition/subtraction.

The decision to use `spaCy` instead of regular expressions was made to allow easier extension in the future (e.g., parsing longer phrases or detecting intent).

To keep the project clear and readable, every function is documented and modular. Although the program doesn't support parentheses or very large numbers ("five thousand two hundred and sixteen"), it could easily be extended.

---

### Notes on Academic Honesty

This project was built with guidance from the CS50 course, and assistance from AI (ChatGPT) was used to debug and explain concepts throughout development. All code was written and understood by me, and any external libraries are credited.

---

### Future Improvements

Some possible future enhancements include:
- Support for negative numbers and decimals.
- Handling parentheses and more complex expressions.
- Voice input support or a GUI.

---

### Conclusion

This natural language calculator combines basic NLP and arithmetic logic to create an intuitive experience for users who want to perform math with words. It reflects my understanding of parsing, tokenization, function design, and control flow, and showcases my ability to break down a problem and build a solution step by step.
