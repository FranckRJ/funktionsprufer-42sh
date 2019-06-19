#!/usr/bin/python3

import sys


def get_next_alias_name(tab):
    tab[0] = chr(ord(tab[0]) + 1)

    idx = 0
    while ord(tab[idx]) > ord('z'):
        if idx >= (len(tab) - 1):
            return None
        tab[idx] = 'a'
        idx += 1
        tab[idx] = chr(ord(tab[idx]) + 1)

    return tab


def print_alias(name_tab, value_tab, nb_of_rec):
    print("alias " + ''.join(name_tab) + "=", end='')
    print("'" + (str(''.join(value_tab) + ";") * nb_of_rec) + "'")


def print_all_aliases(base_alias, base_size_of_aliases, max_nb_of_aliases, nb_of_rec_per_aliases, last_alias=None):
    cur_nb_of_aliases = 0
    size_of_aliases = base_size_of_aliases
    old_tab = list(base_alias)

    if max_nb_of_aliases == 0:
        return
    if last_alias is not None:
        max_nb_of_aliases -= 1

    while True:
        cur_tab = ['a'] * size_of_aliases
        while cur_tab is not None and (max_nb_of_aliases < 0 or cur_nb_of_aliases < max_nb_of_aliases):
            print_alias(old_tab, cur_tab, nb_of_rec_per_aliases)
            old_tab = cur_tab
            cur_tab = get_next_alias_name(cur_tab.copy())
            cur_nb_of_aliases += 1

        if max_nb_of_aliases < 0 or cur_nb_of_aliases >= max_nb_of_aliases:
            break
        size_of_aliases += 1

    if last_alias is not None:
        print_alias(old_tab, list(last_alias), nb_of_rec_per_aliases)


def print_usage():
    print("""
usage: ./aliasbomb.py [-s base_size_of_aliases = 1]
                      [-m max_nb_of_aliases = 10000 (-1 for all combinations of base_size_of_aliases)]
                      [-r nb_of_rec_per_aliases = 1]
                      [-l last_alias_value = \"\"]
""".strip("\n"))


def print_err_and_exit(msg):
    print(msg)
    sys.exit(1)


def get_str_opt_val(opt_name, def_val):
    try:
        opt_idx = sys.argv.index(opt_name)
        if opt_idx < (len(sys.argv) - 1):
            return sys.argv[opt_idx + 1]
        else:
            print_err_and_exit("error: invalid value for option " + opt_name)
    except ValueError:
        return def_val


def get_int_opt_val(opt_name, def_val, can_be_zero_or_neg=True):
    val = get_str_opt_val(opt_name, str(def_val))

    try:
        val = int(val)
        if not can_be_zero_or_neg and val <= 0:
            raise ValueError
        return int(val)
    except ValueError:
        print_err_and_exit("error: invalid value for option " + opt_name)


def to_int_or_def(str_val, def_val):
    try:
        return int(str_val)
    except ValueError:
        return def_val


if "-h" in sys.argv or "--help" in sys.argv:
    print_usage()
    sys.exit()

base_alias_name_param = "aliasbomb"
base_size_of_aliases_param = get_int_opt_val("-s", 1, False)
max_nb_of_aliases_param = get_int_opt_val("-m", 10000)
nb_of_rec_per_aliases_param = get_int_opt_val("-r", 1, False)
last_alias_param = get_str_opt_val("-l", "")

if not last_alias_param:
    last_alias_param = None

print_all_aliases(base_alias_name_param,
                  base_size_of_aliases_param,
                  max_nb_of_aliases_param,
                  nb_of_rec_per_aliases_param,
                  last_alias_param)
print(base_alias_name_param)
