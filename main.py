import data_gathering.person as person
import analysis.communication_frequency as communication_frequency

def main():
    lauren = person.Person("unrealeel@gmail.com")
    communication_frequency.plot(lauren)

main()
