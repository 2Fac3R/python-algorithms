def is_younger(worker: str) -> bool:
    return int(worker['age']) < 18


def get_name(worker: str) -> str:
    return worker['name']


if __name__ == '__main__':
    import json

    # f = open('json/workers.json')
    with open('json/workers.json', 'r') as f:
        data = json.load(f)

    # Lists comprehensions
    python_devs: list = [
        worker for worker in data if worker['language'] == 'python']
    ux_designers: list = [
        worker for worker in data if worker['position'] == 'UX Designer']

    # Lambda - High Order Functions
    younger = list(filter(lambda worker: worker['age'] < 18, data))
    younger_names = list(map(lambda worker: worker['name'], younger))

    # Functions - High Order Functions
    # younger = list(filter(is_younger, data))
    # younger_names = list(map(get_name, younger))

    print(python_devs)
    print(ux_designers)
    # print(younger_names)
