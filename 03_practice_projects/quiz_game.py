questions  = ("What is the last name of Seymour from Final Fantasy X?", 
              "How many endings does Chrono Trigger have in the original version?",
              "I often think about the god who blessed us with this cryptic puzzle... and wonder if we'll ever have the chance to: " 
              "What is the name of Squall's necklace?")

options =   (("A. Strife", "B. Leonhart", "C. Guado", "D. Tribal"), 
            ("A. 12", "B. 14", "C. 8", "D. 10"), 
            ("A. Kinneas", "B. Griever", "C. Ifrit", "D. Siren"
             "A. Know him", "B. See him", "C. Kill him", "Worship him"))

answers = ("C", "A", "B", "C")
guesses = []
score = 0 
question_num = 0

for question in questions: 
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


guess = input("Enter (A, B, C, D): ").upper()
guesses.append(guess)
question_num += 1
if guess == answers[question_num]:
    score += 1 
    print("Correct!")
else:
    print("Incorrect!")    
    print(f"{answers[question_num]} is the correct answer!")
question_num += 1    