class Message:
    def __init__(self, message):
        self.message = message

    def send(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Email(Message):
    def send(self):
        print(f"Your Email Message=\"{self.message}\", is sent")

class SMS(Message):
    def send(self):
        print(f"Your SMS Message=\"{self.message}\", is sent")

class WhatsApp(Message):
    def send(self):
        print(f"Your WhatsApp Message=\"{self.message}\", is sent")

def main():
    e = Email("Hello")
    e.send()
    s = SMS("Hello")
    s.send()
    w = WhatsApp("Hello")
    w.send()
main()