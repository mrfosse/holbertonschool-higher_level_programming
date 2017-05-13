#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    error_list = ("wrong type", "division by 0", "out of range")
    numl = []
    for count in range(list_length):
        flag = 3
        try:
            num = my_list_1[count] / my_list_2[count]
        except TypeError:
            flag = 0
        except ArithmeticError:
            flag = 1
        except IndexError:
            flag = 2
        finally:
            if flag != 3:
                print(error_list[flag])
                num = 0
        numl.append(num)
    return (numl)
