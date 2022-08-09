def generate_phrase(characters, phrase):
    sorted_c = sorted(characters)
    sorted_p = sorted(phrase)
    print(sorted_c)
    print(sorted_p)

    comparison_lst = []

    for item in sorted_p:
        if item in sorted_c:
            sorted_c.remove(item)
            comparison_lst.append(item)   # print(True)

    if sorted_p == comparison_lst:
        print(True)
    else:
        print(False)


generate_phrase('e!m4675xf tma', 'mmea 4!')