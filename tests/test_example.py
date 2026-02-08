"""Unit tests for python_modern_tools."""

import unittest

from python_modern_tools.example import hello


class TestPythonModernTools(unittest.TestCase):
    """Unit tests for python_modern_tools."""

    def test_hello(self) -> None:
        """Test the `hello` function."""
        assert hello("Awesome User") == "Hello Awesome User!"


if __name__ == "__main__":
    unittest.main()
