from abc import ABC, abstractmethod


class Action(ABC):
    @abstractmethod
    def do(self):
        pass


# several implementation
class RepeatableAction(Action):
    def __init__(self, times):
        self._times = times

    def do(self):
        for _ in range(self._times):
            print("do something")


class ComplicatedAction(Action):
    def __init__(self, times):
        self._action = RepeatableAction(times)

    def do(self):
        print("complicated flow starts")
        self._action.do()
        print("complicated flow ends")


class ComplexAction(Action):
    def __init__(self):
        self._action = ComplicatedAction(3)

    def do(self):
        print("super complex flow")
        self._action.do()


# run several actions
for action in (
        ComplexAction(),
        ComplicatedAction(1),
        ComplexAction(),
        RepeatableAction(5)
):
    print("<<< next action >>>")
    action.do()
