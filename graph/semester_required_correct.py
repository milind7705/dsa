num_courses = 8
prereqs = [[1, 3], [2, 3], [3, 5], [4, 6], [5, 6], [6, 7], [7, 8]]

# TODO: this solution considers cyclic dependency
# Key is to first create dag and initiate the in_degree list which will track deps for second course
# now add the no deps course to queue and iterate all of the queue
# inside the queue iterate the neighbor and set the counters accordingly


def build_dag(num_courses, prereqs):
    graph = {}
    in_degrees = [0] * (num_courses + 1)

    for course in range(1, num_courses + 1):
        graph[course] = []

    for preq in prereqs:
        course1, course2 = preq
        graph[course1].append(course2)
        in_degrees[course2] += 1

    return graph, in_degrees


def semester_required(num_courses, prereqs):
    graph, in_degrees = build_dag(num_courses, prereqs)

    # use bfs and add in_degrees
    queue = [i for i in range(1, num_courses + 1) if in_degrees[i] == 0]
    semester = 0
    courses_taken = 0
    print(graph)
    print(queue)
    while len(queue) > 0:
        semester += 1
        for _ in range(len(queue)):
            current = queue.pop(0)
            courses_taken += 1
            for neighbor in graph[current]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
    return semester if courses_taken == num_courses else -1


print(semester_required(num_courses, prereqs))
