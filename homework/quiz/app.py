import os
from contextlib import contextmanager
from datetime import datetime


@contextmanager
def current_file(filename, mode):
    curr_file = open(filename, mode)
    try:
        print(f"{filename} is ready to use.")
        yield curr_file
    finally:
        curr_file.close()


def play_section():
    name_section = next(new_section)
    with current_file(f"{path_to_program}"
                      f"{user_chosen_quiz}/{name_section}", "r") as section, \
            current_file(f"{path_to_program}answers.txt", "a") as answers, \
            current_file(f"{path_to_program}time.txt", "a") as time:

        def line_generator(file):
            for line in file:
                yield line

        line = line_generator(section)

        start_section_time = datetime.now()

        while True:
            try:
                question = next(line).strip()
                print(question)
                user_answer = input('enter the answer: ').strip()
                question_answer = f"{question} : {user_answer} \n"
                answers.write(f"{question_answer}")
            except:
                break

        end_section_time = datetime.now()
        section_duration = (end_section_time - start_section_time)
        time.write(f"{name_section} : {section_duration}\n")


if __name__ == "__main__":
    path_to_program = 'C:/Users/Maksym/Documents/dp-189-taqc/homework/quiz/'
    list_subdirectories = [i for i in os.walk(path_to_program)][0][1]
    print(list_subdirectories)

    dict_quizzes = {i: list_subdirectories[i] for i in
                    range(0, len(list_subdirectories)) if
                    list_subdirectories[i] != '__pycache__'}
    print(dict_quizzes)

    user_chosen_quiz = dict_quizzes.get(
        int(input(f"Hello! Please enter the number of quiz: {dict_quizzes}")))

    quiz_directory = f'{path_to_program}{user_chosen_quiz}'

    files = os.listdir(quiz_directory)
    print(files)

    sections = {i: files[i] for i in range(0, len(files))}


    def section_generator(list):
        for item in list:
            yield item

    new_section = section_generator(files)

    start_quiz_time = datetime.now()

    for item in files:
        user_input = input("Start a new section? y/n").lower()
        if user_input == 'y':
            play_section()
        else:
            print("Goodbye!")
            break
    print("The end of the program.")

    end_quiz_time = datetime.now()

    quiz_duration = (end_quiz_time - start_quiz_time)

    with current_file(f"{path_to_program}time.txt", "a") as time:
        time.write(f"{quiz_duration}\n")
