'''
Input:
    - First line contains an integer 1 <= C <= 50, the number of
      test cases.
    - Rest of lines are C data sets.

    - Each data set begins with an integer 1 <= N <= 100, the
      number of people in the class.
    - The rest of the line consists of N final grades.

Output:
    - For each test case C, output a line giving the percentage
      of students whose grade is above average, rounded to exactly
      3 decimal places.
'''
def get_grades():
    import sys
    data = [i for i in sys.stdin]
    raw_data_sets = [line.split()[1:] for line in data[1:]]
    grades = []
    for data_set in raw_data_sets:
        grades.append([int(n) for n in data_set])
    return grades

def get_average(grades):
    return sum(grades) / len(grades)

def num_above_average(grades):
    avg_grade = get_average(grades)
    return len([grade for grade in grades if grade > avg_grade])

def percentage_above_average(grades):
    return (num_above_average(grades) / len(grades)) * 100

def main():
    grade_data_sets = get_grades()
    for grades in grade_data_sets:
        print("%.3f%%" % percentage_above_average(grades))

if __name__ == '__main__':
    main()
