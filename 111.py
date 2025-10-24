# 导入streamlit库，用于快速创建Web应用
import streamlit as st


# 配置页面信息：设置页面标题为"音乐播放器"，页面图标为🐒
st.set_page_config(page_title='音乐播放器', page_icon='🐬')
# 显示页面标题
st.header("音乐这一块🤏")

# 定义音频文件信息列表，包含每首歌的播放地址、歌手、封面图和歌曲信息
audio_file = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2756303345.mp3',  # 歌曲播放URL
        'parm': '陈奕迅',  # 歌手信息
        'photo': 'http://p2.music.126.net/IDAl-BxdZpWpNb-_3r_Shg==/109951172160870872.jpg?param=130y130',  # 封面图URL
        '1': 'K歌之王\n词：林夕\n 曲：陈奕迅'  # 歌曲名及词曲信息
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2666095018.mp3',
        'parm': '孙燕姿',
        'photo': 'https://p1.music.126.net/Z6rUwSkXwS_cn8AB7KqBaw==/109951170378435887.jpg?param=180y180',
        '1': '日落\nLyricist 词 : 小寒\n Composer 曲 : 张简君伟/邵豪Shao Hao/Nay Shalom宁夏'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=255294.mp3',
        'parm': '刘惜君',
        'photo':  'https://p1.music.126.net/gZ93OHvjWKwnvIwChuRTfA==/109951171315740884.jpg?param=180y180',
        '1': '我很快乐\n作词 : 祈合/张海\n 作曲 : 祈合'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=423406145.mp3',
        'parm': '张信哲',
        'photo': 'https://p2.music.126.net/xt_oovsCzByJNCVOZLWgkA==/2946691201348447.jpg?param=180y180',
        '1': '过火\n作词 : 陈佳明\n作曲 : 曹俊鸿\n编曲 : 屠颖'
    }
]


# 初始化session_state：用于存储当前播放索引（页面刷新时保持状态）
# 如果'session_state'中没有'a'这个键，就创建它并初始化为0（默认播放第一首歌）
if 'a' not in st.session_state:
    st.session_state['a'] = 0


# 定义"下一首"按钮的回调函数
def nextimg():
    # 更新当前播放索引：加1后对歌曲总数取模，实现循环播放（最后一首的下一首是第一首）
    st.session_state['a'] = (st.session_state['a'] + 1) % len(audio_file)


# 定义"上一首"按钮的回调函数
def next2mg():
    # 更新当前播放索引：减1后对歌曲总数取模，实现循环播放（第一首的上一首是最后一首）
    st.session_state['a'] = (st.session_state['a'] - 1) % len(audio_file)


# 渲染音频播放器，播放当前索引对应的歌曲
st.audio(audio_file[st.session_state['a']]['url'])


# 创建两列布局，用于展示歌曲封面和歌曲信息
d1, d2 = st.columns(2)
with d1:  # 第一列显示封面图，图片备注为歌手信息
    st.image(
        audio_file[st.session_state['a']]['photo'],  # 封面图URL
        caption=audio_file[st.session_state['a']]['parm']  # 图片备注（歌手名）
    )
with d2:  # 第二列显示歌曲名和词曲信息
    st.text(audio_file[st.session_state['a']]['1'])


# 创建两列布局，用于放置"上一首"和"下一首"按钮
c1, c2 = st.columns(2)
with c1:  # 第一列放置"上一首"按钮
    # 点击按钮时调用next2mg函数，按钮宽度适应列宽
    st.button('上一首', on_click=next2mg, use_container_width=True)

with c2:  # 第二列放置"下一首"按钮
    # 点击按钮时调用nextimg函数，按钮宽度适应列宽
    st.button('下一首', on_click=nextimg, use_container_width=True)
