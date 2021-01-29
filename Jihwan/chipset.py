import csv

def chipset_writer(file_name):

    m1_tag = ["M1","A2338","MYDA2","MYDC2","MYD82","MYD92","A2337","MGN63","MGND3","MGN93","MGN73","MGNE3","MGNA3"]

    f_chipset = open(file_name.replace(".csv", "_chipset.csv"), 'w', encoding='utf-8', newline='')
    wr = csv.writer(f_chipset)

    f = open(file_name, 'r', encoding='utf-8')
    csv_file = csv.reader(f)

    for line in csv_file:
        name = line[1]
        chipset = line[9]

        if chipset == "":
            if name.upper() in m1_tag:
                chipset = "애플"
            else:
                chipset = "인텔"
        elif chipset == "AMD":
            chipset = "인텔"

        line[9] = chipset

        wr.writerow(line)
        #print(line)

    f.close()
    f_chipset.close()

def main():
    chipset_writer("test.csv")
    chipset_writer("train.csv")

if __name__ == "__main__":
    main()
