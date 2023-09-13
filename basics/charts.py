import matplotlib.pyplot as plt


def generate_bar_chart(labels, values, xlabel, ylabel, file_name):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    # plt.show()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(file_name)


def generate_pie_chart(labels, values, file_name):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    # plt.show()
    plt.savefig(file_name)


if __name__ == '__main__':
    import read_csv

    world_population = read_csv.read_csv('datasets/world_population.csv')
    south_america = list(
        filter(lambda item: item['Continent'] == 'South America', world_population))
    south_america_countries = list(map(lambda x: x['CCA3'], south_america))
    percentages = list(
        map(lambda x: x['World Population Percentage'], south_america))

    generate_bar_chart(south_america_countries, percentages, 'countries',
                       'percentages', 'img/bar.png')
    generate_pie_chart(south_america_countries, percentages, 'img/pie.png')
