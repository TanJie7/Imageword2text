import pandas as pd
from utils import add_newlines, create_and_export_text

def generate_template(index, text1, url):
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
    <section style="margin: 8px 0px 32px; letter-spacing: 0.544px; text-wrap: wrap; background-color: #ffffff; text-align: left; line-height: 1.5em; text-indent: 0em;">
        <img src="{url}" style="width: 100%;" />
    </section>
</section>
'''
    return template

if __name__ == '__main__':
    out_path = "Edit_text"
    topic = "文案11"
    # 读取 Excel 文件，并将所有列转换为字符串类型
    copywriting_df = pd.read_excel('Edit_text/文案.xlsx').astype(str)
    quantity = 7  # 每篇文章7段

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
    
    create_and_export_text(out_path, topic, formatted_copywriting_list, quantity, generate_template)
