def dic_func(**par) :
    print('type(par):', type(par))
    for k in par.keys() :
        print('{} : {} 명입니다'.format(k, par[k]))
        
dic_func(똭뚝뽹 = 123, 꿔익꿔익 = 8, test = '테스뚜')
