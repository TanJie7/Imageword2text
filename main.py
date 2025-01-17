import pandas as pd
from imageword2text_1 import generate_template as template1
from imageword2text_2 import generate_template as template2
from imageword2text_3 import generate_template as template3
from utils import add_newlines, create_and_export_text

def generate_text_type1(excel_path, out_path, topic, quantity=7):
    """生成只包含标题和图片的文案"""
    # 读取 Excel 文件，设置header=None表示没有标题行
    copywriting_df = pd.read_excel(excel_path, header=None).astype(str)

    # 读取所有2列数据（text1, url）
    copywriting_list = [
        [str(col1), str(col2)] 
        for col1, col2 in zip(
            copywriting_df.iloc[:, 0],  # text1
            copywriting_df.iloc[:, 1]   # url
        )
    ]

    
    # 格式化文案数据，对text1应用换行符处理
    formatted_copywriting_list = [
        [
            add_newlines(item[0]),  # text1需要格式化
            item[1]                 # url保持原样
        ] 
        for item in copywriting_list
    ]
    print(formatted_copywriting_list)
    
    create_and_export_text(out_path, topic, formatted_copywriting_list, quantity, template1)

def generate_text_type2(excel_path, out_path, topic, quantity=7):
    """生成包含两段文字和图片的文案"""
    # 读取 Excel 文件，设置header=None表示没有标题行，并将所有列转换为字符串类型
    copywriting_df = pd.read_excel(excel_path, header=None).astype(str)
   
    # 读取所有3列数据（text1, text2, url）
    copywriting_list = [
        [str(col1), str(col2), str(col3)] 
        for col1, col2, col3 in zip(
            copywriting_df.iloc[:, 0],  # text1
            copywriting_df.iloc[:, 1],  # text2
            copywriting_df.iloc[:, 2]   # url
        )
    ]
 
    # 格式化文案数据
    formatted_copywriting_list = [
        [
            add_newlines(item[0]),  # text1需要格式化
            add_newlines(item[1]),  # text2需要格式化
            item[2]                 # url保持原样
        ] 
        for item in copywriting_list
    ]
    
    create_and_export_text(out_path, topic, formatted_copywriting_list, quantity, template2)

def generate_text_type3(excel_path, out_path, topic, quantity=7):
    """生成包含三段文字和图片的文案"""
    # 读取 Excel 文件，设置header=None表示没有标题行
    copywriting_df = pd.read_excel(excel_path, header=None).astype(str)

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
    
    # 格式化文案数据
    formatted_copywriting_list = [
        [
            add_newlines(item[0]),  # text1需要格式化
            add_newlines(item[1]),  # text2需要格式化
            add_newlines(item[2]),  # text3需要格式化
            item[3]                 # url保持原样
        ] 
        for item in copywriting_list
    ]
    
    create_and_export_text(out_path, topic, formatted_copywriting_list, quantity, template3)

if __name__ == '__main__':
    # 设置基本参数
    out_path = "Edit_text"
    topic = "文案17"  # 文案主题
    quantity = 10      # 每篇文章的段落数量
    
    # 选择要生成的类型（1、2或3）
    choice = 2
    
    # 根据选择调用相应的函数
    if choice == 1:
        generate_text_type1(
            excel_path='Edit_text/文案.xlsx',
            out_path=out_path,
            topic=topic,
            quantity=quantity
        )
    elif choice == 2:
        generate_text_type2(
            excel_path='Edit_text/文案2.xlsx',
            out_path=out_path,
            topic=topic,
            quantity=quantity
        )
    else:
        generate_text_type3(
            excel_path='Edit_text/文案3.xlsx',
            out_path=out_path,
            topic=topic,
            quantity=quantity
        ) 