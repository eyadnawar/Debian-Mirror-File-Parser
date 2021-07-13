import unittest
import os
import pathlib

class MyTestCase(unittest.TestCase):
    """def test_something(self):
        self.assertEqual(True, False)
        """

    def setUp(self) -> None:
        self.architecture = "armel"
        self.path = "C:/Users/Lenovo/Desktop//"

    def test_get_supported_architectures(self):

        from Content_indices_parser.cli_functions import get_supported_architectures
        result = get_supported_architectures()

        self.assertTrue(result is not None, msg= "The method returned a non-None result")

        self.assertTrue(isinstance(result, list), msg= "The method returned a list")

        self.assertTrue(len(result) > 0, msg= "The method returned a non-empty list of acceptable architectures")

    def test_download_content_indices_file(self):

        from Content_indices_parser.cli_functions import download_content_indices_file
        download_content_indices_file(self.architecture, self.path)

        output_file = pathlib.Path(self.path) / 'outputFile'

        self.assertTrue(output_file.exists() == True, msg= "File has been created and ready for parsing")

    def test_parseFile(self):

        from Content_indices_parser.cli_functions import parseFile
        result = parseFile(self.path + '/outputFile')

        self.assertTrue(result is not None, msg= "The method returned a non-None result")

        self.assertTrue(isinstance(result, dict), msg= "The method returned a dictionary of packages and their corresponding files")

        self.assertTrue(len(result) > 0, msg= "The method returned a non-empty dictionary of packages and their files")


if __name__ == '__main__':
    unittest.main()
