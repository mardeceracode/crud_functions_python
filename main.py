from _messages import *
from _create import *
from _search import *
from _edit import *
from _show import *
from _delete import *

def main():
    while True:
        try:
            selected = int(input( msn_menu ))
            print(separator_line)

            if selected == 1:
                get_data()
            elif selected == 2:
                search_data()
            elif selected == 3:
                edit_data()
            elif selected == 4:
                show_data()
            elif selected == 5:
                delete_data()
            elif selected == 6:
                break
        except:
            print('\n', msn_error_menu)


if '__main__' == __name__:
    main()