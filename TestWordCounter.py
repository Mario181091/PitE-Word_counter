import unittest
from WordCounter import PersonalWordCounter
from io import StringIO

wc = PersonalWordCounter()
file_object = "smallText.txt"


class TestWordCounter(unittest.TestCase):

    def test_no_option(self):
        results = wc.start_w_c(False, file_object, "")
        self.assertIsInstance(results, list)

    def test_count_words_option(self):
        results = wc.start_w_c(False, file_object, "-w")
        expected_value = 89
        self.assertEqual(expected_value, results[2])

    def test_count_character_option(self):
        results = wc.start_w_c(False, file_object, "-c")
        expected_value = 601
        self.assertEqual(expected_value, results[1])

    def test_count_row_option(self):
        results = wc.start_w_c(False, file_object, "-r")
        expected_value = 8
        self.assertEqual(expected_value, results[0])

    def test_wrong_input(self):
        file_object_wrong = "smallText12.txt"
        results = wc.start_w_c(False, file_object_wrong, "-c")
        expected_value = 0
        self.assertEqual(expected_value, len(results))

    def test_print_statistic(self):

        results = wc.start_w_c(False, file_object, "-w")
        wc.set_results(results)
        total_number_of_word = wc.get_results().__getitem__(2)
        total_number_of_char = wc.get_results().__getitem__(1)
        total_number_of_row = wc.get_results().__getitem__(0)

        out = StringIO()
        wc.print_statistic("-w", results, out=out)
        output = out.getvalue().strip()
        assert output == str(total_number_of_word)

        out = StringIO()
        wc.print_statistic("-c", results, out=out)
        output = out.getvalue().strip()
        assert output == str(total_number_of_char)

        out = StringIO()
        wc.print_statistic("-r", results, out=out)
        output = out.getvalue().strip()
        assert output == str(total_number_of_row)


if __name__ == '__main__':
    unittest.main()