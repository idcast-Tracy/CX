# 打开网页，在cmd命令界面运行下面一段
# # streamlit run C:\Users\Tracy\Desktop\2024Winter\科研\01.20Python-oneleaf\一叶知秋.py [ARGUMENTS]

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
import os
import time
import datetime
os.chdir(r'C:\Users\Tracy\Desktop\2024Winter\科研\01.20Python-oneleaf') # 设定文件路径
# 设置页面配置
st.set_page_config(page_title="CX-copilot 1.0", page_icon="⭐", layout="wide")
# 通过 css样式隐藏主菜单和页脚
hide_menu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(hide_menu,unsafe_allow_html=True)
# st.balloons()

with st.sidebar:
    choose = option_menu("管理层", ["数据监控与分析", "数据安全与运维保障服务", "AI启动项","跨平台同步学习模块"],
                         icons=['house', 'book-half', 'bar-chart', "boombox-fill"],
                         menu_icon="bullseye", default_index=0)

## ==================================  数据监控与分析  ==========================================
if choose == "数据监控与分析":
    with st.sidebar:
        choose = option_menu("数据监控与分析", ["数据上传", "用户行为数据", "系统性能评估"],
                             icons=['house', 'book-half', 'bar-chart', "boombox-fill"],
                             menu_icon="house", default_index=0)

    if choose == "数据上传":
        ## file_uploader【文件上传】
        uploaded_files = st.file_uploader("请选择文件(试卷库、作业库、题库、PPT等)：", accept_multiple_files=True, type=["csv"])
        for uploaded_file in uploaded_files:
            df = pd.read_csv(uploaded_file,encoding='gbk')
            st.write("文件名:", uploaded_file.name)
            latest_iteration = st.empty() ##  显示进度
            bar = st.progress(0)
            for i in range(100): # Update the progress bar with each iteration.
                latest_iteration.text(f'Iteration {i + 1}')
                bar.progress(i + 1)
                time.sleep(0.00000000001)
            st.success('数据导入成功，请检查数据完整性和真实性。')
            st.dataframe(df)

    elif choose == "用户行为数据":
        selecte = option_menu(None, ["用户分布地区", "用户特征分布", "用户活跃度"],
                              icons=["bar-chart-fill", "pie-chart-fill", "graph-up"],
                              menu_icon="cast", default_index=0, orientation="horizontal")
        if selecte == "用户分布地区":
            st.image("用户分布地区.png")

        elif selecte == "用户特征分布":
            st.image("用户特征分布.png")

        elif selecte == "用户活跃度":
            st.image("用户活跃度.png")


    elif choose == "系统性能评估":
        selecte = option_menu(None, ["推荐效果评估","问答系统性能评估"],icons=["pie-chart-fill","graph-up"],
                              menu_icon="cast", default_index=0, orientation="horizontal")
        if selecte == "推荐效果评估":
            st.info('一个用于分析和展示系统推荐性能的核心功能，这有助于管理层精准掌握系统性能，为决策提供有力支持，推动系统持续优化发展')
            st.image("推荐效果评估.png")

        elif selecte == "问答系统性能评估":
            st.info('智能问答系统性能检测：确保高效、准确的问答体验。让学习更便捷！')
            st.image("问答系统性能评估.png")


## ==================================  数据安全与运维保障服务  ==========================================
elif choose == "数据安全与运维保障服务":
    with st.sidebar:
        choose = option_menu("数据安全与运维保障服务", ["数据备份", "安全审计", "系统监控"],
                             icons=['house', 'bar-chart', "boombox-fill"],
                             menu_icon="book-half", default_index=0)

    if choose == "数据备份":
        selecte = option_menu(None, ["配置选项", "高级选项", "更新备份数据"],icons=["bar-chart-fill", "pie-chart-fill", "graph-up"],
                              menu_icon="cast", default_index=0, orientation="horizontal")
        if selecte == "配置选项":
            option2 = st.selectbox("数据源", ("数据库服务器", "文件服务器", "应用服务器"))
            option3 = st.selectbox("备份频率", ("每小时", "每日", "每周", "每月"))
            txt1 = st.text_area('请输入存储位置')
            txt2 = st.text_area('请输入备份任务名称')
        elif selecte == "高级选项":
            option4 = st.selectbox("备份压缩", ("启用备份数据压缩","不启用"))
            option5 = st.selectbox("增量备份", ("启用增量备份","不启用"))
            option6 = st.selectbox("备份日志级别", ("详细",'标准',"简单"))
            txt3 = st.date_input("过期备份保留时间", datetime.date(2024, 4, 8))
        elif selecte == "更新备份数据":
            df = pd.DataFrame({'任务名称': ['任务1', '任务2', '任务3', '任务4'],
                               '数据源': ['数据库服务器', '文件服务器', '应用服务器', '数据库服务器'],
                               '备份频率': ['每小时', '每日', '每周', '每月'],
                               '备份状态': ['已完成', '进行中', '未开始', '已完成'],
                               '上次备份时间': ['2024-04-08 08:00', '2024-04-07 18:30', '-', '2024-03-30 22:00'],
                               '下次备份时间': ['2024-04-09 08:00', '2024-04-10 18:30', '2024-04-06 12:00', '2024-04-03 22:00']})
            df

    if choose == "安全审计":
        selecte = option_menu(None, ["审计日志图表","审计日志详细界面"],icons=["pie-chart-fill","graph-up"],
                              menu_icon="cast", default_index=0, orientation="horizontal")
        if selecte == "审计日志图表":
            st.image("安全审计1.png")

        elif selecte == "审计日志详细界面":
            st.image("安全审计2.png")

    if choose == "系统监控":
        selecte = option_menu(None, ["安全监控","服务监控","日志监控","性能监控"],icons=["pie-chart-fill","graph-up"],
                              menu_icon="cast", default_index=0, orientation="horizontal")
        if selecte == "安全监控":
            st.image("安全监控.png")
        elif selecte == "服务监控":
            st.image("服务监控.png")
        elif selecte == "日志监控":
            st.image("日志监控.png")
        elif selecte == "性能监控":
            st.image("性能监控.png")


## ==================================  AI启动项  ==========================================
elif choose == "AI启动项":
    with st.sidebar:
        choose = option_menu("AI启动项", ["创造力", "平衡", "保守"],
                             icons=['house', 'book-half', "boombox-fill"],
                             menu_icon="bar-chart", default_index=0)
    # 结合Plotly来添加柱状图、饼图和折线图
    # 将图表分为三种
    selecte = option_menu(None, ["柱状图", "饼图", "折线图"],
                          icons=["bar-chart-fill", "pie-chart-fill", "graph-up"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "柱状图":
        # px.data.tips()`是Plotly Express提供的一个示例数据集，其中包含有关餐厅小费的数据它是一个DataFrame对象
        data_bar = px.data.tips()
        fig_bar = px.bar(data_bar, x='day', y='total_bill', color='sex')
        st.plotly_chart(fig_bar)

    elif selecte == "饼图":
        data_pie = px.data.tips()
        fig_pie = px.pie(data_pie, names='day')
        st.plotly_chart(fig_pie)

    elif selecte == "折线图":
        data_line = px.data.gapminder().query("country=='China'")
        fig_line = px.line(data_line, x='year', y='pop')
        st.plotly_chart(fig_line)


## ==================================  跨平台同步学习模块  ==========================================
elif choose == "跨平台同步学习模块":
    with st.sidebar:
        choose = option_menu("跨平台同步学习模块", ["手机端", "平板端", "电脑端"],
                             icons=['house', 'book-half', 'bar-chart'],
                             menu_icon="boombox-fill", default_index=0)
    selecte = option_menu(None, ["音乐", "视频"],
                          icons=["file-music-fill", "badge-vo-fill"],
                          menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte == "音乐":
        st.write("我的梦")
        st.audio("Dream It Possible.mp3")
        st.write("离别开出花")
        st.audio("离别开出花.mp3")
        st.write("明天，你好")
        st.audio("明天,你好.mp3")

    elif selecte == "视频":
        # st.video("S4.原型演示(视频)-赛题08-可视化AI模型平台-视界AI.mp4")
        st.write('傻逼')
