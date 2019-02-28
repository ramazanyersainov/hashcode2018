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
            if  not (p_list[0] == 'V' and p_list[1] == 'V'):
                print("not two verticals for slide")
                return
        self.tags = set()

        self.p_i_list=[]


        for p in p_list:
            self.p_i_list.append(p.index)
            self.tags |= p.tags



def score(sl):

    if sl.index == len(sl_list):
        return 0

    set1 = set(sl.tags)
    set2 = set(sl_list[sl.index + 1].tags)
    return min(len(set1 & set2), len(set1 - set2), len(set2 - set1))

if __name__ == "__main__":

    photo_list = []
    file_input = open("a_example.txt")

    N = file_input.readline()
    N = int(N)

    for i in range(0,N):
        temp_list = [x for x in file_input.readline().split(" ")]
        temp_list[len(temp_list)-1] =  temp_list[len(temp_list)-1][:-1]
        photo_list.append(photo(i,temp_list[0],temp_list[2:]))

    print(photo_list)
    #for i in range(0,N):
