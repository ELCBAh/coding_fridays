#!/usr/bin/python3
"""
AUTHOR: SEBASTIAN MAIDANA

+* Coding friday challenge suggested by jvalenzani-hbtn *+

https://github.com/jvalenzani-hbtn/

Student Grades
==============

Reads a list of students from a .csv file (student_name, grade)
and outputs a JSON file containing; Highest Score, Lowest Score,
Total Number of Students, Average Score, and a list of students
sorted by their grade.

"""
import json


def main():
    """
    Main function that first splits input file data (comma as divisor).
    Processes the data and stores it in a dictionary with student names
    as keys and grades as values. Then, sorts the dictionary and stores
    the sorted dictionary in a JSON file.
    """
    students = {}
    with open("input.csv", "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            students[line[0]] = int(line[1])

    sorted_students = sorted(
        students.items(), key=lambda x: x[1], reverse=True)
    highest_score = sorted_students[0][1]
    lowest_score = sorted_students[-1][1]
    total_students = len(sorted_students)
    average_score = sum(students.values()) / len(students)

    output = {
        "high_score": highest_score,
        "low_score": lowest_score,
        "total_students": total_students,
        "avg_score": average_score,
        "students": sorted_students
    }

    with open("output.json", "w") as file:
        json.dump(output, file)


if __name__ == "__main__":
    main()
