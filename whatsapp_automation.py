try:
    import pywhatkit
    import termcolor
except:
    import os

    print("Installing requirements . . . .")

    os.system("pip3 install pywhatkit")
    os.system("pip3 install termcolor")
    
import pywhatkit
import termcolor
    
class Autobot:
    def __init__(self, contact, message, hour, minute):
        self.contact = contact
        self.message = message
        self.hour = hour
        self.minute = minute
        
    def send_message(self):
        result = pywhatkit.sendwhatmsg(self.contact, self.message, self.hour, self.minute)
        return result
        
contact=input(termcolor.colored("Enter Target's Contact: ","cyan"))
message=input(termcolor.colored("Enter Message: ","cyan"))
hour=input(termcolor.colored("Enter Hour to send message: ","cyan"))
minute=input(termcolor.colored("Enter Minute to send message: ","cyan"))

data = (contact, message, hour, minute)

Autobot.send_message(data)
