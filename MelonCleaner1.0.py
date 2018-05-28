import os


def trim_list(r_list):
    mu_list = []
    for name in r_list:
        if name.endswith('mp3'):
            mu_list.append(name)
    return mu_list


def find_delete_target(mu_list):
    target = []
    for n1 in range(len(mu_list)):
        for n2 in range(n1+1, len(mu_list)):
            if mu_list[n1][3:] == mu_list[n2][3:]:
                target.append(mu_list[n2])
                break
    return target


def delete_target(target):
    for name in target:
        os.remove(os.getcwd()+'/'+name)


raw_list = os.listdir(os.getcwd())
music_list = trim_list(raw_list)
target_list = find_delete_target(music_list)
delete_target(target_list)
