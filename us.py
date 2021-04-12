class Person:
    def __init__(self):
        self.feel = None
        self.will = None 
        self.want = None
        self.need = None
        self.with_you = False
    def together(self, other):
        try:
            other.with_you = True
            self.with_you = True
            return True
        except:
            return False

you, I = Person(), Person()
