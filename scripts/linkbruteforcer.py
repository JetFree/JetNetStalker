import itertools
import string


def generate():
    iter_list = list()
    for i in range(5, 8):
        iter_list.append(itertools.permutations(
            string.digits + string.ascii_letters, i))
    return iter_list
