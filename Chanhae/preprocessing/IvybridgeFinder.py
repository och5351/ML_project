import pandas as pd
import numpy as np

if __name__ == '__main__':

    var = ['MD101KH', 'ME664KH', 'MD224KH', 'ME665KH', 'MD232KH']

    data = pd.read_csv('data/train.csv', na_values = ['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null', '']).replace('하스웰(4세대리프레시)', '하스웰(4세대,리프레시)')

    data = pd.DataFrame(data)
    nameData = []
    data['codename'] = data['codename'].astype(str)

    for index, row in enumerate(data.itertuples()):

        for x in var:
            if x in row[2]:
                if str(data.iat[index,6]) == 'nan':
                    # data.iloc[index][7] = '아이비브릿지(3세대)'
                    # data.loc[index][6] = '아이비브릿지(3세대)'
                    # data['codename'][index] = '아이비브릿지(3세대)'
                    data.iat[index,6] = '아이비브릿지(3세대)'
                    print(index, '//' ,row[2], '//', data.iat[index, 6], '//', type(data.iat[index, 6]))

    data2 = pd.read_csv('data/test.csv', na_values=['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null', '']).replace('하스웰(4세대리프레시)', '하스웰(4세대,리프레시)')

    for index, row in enumerate(data2.itertuples()):

        for x in var:
            if x in row[2]:
                if str(data2.iat[index,6]) == 'nan':
                    data2.iat[index, 6] = '아이비브릿지(3세대)'
                    print(row[2], '//', data2.iat[index, 6], '//', type(data2.iat[index, 6]))

    print(data.shape)

    data.to_csv('data/editData/train.csv', index=False)
    data2.to_csv('data/editData/test.csv', index=False)

