import re

html = """<p data-v-58f864bf="" class="recruit-tips">
    <span data-v-58f864bf="">深圳</span> 
    <span data-v-58f864bf="">|</span> 
    <span data-v-58f864bf="">产品类</span> 
    <span data-v-58f864bf="">|</span> 
    <span data-v-58f864bf="">2020年03月06日</span>
</p>
<ul>
    <li data-v-58f864bf="" class="explain-item">
        1）努力学习的人；
        <br>
        2）多敲代码的人；
        <br>
        3) 面试表现不紧张的人；
    </li>
</ul>
"""
regex = '<p.*?>.*?>(.*?)</span>.*?</span>.*?>(.*?)</span>.*?</span>.*?>(.*?)</span>.*?<li.*?>(.*?)</li>'
pattern = re.compile(regex,re.S)
r_list = pattern.findall(html)
for r in r_list:
    print('工作地点:',r[0].strip())
    print('工作类别:',r[1].strip())
    print('发布时间:',r[2].strip())
    print('工作要求:',r[3].strip().replace('<br>','').replace('\n','').replace(' ',''))





