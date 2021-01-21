import pandas as pd
import numpy as np

if __name__ == '__main__':
    # 하스웰(4세대,리프레시) 제품군 코드 담는 배열
    var = []
    # 하스웰(4세대,리프레시) 기입되어있는 name data open
    f = open('./codenameFolder/아이스레이크.txt', 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        code = line.split()[-1].replace('/B','').replace('/A','').replace('(','').replace(')','').replace('구매가능','').replace('가능','').replace('재고보유','').replace('512GB','').replace(']','')
        if code not in var and code != '':
            var.append(code)

    f.close()

    data = pd.read_csv('data/train.csv', na_values = ['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null', '']).replace('하스웰(4세대리프레시)', '하스웰(4세대,리프레시)')

    data = pd.DataFrame(data)
    nameData = []
    data['codename'] = data['codename'].astype(str)

    for index, row in enumerate(data.itertuples()):

        for x in var:
            if x in row[2]:
                if str(data.iat[index,6]) == 'nan':
                    data.iat[index,6] = '아이스레이크'
                    print(index, '//' ,row[2], '//', data.iat[index, 6], '//', type(data.iat[index, 6]))

    data2 = pd.read_csv('data/test.csv', na_values=['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null', '']).replace('하스웰(4세대리프레시)', '하스웰(4세대,리프레시)')

    for index, row in enumerate(data2.itertuples()):

        for x in var:
            if x in row[2]:
                if str(data2.iat[index,6]) == 'nan':
                    data2.iat[index, 6] = '아이스레이크'
                    print(index, '//', row[2], '//', data2.iat[index, 6], '//', type(data2.iat[index, 6]))

    print(data.shape)

    data.to_csv('data/editData/train.csv', index=False)
    data2.to_csv('data/editData/test.csv', index=False)

