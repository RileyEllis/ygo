import sys
import re

args = sys.argv[1:]

with open(args[0],'r+') as card_list:
    with open(args[1],'r') as ban_list:
        card_list_source = card_list.read()
        for idx, line in enumerate(ban_list):
            if idx > 1:
                split = line.split()[:2]
                reg = '^' + split[0] + ' \d'
                m = re.findall(reg, card_list_source, flags=re.M)
                if m and int(m[0][-1]) > int(split[1]):
                    card_list_source = re.sub(reg, ' '.join(split), card_list_source, flags=re.M)
    card_list.seek(0)
    card_list.write(card_list_source)
    card_list.truncate()
