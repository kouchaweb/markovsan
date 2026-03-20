"""
Markov Chain implementation for text generation.
"""


class MarkovChain:
    """A simple Markov chain for text generation."""

    def __init__(self, order: int = 2):
        """
        Initialize the Markov chain.

        Args:
            order: The order of the Markov chain (number of previous words to consider)
        """
        self.order = order
        self.transitions = {}

    def train(self, text: str) -> None:
        """
        Train the Markov chain with the given text.

        Args:
            text: The input text to train on
        """
        words = text.split()
        for i in range(len(words) - self.order):
            key = tuple(words[i : i + self.order])
            next_word = words[i + self.order]
            if key not in self.transitions:
                self.transitions[key] = []
            self.transitions[key].append(next_word)

    def generate(self, start_words: list[str], length: int = 20) -> str:
        """
        Generate text using the trained Markov chain.

        Args:
            start_words: The starting words for generation
            length: The number of words to generate

        Returns:
            Generated text as a string
        """
        current = tuple(start_words)
        result = list(current)

        for _ in range(length):
            if current not in self.transitions:
                break
            next_word = self.transitions[current][0]
            result.append(next_word)
            current = tuple(result[-self.order :])

        return " ".join(result)
