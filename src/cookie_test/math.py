from typing import Union


class SimpleMath:
    """Class to perform basic mathematical operations."""

    @staticmethod
    def add(
        number_1: Union[float, int], number_2: Union[float, int]
    ) -> Union[float, int]:
        """Return the sum of two numbers.

        Parameters:
        number_1 (float or int): First number.
        number_2 (float or int): Second number.

        Returns:
        float or int: Sum of a and b.
        """
        return number_1 + number_2

    @staticmethod
    def subtract(
        number_1: Union[float, int], number_2: Union[float, int]
    ) -> Union[float, int]:
        """Return the difference between two numbers.

        Parameters:
        number_1 (float or int): First number.
        number_2 (float or int): Second number.

        Returns:
        float or int: Difference between a and b.
        """
        return number_1 - number_2

    @staticmethod
    def multiply(
        number_1: Union[float, int], number_2: Union[float, int]
    ) -> Union[float, int]:
        """Return the product of two numbers.

        Parameters:
        number_1 (float or int): First number.
        number_2 (float or int): Second number.

        Returns:
        float or int: Product of a and b.
        """
        return number_1 * number_2

    @staticmethod
    def divide(number_1: Union[float, int], number_2: Union[float, int]) -> float:
        """Return the division of two numbers.

        Parameters:
        a (float or int): Numerator.
        b (float or int): Denominator.

        Returns:
        float: Result of division a by b.

        Raises:
        ValueError: If b is 0 (to avoid division by zero).
        """
        if number_2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return number_1 / number_2
