import read_csv
import charts


if __name__ == '__main__':
    data = read_csv.read_csv('datasets/world_population.csv')
    data = list(
        filter(lambda item: item['Continent'] == 'South America', data))
    countries = list(map(lambda x: x['CCA3'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))

    charts.generate_bar_chart(countries, percentages,
                              'countries', 'percentages', 'bar.png')
    charts.generate_pie_chart(countries, percentages, 'pie.png')
