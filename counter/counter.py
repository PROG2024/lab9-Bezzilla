"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:
    __instance = None

    def __str__(self):
        """return str count"""
        return f"{self.__count}"

    def __new__(cls, *args, **kwargs):
        """
        >>> counter = Counter()
        >>> counter.count
        0
        >>> counter.count        # invoking count doesn't change anything
        0
        >>> counter.increment()  # add 1 and return the new count
        1
        >>> counter2 = Counter()
        >>> counter2 is counter
        True
        >>> counter2.count       # shares same count
        1
        >>> counter2.increment()  # add 1 and return the new count
        2
        >>> counter.count
        2
        """
        if cls.__instance is None:
            cls.__instance = super(Counter, cls).__new__(cls)
            cls.__instance.__count = 0
        return cls.__instance

    @property
    def count(self):
        """return count value"""
        return self.__count

    def increment(self):
        """add number to count"""
        self.__count += 1
        return self.__count

