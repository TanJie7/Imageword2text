import os
from datetime import datetime

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

def create_and_export_text(out_path, topic, formatted_copywriting_list, quantity, template_generator):
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
            result = result + template_generator(j, *text_image_list[j])
        # 将内容写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(result)
        print(f"文件已生成: {file_path}") 