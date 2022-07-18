#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = list()
    i = 0
    while i == 0 or i < list_length:
        try:
            res.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            res.append(0)
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        except IndexError:
            print("out of range")
            res.append(0)
        finally:
            i += 1
    return (res)
