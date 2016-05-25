import datetime

class Message:
    def __init__(self, message_string):
        self.message_string = message_string
        parts_of_message = message_string.split(" ")
        date_string = parts_of_message[0] + " " + parts_of_message[1]
        self.datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

        from_string, number_to_remove = self.from_string(parts_of_message[2], parts_of_message[3])

        self.incoming = from_string != "<dima.kamalov@gmail.com>" and from_string != "<Dima Kamalov>"
        self.number_of_words = len(parts_of_message) - number_to_remove

    def append_line(self, line):
        self.message_string += line
        self.number_of_words += len(line.split(" "))

    def from_string(self, first_string, second_string):
        if ">" not in first_string:
            final_string = first_string + second_string
            number_to_remove = 4
        else:
            final_string = first_string
            number_to_remove = 3
        return final_string, number_to_remove
