# Cookie Jar 🍪

class Jar:

    """
    A class representing a jar that can hold cookies.

    Attributes:
        capacity (int): The maximum number of cookies the jar can hold.
        size (int): The current number of cookies in the jar.
    """
    def __init__(self, capacity=12):
        """
        Initialize a new Jar with a specified capacity.

        Args:
            capacity (int): The maximum number of cookies the jar can hold. Defaults to 12.

        Raises:
            ValueError: If the capacity is a negative number.
        """
        if capacity < 0:
            raise ValueError("capacity must be non-negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """
        Return a string representation of the jar, showing its cookies.

        Returns:
            str: A string with '🍪' repeated for each cookie in the jar.
        """
        return int(self.size) * "🍪"

    def deposit(self, n):
        """
        Add a specified number of cookies to the jar.

        Args:
            n (int): The number of cookies to add.

        Raises:
            ValueError: If `n` is negative or if adding `n` would exceed the jar's capacity.
        """
        if n < 0:
            raise ValueError("only non-negative numbers allowed.")
        elif (n + self.size) > self.capacity:
            raise ValueError("deposit does not fit into jar.")
        self.size = self.size + n

    def withdraw(self, n):

        """
        Remove a specified number of cookies from the jar.

        Args:
            n (int): The number of cookies to remove.

        Raises:
            ValueError: If `n` is negative or if there are not enough cookies to remove.
        """
        if n < 0:
            raise ValueError("only non-negative numbers allowed.")
        elif self.size < n:
            raise ValueError("not enough cookies!")
        self.size = self.size - n

    @property
    def capacity(self):
        """
        int: The maximum number of cookies the jar can hold.
        """
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        """
        Set the current capacity of the jar, ensuring it is not negative.

        Args:
            capacity (int): The desired capacity.

        Raises:
            ValueError: If `capacity` is negative.
        """
        if capacity < 0:
            raise ValueError("capacity must be non-negative.")
        self._capacity = capacity

    @property
    def size(self):
        """
        int: The current number of cookies in the jar.
        """
        return self._size 
    @size.setter
    def size(self, size):

        """
        Set the current size of the jar, ensuring it does not exceed capacity.

        Args:
            size (int): The desired size.

        Raises:
            ValueError: If `size` exceeds the jar's capacity.
        """
        if self.capacity < size:
            raise ValueError("size over limit set by capacity.")
        self._size = size
