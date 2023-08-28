class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
    def talk(self):
        return "I can talk!"
    def say_favourite_language(self, fave_lang):
        return f"I love {fave_lang}!"