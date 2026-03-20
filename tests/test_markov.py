"""
Tests for the Markov Chain implementation.
"""

import pytest
from markovsan.markov import MarkovChain


class TestMarkovChain:
    """Test cases for the MarkovChain class."""

    def test_initialization(self):
        """Test that MarkovChain initializes with correct order."""
        mc = MarkovChain(order=2)
        assert mc.order == 2
        assert mc.transitions == {}

    def test_train(self):
        """Test that training populates transitions."""
        mc = MarkovChain(order=1)
        text = "the cat sat on the mat"
        mc.train(text)
        assert len(mc.transitions) > 0

    def test_generate(self):
        """Test basic text generation."""
        mc = MarkovChain(order=1)
        text = "the cat sat on the mat the cat ran"
        mc.train(text)
        result = mc.generate(["the"], length=3)
        assert len(result.split()) >= 1


if __name__ == "__main__":
    pytest.main([__file__])
