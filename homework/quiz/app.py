from datetime import datetime


def quiz():
    input('Choose ')
    file = open("test.txt", "r")

    start_quiz_time = datetime.today()
    print(start_quiz_time)

    for line in file:
        text = line.split("?")
        question = text[0]
        right_answer = text[1]
        print(question)

        answer = input("Enter the answer: ")

        if answer == right_answer.strip():
            print("correct")
        else:
            print("incorrect")

        recording = open("test_recording.txt", "a")
        recording.write(f"{question} : {answer} \n")
        recording.close()

    end_quiz_time = datetime.today()
    how_long = end_quiz_time - start_quiz_time
    current_date_time = datetime.now().strftime("%d-%m-%Y %H:%M")
    time_recording = open("time_recording.txt", "a")
    time_recording.write(f"{current_date_time} test quiz took:  {how_long} \n")
    time_recording.close()


if __name__ == "__main__":
    quiz()
