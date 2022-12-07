class MyBaseClass:

    def __init__(self, string):

        self.string = string

    def get_string(self):

        return self.string * self.get_multiplier()

    def get_multiplier(self):

        return 1    


class MySubClass(MyBaseClass):

    def __init__(self, string: str, multiplier: int):

        self.multiplier = multiplier
        super().__init__(string)

    def get_multiplier(self):
        
        """
        Overwriting the method in the base class,
        also when calling method is in the base class.
        This is because they have been incorporated into one class.
        """

        return self.multiplier

bc = MyBaseClass("A")
print(bc.get_string())
sc = MySubClass("B", 3)
print(sc.get_string())
