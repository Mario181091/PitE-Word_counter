import sys
import os.path

tot_num_of_Row = 0
tot_num_of_Word = 0
tot_num_of_Char = 0
no_file_input = False


if len(sys.argv) == 1:
    no_file_input = True
    option = ""

elif len(sys.argv) == 2:
    option = ""

elif len(sys.argv) == 3:
    option = sys.argv[2]


def count_word(current_row):
    num_of_char = 0
    num_of_char += len(current_row.split())
    return num_of_char


def count_row():
    num_of_row = 1
    return num_of_row


def count_character(current_row):
    num_of_char = 0
    num_of_char += len(current_row)
    return num_of_char


def print_statistic(option):
    if option == "-w":
        print(tot_num_of_Word)
    elif option == "-r":
        print(tot_num_of_Row)
    elif option == "-c":
        print(tot_num_of_Char)
    elif option == "":
        print (tot_num_of_Row, tot_num_of_Word, tot_num_of_Char)
    else:
        print ("invalid parameter")


if no_file_input:
    text_input = input()
    tot_num_of_Word += count_word(text_input)
    tot_num_of_Row += count_row()
    tot_num_of_Char += count_character(text_input)
    print_statistic(option)

elif os.path.isfile(sys.argv[1]):
    with open(sys.argv[1]) as infile:
        for row in infile:
            if option == "-w":
                tot_num_of_Word += count_word(row)
            elif option == "-r":
                tot_num_of_Row += count_row()
            elif option == "-c":
                tot_num_of_Char += count_character(row)
            elif option == "":
                tot_num_of_Word += count_word(row)
                tot_num_of_Row += count_row()
                tot_num_of_Char += count_character(row)

    print_statistic(option)
else:
    print("file not found")







