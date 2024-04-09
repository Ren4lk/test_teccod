import math


def get_unique_items(lst_in: list) -> list:
    return list(set(lst_in))


def get_prime_numbers_range(first: int, last: int) -> list:
    first, last = min(first, last), max(first, last)
    return [x for x in range(first, last) if all(x % y != 0 for y in range(2, x))]


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def get_coordinates(self) -> tuple:
        return (self.x, self.y)

    def set_coordinates(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"(Point({self.x}, {self.y}))"


def sort_ascending(lst_in: list[str]) -> list[str]:
    return sorted(lst_in, key=len)


def sort_descending(lst_in: list[str]) -> list[str]:
    return sorted(lst_in, key=len, reverse=True)


test = [
    "lorem",
    "ipsum",
    "dolor",
    "sit",
    "amet",
    "consectetur",
    "adipiscing",
    "elit",
    "sed",
    "do",
]

print(sort_ascending(test))
print(sort_descending(test))
