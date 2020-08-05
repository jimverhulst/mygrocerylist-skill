from mycroft import MycroftSkill, intent_file_handler


class Mygrocerylist(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mygrocerylist.intent')
    def handle_mygrocerylist(self, message):
        self.speak_dialog('mygrocerylist')


def create_skill():
    return Mygrocerylist()

