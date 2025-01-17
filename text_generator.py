import pandas as pd
from imageword2text_1 import generate_template as template1
from imageword2text_2 import generate_template as template2
from imageword2text_3 import generate_template as template3
from utils import add_newlines, create_and_export_text


def generate_text_type1(excel_path, out_path, topic, quantity=7):
    """生成只包含标题和图片的文案"""
    copywriting_df = pd.read_excel(excel_path, header=None).astype(str)
    
    copywriting_list = [
        [str(col1), str(col2)] 
        for col1, col2 in zip(
            copywriting_df.iloc[:, 0],  # text1
            copywriting_df.iloc[:, 1]   # url
        )
    ]
    
    
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
    copywriting_df = pd.read_excel(excel_path, header=None).astype(str)
   
    copywriting_list = [
        [str(col1), str(col2), str(col3)] 
        for col1, col2, col3 in zip(
            copywriting_df.iloc[:, 0],  # text1
            copywriting_df.iloc[:, 1],  # text2
            copywriting_df.iloc[:, 2]   # url
        )
    ]
 
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
    copywriting_df = pd.read_excel(excel_path, header=None).astype(str)

    copywriting_list = [
        [str(col1), str(col2), str(col3), str(col4)] 
        for col1, col2, col3, col4 in zip(
            copywriting_df.iloc[:, 0],  # text1
            copywriting_df.iloc[:, 1],  # text2
            copywriting_df.iloc[:, 2],  # text3
            copywriting_df.iloc[:, 3]   # url
        )
    ]
    
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