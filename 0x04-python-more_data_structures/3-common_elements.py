#!/usr/bin/python3
def common_elements(set_1, set_2):

    return [e1 for e1 in set_1 for e2 in set_2 if e1 == e2]


set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
