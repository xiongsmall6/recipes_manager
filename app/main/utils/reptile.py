import requests
from lxml import etree
import re


def reptile_food(page):
    food_list = list()
    for index in range(1, page):
        html = requests.get("https://home.meishichina.com/recipe/ertong/page/{0}/".format(index))
        html.encoding = "utf-8"
        if html.status_code != requests.codes.ok:
            continue
        etree_html = etree.HTML(html.text)
        content = etree_html.xpath('//*[@id="J_list"]/ul/li/div/a/@href')
        print(content)
        for each in content:
            data = dict()
            html2 = requests.get(each)
            if html2.status_code != requests.codes.ok:
                continue
            html2.encoding = "utf-8"
            etree_html2 = etree.HTML(html2.text)
            food_name = etree_html2.xpath('//*[@id="recipe_title"]/text()')
            if len(food_name) == 0:
                continue
            else:
                data['food_name'] = replace_str(food_name[0].replace("#", "").replace("信任之美", ""))
            food_image = etree_html2.xpath('//*[@id="recipe_De_imgBox"]/a/img/@src')
            data['food_image'] = food_image[0]
            food_info = etree_html2.xpath('//*[@id="block_txt1"]/text()')
            if len(food_info) == 0:
                continue
            else:
                data['food_info'] = replace_str(food_info[0])
            food_material = etree_html2.xpath('//*[@class="particulars"]/div/ul/li/span[1]/a/b/text()')
            food_material_num = etree_html2.xpath('//*[@class="particulars"]/div/ul/li/span[2]/text()')
            food_material_list = list()
            for i in range(len(food_material)):
                food_material_list.append({'material_name': food_material[i], 'material_unit': food_material_num[i]})
            data['food_material'] = food_material_list
            food_step_image = etree_html2.xpath('//*[@class="recipeStep"]/ul/li/div[1]/img/@src')
            food_step_text = etree_html2.xpath('//*[@class="recipeStep"]/ul/li/div[2]/text()')
            food_step_list = list()
            for j in range(len(food_step_text)):
                food_step_list.append(
                    {"step_num": (j + 1), "step_info": replace_str(food_step_text[j]), "step_image": food_step_image[j]})
            data['food_step'] = food_step_list
            food_type = etree_html2.xpath('//*[@class="recipeTip mt16"]/a/text()')
            if '早餐' in food_type or ('烘焙' in food_type and '晚餐' not in food_type and '午餐' not in food_type):
                data['food_type'] = 1
            elif '晚餐' in food_type:
                data['food_type'] = 3
            else:
                data['food_type'] = 2
            food_list.append(data)
    return food_list


def replace_str(item):
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9.,!@#。，：“”"",,《《》》！；;]")  # 匹配不是中文、大小写、数字的其他字符
    return cop.sub('', item)  # 只保留中文数字 应为和部分标点


def ge_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    }
    response = requests.get("https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0&genres=剧情"
                        ,headers=headers)

    print(response.text)


if __name__ == "__main__":
    ge_data()
