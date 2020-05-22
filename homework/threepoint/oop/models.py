import math


class Project:
    def __init__(self, estimated_tasks, standard_deviation_tasks):
        self.estimated_tasks = estimated_tasks
        self.standard_deviation_tasks = standard_deviation_tasks

    def calculate_expected_value_project(self):
        return sum(self.estimated_tasks)

    def calculate_standard_error_project(self):
        squared_list = []
        for i in self.standard_deviation_tasks:
            squared_list.append(pow(i, 2))
        return math.sqrt(sum(squared_list))

    @staticmethod
    def calculate_confidence_interval(expected_value_project, standard_error_project):
        min_confidence_interval = expected_value_project - 2 * standard_error_project
        max_confidence_interval = expected_value_project + 2 * standard_error_project
        return f"CI (confidence interval for project): {min_confidence_interval} ... {max_confidence_interval} points"


class Task:
    def __init__(self, best_case_estimate, most_likely_estimate, worst_case_estimate):
        self.best_case_estimate = best_case_estimate
        self.most_likely_estimate = most_likely_estimate
        self.worst_case_estimate = worst_case_estimate

    def calculate_task_estimation(self):
        return (self.best_case_estimate + 4 * self.most_likely_estimate + self.worst_case_estimate) / 6

    def calculate_task_standard_deviation(self):
        return (self.worst_case_estimate - self.best_case_estimate)/6