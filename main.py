class photo:
    def __init__(self, i, orien, tags):
        self.index = i
        self.tags = set(tags)
        self.orien = orien

    def __repr__(self):
        return "index = {}\t orien = {}\t tags = {}\n".format(self.index,self.orien,self.tags)


class slide:
    def __init__(self, p_list):
        if len(p_list) > 2 or len(p_list) < 1:
            print("wrong number of photos for slide")
            return
        if len(p_list) == 2:
            if p_list[1].orien != 'V' or p_list[1].orien != 'V':
                print("not two verticals for slide")
                return
        self.tags = set()
        self.occup = 0
        self.p_i_list=[]
        for p in p_list:
            self.p_i_list.append(p.index)
            self.tags |= p.tags

    def __repr__(self):
        return '{}'.format(self.tags)

def score(sl):

    if sl.index == len(sl_list):
        return 0

    set1 = set(sl.tags)
    set2 = set(sl_list[sl.index + 1].tags)
    return min(len(set1 & set2), len(set1 - set2), len(set2 - set1))

def make_sl_list(p_list):
    res = []
    p_V_list = []
    for p in p_list:
        if p.orien == 'H':
            res.append(slide([p]))
        else:
            p_V_list.append(p)
    p_taken = [False for i in range(len(p_V_list))]
    for i in range(len(p_V_list)):
        max = 0
        if p_taken[i]:
            continue
        p_max = i
        for j in range(len(p_V_list)):
            if (i != j and p_taken[i] == False and p_taken[j] == False):
                if (len(p_V_list[i].tags | p_V_list[j].tags) >= max):
                    max = len(p_V_list[i].tags | p_V_list[j].tags)
                    p_max = j
        res.append(slide([p_V_list[i], p_V_list[p_max]]))
        p_taken[i] = True
        p_taken[p_max] = True

    return res

if __name__ == "__main__":

    p_list = [photo(i, 'V', [j for j in range(i)]) for i in range(10)]

    sl_list = make_sl_list(p_list)

    print(sl_list)
