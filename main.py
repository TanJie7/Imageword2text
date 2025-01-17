from text_generator import generate_text_type1, generate_text_type2, generate_text_type3

if __name__ == '__main__':
    # 设置基本参数
    out_path = "Edit_text"
    topic = "文案17"  # 文案主题
    quantity = 10     # 每篇文章的段落数量
    
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