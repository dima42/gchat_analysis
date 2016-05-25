import datetime

class Message:
    def __init__(self, message_string):
        self.message_string = message_string
        parts_of_message = message_string.split(" ")
        date_string = parts_of_message[0] + parts_of_message[1]
        self.date = datetime.strptime(date_string, ""%Y-%m-%d %H:%M:%S")
        self.incoming = parts_of_message[2] != "<dima.kamalov@gmail.com>"
        self.number_of_words = len(parts_of_message) - 3
