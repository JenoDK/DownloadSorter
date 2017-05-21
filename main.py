import os
import re

def main() :
    for root, dirs, files in os.walk("../../Download"):
        for file in files:
            file_path = os.path.join(root, file)
            possible_name = re.sub('[.\-,=!@#$\[\]]', '', file_path)
            season_episode = find_name(file_path)
            if (season_episode[2] != 'NO MATCH'):
                print()
                index_of_s_and_e = file_path.index(season_episode[2])
                print(file)
                print(file_path[re.search(root, file_path).end() + 1:index_of_s_and_e])
                print('Season ' + str(season_episode[0]) + ' episode ' + str(season_episode[1]))
            else:
                print()
                print('Probably a movie? ' + file)
        for dir in dirs:
            find_name(dir)
            return

def find_name(file_or_dir):
    SXEX_match = re.search('[S]\d\d[E]\d\d', file_or_dir)
    sxex_match = re.search('[s]\d\d[e]\d\d', file_or_dir)
    x_match = re.search('\d\d[x]\d\d', file_or_dir)
    of_match = re.search('\dof\d', file_or_dir)
    if SXEX_match:
        return handle_match(SXEX_match, 1, 3, 4, 6)
    elif sxex_match:
        return handle_match(sxex_match, 1, 3, 4, 6)
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