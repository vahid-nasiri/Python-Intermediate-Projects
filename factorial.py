from pprint import pprint


def main():
    # List Comprehension
    fact_list = [f"{x}! = {factorial(x)}" for x in
                 range(10)]
    # Dictionary Comprehenstion
    fact_dict = {f"{x}!": factorial(x) for x in range(10) if x % 2 == 0}
    # map() with filter() function
    fact_map = list(map(factorial, filter(lambda x: x % 2, range(10))))
    pprint(fact_list, width=1)
    pprint(fact_dict, width=1)
    pprint(fact_map, width=1)


def factorial(x: int):
    """This is sample of recursion, that returns the
      factorial of a given number.
        Args:   
            x (int): takes an integer as an argument.
        Returns:
            int | Literal [1]: returns literal integer.
            can be a list of integer or 
                a dictionary of key-value-pair."""
    return 1 if x < 2 else x * factorial(x - 1)


main()
