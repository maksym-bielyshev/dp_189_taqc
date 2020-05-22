import math


def task_time_borders():
    best_case_estimate = float(input('best-case estimate: '))
    most_likely_estimate = float(input('most-likely estimate: '))
    worst_case_estimate = float(input('worst-case estimate: '))
    return best_case_estimate, most_likely_estimate, worst_case_estimate


estimated_tasks = []
standard_deviation_tasks = []


def sd_project():
    quadra_list = []
    for i in standard_deviation_tasks:
        quadra_list.append(pow(i, 2))
        # quadra_list.append(i ** 2)
    print(math.sqrt(sum(quadra_list)))


sd_project()


def task_estimation(best_case_estimate, most_likely_estimate, worst_case_estimate):
    return (best_case_estimate+4 * most_likely_estimate + worst_case_estimate)/6


def task_standard_deviation(best_case_estimate, most_likely_estimate, worst_case_estimate):
    return (worst_case_estimate-best_case_estimate)/6


def flow():
    while True:
        task = task_time_borders()
        estimated_tasks.append(task_estimation(*task))
        standard_deviation_tasks.append(task_standard_deviation(*task))

        answer = input('Do you want to add another task? y/n: ').lower()
        if answer != 'y':

            print(estimated_tasks)
            print(sum(estimated_tasks))

            print(standard_deviation_tasks)
            print(sum(standard_deviation_tasks))
            break


if __name__ == '__main__':
    flow()
