import os
import re

def main() :
    for root, dirs, files in os.walk("../../Download"):
        for file in files:
            file_path = os.path.join(root, file)
            find_name(file_path)
        for dir in dirs:
            find_name(dir)
            return

def find_name(file_or_dir):
    possible_name = re.sub('[.\-,=!@#$\[\]]', '', file_or_dir)
    SXEX_match = re.search('[Ss]\d\d[Ee]\d\d', file_or_dir)
    print('File ' + file_or_dir)
    if SXEX_match:
        season = SXEX_match.string[SXEX_match.start(0):SXEX_match.end(0)]
        season_int = int(season[season.index('S') + 1:season.index('E')])
        episode_int = int(season[season.index('E') + 1:len(season)])
        print('Season ' + str(season_int) + ' Episode ' + str(episode_int))
        return possible_name + " -> "
    else:
        print('NO MATCH')
    return possible_name + " -> "


if __name__ == '__main__':
    main()