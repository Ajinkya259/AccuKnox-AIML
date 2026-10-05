import requests
import matplotlib.pyplot as plt

API_URL = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"


def fetch_students():
    response = requests.get(API_URL)
    data = response.json()

    students = []
    for item in data:
        scores = {}
        for field in item:
            if field.endswith("_score"):
                scores[field] = item[field]
        students.append(scores)
    return students


def calculate_averages(students):
    averages = {}
    for subject in students[0]:
        total = 0
        for student in students:
            total = total + student[subject]
        averages[subject] = round(total / len(students), 2)
    return averages


def calculate_overall_average(averages):
    total = 0
    for subject in averages:
        total = total + averages[subject]
    return round(total / len(averages), 2)


def show_averages(averages, overall):
    for subject in averages:
        print(subject, ":", averages[subject])
    print("Overall :", overall)


def make_chart(averages, overall):
    subjects = list(averages.keys())
    scores = list(averages.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(subjects, scores, color="steelblue")
    plt.bar_label(bars, label_type="center", color="white")
    plt.axhline(overall, color="red", linestyle="--", label=f"Overall average: {overall}")

    plt.title("Average Test Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.legend()

    plt.savefig("scores_chart.png")
    plt.show()


students = fetch_students()
print("Students:", len(students))
print("First student:", students[0])

averages = calculate_averages(students)
overall = calculate_overall_average(averages)
show_averages(averages, overall)
make_chart(averages, overall)
