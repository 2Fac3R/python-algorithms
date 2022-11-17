from typing import Dict, List


def read_csv(path: str) -> List[Dict[str, str]]:
    """Read a csv file

    Args:
        path (str): file path

    Returns:
        List[Dict[str, str]]: data
    """
    import csv

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data: List[Dict[str, str]] = []
        for row in reader:
            iterable = zip(header, row)
            data_dict = dict({key: value for key, value in iterable})
            data.append(data_dict)
        return data


if __name__ == '__main__':
    data = read_csv('datasets/world_population.csv')
    print(data[0])
