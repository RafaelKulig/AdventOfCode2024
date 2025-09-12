def list_distance(report:str)->int:
    """
    Advent of code day 1 part 1 challenge
    Calculate the distance between two lists of integers.
    The distance is defined as the sum of the absolute differences between corresponding elements in the two lists after sorting them.
    :param report: A string containing pairs of integers separated by whitespace, one pair per line.
    :return: The distance between the two lists of integers.
    :raises ValueError: If the two lists do not have the same length.
    """

    reports = report.split('\n')
    left_list = [int(line.split()[0]) for line in reports]
    right_list = [int(line.split()[1]) for line in reports]
    right_list.sort()
    left_list.sort()
    if len(left_list) != len(right_list):
        raise ValueError("Left and right lists must have the same length")
    distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return distance

def similarity(report:str)->int:
    """
    Advent of code day 1 part 2 challenge
    Calculate the similarity between two lists of integers.
    The similarity is defined as the sum of the products of the elements on the left list and the count of the same element in the right list.
    :param report: A string containing pairs of integers separated by whitespace, one pair per line.
    :return: The similarity between the two lists of integers.
    :raises ValueError: If the two lists do not have the same length.
    """

    reports = report.split('\n')
    left_list = [int(line.split()[0]) for line in reports]
    right_list = [int(line.split()[1]) for line in reports]
    if len(left_list) != len(right_list):
        raise ValueError("Left and right lists must have the same length")
    similarity = 0
    for item in left_list:
        similarity += item*right_list.count(item)
    return similarity