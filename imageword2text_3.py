import pandas as pd
from datetime import datetime
import os

def generate_template(index, text1, text2, text3, url):
    # 使用 :02d 格式化序号，确保是两位数
    formatted_index = f"{index+1:02d}"
    template = f'''
<section class="_editor">
    <section style="margin: 24px 0px 16px; letter-spacing: 0.544px; text-wrap: wrap; background-color: #ffffff; text-align: left; line-height: 1.5em; text-indent: 0em;">
        <span style="font-size: 20px; text-decoration: underline; letter-spacing: 1px; font-family: Optima-Regular, PingFangTC-light;">
            <strong>
                <strong style="font-size: 14px; letter-spacing: 0.544px; text-align: center; caret-color: #ff0000; text-wrap: wrap; background-color: #ffffff;">
                    <strong style="font-family: Optima-Regular, PingFangTC-light; font-size: 45px; letter-spacing: 1px;">
                        {formatted_index}
                    </strong>
                </strong>
            </strong>
        </span>
    </section>
    <p>
        <span style="font-size: 24px; color: #7b0c00; font-family: Optima-Regular, PingFangTC-light;">
            <strong>{text1}</strong>
        </span>
    </p>
    <p>
        <span style="font-size: 12px; font-family: Optima-Regular, PingFangTC-light;">
            {text2}
        </span>
    </p>
    <section style="margin: 8px 0px 32px; letter-spacing: 0.544px; text-wrap: wrap; background-color: #ffffff; text-align: left; line-height: 1.5em; text-indent: 0em;">
        <img src="{url}" style="width: 100%;" />
    </section>
    <p style="line-height: 2em;">
        <span style="font-size: 14px; letter-spacing: 2px; font-family: Optima-Regular, PingFangTC-light;">{text3}</span>
    </p>
</section>
'''
    return template

def add_newlines(text):
    # 确保输入是字符串类型
    text = str(text)
    # 定义需要处理的符号
    symbols = {'。', '！', '？', '，'}
    result = []
    for i, char in enumerate(text):
        result.append(char)
        # 如果当前字符是符号，且不是最后一个字符，则添加两个换行符
        if char in symbols and i != len(text) - 1:
            result.append('\n\n')
    return ''.join(result)

def create_and_export_text(out_path, topic, formatted_copywriting_list, quantity):
    # 获取当前日期
    today_date = datetime.now().strftime("%y%m%d")
    # 创建子文件夹路径，例如 "output/文案-241231"
    subfolder_name = f"{topic}-{today_date}"
    subfolder_path = os.path.join(out_path, subfolder_name)

    # 确保子文件夹存在
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # 文章数量
    text_num = len(formatted_copywriting_list)//quantity
    for i in range(text_num):
        file_name = f"{topic}-{i + 1}.md"
        file_path = os.path.join(subfolder_path, file_name)
        # 循环提取文案图片列表
        text_image_list = formatted_copywriting_list[i*quantity:(i+1)*quantity]
        print(text_image_list)
        # 生成内容
        result = ""
        for j in range(len(text_image_list)):
            print(text_image_list[j])
            result = result + generate_template(
                j, 
                text_image_list[j][0],  # text1
                text_image_list[j][1],  # text2
                text_image_list[j][2],  # text3
                text_image_list[j][3]   # url
            )
        # 将内容写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(result)
        print(f"文件已生成: {file_path}")

if __name__ == '__main__':
    out_path = "Edit_text"
    topic = "文案14"
    # 读取 Excel 文件，并将所有列转换为字符串类型
    copywriting_df = pd.read_excel('Edit_text/文案3.xlsx').astype(str)
    quantity = 7  # 每篇文章7段

    # 读取所有4列数据（text1, text2, text3, url）
    copywriting_list = [
        [str(col1), str(col2), str(col3), str(col4)] 
        for col1, col2, col3, col4 in zip(
            copywriting_df.iloc[:, 0],  # text1
            copywriting_df.iloc[:, 1],  # text2
            copywriting_df.iloc[:, 2],  # text3
            copywriting_df.iloc[:, 3]   # url
        )
    ]
    
    # 格式化文案数据，对text1、text2和text3应用换行符处理
    formatted_copywriting_list = [
        [
            add_newlines(item[0]),  # text1需要格式化
            add_newlines(item[1]),  # text2需要格式化
            add_newlines(item[2]),  # text3需要格式化
            item[3]                 # url保持原样
        ] 
        for item in copywriting_list
    ]
    
    create_and_export_text(out_path, topic, formatted_copywriting_list, quantity)
    

