import matplotlib.pyplot as plt
import read_csv


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
    data = read_csv.read_csv('datasets/world_population.csv')
    data = list(
        filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['CCA3'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))

    generate_bar_chart(countries, percentages, 'countries',
                       'percentages', 'bar.png')
    generate_pie_chart(countries, percentages, 'pie.png')
