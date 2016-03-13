import numpy
import matplotlib.pyplot as plt


# ---------------
# L1 Problem 3
# ---------------
def get_temp_list(file_name):
    in_file = open(file_name, 'r')

    low_temps = []
    high_temps = []

    for line in in_file:
        fields = line.split(' ')

        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue

        high_temps.append(int(fields[1]))
        low_temps.append(int(fields[2]))

    return low_temps, high_temps


# ---------------
# L1 Problem 4
# ---------------
def produce_plot(low_temps, high_temps):
    # The element by element difference between highTemps and lowTemps
    diff_temps = numpy.array(high_temps) - numpy.array(low_temps)

    plt.plot(range(1, 32), diff_temps)
    plt.title('Day by Day Ranges in Temperature in Boston in July 2012')
    plt.xlabel('Days')
    plt.ylabel('Temperature Ranges')
    plt.show()


produce_plot(*get_temp_list('julyTemps.txt'))
