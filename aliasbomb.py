#!/usr/bin/python3


def get_next_name(tab):
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
            cur_tab = get_next_name(cur_tab.copy())
            cur_nb_of_aliases += 1

        if max_nb_of_aliases < 0 or cur_nb_of_aliases >= max_nb_of_aliases:
            break
        size_of_aliases += 1

    if last_alias is not None:
        print_alias(old_tab, list(last_alias), nb_of_rec_per_aliases)


print_all_aliases("aliasbomb", 1, 3, 3, "coucou")
print("aliasbomb")
