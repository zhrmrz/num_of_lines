class Sol:
    def num_of_lines(self, widths,s):
        line,width=0,100
        for char in s:
            c_len=widths[ord(char)-ord('a')]
            if c_len+width>100:
                line+=1
                width=0
            width+=c_len
        return [line,width]

if __name__ == '__main__':
    p = Sol()
    print(p.num_of_lines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))
