# Examination Question Difficulty and Performance Analysis

# Correct answer key
answer_key = ["A", "B", "C", "D", "A"]

# Student answers
students = {
    "Student 1": ["A", "B", "C", "D", "A"],
    "Student 2": ["A", "C", "C", "B", "A"],
    "Student 3": ["B", "B", "C", "D", "C"],
    "Student 4": ["A", "B", "D", "D", "A"]
}

total_questions = len(answer_key)
correct_counts = [0] * total_questions

print("EXAMINATION PERFORMANCE ANALYSIS")
print("--------------------------------")

# Calculate each student's score
for name, answers in students.items():
    score = 0

    for i in range(total_questions):
        if answers[i] == answer_key[i]:
            score += 1
            correct_counts[i] += 1

    percentage = (score / total_questions) * 100

    print("\n", name)
    print("Correct Answers:", score)
    print("Percentage:", percentage, "%")

# Analyze question-wise performance
print("\nQUESTION-WISE ANALYSIS")
print("----------------------")

for i in range(total_questions):
    success_rate = (correct_counts[i] / len(students)) * 100
    missed = len(students) - correct_counts[i]

    print("Question", i + 1)
    print("Success Rate:", success_rate, "%")
    print("Students Who Missed:", missed)

    if success_rate >= 75:
        print("Classification: Easy")
    elif success_rate >= 50:
        print("Classification: Moderate")
    else:
        print("Classification: Difficult")

# Find the most frequently missed questions
maximum_missed = max(
    len(students) - count for count in correct_counts
)

print("\nMOST FREQUENTLY MISSED QUESTIONS:")

for i in range(total_questions):
    missed = len(students) - correct_counts[i]

    if missed == maximum_missed:
        print("Question", i + 1, "-", missed, "students missed it")
