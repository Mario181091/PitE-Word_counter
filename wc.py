from WordCounter import  PersonalWordCounter
import sys

if __name__ == '__main__':
    personal_w_c = PersonalWordCounter()

    if len(sys.argv) == 1:
        is_not_file_input = True
        text_input = input()
        personal_w_c.set_Keyboard_input_user(text_input)
        option = ""
        results = personal_w_c.start_w_c(is_not_file_input, "", "")
        personal_w_c.set_results(results)
        personal_w_c.print_statistic(option, personal_w_c.get_results())

    elif len(sys.argv) == 2:
        input_file = sys.argv[1]
        option = ""
        results = personal_w_c.start_w_c(False, input_file, option)
        personal_w_c.set_results(results)
        personal_w_c.print_statistic(option, personal_w_c.get_results())

    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        option = sys.argv[2]
        results = personal_w_c.start_w_c(False, input_file, option)
        personal_w_c.set_results(results)
        personal_w_c.print_statistic(option, personal_w_c.get_results())

