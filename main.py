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

    tags_left = set()
    tags_right = set()
    p_V_left = []
    p_V_right = []
    for i in range(len(p_V_list)):
        '''
        max = 0
        if p_taken[i]:
            continue
        p_max = i

        for j in range(len(p_V_list)):
            if (i != j and p_taken[i] == False and p_taken[j] == False):

                if (len(p_V_list[i].tags | p_V_list[j].tags) >= max):
                    max = len(p_V_list[i].tags | p_V_list[j].tags)
                    p_max = j
                    break

        res.append(slide([p_V_list[i], p_V_list[p_max]]))
        p_taken[i] = True
        p_taken[p_max] = True
        '''
        if p_V_list[i].tags & tags_left > p_V_list[i].tags & tags_right:
            p_V_left.append(p_V_list[i])
        else:
            p_V_right.append(p_V_list[i])

    while (len(p_V_left) > len(p_V_right)):
        p_V_right.append(p_V_left[0])
        del p_V_left[0]

    while (len(p_V_right) > len(p_V_left)):
        p_V_left.append(p_V_right[0])
        del p_V_right[0]

    for i in range(len(p_V_left)):
        res.append(slide([p_V_left[i], p_V_right[i]]))
    print("make sl done.")
    return res

if __name__ == "__main__":

    photo_list = []
    file_input = open("e_shiny_selfies.txt","r")
    N = file_input.readline()
    N = int(N)
    tag_dict = {}
    for i in range(0,N):
        temp_list = [x for x in file_input.readline().split(" ")]
        temp_list[len(temp_list)-1] =  temp_list[len(temp_list)-1][:-1]
        photo_list.append(photo(i,temp_list[0],temp_list[2:]))
    file_input.close()
    #print(photo_list)
    #print(tag_dict
    sl_list = make_sl_list(photo_list)
    #print(sl_list)
    for i in range(len(sl_list)):
        for tag in sl_list[i].tags:
            if tag not in tag_dict:
                tag_dict[tag] = [i]
            else:
                tag_dict[tag].append(i)
    output_sl = []
    n = 0
    while (n < len(sl_list)):
        if sl_list[i].occup == 1:
            continue
        index_dict = {}
        for tag in sl_list[i].tags:
            for index in tag_dict[tag]:
                if sl_list[index].occup:
                    continue
                if index not in index_dict:
                    index_dict[index]=1
                else:
                    index_dict[index]+=1
        print(i)
        max = list(index_dict.keys())[0]
        max_val = 0
        for index in index_dict:
            if max_val <= index_dict[index] and max != index:
                if sl_list[max].occup == 1:
                    continue
                max = index
            #print("\n{}\n".format(max))
        if i == max:
            continue
        sl_list[i].occup = 1
        sl_list[max].occup = 1
        output_sl.append(sl_list[i])
        output_sl.append(sl_list[max])
        
    output_file = open("output.txt","w")
    output_file.write(str(len(output_sl)))
    output_file.write("\n")



    for slide in output_sl:
        for i in range(0,len(slide.p_i_list)):
            if i != 0:
                output_file.write(" ")
            output_file.write(str(slide.p_i_list[i]))
        output_file.write("\n")
    output_file.close()
