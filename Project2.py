# -------------------------------------
# Console-Based Quiz System
# Topics: Variables, Conditions, Loops, Functions, Recursion
# -------------------------------------

questions = [
    {
        "question": "What is the output of 2 + 3?",
        "options": ["A. 4", "B. 5", "C. 6", "D. 23"], 
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",  
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which loop is used when the number of iterations is unknown?",
        "options": ["A. for", "B. while", "C. do-while", "D. repeat"],
        "answer": "B"
    },
    {
        "question": "What is the data type of 5.5?",
        "options": ["A. int", "B. float", "C. double", "D. string"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /* */", "C. #", "D. --"],
        "answer": "C"
    }
]


def show_menu():
    print("\n--- QUIZ SYSTEM ---")
    print("1. Start Quiz")
    print("2. Exit")


def ask_question(q):
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    answer = input("Your answer (A/B/C/D): ").upper()
    return answer   # returns user answer


def show_result(score):
    print("\n--- RESULT ---")
    print("Your Score:", score, "/", len(questions))

    if score >= 3:
        print("Status: PASS")
    else:
        print("Status: FAIL")


def retry_quiz():
    choice = input("\nDo you want to retry? (yes/no): ").lower()

    if choice == "yes":
        start_quiz()          # recursion
    elif choice == "no":
        print("Thank you for playing!")
    else:
        print("Invalid choice!")
        retry_quiz()          # recursion again


def start_quiz():             
    score = 0

    for q in questions:       
        user_answer = ask_question(q)   
        if user_answer == q["answer"]:
            score += 1

    show_result(score)
    retry_quiz()


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            start_quiz()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")


main()
