# https://medium.com/mindorks/understanding-python-dataclasses-part-1-c3ccd4355c34 - Part 1, mostly read
# https://medium.com/mindorks/understanding-python-dataclasses-part-2-660ecc11c9b8 - Part 2, not read

from dataclasses import dataclass

@dataclass  # This decorator turns the class into a dataclass, use frozen=True to set as immutable.
class A:
    """
    Example of dataclass.
    You do not have to use an __init__ method.
    """

    number1: int
    number2: int
    text1: str = "Howdy"
    

a1 = A(4, 6)
print(a1)
print("")

# Anyway - can create dataclasses from dicts and vice-versa.
d = {"text1": "Bazinga!", "number2": 10, "number1": 1}
print(d)
a2 = A(**d)

print(a2)
from dataclasses import asdict
print(asdict(a2))
print(asdict(a2) == d)  # True
print("")


        

@dataclass
class B:
    """
    dataclass with You do not have to use an __init__ method.
    """

    number1: int
    number2: int
    text1: str = "Howdy"

    #@classmethod  - TO BE DONE
    #def init_from_dict(cls, config):
    #    "A function which is bound to a class."
    #    # Mumble, mumble.. may do some initial calculations.
    #    return cls(**config)
    
b1 = B(5, -2) 
print(b1)

d = {"text1": "Bazinga!", "number2": 10, "number1": 1}
#b2 = B.init_from_dict(d)  # Magnus think @classmethod is nice. Haven't really understood why yet, hmmm...


## Remember: You can also make custom asdict methods, something like:
# def asjson(self):
#     d = asdict(self)
#     d["some_key"] = self.some_key + 10  # Overwrite
#     return d  # Evt return json.dumps(d)



print("That was fun!")

