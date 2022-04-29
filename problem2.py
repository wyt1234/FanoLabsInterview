# 分割字符串
def split_multi(line, split_symbol_list=None):
    if not split_symbol_list:
        split_symbol_list = [' ', '.', '/', '*', '?']
    temp = []
    result_list = []
    for s in line:
        if s in split_symbol_list:
            result_list.append(''.join(temp))
            temp = []
        else:
            temp.append(s)
    return result_list


# 计数，取topk
def word_count(file_name: str, k: int):
    '''计数'''
    word_dic = {}
    with open(file_name) as f:
        symbol = True
        while symbol:
            line = f.readline()
            for word in split_multi(line):
                if word in list(word_dic):
                    word_dic[word] += 1
                else:
                    word_dic[word] = 1
            if not line:
                symbol = False
    # print(word_dic)
    '''取topk'''
    topk_num_list = list(set(word_dic.values()))
    topk_num_list.sort(reverse=True)
    word_list = [{'word': word, 'count': word_dic[word]} for word in list(word_dic) if
                 word_dic[word] in topk_num_list]
    word_list = sorted(word_list, key=lambda x: x['count'], reverse=True)
    return word_list


if __name__ == '__main__':
    word_list = word_count('test.txt', 3)
    print(f"结果列表为{word_list}")
