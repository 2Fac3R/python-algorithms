from typing import Awaitable, Callable, Literal, Sequence, Optional

# Type aliases - The type statement is new in Python 3.12
type Number = list[int | float]
type Vector = list[float]
type ConnectionOptions = dict[str, str]
type Address = tuple[str, int]
type Server = tuple[Address, ConnectionOptions]


def greeting(name: str) -> str:
    return f"Hello {name}"


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    pass


"""Annotating callable objects
    Functions or other callable objects can be annotated using collections.abc.Callable
    or typing.Callable. Callable[[int], str] signifies a function that takes
    a single parameter of type int and returns a str.
"""


def feeder(get_next_item: Callable[[], str], item: Optional[str] = None) -> None:
    pass


def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    pass


async def on_update(value: str) -> None:
    pass

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
callback: Callable[[str], Awaitable[None]] = on_update
