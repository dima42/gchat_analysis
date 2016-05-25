import data_gathering.person as person
import analysis.communication_frequency as communication_frequency
import datetime

def main():
    lauren = person.Person("Lauren_Lee")
    date = datetime.date(2014, 11, 01)
    print lauren.message_volume(date)
    # communication_frequency.plot(lauren)

main()
