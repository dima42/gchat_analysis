import datetime
import message

class Person:
    def __init__(self, name):
        self.name = name
        self.extract_data()

    def extract_data(self):
        person_file = open("/Users/Drifter/dima/gchat_analysis/data_gathering/text_data_files/" + self.name + ".txt")
        chat_lines = person_file.readlines()
        self.messages = []
        for line in chat_lines:
            try:
                parts_of_line = line.split(" ")
                date_string = parts_of_line[0] + " " + parts_of_line[1]
                line_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
                self.messages.append(message.Message(line))
            except:
                self.messages[-1].append_line(line)

        self.messages.sort(key=lambda message: message.datetime)

    def message_volume(self, date):
        index = 0
        current_date = self.messages[index].datetime.date()
        word_count = 0
        while current_date < date:
            index += 1
            current_date = self.messages[index].datetime.date()
        while current_date == date:
            word_count += self.messages[index].number_of_words
            index += 1
            current_date = self.messages[index].datetime.date()

        return word_count
