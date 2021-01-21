import requests
from bs4 import BeautifulSoup as bs
import re
import csv

def get_soup(url):
    # user agent 추가
    headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    req = requests.get(url, headers=headers)
    req.encoding = "utf-8"
    html = req.text
    soup = bs(html, 'html.parser')
    return soup

def main():
    # 정리 버전
    f = open('everymac.csv', 'w', encoding='utf-8', newline='')
    # 자세한 버전
    f_log = open('everymac_log.csv', 'w', encoding='utf-8', newline='')

    wr = csv.writer(f)
    wr_log = csv.writer(f_log)

    # 파싱할 목록
    save_tag = ["Processors", "Processor Speed", "Processor Type", "Standard RAM", "Built-in Display", "Standard Storage", "Apple Order No", "Apple Model No", "Form Factor", "Original Price (US)", "Avg. Weight","Introduction Date", "Form Factor"]

    core_expression = re.compile("[0-9](?=[ ][C][o][r][e][s][)])")
    weight_expression = re.compile("[0-9][.][0-9]{1,2}(?=[ ][k][g][)])")

    core_change = {"2":"듀얼코어","4":"쿼드코어","6":"헥사코어","8":"옥타코어"}
    inch_change = {"11":"11인치(27~29cm)","12":"12인치(29~31cm)","13":"13인치(32~35cm)","14":"14인치(33~36cm)","15":"15인치(37~39cm)","16":"16인치(40~42cm)","17":"17인치(43~45cm)"}

    # 맥북 에어 2011~
    url = "https://everymac.com/systems/apple/macbook-air/index-macbook-air.html"
    soup = get_soup(url)

    generation_url_bundle = soup.find_all("span", {"id": "contentcenter_specs_externalnav_wrapper"})[11:]

    # 맥북 프로 2011~
    url = "https://everymac.com/systems/apple/macbook_pro/index-macbookpro.html"
    soup = get_soup(url)

    generation_url_bundle.extend(soup.find_all("span", {"id": "contentcenter_specs_externalnav_wrapper"})[43:])

    # 정리할 목록
    index_list = ["name","core","display","weight(kg)","cpu(GHz)","model_year","price"]

    wr.writerow(index_list)
    wr_log.writerow(save_tag)

    result = list()
    for generation_url in generation_url_bundle:
        log = dict()
        log_select = dict()

        url = "https://everymac.com" + generation_url.a['href']
        soup = get_soup(url)

        #spec_table = soup.find("div",{"id": "contentcenter_specs_table"})

        # 정보 파싱
        pairs = soup.find_all("div",{"id": "contentcenter_specs_table_pairs"})

        for pair in pairs:
            for idx, element in enumerate(pair.find_all("td")):
                if (idx % 2 == 0):
                    tag = element.text.replace(":","")

                    if tag in save_tag:
                        save_flag = True
                    else:
                        save_flag = False
                else:
                    if save_flag:
                        log[tag] = element.text
                        if tag == "Processors":
                            core_count = core_expression.search(element.text).group()
                            log_select["core"] = core_change[core_count]
                        elif tag == "Built-in Display":
                            inch = element.text.split('"')[0].split(".")[0]
                            log_select["display"] = inch_change[inch]
                        elif tag == "Avg. Weight":
                            weight = weight_expression.search(element.text).group()
                            log_select["weight(kg)"] = weight + "kg"
                        elif tag == "Processor Speed":
                            clock_speed = element.text.replace("GHz","").strip()
                            log_select["cpu(GHz)"] = clock_speed
                        elif tag == "Introduction Date":
                            model_year = element.text.split(",")[-1].strip()
                            log_select["model_year"] = model_year
                        elif tag == "Form Factor":
                            log_select["name"] = element.text
                        elif tag == "Original Price (US)":
                            log_select["price"] = element.text
        
        result.append(log_select)
        print(log_select)

        write_list = list()
        for i in index_list:
            write_list.append(log_select[i])
        wr.writerow(write_list)

        write_list = list()
        for i in save_tag:
            write_list.append(log[i])
        wr_log.writerow(write_list)

    f.close()
    f_log.close()

if __name__ == "__main__":
    main()