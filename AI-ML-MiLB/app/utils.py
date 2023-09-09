def calculate_average(data):
    """
    Calculate the average of a list of numbers.

    Args:
        data (list): List of numbers.

    Returns:
        float: Average of the numbers.
    """
    if not data:
        return 0
    
    total = sum(data)
    average = total / len(data)
    return average


def normalize_data(data):
    """
    Normalize a list of numbers between 0 and 1.

    Args:
        data (list): List of numbers.

    Returns:
        list: Normalized list of numbers.
    """
    if not data:
        return []
    
    max_value = max(data)
    min_value = min(data)
    
    normalized_data = [(x - min_value) / (max_value - min_value) for x in data]
    return normalized_data


def remove_duplicates(data):
    """
    Remove duplicates from a list.

    Args:
        data (list): List of elements.

    Returns:
        list: List with duplicates removed.
    """
    return list(set(data))