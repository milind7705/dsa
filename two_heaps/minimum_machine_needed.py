# We are given an input array, tasks, which contains the start and end times of n tasks.
# Your task is to find the minimum number of machines required to complete these n tasks.

# Input list [(1, 1), (5, 5), (8, 8), (4, 4),(6, 6), (10, 10), (7, 7)]
# heapq.heapify: This satisfies the min-heap property: every parent node is smaller than its children.
# the first value is treated as the priority for the heapify
#          (1, 1)
#        /       \
#    (4, 4)     (7, 7)
#    /   \       /   \
# (5, 5) (6, 6) (10, 10) (8, 8)
import heapq


def tasks(tasks_list):
    # to count the total number of machines for "optimal_machines" tasks
    optimal_machines = 0
    # empty list to store tasks finish time
    machines_available = []
    # converting list of set "optimal_machines" to a heap
    heapq.heapify(tasks_list)

    while tasks_list:  # looping through the tasks list
        # remove from "tasks_list" the task i with earliest start time
        task = heapq.heappop(tasks_list)

        if machines_available and task[0] >= machines_available[0][0]:
            # top element is deleted from "machines_available"
            machine_in_use = heapq.heappop(machines_available)

            # schedule task on the current machine
            machine_in_use = (task[1], machine_in_use[1])

        else:
            # if there's a conflicting task, increment the
            # counter for machines and store this task's
            # end time on heap "machines_available"
            optimal_machines += 1
            machine_in_use = (task[1], optimal_machines)

        heapq.heappush(machines_available, machine_in_use)

    # return the total number of machines used by "tasks_list" tasks
    return optimal_machines


# driver code
def main():

    # Input: A set "tasks_list" of "n" tasks, such that
    # each task has a start time and a finish time
    input_tasks_list = [[(1, 1), (5, 5), (8, 8), (4, 4),
                        (6, 6), (10, 10), (7, 7)],
                        [(1, 7), (1, 7), (1, 7),
                        (1, 7), (1, 7), (1, 7)],
                        [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)],
                        [(1, 3), (3, 5), (5, 9), (9, 12),
                        (12, 13), (13, 16), (16, 17)],
                        [(12, 13), (13, 15), (17, 20),
                        (13, 14), (19, 21), (18, 20)]]

    # loop to execute till the length of tasks
    for i in range(len(input_tasks_list)):
        print(i + 1, ".\t Tasks = ", input_tasks_list[i], sep="")

        # Output: A non-conflicting schedule of tasks in
        # "tasks_list" using the minimum number of machines
        print("\t Optimal number of machines = ",
              tasks(input_tasks_list[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
