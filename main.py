# Grade Calculator

# Takes a list of scores, calculates the average, and returns the average.
def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average


# Takes an average score and returns the letter grade.
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Dictionary to store the information about the grades
grade_info = {
    "student": "",
    "scores": []
}

grade_info["student"] = input("Enter your name: ")

print(f"\nGrade Calculator for {grade_info['student']}")

while True:
    score_input = input("Enter a score (or type 'done' to finish): ")

    if score_input.lower() == "done":
        break
    elif score_input.isdigit():
        score = int(score_input)

        if score >= 0 and score <= 100:
            grade_info["scores"].append(score)
        else:
            print(f"{score} is not a valid score. Enter a score from 0 to 100.")
    else:
        print(f"{score_input} is not a valid number. Please try again.")

if len(grade_info["scores"]) > 0:
    scores = grade_info["scores"]

    average = calculate_average(scores)
    scores.sort()

    highest = scores[-1]
    lowest = scores[0]
    letter_grade = get_letter_grade(average)

    print("\n----- Results -----")
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Letter grade: {letter_grade}")
else:
    print("No scores were entered.")