class photo:
    def __init__(self, i, or, tags):
        self.index = i
        self.tags = set(tags)
        self.or = or

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

        for p in p_list:
            self.tags |= p.tags



def score(sl):
    if sl.index == N
    set1 = set(sl.tags)
    set2 = set(sl_list[sl.index + 1].tags)

if __name__ == "__main__":
    pass
    #Comment
    photo_list = []
    file = open("")
