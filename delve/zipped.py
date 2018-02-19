''' compute the average scores of each student.

The first line contains  and  separated by a space.
The next  lines contains the space separated marks obtained by
students in a particular subject.
Sample Input:
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5  '''


def main():
    marks_list, subjects = get_student_marks()
    compute_stud_avg(marks_list, subjects)


def get_student_marks():
    # Map produces a generator object
    students, subjects = (
        map(lambda x: int(x), input('Enter no of students and '
                                    'subjects').split()))

    marks_list = []
    for i in range(subjects):
        marks = input().split()
        marks_list.append(marks)

    return marks_list, subjects


def compute_stud_avg(marks_list, subjects):
    # to generate tuples of items based on index from nested list

    for i in zip(*marks_list):
        # Compute average marks of each student
        stud_avg = sum(map(lambda x: float(x), i)) / subjects
        print(stud_avg)


if __name__ == '__main__':
    main()
