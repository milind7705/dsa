# Write a function, semesters_required, that takes in a number of courses (n)
# and a list of prerequisites as arguments.
# Courses have ids ranging from 0 through n - 1.
# A single prerequisite of (A, B) means that course A must be taken before course B.
# Return the minimum number of semesters required to complete all n courses.
# There is no limit on how many courses you can take in a single semester,
# as long the prerequisites of a course are satisfied before taking it.
#
# Note that given prerequisite (A, B),
# you cannot take course A and course B concurrently in the same semester.
# You must take A in some semester before B.
#
# You can assume that it is possible to eventually complete all courses.
# TODO this is tricky problem so understand the examples first with the help of drawing graph
# num_courses = 6
# prereqs = [
#   (1, 2),
#   (2, 4),
#   (3, 5),
#   (0, 5),
# ]
# semesters_required(num_courses, prereqs) # -> 3

# Graph:
# 1 -> 2 -> 4
# 3 -> 5
# 0 -> 5
# Semester 1 : 0, 1, 3
# Semester 2: 2, 5
# Semester 3: 4

# Another example:
# num_courses = 7
# prereqs = [
#   (4, 3),
#   (3, 2),
#   (2, 1),
#   (1, 0),
#   (5, 2),
#   (5, 6),
# ]
# semesters_required(num_courses, prereqs) # -> 5

# Graph: 4-> 3 -> 2 -> 1 -> 0
#         5-> 2
#         5 -> 6
# Semester 1: 4, 5
# Semester 2: 3, 6
# Semester 3: 2
# Semester 4: 1
# Semester 5: 0

#
# num_courses = 7
# prereqs = [
#     (4, 3),
#     (3, 2),
#     (2, 1),
#     (1, 0),
#     (5, 2),
#     (5, 6),
# ]

num_courses = 3
prereqs = [[1, 2], [2, 3], [3, 1]]


def build_directed_acyclic_graph(num_courses, prereqs):
    graph = {}
    for course in range(1, num_courses + 1):
        if course not in graph:
            graph[course] = []
    for prereq in prereqs:
        course1, course2 = prereq
        graph[course1].append(course2)
    return graph


def semesters_required(num_courses, prereqs):
    graph = build_directed_acyclic_graph(num_courses, prereqs)
    print(graph)
    # dictionary to store number of semester required for each course
    num_of_semester = {}

    # initialize it with the course having no dependency
    for course in graph:
        if graph[course] == []:
            num_of_semester[course] = 1

    print(num_of_semester)
    # now do a depth first traversal of this acyclic graph

    for course in graph:
        get_semester_required(course, graph, num_of_semester)
    print(num_of_semester)
    return max(num_of_semester.values())


def get_semester_required(course, graph, num_of_semester):
    # initial check if the course is already calculated retur
    if course in num_of_semester:
        return num_of_semester[course]

    maximum = 0
    for neighbor in graph[course]:
        temp_max = get_semester_required(neighbor, graph, num_of_semester)
        if temp_max > maximum:
            maximum = temp_max

    num_of_semester[course] = 1 + maximum
    return num_of_semester[course]


print(semesters_required(num_courses, prereqs))  # -> 5
