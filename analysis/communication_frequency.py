import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot(person, word_filter = [], inc=True, out=True):
    current_date = person.messages[0].datetime.date() - datetime.timedelta(days=1)
    dates = []
    dima_values = []
    lauren_values = []
    granularity = 60
    while current_date < (person.messages[-1].datetime.date()):
        current_date += datetime.timedelta(days=1)
        dates.append(current_date)
        dima_values.append(person.message_volume(current_date, word_filter, False, True))
        lauren_values.append(person.message_volume(current_date, word_filter, True, False))

    
    dima_values = [np.average(dima_values[i-granularity/2-1:i+granularity/2]) for i in range(len(dima_values))]
    lauren_values = [np.average(lauren_values[i-granularity/2-1:i+granularity/2]) for i in range(len(lauren_values))]

    """
    maxsf = 0
    maxdate=None
    for i in range(len(dates)):
        if values[i]>maxsf:
            maxsf=values[i]
            maxdate = dates[i]
    print maxsf, maxdate
    """
    dates = matplotlib.dates.date2num(dates)
    plt.plot_date(dates, dima_values, label='dima')
    plt.plot_date(dates, lauren_values, label='lauren')
    plt.legend()
    plt.show()
