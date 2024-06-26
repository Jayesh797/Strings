def frequencySort(self, s):
        res=""
        c=Counter(s)
        c_list = sorted(c.items(), key=lambda item: item[1], reverse=True)
        # print(c_list)
        # print(list(c))
        res=''.join([char*freq for char,freq in c_list])
        return res