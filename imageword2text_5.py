def generate_template(index, text1, text2, text3, text4, text5, url):
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
        <span style="font-size: 12px; font-family: Optima-Regular, PingFangTC-light;">{text2}
        </span>
        <span style="color: black; font-size: 14px; font-family: Optima-Regular, PingFangTC-light; text-align: middle; display: block; line-height: 1.5; margin-top: 24px;">
{text3}
</span>
    </p>
</section>
 <section style="margin: 8px 0px 32px; letter-spacing: 0.544px; text-wrap: wrap; background-color: #ffffff; text-align: left; line-height: 1.5em; text-indent: 0em;">
        <img src="{url}" style="width: 100%;" />
 <span style="color: #B2B2B2; font-size: 12px; font-family: Optima-Regular, PingFangTC-light; text-align: right; display: block; line-height: 2.5;">{text4}</span>
<br/>
<span style="color: black; font-size: 15px; font-family: Optima-Regular, PingFangTC-light; text-align: middle; display: block; line-height: 1.5;">
{text5}
</span>
</section>
'''
    return template 

    