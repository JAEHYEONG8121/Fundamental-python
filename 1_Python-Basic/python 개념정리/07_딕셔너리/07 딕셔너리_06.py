singer = {}
singer['이름'] = input('가수 이름 입력: ')
singer['구성원'] = input('인원수 입력: ')
singer['대표곡'] = input('대표곡 입력: ')
for i in singer.keys() :
    print('%s : %s' % (i, singer[i]))
print(singer)