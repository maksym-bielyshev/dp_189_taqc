from homework.threepoint.oop.models import Project, Task


def user_estimation():
    best_case_estimate = int(input("Best-case estimate: "))
    most_likely_estimate = int(input("Most-likely estimate: "))
    worst_case_estimate = int(input("Worst-case estimate: "))
    return best_case_estimate, most_likely_estimate, worst_case_estimate


def console():
    while True:
        estimated_tasks = []
        standard_deviation_tasks = []

        user_input = user_estimation()
        task = Task(*user_input)

        estimated_tasks.append(task.calculate_task_estimation())
        print("E(task) (estimation for each task): ", estimated_tasks)

        standard_deviation_tasks.append(
            task.calculate_task_standard_deviation())
        print("SD(task) (standard deviation for each task): ",
              standard_deviation_tasks)

        answer = input("Do you want to add another task? y/n: ").lower()
        if answer != "y":
            project = Project(estimated_tasks, standard_deviation_tasks)

            expected_value_project = project.calculate_expected_value_project()
            print(f"E(project)(expected value for project): "
                  f"{expected_value_project}")

            standard_error_project = project.calculate_standard_error_project()
            print(f"SE(project)(standard error for project): "
                  f"{standard_error_project}")

            confidence_interval_project = \
                Project.calculate_confidence_interval(expected_value_project,
                                                      standard_error_project)

            print(confidence_interval_project)
            break


if __name__ == "__main__":
    console()
