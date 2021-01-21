import pandas as pd

# iterrows / itertuples
# for column_name, item in mainData.iteritems():

if __name__ == '__main__':
    data = pd.read_csv('data/train.csv', na_values = ['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null', ''])
    # 하스웰(4세대,리프레시)로 통일
    mainData = data[['name','core',"codename",'cpu(GHz)','chipset']].replace('하스웰(4세대리프레시)', '하스웰(4세대,리프레시)')

    # CPU codename 존재하는 제목 담을 배열
    nameWithCodeName = []

    # codename 열 Unique
    primaryVar = mainData['codename'].unique()
    primaryVar = primaryVar[1:]

    # Index, name, codename 데이터 생성
    for row in mainData.itertuples():
        if row[3] in primaryVar:
            nameWithCodeName.append((row[0],row[1],row[3]))

    df2 = pd.DataFrame(nameWithCodeName)  # 데이터 프레임 작성

    # CPU 제목 정리
    for cpu in primaryVar:

        textName = 'codenameFolder/'+cpu+'.txt'
        f = open(textName, 'w', encoding='utf-8')
        for rows in df2.itertuples():
            if rows[3] == cpu:
                data = str(rows[2])+"\n"
                f.write(data)
        f.close()
    data = pd.read_csv('data/test.csv', na_values=['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan', '-NaN', 'null', ''])
    mainData = data[['name', 'core', "codename", 'cpu(GHz)', 'chipset']].replace('하스웰(4세대리프레시)', '하스웰(4세대,리프레시)')
    primaryVar = mainData['codename'].unique()
    primaryVar = primaryVar[1:]
    nameWithCodeName = []
    # Indes, name, codename 데이터 생성
    for row in mainData.itertuples():
        if row[3] in primaryVar:
            nameWithCodeName.append((row[0],row[1],row[3]))

    df2 = pd.DataFrame(nameWithCodeName)

    for cpu in primaryVar:
        textName = 'codenameFolder/'+cpu+'.txt'
        f = open(textName, 'a', encoding='utf-8')
        for rows in df2.itertuples():
            if rows[3] == cpu:
                data = str(rows[2])+"\n"
                f.write(data)
        f.close()
