import requests
from bs4 import BeautifulSoup as bs
import csv
from urllib.parse import unquote

def get_soup(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    html = req.text
    soup = bs(html, 'html.parser')
    return soup

def pro_parse(wr):
    # 맥북 프로 파싱 (2011~2020)
    url = "https://namu.wiki/w/MacBook%20Pro/%EC%97%AD%EB%8C%80%20%EB%AA%A8%EB%8D%B8"
    soup = get_soup(url)

    generation_url_bundle = soup.find_all("div",class_ = "wiki-paragraph")

    for generation_url in generation_url_bundle[8:]:
        url = "https://namu.wiki" + generation_url.find_all("a")[1]["href"]
        soup = get_soup(url)
        
        wr.writerow([unquote(url.split("/")[-1]), url])
        table_bundle = soup.find_all("tbody")

        for table in table_bundle:
            data_list = list()
            index_list = list()

            # 모델명 추가(일부 데이터 수동 작업 필요)
            name = table.previous_element.previous_element.previous_element
            index_list.append("모델명")
            data_list.append(name)

            row_count = 0

            tr_bundle = table.find_all("tr")
            for tr in tr_bundle:
                td_bundle = tr.find_all("td")

                try:
                    if td_bundle[0]["rowspan"]:
                        row_count += -int(td_bundle[0]["rowspan"])
                except:
                    pass

                for idx, td in enumerate(td_bundle):
                    # 한 행에 여러 줄 있을경우 수동 작업 필요
                    if row_count < 0:
                        for i in range(-row_count):
                            index_list.append(td.text)
                        row_count = -row_count
                    elif row_count > 0:
                        data_list.append(td.text)
                        row_count -= 1
                    else:
                        if (idx % 2 == 0):
                            index_list.append(td.text)
                        else:
                            data_list.append(td.text)

            wr.writerow(index_list)
            wr.writerow(data_list)

def air_parse(wr):
    # 맥북 에어 파싱 (2011~2020)
    url = "https://namu.wiki/w/MacBook%20Air/%EC%97%AD%EB%8C%80%20%EB%AA%A8%EB%8D%B8"
    soup = get_soup(url)

    generation_url_bundle = soup.find_all("div",class_ = "wiki-paragraph")

    for generation_url in generation_url_bundle[5:]:
        try:
            url = "https://namu.wiki" + generation_url.find_all("a")[1]["href"]
            soup = get_soup(url)

            wr.writerow([unquote(url.split("/")[-1]), url])
            table_bundle = soup.find_all("tbody")

            for table in table_bundle:
                data_list = list()
                index_list = list()

                # 모델명 추가(일부 데이터 수동 작업 필요)
                name = table.previous_element.previous_element.previous_element
                index_list.append("모델명")
                data_list.append(name)

                row_count = 0

                tr_bundle = table.find_all("tr")
                for tr in tr_bundle:
                    td_bundle = tr.find_all("td")

                    try:
                        if td_bundle[0]["rowspan"]:
                            row_count += -int(td_bundle[0]["rowspan"])
                    except:
                        pass

                    for idx, td in enumerate(td_bundle):
                        # 한 행에 여러 줄 있을경우 수동 작업 필요
                        if row_count < 0:
                            for i in range(-row_count):
                                index_list.append(td.text)
                            row_count = -row_count
                        elif row_count > 0:
                            data_list.append(td.text)
                            row_count -= 1
                        else:
                            if (idx % 2 == 0):
                                index_list.append(td.text)
                            else:
                                data_list.append(td.text)

                wr.writerow(index_list)
                wr.writerow(data_list)
        except:
            pass

def main():
    f = open('output.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)

    pro_parse(wr)
    air_parse(wr)

    f.close()

if __name__ == "__main__":
    main()