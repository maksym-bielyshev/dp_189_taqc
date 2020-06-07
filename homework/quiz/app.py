import inspect

"""The program for conducting the quiz and saving the results."""

import os
from datetime import datetime



def run_section():
    """Run section and write down results."""
    name_section = next(new_section)
    with open(f"{path_to_quizzes}"
              f"{user_chosen_quiz}/{name_section}", "r") as section, \
            open(f"{path_to_quizzes}answers.txt", "a") as answers, \
            open(f"{path_to_quizzes}time.txt", "a") as time:

        def line_generator(file):
            for line in file:
                yield line

        line = line_generator(section)

        # section.readline()

        start_section_time = datetime.now()

        while True:
            try:
                question = next(line).strip()
                print(question)
                user_answer = input('Your answer: ').strip()
                question_answer = f"{question} : {user_answer} \n"
                answers.write(f"{question_answer}")
            except:
                break

        end_section_time = datetime.now()
        section_duration = (end_section_time - start_section_time)
        time.write(f"{name_section} : {section_duration}\n")


if __name__ == "__main__":
    path_to_quizzes = input("Hello! Please enter the path to the quizzes:")

    list_subdirectories = [item for item in os.walk(path_to_quizzes)][0][1]

    dict_quizzes = {index: list_subdirectories[index] for index in
                    range(0, len(list_subdirectories)) if
                    list_subdirectories[index] != '__pycache__'}

    user_chosen_quiz = dict_quizzes.get(
        int(input(f"Please enter the number of quiz: {dict_quizzes}")))

    quiz_directory = f'{path_to_quizzes}{user_chosen_quiz}'

    files = os.listdir(quiz_directory)

    sections = {index: files[index] for index in range(0, len(files))}

    def section_generator(sections):
        """Get the next section of the quiz.

        :param sections:
        :return: next list item
        """
        for section in sections:
            yield section

    new_section = section_generator(sections)

    def run_quiz():
        """Run all sections from the directory one by one.

        :return: next quiz
        """
        for item in sections:

            run_section()

    start_quiz_time = datetime.now()
    run_quiz()
    end_quiz_time = datetime.now()
    quiz_duration = f"Total time for '{user_chosen_quiz}': " \
                    f"{(end_quiz_time - start_quiz_time)}"

    with open(f"{path_to_quizzes}time.txt", "a") as time:
        time.write(f"{quiz_duration}\n")

    print("Thank you, your answers and time of the quiz are recorded.")
