# c2 = 0
# c3 = 0
# ids = []
# for line in open('02_input.txt'):
#     s = line.strip()
#     ids.append(s)
#     count = {}
#     for c in s:
#         if c not in count:
#             count[c] = 0
#         count[c] += 1
#     has_two = False
#     has_three = False
#     for k, v in count.items():
#         if v == 2:
#             has_two = True
#         if v == 3:
#             has_three = True
#     if has_two:
#         c2 += 1
#     if has_three:
#         c3 += 1
# print
# print(c2 * c3)
# c2 * c3
#
# for x in ids:
#     for y in ids:
#         diff = 0
#         for i in range(len(x)):
#             if x[i] != y[i]:
#                 diff += 1
#         if diff == 1:
#             ans = []
#             for i in range(len(x)):
#                 if x[i] == y[i]:
#                     ans.append(x[i])
#             print
#             ''.join(ans)
#             print(x,y)
#             x, y

list_IDs = ["tjxmoewpqkyaiqvmndgflunszc", "tjxmobwpqkyaihvrndgfjubszm", "tjxmzewpqkyaihvrydgflrbszc",
            "tjxmoeypqkyvihvrndgflubsza", "tjcmoewpqkytihvrndgflgbszc", "tjvmoewpqkyanevrndgflubszc",
            "tjxmoewpqkdiihirndgflubszc", "tjxboewpqkyaihbrnogflubszc", "ojpmoewpqkyaihvjndgflubszc",
            "tjxyoewpqkyaiuvrndgflutszc", "tjxmoewpqkyalhvrndmflebszc", "tjxmoewpqzyaihhrndgflubszf",
            "tjxmrewpqkyaihirndgfjubszc", "pjxmoewpqkyaihvendgfbubszc", "txxmkewpqkyjihvrndgflubszc",
            "tjxmoewcqkyaihvrnmgflubczc", "tjxmoewkqkyaghvrndgfluvszc", "tjxmoewfqkhaihvrndgflubhzc",
            "jjqmoewpqkyaihvrndzflubszc", "tjxmoewmqksaihvcndgflubszc", "tjrmoewpqkyaihvrvdgflubzzc",
            "tjxxoewpqkyaiiwrndgflubszc", "cjxmoawxqkyaihvrndgflubszc", "tjxdoewpvkyaihvrndgflubsoc",
            "tjxmsewpqkyaihvrndgfluzozc", "tjxmoewpqkyafhvrnyeflubszc", "tjxmlewpqkyawhvondgflubszc",
            "tjxmonwpqkyaiqvrnxgflubszc", "tjxmoewcqkyaihvrnjgflumszc", "tjvmoewpqkyaihveadgflubszc",
            "tjxmogfpqkyaigvrndgflubszc", "tybmoewpqkyaihvrndgllubszc", "tjxmoewpdkyaihvrndgfluwbzc",
            "etxmbewpqkyaihvrndgflubszc", "tjxmoeapqcynihvrndgflubszc", "tbxmoewpqkyaihvrndgfdebszc",
            "haxmoewpqyyaihvrndgflubszc", "ojxmoewpqkyaihvrnegflubszr", "tjxmoewpqkyaihvrndoflubarc",
            "ljxmoewpqkykihvrndgflvbszc", "tjxmovwpqkyaihvrndgfluzsyc", "tvxmoewpqkyanhvrkdgflubszc",
            "tjxmoewpqkyaihkrndgfluwwzc", "zjxmoewpfkyaihvrndgfrubszc", "tjxyoegpqkyaihvrndlflubszc",
            "tjxmoewpqkyamhvrnsgflubmzc", "tjmmoewpqkyaihvrndgftuwszc", "tjxmoewpqbraihvrncgflubszc",
            "tjxmeeepqkyainvrndgflubszc", "tjemoegpqkyaihvredgflubszc", "tjxmoewpqkyaihvdndgfzubqzc",
            "tjxmoegrqkyaihfrndgflubszc", "tjxmoewpqxyaihvrndgfluyvzc", "qjxmoewpqkyaiwvrnfgflubszc",
            "tjxwoewpqkyashkrndgflubszc", "tjzmoewiqkyaihurndgflubszc", "tjumuewpqkyaihvrndgflubssc",
            "tyxooewpukyaihvrndgflubszc", "tjxvoewpqkyaiivindgflubszc", "ijxmoqwpqkyaihvradgflubszc",
            "tjxmlewpqkyaihvrhdgflubwzc", "tjxmkewpqkyajhqrndgflubszc", "tjxmoewpqkqaiherndgflurszc",
            "tjamoewpqkyaizvondgflubszc", "tjxgogwpqkyalhvrndgflubszc", "tjxmoewpqkyachvrndgflubuzq",
            "tjxmowqpqkyaihvrnegflubszc", "mjxmoewpwkyaihvrndgfkubszc", "tpbmoewpqkyaihvrzdgflubszc",
            "tjbmoewpqkyaiuvrndgflsbszc", "tjxmoewpqklaghvrndgflubazc", "tjxmoewpqkyrihvrndgwlpbszc",
            "tjcmoewpqksaiyvrndgflubszc", "tjxmoeapqkymihvindgflubszc", "tjxmdewpqkyafhvrndgflqbszc",
            "tjxmoewpqxyaihvrndsflubszi", "tjxmoeppqkyaihvrcdgflubszd", "tjxmomwpqkyainvrmdgflubszc",
            "tjxmovwpqkyaihvrndgfdubdzc", "tjxmoewwqkiaihvrjdgflubszc", "tmxmoewpqkyaifvrndgflubszs",
            "tbxmoewpqkyaihvrbdgflunszc", "tjxmoewrqkyaihvxndgflubszp", "ujxmoewpqkyaihvxndgflubpzc",
            "tdxmotwpqkyaihvdndgflubszc", "tjxmvewpqkyaihfrndgtlubszc", "tjfmoewpqkyaihvrnyqflubszc",
            "tjxfolwzqkyaihvrndgflubszc", "ojrmoiwpqkyaihvrndgflubszc", "tjsmoqwpqkyqihvrndgflubszc",
            "tjxmohwpqkyaihvrudgflubslc", "tjxtoiwpqkyaihvrnogflubszc", "taxmoewpqkyaiyvrndgfwubszc",
            "tjxwnezpqkyaihvrndgflubszc", "tjxmyevpqkyaivvrndgflubszc", "tjxdoeopqkyaihvgndgflubszc",
            "tjxaoewpqkmaihvrndgflufszc", "tjxmoewpqkyaxhvrndgflubncc", "tjxmoewpqkyaihurndgflubbjc",
            "tjxmjewpqgyaihvrnngflubszc", "tjxmogwpqkyaihvrndgflubbcc", "tjxmoewplkyaihvrnpgflibszc",
            "tjwmoewpqkyaohvrndgfbubszc", "tjwmoewpqkyaihvrndgfsubszm", "tjxmogwpqkyaihvrndiflubqzc",
            "tjxmoewpqkyaihvrndgflopshc", "rjxmlewpvkyaihvrndgflubszc", "tjxmogwpakyaihvrndgflzbszc",
            "tjxmoeppqkyaihvrndgflmxszc", "tjxmoewpqkyhihgrndgfzubszc", "tjxqoewpqkyaihtrndgwlubszc",
            "tjxnoespqkyaihvrndgflubsuc", "tjmmoewpqkraihvrndgflfbszc", "tjxmoewnqkwaihvrndgflubstc",
            "tjxmoewpqqyaihvrndgfljbszi", "tjxmoewpqkyaihkrkdgalubszc", "tjxmoewpqkyaihvradgjlurszc",
            "tvxmoewpqkybihvrndbflubszc", "tjxvoewpqkyaihvradgfoubszc", "tjxmoewpqfyaihvlodgflubszc",
            "tjxmoewmnkyaiivrndgflubszc", "kjxmoewpqkyaihprndgflcbszc", "hjxmoewpqkcaihvrndgvlubszc",
            "tjxmoewcqkyaihvrncgfllbszc", "tuxmoewpckyaihvrndoflubszc", "tjxmdewpokyaihvrndgflubszn",
            "mjxmaewpqkyaqhvrndgflubszc", "tjxmoewpmzyaihvrndgfiubszc",
            "tjxmoewnqkyvihvrndgflubszk", "tjxmoewpmnyaihvrndgftubszc", "zjxmoewpqkysihvrndgfmubszc",
            "tjxmoewpqkyaihzrntgflubbzc", "tjxmoewpqkgaihwrndsflubszc", "tjxjoewpqkyaihvrndgflgbizc",
            "oqxmoewpqkyaihvrndgfldbszc", "wjamoewpqkyaihvfndgflubszc", "tjxmoewtmkyvihvrndgflubszc",
            "tjlmojwpqkyaihvrndgfludszc", "tjxmowwpqkyaihvrndefludszc", "tjxmoewpqkbaihvrndgfluaszt",
            "tjxmoewpqkzaahvrodgflubszc", "tjxmoewpqkgaihvrndgflubtpc", "tjxmoenpqkyaihcrndgfqubszc",
            "tbxmoewpqbyaihvrndgalubszc", "tjvmoewqqkyaihvrndvflubszc", "tjxmoewpqkeaihvundgfaubszc",
            "txxmoewpqkyaihvrwdgflpbszc", "tzxmoewpqkijihvrndgflubszc", "tjxmoewoqkytiuvrndgflubszc",
            "tjxmrejplkyaihvrndgflubszc", "tjxmoewpqkynihvrpxgflubszc", "tjxmoewpqkvanhvrndgvlubszc",
            "tjxmoewpdkyiihvrndgflubszs", "tpxmyewpqkyaihvrndgfeubszc", "tpxmoewpqyyaihvrndhflubszc",
            "tjsmoewpqkyaihvrndhflubnzc", "tjxmoewpukyaihvrnmgflubwzc", "txxmoewpqlyaihwrndgflubszc",
            "tjxmoewprkyaiovrndgflubxzc", "tjxmouwpqkyaihzrodgflubszc", "tjxmojwpqkywimvrndgflubszc",
            "tjxsoewpqkyaihvrzdgqlubszc", "tfxmoewpakyaihvrndgllubszc", "tjhmoewpqiyaihvrndgflubsac",
            "tjxmoewpqkoaihvrndoflubsxc", "tjxmoewpqkyzpjvrndgflubszc", "tjxmoewpqkyaiharndgzlnbszc",
            "tjimoevpqkyaihvrndgflubbzc", "tjxsoewpqkyahhvrndgfzubszc", "txxmoewpqkyaimvrrdgflubszc",
            "tjxmoewpwkyaihvrndpylubszc", "tjxmoewpskyaghvrndgfbubszc", "tjxmuewpqmyaihvrndgfyubszc",
            "tjxmoewpqkyaihvdndgglubsxc", "xjxmoewpqkyjiovrndgflubszc", "gjxmoewpqkyaihvrndodlubszc",
            "tjbmoewpqkyaihvridgflvbszc", "tjxmozwpqkyapbvrndgflubszc", "tjxeoewpqkyqihvrndgflubhzc",
            "tjxdoewpqzyaihvrndgflubsmc", "tjxmwewpqkyathvcndgflubszc", "tjxmoewpszyaihvrndgflusszc",
            "tuxmoewpqkyaihvrndgfluasxc", "tjemoewpnvyaihvrndgflubszc", "tjxmoewpjkyaihvrndgjlufszc",
            "tjomoewppkyaihvzndgflubszc", "tjxmvewpqkyaimvrntgflubszc", "rjxmoewpqkyaihvpndgflubszq",
            "hjxzoewpqkyaihvridgflubszc", "texmoejpqkyaihvrndgflubszx", "tjxcoewpqkyaihbrxdgflubszc",
            "tjxmoewpnkyaihvrndgfltbsze", "tjxmoewpdkyaihvrndwfluwbzc", "tjxmoewpqryjihkrndgflubszc",
            "tjlmoewpqkhaihvrndgflubsnc", "tjxmovapqkjaihvrndgflubszc", "tjxvoewpqkyaihqrndgfluyszc",
            "tjxwoewnqkyaihvrndgfgubszc", "tjdmoewpqklaihvcndgflubszc", "tjxmoewpvkynihvrndgflubskc",
            "tjxmtewpqkyaihvhndgfluaszc", "tjxmoewpqkyanhvrnpgfluvszc", "tjxmoewpqkyaifvbndgflubspc",
            "tjxmoexpqknaihvrndgxlubszc", "qjxmoewqqkyaihvrndgflubpzc", "tjxmoewppkyaihvaxdgflubszc",
            "myxmoewpqkyaihvrudgflubszc", "tjxmwewpmkyaihvrndgflubssc", "tjxmoewpqkyaihvrndgfxqbszq",
            "tjxmoewhqkyaahvrndgflubbzc", "tbxmoewmqkyaihvrndgflubszu", "toxmolwpqkyaihvrndnflubszc",
            "tjxmoewhqkyaihvrnrgflubvzc", "yjxmoewcqkyaihvrndgflubfzc", "tjxmoewpqkyamhvrgdgflmbszc",
            "tjxmtewpqkyaizvrndgfluoszc", "tjxmoewpqzyaihvrntsflubszc", "fjxmoewpqkyaihyrmdgflubszc",
            "tjxwoewpqcyaihbrndgflubszc", "tjxmoebpqkzaihvrndcflubszc", "tjxmoewpqkyaihvrndnlmubszc",
            "tjxmoewpqkyaihvrndgeyubskc", "tfxmoewpqryaihvrndgfluiszc", "tjxmoewpqkjaihvynngflubszc",
            "tjxmoewpqkqaihvonjgflubszc", "tjfmokwpqkyeihvrndgflubszc", "djxmoewpkkyaihvrnmgflubszc",
            "tjxmiewpqkyaihvrndgflubhlc", "tjxmmejpqkyaihvrnhgflubszc", "djxmoewmqkyaihvrnggflubszc",
            "tjxmoewpqkyaihvrkggflubsze", "gjxmoewpqkyaihjrndgflvbszc", "tjxmoewpqkyaidvrndgkzubszc",
            "tjxmoewpqkyaedvrnpgflubszc", "sjxmoewpqkyaihvrnngfluhszc", "tjxmoewpqkuaihvrndghlubxzc",
            "tjxmoewgqkyuihvrndgftubszc", "tjxmoewpqsyaifvrkdgflubszc", "tjxrrewpqkyaihvrnpgflubszc",
            "tjxmoezpqkyaihvrwdgflabszc", "tjfmoewpqknaihvrndgflubkzc", "tjxmoewnqkxaihvrndgflubtzc",
            "tjxmoewpkkyaihvrndgfrnbszc", "tjxmorwpnkqaihvrndgflubszc", "tsxmoewwqkyathvrndgflubszc",
            "tjxmoeupqkyaihvrndyflubszp", "bjxmoewdqkyaihvrndgflurszc", "tjxmoewpvkyaihvrndoflubszq",
            "sjxmoewpqkyaihvrndgflubyec", "tjxmoewpqkyaizcrndgfnubszc"]

list1_IDs = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

two, three = 0, 0
twice, thrice = [], []
for ID in list_IDs:
    twiceappeared, thriceappeared = False, False
    if len(ID) == len(set(ID)):
        pass
    else:
        for letter in sorted(set(ID)):
            appears = ID.count(letter)
            if appears != 2 and appears != 3:
                pass
            else:
                if appears == 2 and not twiceappeared:
                    twiceappeared = True
                    two += 1
                elif appears == 3 and not thriceappeared:
                    thriceappeared = True
                    three += 1
print(two * three)
