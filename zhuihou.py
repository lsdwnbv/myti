import streamlit as st
import pandas as pd
import random
import time
from io import BytesIO
from datetime import datetime

st.title("学习成果")
tab1, tab2, tab3, tab4, tab5, tab6,tab7 = st.tabs(["学生档案", "美食地图", "相册","视频播放器","音乐","个人简介","扩展器"])

with tab1:
    st.markdown('# 🕶️学生天真—数字档案')
    st.markdown('# 🔑基础信息')
    st.markdown('学生ID:ONE-2025-10-20')
    st.markdown('##### 注册时间'':blue[2025-10-20]|' '精神状态：OK?')
    st.markdown('##### 当前教室：'':blue[实训楼301]|''安全等级：:red[绝密航天]')
    st.markdown('# 📊技能这一块')
    st.markdown('C语言   python    java')
    st.markdown('### 0.1%       12.5%    5%')
    st.markdown('### streamlit课程进度')
    st.markdown('1%')
    st.markdown('# 📝任务日志')
    data = {
        '日期':['2025-10-20', '2025-10-20', '2025-10-20'],
        '任务':['学生数字档案', '课程管理系统', '数据图标展示'],
        '状态':['没压力', '小压', '压力有点爆骚缸'],
        '难度':['★☆☆☆☆', '★★☆☆☆','★★★☆☆'],
    }
    # 定义数据框所用的索引
    index = pd.Series(['01', '02', '03'], name='序号')
    # 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)
    st.write(df)

    st.markdown('# 🔐最新代码展示')
    python_code = '''def hello():
        print("你好，Streamlit！")
    '''
    # 创建一个代码块，用于展示python_code的内容
    # 并设置language为None，即该代码块无语法高亮
    st.code(python_code, language=None)
    st.markdown('>> :green[SYSTEM MESSAGE]: 下一个任务目标已解锁...')
    st.markdown('>> :green[TARGET]: 课程管理系统')
    st.markdown('>> :green[COUNTDOWN]: 2025-10-20 02:55:26')
    st.markdown('系统状态: 在线 连接状态: 已加密')


with tab2:
    st.header("❤ 桂林TOP5本人最爱 ❤")
    st.text('麦香坊|椿记烧鹅|桂小厨|酒拾烤肉|绿茶餐厅')

    map_data = {
        'latitude':[25.281724,25.257572,25.262201,25.248653,25.262203],
        'longitude':[110.301915,110.222554,110.269705,110.168359,110.268694],
    }

    st.header("📍 桂林美食地图 📍")
    st.map(pd.DataFrame(map_data))

    data = {
        '用餐时间':['11', '12', '13','17','18','19','20'],
        '麦香坊':[30, 60, 54, 34, 45, 58, 28],
        '椿记烧鹅':[36, 71, 50, 35, 88, 65, 44],
        '桂小厨':[17, 50, 32, 40, 55, 43, 20],
        '酒拾烤肉':[22,65,45,50,33,50,60],
        '绿茶餐厅':[35,55,44,33,71,76,50]
    }

    df = pd.DataFrame(data)
    index = pd.Series([1, 2, 3, 4, 5, 6, 7], name='序号')
    df.index = index

    st.header("🚶用餐时间人流量🚶")
    st.area_chart(df, x='用餐时间')

    st.subheader('当前人流量')
    progress_text_1 ="正在统计"
    my_bar = st.progress(0,text=progress_text_1)
    time.sleep(0.5)
    for precent in range(80):
        time.sleep(0.1)
        my_bar.progress(precent+1,text=f'{precent}%:拥挤:')

    data1 = {
        '价格':['早餐','午餐','晚餐','宵夜'],
        '麦香坊':[20,40,55,35],
        '椿记烧鹅':[50,70,75,50],
        '桂小厨':[35,55,65,60],
        '酒拾烤肉':[22,65,45,50],
        '绿茶餐厅':[35,55,60,45]
    }

    df1 = pd.DataFrame(data1)
    index1 = pd.Series([1, 2, 3, 4,], name='序号')
    df1.index = index1

    month_order = ['早餐','午餐','晚餐','宵夜']
    df1['价格'] = pd.Categorical(df1['价格'], categories=month_order, ordered=True)
    df1_sorted = df1.sort_values('价格').set_index('价格')

    st.header("💰 不同类型餐厅价格 💰")
    st.line_chart(df1, x='价格')

    data2 = {
        '店铺':['麦香坊','椿记烧鹅','桂小厨', '酒拾烤肉', '绿茶餐厅'],
        '评分':[4.6,4.1,4,4.5,4.3]
    } 

    df2 = pd.DataFrame(data2)
    index2 = pd.Series([1,2,3,4,5,], name='')
    df2.index = index2

    st.header("⭐ 餐厅评分 ⭐")
    st.bar_chart(df2, x='店铺')

    data3 = {
        '月份': ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
        '麦香坊': [50,55,60,66,70,73,78,75,89,99,92,90],
        '椿记烧鹅': [70,80,90,85,74,88,99,93,88,77,96,99],
        '桂小厨': [40,49,54,60,58,64,60,75,85,92,91,98],
        '酒拾烤肉': [42,48,52,54,58,66,77,89,91,99,85,92],
        '绿茶餐厅': [55,60,58,66,67,78,88,92,98,96,99,95]
    }
    df3 = pd.DataFrame(data3)
    index3 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], name='序号')
    df3.index = index3

    month_order = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
    df3['月份'] = pd.Categorical(df3['月份'], categories=month_order, ordered=True)

    st.header("💸 今年各餐厅营业额 💸")
    df3_sorted = df3.sort_values('月份').set_index('月份')
    st.line_chart(df3_sorted)

    img_list = ["https://ts1.tc.mm.bing.net/th/id/OIP-C.ldUbad0bkLsnmQ23g0eOYQHaE8?w=299&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2", 
                "https://ts1.tc.mm.bing.net/th/id/OIP-C.pE5bkLcIR3A2R71OBO9nVQHaGH?w=241&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2", 
                "https://ts1.tc.mm.bing.net/th/id/OIP-C.Yx1KKVfhuodK4IluqqGuKgHaE7?w=299&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2",
                "https://www.china-greentea.com.cn/uploads/upload/images/20250120/dd1a4ae024a7c75bc2169d0530e7e9dd.jpg",
                "https://img1.qunarzz.com/travel/d3/1809/68/90e7cff1437c7fb5.jpg"]

    st.title("🎲 今天吃什么 🎲")
    if st.button("看看吃啥吧"):
        random_img = random.choice(img_list)
        st.image(random_img, caption=f"Delicious Food", use_container_width=True)
    else:
        st.image(img_list[0], caption="Delicious Food", use_container_width=True)


with tab3:
    # 1. 配置图片路径列表
    img_list = ["https://ts1.tc.mm.bing.net/th/id/OIP-C.ldUbad0bkLsnmQ23g0eOYQHaE8?w=299&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2", 
                "https://ts1.tc.mm.bing.net/th/id/OIP-C.pE5bkLcIR3A2R71OBO9nVQHaGH?w=241&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2", 
                "https://ts1.tc.mm.bing.net/th/id/OIP-C.Yx1KKVfhuodK4IluqqGuKgHaE7?w=299&h=204&c=8&rs=1&qlt=90&o=6&cb=12&pid=3.1&rm=2"]

    # 2. 页面标题与核心功能
    st.title("相册回忆")
    if st.button("切换"):
        # 选一张图的路径
        random_img = random.choice(img_list)
        # 展示选中的图片
        st.image(random_img, caption=f"1：{random_img}", use_container_width=True)
    else:
        # 初始未点击时，默认显示第一张图
        st.image(img_list[0], caption="初始展示：第一张图", use_container_width=True)
with tab4:  # 修正：使用定义好的选项卡变量tab4
    st.set_page_config(page_title='Delta Force', page_icon='🔺')
    st.header("🤘🏽 我的日常视频 🤘")
    
    # 视频列表
    video = [{
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/42/66/33133756642/33133756642-1-192.mp4?e=ig8euxZM2rNcNbNMhwdVhwdlhbKVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=cosovbv&og=hw&deadline=1761301871&oi=771356656&trid=8f49d0b76df541369347ee2c8ea700ah&nbs=1&uipk=5&platform=html5&mid=0&gen=playurlv3&upsig=f55101c13eec69d98026bb46939cf72a&uparams=e,os,og,deadline,oi,trid,nbs,uipk,platform,mid,gen&bvc=vod&nettype=0&bw=1924611&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
        'title':'只玩帅的',
        'episode':'1',
        'Author': '👤 YLG小叶',
        'Map':'🗺 巴克什',
        'k':'小帅'
        },
        {
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/44/06/30609900644/30609900644-1-192.mp4?e=ig8euxZM2rNcNbNMhWdVhwdlhbK1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=771356656&gen=playurlv3&og=ali&nbs=1&mid=0&deadline=1761301983&os=cosovbv&uipk=5&platform=html5&trid=d96cb9aae9a04e39b3bdadbada702aeh&upsig=caa297eca5a110d16641b2d5f3dba5ab&uparams=e,oi,gen,og,nbs,mid,deadline,os,uipk,platform,trid&bvc=vod&nettype=0&bw=1939574&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
        'title':'只玩帅的',
        'episode':'2',
        'Author': '👤 丷Bling',
        'Map':'🗺 航天基地/巴克什',  # 修正路径分隔符为/，避免转义错误
        'k':'中帅'},
        {
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/59/90/31978229059/31978229059_qe1-1-192.mp4?e=ig8euxZM2rNcNbNzhbdVhwdlhbhghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=ca792c4a54e347f48eb111a9ef31b0bh&uipk=5&platform=html5&gen=playurlv3&os=cosovbv&og=cos&oi=771356656&mid=0&nbs=1&deadline=1761302036&upsig=944232e953a3265b3c742952928d84e4&uparams=e,trid,uipk,platform,gen,os,og,oi,mid,nbs,deadline&bvc=vod&nettype=0&bw=1866255&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        'title':'只玩帅的',
        'episode':'3',
        'Author': '👤 苏6の',
        'Map':'🗺 航天基地/潮汐监狱',  # 修正路径分隔符
        'k':'大帅'},
        {
        'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/65/91/32904709165/32904709165-1-192.mp4?e=ig8euxZM2rNcNbNM7zdVhwdlhbKahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&mid=0&deadline=1761302314&uipk=5&gen=playurlv3&og=cos&nbs=1&oi=771356656&trid=378bd57889fb4c5eb2ad0c5a9001a75h&os=cosovbv&upsig=49ffce4cd47d21514acfa0ebb5698fac&uparams=e,platform,mid,deadline,uipk,gen,og,nbs,oi,trid,os&bvc=vod&nettype=0&bw=1992653&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
        'title':'只玩帅的',
        'episode':'4',
        'Author': '👤 璃茉Kira',
        'Map':'🗺 航天基地',
        'k':'超帅'}
    ]

    # 初始化视频索引（记录当前播放的视频）
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    
    # 显示视频标题和信息
    st.title(f"{video[st.session_state['ind']]['title']}-第{video[st.session_state['ind']]['episode']}集")
    st.header(video[st.session_state['ind']]['k'])
    st.subheader(f"{video[st.session_state['ind']]['Author']} {video[st.session_state['ind']]['Map']}")  # 加空格分隔
    
    # 播放视频
    st.video(video[st.session_state['ind']]['url'])
    
    # 切换视频的函数
    def play(arg):
        st.session_state['ind'] = int(arg)
    
    # 生成每一集的切换按钮
    for x in range(len(video)):
        st.button(f'第{x+1}集', use_container_width=True, on_click=play, args=([x]))


# ------------------------------ 选项卡5：音乐播放 ------------------------------
with tab5:  # 修正：使用定义好的选项卡变量tab5
    # 配置页面信息
    st.set_page_config(page_title='音乐播放器', page_icon='🐬')
    st.header("音乐这一块🤏")

    # 音频列表
    audio_file = [
        {
            'url': 'https://music.163.com/song/media/outer/url?id=2756303345.mp3',
            'parm': '陈奕迅',  # 歌手
            'photo': 'http://p2.music.126.net/IDAl-BxdZpWpNb-_3r_Shg==/109951172160870872.jpg?param=130y130',  # 封面
            'info': 'K歌之王\n词：林夕\n曲：陈奕迅'  # 修正键名，避免用数字
        },
        {
            'url': 'https://music.163.com/song/media/outer/url?id=2666095018.mp3',
            'parm': '孙燕姿',
            'photo': 'https://p1.music.126.net/Z6rUwSkXwS_cn8AB7KqBaw==/109951170378435887.jpg?param=180y180',
            'info': '日落\nLyricist 词 : 小寒\nComposer 曲 : 张简君伟/邵豪Shao Hao/Nay Shalom宁夏'
        },
        {
            'url': 'https://music.163.com/song/media/outer/url?id=255294.mp3',
            'parm': '刘惜君',
            'photo': 'https://p1.music.126.net/gZ93OHvjWKwnvIwChuRTfA==/109951171315740884.jpg?param=180y180',
            'info': '我很快乐\n作词 : 祈合/张海\n作曲 : 祈合'
        },
        {
            'url': 'https://music.163.com/song/media/outer/url?id=423406145.mp3',
            'parm': '张信哲',
            'photo': 'https://p2.music.126.net/xt_oovsCzByJNCVOZLWgkA==/2946691201348447.jpg?param=180y180',
            'info': '过火\n作词 : 陈佳明\n作曲 : 曹俊鸿\n编曲 : 屠颖'
        }
    ]

    # 初始化播放索引
    if 'a' not in st.session_state:
        st.session_state['a'] = 0

    # 下一首函数
    def nextimg():
        st.session_state['a'] = (st.session_state['a'] + 1) % len(audio_file)

    # 上一首函数
    def next2mg():
        st.session_state['a'] = (st.session_state['a'] - 1) % len(audio_file)

    # 播放音频
    st.audio(audio_file[st.session_state['a']]['url'])

    # 显示封面和歌曲信息（修正缩进）
    d1, d2 = st.columns(2)
    with d1:  # 第一列：封面图
        st.image(
            audio_file[st.session_state['a']]['photo'],
            caption=audio_file[st.session_state['a']]['parm'],
            use_container_width=True
        )
    with d2:  # 第二列：歌曲信息
        st.text(audio_file[st.session_state['a']]['info'])

    # 上一首/下一首按钮（修正缩进）
    c1, c2 = st.columns(2)
    with c1:
        st.button('上一首', on_click=next2mg, use_container_width=True)
    with c2:
        st.button('下一首', on_click=nextimg, use_container_width=True)


# ------------------------------ 选项卡6：个人简历生成器 ------------------------------
with tab6:  # 修正：使用定义好的选项卡变量tab6
    st.set_page_config(page_title="个人简历生成器", page_icon="📄", layout="wide")
    st.title('个人简历生成器')
    st.text('生成你的个性化简历')

    # 左右布局：左侧表单，右侧预览
    c1, c2 = st.columns([1, 2])
    with c1:  # 左侧：信息填写表单
        st.subheader('个人信息表单')
        st.markdown('***')
        
        def my_format_func(option):
            return f'{option}'
        
        name = st.text_input('姓名', autocomplete='name')
        gender = st.radio(  # 修正变量名，更清晰
            '性别',
            ['男', '女', '其他'],
            horizontal=True,
            label_visibility='hidden',
        )
        country = st.selectbox(  # 修正变量名
            '国家：',
            ['火之国', '水之国', '雷之国', '风之国', '土之国'],
            format_func=my_format_func,
            index=2
        )
        chakra = st.multiselect(  # 修正变量名
            '查克拉属性：',
            ['火', '风', '雷', '土', '水', '阴'],
            format_func=my_format_func
        )
        job = st.text_input('应聘职位', autocomplete='job')
        identity = st.text_input('特殊身份', autocomplete='tl')  # 修正变量名
        jutsu = st.text_input('忍术', autocomplete='email')  # 修正变量名
        age = st.number_input("年龄", min_value=1, max_value=130, value=10)
        birthday = st.date_input("生日", value=None)  # 修正变量名
        contact_time = st.time_input(  # 修正变量名
            "每日最佳联系时间段", 
            datetime(2019, 7, 6, 21, 15)
        )
        exp = st.slider('工作经验（年）', 0, 50)  # 修正变量名，避免与age冲突
        salary = st.slider(  # 修正变量名
            '期望薪资',
            0, 100000, (10000, 20000)
        )
        intro = st.text_area(  # 修正变量名
            label='个人简介：', 
            placeholder='请简单描述自己'
        )
        # 上传照片
        uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            photo_data = uploaded_file.getvalue()  # 修正变量名

    with c2:  # 右侧：实时预览
        st.subheader('实时简历预览')
        st.markdown('***')
        a1, a2, a3 = st.columns(3)
        
        with a1:  # 照片区域
            if uploaded_file is not None:
                st.image(photo_data, caption="本人照片", width=250)
        
        with a2:  # 基础信息区域
            st.title(name if name else "请输入姓名")  # 为空时提示
            st.write('**国家**:', country)
            st.write(f'**性别**: {gender}')
            st.write('**忍术**:', jutsu)
            st.write('**特殊身份**:', identity)
            st.write('**年龄**:', age)
        
        with a3:  # 求职信息区域
            st.write('**应聘职位**:', job)
            st.write("**生日**:", birthday)
            st.write("**最佳联系时间**:", contact_time)
            st.write('**期望薪资**:', f'{salary[0]} - {salary[1]}')
            st.write('**查克拉属性**:', ', '.join(chakra) if chakra else '未填写')  # 格式化显示
            st.write("**工作经验**: ", exp, '年')
        
        # 个人简介区域
        st.markdown('***')
        st.title('**个人简介**')
        st.write(intro if intro else "请填写个人简介")  # 为空时提示
with tab7:
    st.subheader("扩展器示例")  # 标题与扩展器同属tab7，需统一缩进
    # 扩展器代码缩进在with tab7块内，确保属于当前选项卡
    with st.expander("点击展开", expanded=True):  # expanded=True：默认展开状态
        st.write("再次点击关闭")
    

