class photo:
    def __init__(self, i, or, tags):
    def __init__(self, i, orien, tags):
        self.index = i
        self.tags = set(tags)
        self.or = or
        self.orien = orien

class slide:
    def __init__(self, p_list):
        if len(p_list) > 2 or len(p_list) < 1:
            print("wrong number of photos for slide")
            return
        if len(p_list) == 2:
            if  not (p_list[0] == 'V' and p_list[1] == 'V'):
                print("not two verticals for slide")
                return
        self.tags = set()
        self.p_i_list = []
        for p in p_list:
            self.p_i_list.append(p.index)
            self.tags |= p.tags



def score(sl):
    if sl.index == N
    if sl.index == len(sl_list) - 1:
        return 0;
    set1 = set(sl.tags)
    set2 = set(sl_list[sl.index + 1].tags)
    return min(len(set1 & set2), len(set1 - set2), len(set2 - set1))


if __name__ == "__main__":
    pass
    #Comment
    photo_list = []
    file = open("")
    p1 = photo(0, 'H', ['3', '3'])
    p2 = photo(1, 'V', ['3', '3'])
    s1 = slide([p1])
    s2 = slide([p2])
    sl_list = [s1, s2]
    print(score(p1))
