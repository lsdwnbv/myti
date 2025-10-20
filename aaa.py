import pandas as pd
import streamlit as st
st.markdown('# 🕶️学生天真—数字档案')
st.markdown('# 🔑基础信息')
st.markdown('学生ID:ONE-2025-10-20')
st.markdown('##### 注册时间'':blue[2025-10-20]|' '精神状态：OK?')
st.markdown('##### 当前教室：'':blue[实训楼301]|''安全等级：:red[绝密航天]')
st.markdown('# 📊技能这一块')
st.markdown('C语言   python    java')
st.markdown('### 0.1%       12.5%    5%')
st.markdown('### streamlit课程进度')
import streamlit as st
import time

# 最简进度条
progress = st.progress(0)
for i in range(100):
    time.sleep(0.02)  # 模拟任务耗时
    progress.progress(i + 1)
st.success("完成")


st.markdown('# 📝任务日志')
data = {
    '日期':[2025-1020, 2025-10-20, 2025-10-20],
    '任务':['学生数字档案', '课程管理系统', '数据图标展示'],
    '状态':['没压力', '小压', '压力有点爆骚缸'],
    '难度':['★☆☆☆☆',	
'★★☆☆☆','★★★☆☆'],
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
# 技能矩阵章节

st.header("📊 技能矩阵")

col1, col2, col3 = st.columns(3)

col1.metric("C语言", "95%", "2%", help="近期训练提升") 

col2.metric("Python", "87%", "-1%")

col3.metric("Java", "68%", "-10%", help="用则进废则退")
