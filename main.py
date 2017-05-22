import os
import re
import numpy as np
from imdb_rest import lookup


def main():
    for root, dirs, files in os.walk("."):
        names = np.empty_like([['', '', '']])
        for file in files:
            file_path = os.path.join(root, file)
            season_episode = find_name(file_path)
            if season_episode[2] != 'NO MATCH':
                index_of_s_and_e = file_path.index(season_episode[2])
                contains_name = file_path[re.search(root, file_path).end() + 1:index_of_s_and_e]
                possible_name = re.sub('[.\-,=!@#$\[\]]', ' ', contains_name).lower().strip()
                array_object = np.array([[possible_name, season_episode[0], season_episode[1]]])
                names = np.append(names, array_object, 0)
            else:
                print('Probably a movie? ' + file)
        for dir in dirs:
            season_episode = find_name(dir)
            if season_episode[2] != 'NO MATCH':
                index_of_s_and_e = dir.index(season_episode[2])
                contains_name = dir[0:index_of_s_and_e]
                possible_name = re.sub('[.\-,=!@#$\[\]]', ' ', contains_name)
        iter_names = iter(names)
        next(iter_names)
        for name in iter_names:
            possible_title = name[0]
            looked_up_name = lookup(possible_title)
            if looked_up_name:
                print(looked_up_name)
            else:
                possible_title = possible_title.split(' ', 1)[1]
                print(possible_title)
        break


def find_name(file_or_dir):
    SXXEXX_match = re.search('[S]\d\d[E]\d\d', file_or_dir)
    SXEX_match = re.search('[S]\d[E]\d', file_or_dir)
    sxxexx_match = re.search('[s]\d\d[e]\d\d', file_or_dir)
    sxex_match = re.search('[s]\d[e]\d', file_or_dir)
    x_match = re.search('\d\d[x]\d\d', file_or_dir)
    of_match = re.search('\dof\d', file_or_dir)
    if SXXEXX_match:
        return handle_match(SXXEXX_match, 1, 3, 4, 6)
    elif SXEX_match:
        return handle_match(SXEX_match, 1, 2, 3, 5)
    elif sxex_match:
        return handle_match(sxex_match, 1, 2, 3, 5)
    elif sxxexx_match:
        return handle_match(sxxexx_match, 1, 3, 4, 6)
    elif x_match:
        return handle_match(x_match, 0, 2, 3, 5)
    elif of_match:
        e_s_season = handle_match(of_match, 0, 1, 3, 4)
        return [e_s_season[1], e_s_season[0], e_s_season[2]]
    else:
        return [0, 0, 'NO MATCH']


def handle_match(match, start_season_index, end_season_index, start_episode_index, end_episode_index):
    season = match.string[match.start(0):match.end(0)]
    season_int = int(season[start_season_index:end_season_index])
    episode_int = int(season[start_episode_index:end_episode_index])
    return [season_int, episode_int, season]


if __name__ == '__main__':
    main()
