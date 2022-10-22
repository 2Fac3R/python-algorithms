import matplotlib.pyplot as plt


def generate_bar_chart(labels, values, xlabel, ylabel, file_name):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    # plt.show()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f"img/{file_name}")


def generate_pie_chart(labels, values, file_name):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    # plt.show()
    plt.savefig(f"img/{file_name}")


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    xlabel = 'x'
    ylabel = 'y'

    generate_bar_chart(labels, values, xlabel, ylabel, 'bar_test.png')
    generate_pie_chart(labels, values, 'pie_test.png')
