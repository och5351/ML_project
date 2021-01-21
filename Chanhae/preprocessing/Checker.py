import pandas as pd
#5: core | 6: codename | 7: GHz




def columnChecker(data, column):
    i = 0
    while (True):
        if str(data.iat[i, column]) != 'nan':
            print(i, data.iat[i, column], type(data.iat[i, column]))
            break

        i += 1

if __name__ == '__main__':
    data = pd.read_csv('./data/editData/train.csv', na_values=['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null', ''])
    columnChecker(data,6)
    print(data['codename'].unique())