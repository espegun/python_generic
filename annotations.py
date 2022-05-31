import time
from dataclasses import dataclass


@dataclass
class Point:
    lat: float
    long: float

def locate(latitude: float, longitude: float) -> Point:
    """
    Find an object in the map by it's coordinates.
    """

    return Point(lat=latitude, long=longitude)

# Alternative annotation
Seconds = float
def launch_task(delay: Seconds) -> None:
    
    time.sleep(delay)
    print("Launching task!")


if __name__ == "__main__":

    print(locate.__annotations__)
    p = locate(56.1, 10)
    print(p)
    launch_task(1.2)
