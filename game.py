class Game(object):
    def __init__(self, word_length=4):
        self.word_length = word_length
        self.chain = []
        self.used = set()
        self.dictionary = self._load_words()

    def _letter(self):
        if not self.chain:
            return None
        return self.chain[-1][-1]

    def _load_words(self):
        return {word
                for word in open('words.txt').read().split()
                if len(word) == self.word_length}

    def play(self):
        while True:
            self.your_turn()
            self.my_turn()

    def _is_valid(self, word):
        if len(word) != self.word_length:
            print "Not a %d-letter word." % self.word_length
        elif word in self.used:
            print "Already used that word."
        elif word not in self.dictionary:
            print "Not a word."
        elif self._letter() and word[0] != self._letter():
            print "That doesn't start with '%s'." % self._letter()
        else:
            return True
        return False

    def your_turn(self):
        while True:
            if not self._letter():
                prompt = "Enter any %d-letter word: " % self.word_length
            else:
                prompt = "Enter a %d-letter '%s' word: " % (
                        self.word_length, self._letter().upper())
            guess = raw_input(prompt).lower()
            if self._is_valid(guess):
                self.chain.append(guess)
                self.used.add(guess)
                return
            print

    def my_turn(self):
        letter = self._letter()
        for word in self.dictionary:
            if word.startswith(letter) and word not in self.used:
                self.chain.append(word)
                self.used.add(word)
                print "My word: %s." % word
                return
        print "I can't find a word starting with '%s'.  You win!" % letter

def main():
    game = Game(4)
    game.play()


if __name__ == '__main__':
    main()
