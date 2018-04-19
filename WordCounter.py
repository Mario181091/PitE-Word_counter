import sys
import os.path


class PersonalWordCounter:
        def __init__(self):
            self.tot_num_of_Word = 0
            self.tot_num_of_Row = 0
            self.tot_num_of_Char = 0
            self.results = []
            self.text_input = ""

        def set_results(self, res):
            self.results = res

        def get_results(self):
            return self.results

        def count_word(self, current_row):
            num_of_char = 0
            num_of_char += len(current_row.split())
            return num_of_char

        def count_row(self):
            num_of_row = 1
            return num_of_row

        def count_character(self, current_row):
            num_of_char = 0
            num_of_char += len(current_row)
            return num_of_char

        def reinit_variable_for_next_step(self):
            self.tot_num_of_Word = 0
            self.tot_num_of_Row = 0
            self.tot_num_of_Char = 0
            self.results = []

        def print_statistic(self, option, results, out=sys.stdout):
            if len(results) == 0:
                out.write("Invalid file input\n")
                return False
            if option == "-w":
                out.write(str(results[2]))
                out.write("\n")
            elif option == "-r":
                out.write(str(results[0]))
                out.write("\n")
            elif option == "-c":
                out.write(str(results[1]))
                out.write("\n")
            elif option == "":
                out.write(str(results[0]))
                out.write(" ")
                out.write(str(results[1]))
                out.write(" ")
                out.write(str(results[2]))
                out.write("\n")
            else:
                out.write("Invalid parameter\n")
                return False

        def set_Keyboard_input_user(self,text_input):
            self.text_input = text_input

        def start_w_c(self, is_not_file_input, file, option):
            if is_not_file_input:
                self.tot_num_of_Word += self.count_word(self.text_input)
                self.tot_num_of_Row += self.count_row()
                self.tot_num_of_Char += self.count_character(self.text_input)
                list_results = [self.tot_num_of_Row, self.tot_num_of_Char, self.tot_num_of_Word]
                self.reinit_variable_for_next_step()
                return list_results

            elif os.path.isfile(file):
                with open(file) as infile:
                    for row in infile:
                        if option == "-w":
                            self.tot_num_of_Word += self.count_word(row)
                        elif option == "-r":
                            self.tot_num_of_Row += self.count_row()
                        elif option == "-c":
                            self.tot_num_of_Char += self.count_character(row)
                        elif option == "":
                            self.tot_num_of_Word += self.count_word(row)
                            self.tot_num_of_Row += self.count_row()
                            self.tot_num_of_Char += self.count_character(row)

                list_results = [self.tot_num_of_Row, self.tot_num_of_Char, self.tot_num_of_Word]
                self.reinit_variable_for_next_step()
                return list_results
            else:
                list_results = []
                return list_results







