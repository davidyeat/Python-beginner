# Python Quiz Game
print("---------- Welcome to Python Quiz Game ----------")
print()
questions = ("1. If you get lost,_____________ the information desk.",
            "2. What is the _____________ for two museum tickets?",
            "3. The tour will start at _____________ 3 p.m.",
            "4. Eric _____________ his leg while running down the stairs.",
            "5. You must talk quietly in the library because it's a _____________ for study.")
options = (("A. avoid", "B. fine", "C. look for", "D. keep"),
           ("A.cost", "B.place", "C.attention", "D.crime"),
           ("A. bring", "B. stay", "C. exactly", "D. delay"),
           ("A. shut", "B. avoided", "C. followed", "D. injured"),
           ("A. crime", "B. place", "C. problem", "D. copy"))
answers = ("C", "A", "C", "D", "B")
guesses = []
score = 0
question_num = 0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Choose your answer(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1
    print()
print("---------------------------------")
print("             RESULTS             ")
print("---------------------------------")
print("Correct Answers: ", end=" ")
for correct in answers:
    print(correct, end=" ")
print()
print("Your Answers: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
