import spacy           # For natural language processing (tokenization, etc.)
import operator        # For mapping operator words to Python functions
from word2number import w2n  # For converting number words to integers

# Load the small English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Dictionary mapping math keywords to their corresponding Python operator functions
ops = {
    "plus": operator.add,
    "add": operator.add,
    "added": operator.add,
    "minus": operator.sub,
    "subtract": operator.sub,
    "subtracted": operator.sub,
    "times": operator.mul,
    "multiplied": operator.mul,
    "divide": operator.truediv,
    "divided": operator.truediv,
    "over": operator.truediv
}

# List of all math keywords for quick lookup
math_keywords = list(ops.keys())

def main():
    """Main loop for the math assistant chatbot."""
    print("👋 Hello! I'm your math assistant. Ask me a question like 'what is twenty over two plus two'.")

    while True:
        prompt = input("\nWhat's on your mind? ")
        try:
            # Parse, convert, and evaluate the user's input
            answer = evaluate(convert(parse_input(prompt)))
            print(f"🧠 The answer is: {answer}")
        except Exception as e:
            print(f"⚠️ Oops! I couldn't understand that. ({e})")

        # Ask if the user wants to continue
        resume = input("Do you have another question? (yes/no): ").strip().lower()
        if resume in ("no", "n"):
            print("👋 Alright, that was CS50")
            break

def parse_input(text):
    """
    Tokenize the input text and extract only math keywords and numbers.
    Returns a list of relevant tokens.
    """
    doc = nlp(text)
    tokens = [token.text for token in doc if token.text in math_keywords or token.like_num]
    return combine_number_words(tokens)

def combine_number_words(words):
    """
    Combine consecutive number words into single strings for conversion.
    For example, ['twenty', 'five', 'plus', 'two'] -> ['twenty five', 'plus', 'two']
    """
    if not words:
        return []

    if words[0] in math_keywords:
        # If the first word is an operator, keep it and process the rest
        return [words[0]] + combine_number_words(words[1:])

    # Build the longest chunk of number words
    number_chunk = []
    i = 0
    while i < len(words) and words[i] not in math_keywords:
        number_chunk.append(words[i])
        i += 1

    # Join the chunk and process the rest recursively
    return [" ".join(number_chunk)] + combine_number_words(words[i:])

def convert(tokens):
    """
    Convert number words to integers using word2number.
    Operators remain as strings.
    """
    for i, token in enumerate(tokens):
        try:
            tokens[i] = w2n.word_to_num(token)
        except Exception:
            pass  # Leave operators and unconvertible tokens as is
    return tokens

def evaluate(expression):
    """
    Evaluate the expression list, respecting operator precedence:
    - First, process multiplication and division (left to right)
    - Then, process addition and subtraction (left to right)
    """
    # First, process all multiplication and division
    i = 0
    while i < len(expression):
        if isinstance(expression[i], str) and expression[i] in ("times", "multiplied", "divide", "divided", "over"):
            op = expression[i]
            a = expression[i - 1]
            b = expression[i + 1]
            result = ops[op](a, b)
            # Replace a op b with result in the list
            expression = expression[:i - 1] + [result] + expression[i + 2:]
            i -= 1  # Stay at the same index for next pass
        else:
            i += 1

    # Then, process all addition and subtraction
    i = 0
    while i < len(expression):
        if isinstance(expression[i], str) and expression[i] in ("plus", "add", "added", "minus", "subtract", "subtracted"):
            op = expression[i]
            a = expression[i - 1]
            b = expression[i + 1]
            result = ops[op](a, b)
            expression = expression[:i - 1] + [result] + expression[i + 2:]
            i -= 1
        else:
            i += 1

    # The final result is the only item left in the list
    return expression[0]

if __name__ == "__main__":
    main()
