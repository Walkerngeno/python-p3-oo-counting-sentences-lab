class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        sentences = [sentence.strip() for sentence in self._value.split('.') if sentence.strip()]
        sentences = [sentence.strip() for sentence in sentences if not sentence.endswith('?') and not sentence.endswith('!')]
        return len(sentences)
