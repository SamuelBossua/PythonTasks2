pass_count = 0
fail_count = 0

for student in range(1, 16):
    score = int(input(f"Enter score for student {student}: "))

    if score >= 45:
        pass_count += 1
    else:
        fail_count += 1

print("Number of students that passed:", pass_count)
print("Number of students that failed:", fail_count)