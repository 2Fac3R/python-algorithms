from datetime import datetime


def execution_time(func):
    """Execution time

    Prints the execution time of a given function in seconds

    Args:
        func (function): a function to wrap up
    """
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Execution time: {time_elapsed.total_seconds()} seconds.')
    return wrapper
