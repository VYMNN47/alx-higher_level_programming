#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []

    for x in range(list_lenght):
        try:
            my_list.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            my_list.append(0)
            print('wrong type')
            continue
        except ZeroDivisionError:
            my_list.append(0)
            print('division by 0')
            continue
        except IndexError:
            my_list.append(0)
            print('out of range')
            continue
        finally:
            pass

    return my_list
