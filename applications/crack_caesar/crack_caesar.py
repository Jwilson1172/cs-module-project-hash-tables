import numpy as np


class CipherBreaker():
    def __init__(self):
        self.ref = [
            'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
            'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
        ]
        return

    def load_file(self):
        """Takes the file and loads it into a text string object
        """

        data = None
        with open('ciphertext.txt', 'rt') as fp:
            data = fp.read()
        self.data = data
        return

    def calc_freq(self, x) -> list:
        """calculates the frequencies of the letters occuring in x
        """
        seen = {}
        # counts the times that we see a particular letter
        for letter in x:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1
        norm = len(x)
        self._freqs = {k: v / norm for k, v in seen.items()}
        return self._freqs

    def decode(self, x):
        """Attempts to find the cesar cipher based on the distribution frequency
        fo the given letters
        """
        decoded = ""
        # where pt is the predicted plaintext character based on the known
        # probabilities of character distribution in the english language
        # and ct is the corresponding character in the crypt text that matches
        # that predicted character
        # given these two values I want to replace the letter that is in the
        # ciphertext with the letter that is predicted to be it's plaintext
        # equivalent
        for pt, ct in zip(,):
            self.data.replace(ct, pt)
        return decoded
