class ArrogantProfessor(Person):
    def say(self, stuff):
        return self.name + ' says: ' + 'It is obvious that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff