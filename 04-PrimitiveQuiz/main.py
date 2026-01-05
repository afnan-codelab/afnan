def main():
    questions = {
        "What is the capital of France?": "paris",
        "What is the capital of Germany?": "berlin",
        "What is the capital of Italy?": "rome",
        "What is the capital of Spain?": "madrid",
        "What is the capital of Portugal?": "lisbon",
        "What is the capital of Belgium?": "brussels",
        "What is the capital of Netherlands?": "amsterdam",
        "What is the capital of Austria?": "vienna",
        "What is the capital of Greece?": "athens",
        "What is the capital of Switzerland?": "bern"
    }

    for question, correct_answer in questions.items():
        user_answer = input(question + " ").lower()

        if user_answer == correct_answer:
            print("Correct answer!")
        else:
            print("Wrong answer!")

if __name__ == "__main__":
    main()
