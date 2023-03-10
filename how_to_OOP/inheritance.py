import typing
import datetime
from abc import ABC, abstractmethod

class TestStep(ABC):

    """
    ABC = Abstract Base Class
    """

    def __init__(self, name):

        self.name = name

    def summarize_results(self, result_string: str) -> dict:

        return {"name": self.name,
                "timestamp": datetime.datetime.now(),
                "results_string": result_string
                }

    @abstractmethod  # Must be overwritten
    def run(self):
        pass

class TestStepSSHCommand(TestStep):

    def __init__(self, name: str):

        pass


class TestStepCustomFunction(TestStep):

    def __init__(self, name: str, function: typing.Callable):

        self.function = function
        super().__init__(name)
        
    def run(self, arg):

        # Overriding abstract method
        results_string = self.function(arg)
        return self.summarize_results(result_string=results_string)


if __name__ == "__main__":

    try:
        TestStep(name="Abstract class")
    except TypeError as e:
        print(e)

    try:
        TestStepSSHCommand(name="Not overwritten abstract method.")
    except TypeError as e:
        print(e)
    
    tscf = TestStepCustomFunction(name="Should work", function=lambda x: x*2)
    results = tscf.run("ABCD")
    print(results)

    print("That was fun.")
