# Les også: https://medium.datadriveninvestor.com/mutable-and-immutable-python-2093deeac8d9

class MutableObj:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"The value is {self.value}."

mut1 = MutableObj(value="a")
print(mut1)
mut2 = mut1
mut2.value = "b"  # The new reference is used to change the object.
print(mut1, mut2)
del mut1  # Deletes only the reference, not the object.
print(mut2)  #
del mut2  # Deletes the last reference. The Garbage collector deletes the object.