import pandas as pd
import csv

if __name__ == '__main__':

    # f = open('../Jeonghoon/complete.csv','rt', encoding='utf-8')
    # reader = csv.reader(f)
    #
    # csv_list = []
    # for l in reader:
    #     csv_list.append(l)
    #
    # f.close()
    #
    # df = pd.DataFrame(csv_list)
    #
    # for idx, x in enumerate(df[2]):
    #     if '인치' not in x:
    #         print(idx,'//',x)

    data = pd.read_csv('../Inho/train_display.csv', na_values=['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null', ''])


    for x in data['display']:
        if '인치' not in str(x) and str(x) != 'nan':
            print(x, type(x))