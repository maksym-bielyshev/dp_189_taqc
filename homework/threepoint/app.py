"""The app estimates a project based on the "three points" technique."""

import math


class Project:
    """Project calculation."""

    def __init__(self,
                 estimated_tasks: list,
                 standard_deviation_tasks: list) -> None:
        """Create a project.

        :param estimated_tasks: list of estimated tasks
        :param standard_deviation_tasks: list of standard deviation tasks
        """
        self.estimated_tasks = estimated_tasks
        self.standard_deviation_tasks = standard_deviation_tasks
        self.expected_value_project = None
        self.standard_error_project = None

    def calculate_expected_value_project(self) -> object:
        """Calculate an expected value of a project.

        :return: expected value of a project
        """
        if self.expected_value_project is None:
            self.expected_value_project = sum(self.estimated_tasks)
        return self.expected_value_project

    def calculate_standard_error_project(self) -> object:
        """Calculate standard error for a project.

        :return: standard error for a project
        """
        squared_list = []
        for i in self.standard_deviation_tasks:
            squared_list.append(pow(i, 2))
        self.standard_error_project = math.sqrt(sum(squared_list))
        return self.standard_error_project

    def calculate_confidence_interval(self) -> object:
        """Calculate 95% confidence interval.

        :return: 95% confidence interval
        """
        min_confidence_interval = \
            self.expected_value_project - 2 * self.standard_error_project

        max_confidence_interval = \
            self.expected_value_project + 2 * self.standard_error_project

        return min_confidence_interval, max_confidence_interval


class Task:
    """Task calculation."""

    def __init__(self,
                 best_case_estimate: int,
                 most_likely_estimate: int,
                 worst_case_estimate: int) -> None:
        """Create a task.

        :param best_case_estimate: user best case estimation
        :param most_likely_estimate: user most likely case estimation
        :param worst_case_estimate: user worst case estimation
        """
        self.best_case_estimate = best_case_estimate
        self.most_likely_estimate = most_likely_estimate
        self.worst_case_estimate = worst_case_estimate
        self.estimation = None
        self.standard_deviation = None

    def calculate_task_estimation(self):
        """Calculate a task estimation.

        :return: task estimation
        """
        if self.estimation is None:
            self.estimation = (self.best_case_estimate
                               + self.most_likely_estimate * 4
                               + self.worst_case_estimate) / 6
        return self.estimation

    def calculate_task_standard_deviation(self):
        """Calculate standard deviation for a task.

        :return: standard deviation for a task
        """
        if self.standard_deviation is None:
            self.standard_deviation = \
                (self.worst_case_estimate - self.best_case_estimate) / 6
        return self.standard_deviation


if __name__ == "__main__":

    estimated_tasks_values = []
    standard_deviation_tasks_values = []

    run_app = "y"
    while run_app == "y":

        best_case_estimate_str = input("Best-case estimate: ")
        most_likely_estimate_str = input("Most-likely estimate: ")
        worst_case_estimate_str = input("Worst-case estimate: ")

        try:
            best_case_estimate_int = int(best_case_estimate_str)
            most_likely_estimate_int = int(best_case_estimate_str)
            worst_case_estimate_int = int(best_case_estimate_str)

        except ValueError:
            print("Please enter valid data!")

        else:
            task = Task(best_case_estimate_int,
                        most_likely_estimate_int,
                        worst_case_estimate_int)

            task_estimation = task.calculate_task_estimation()
            estimated_tasks_values.append(task_estimation)

            standard_deviation_task = task.calculate_task_standard_deviation()
            standard_deviation_tasks_values.append(standard_deviation_task)

        answer = input("Do you want to add another task? y/n: ").lower()

        if answer != "y":
            project = Project(estimated_tasks_values,
                              standard_deviation_tasks_values)

            project.calculate_expected_value_project()
            project.calculate_standard_error_project()

            result_min_confidence_interval, result_max_confidence_interval = \
                project.calculate_confidence_interval()

            print(f"CI (confidence interval for project): "
                  f"{result_min_confidence_interval} ... "
                  f"{result_max_confidence_interval} points")

            run_app = input(
                "Do you want to calculate another project? y/n: ").lower()
