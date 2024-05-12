print("Please input subject scores of a student and compute the average score.")

# Initialize the total score and the number of subjects
total_score = 0

# Ask for the number of subjects
num_subjects = int(input("Input the number of subjects: "))

# Start the loop for inputting scores
current_subject = 1
while current_subject <= num_subjects:
    score = int(input("Input the score of subject {}: ".format(current_subject)))

    if score < 0:
        print("You input a negative score. Please input again!")
    else:
        total_score += score
        current_subject += 1

average_score = total_score / num_subjects

print("The average score is {} / {} = {}.".format(total_score, num_subjects, average_score))
