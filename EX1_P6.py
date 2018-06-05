# Lucas Hanson - Exam 1 - Problem 6

Course = []
Grade = []

N = int(input("Enter in the number of courses taken last semester: "))

for i in range(N):
    Course.append(input("Enter course name: "))
    Grade.append(int(input("Enter corresponding course grade: ")))

print("REPORT CARD:")
for j in range(N):
    print(Course[j] + " - " + str(Grade[j]))

sum = 0
for k in range(N):
    sum = sum + Grade[k]

avg = sum / N

print("Average grade - ",avg)


