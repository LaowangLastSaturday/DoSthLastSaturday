# coding=utf-8
import requests
import re

# 创建输出文件
output = open('%s.txt' % "US_cs_is", 'w')

# 提取大学排名信息
# rank_information.txt 内容为谷歌浏览器网页源代码直接
# 提取的大学信息
with open('mit nb') as file_obj:
    ranking_content = file_obj.read()


# 定义录入大学学生数量信息function
def find_population(sub_url, title):
    url = 'https://www.topuniversities.com%s' % sub_url
    response = requests.get(url)
    html = response.text
    international_students_population = re.findall(r'<h4>International students - (.*?)</h4>', html) [0]
    international_students_distribute = \
        re.findall(r'<div class="grpst"><div class="gr"><div> (.*?)</div><label>UG students</label>', html, re.S) [1]

    output.write(title)
    output.write("  ")
    output.write(":%s:" % international_students_population)
    output.write("%s:" % international_students_distribute)
    output.write('\n')


# 查找目标内容
ranking_information = re.findall(r'<a class="title" href="(.*?)">(.*?)<', ranking_content)

# 开始录入
for single_uni in ranking_information:
    uni_url, uni_title = single_uni
    find_population(uni_url, uni_title)