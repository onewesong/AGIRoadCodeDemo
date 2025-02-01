import streamlit as st
from ollama import Client
import os

# 页面配置
st.set_page_config(
    page_title="DeepSeek Chat",
    page_icon="🤖",
    layout="wide"
)

# 初始化聊天历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 初始化Ollama客户端
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
client = Client(host=OLLAMA_HOST)

# 设置页面标题
st.title("🤖 DeepSeek Chat")

# 侧边栏配置
with st.sidebar:
    st.markdown("## 模型配置")
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7)
    
    if st.button("清空对话", type="primary"):
        st.session_state.messages = []
        st.rerun()

# 显示聊天历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用户输入
if prompt := st.chat_input("说点什么吧..."):
    # 添加用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 显示AI思考状态
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 使用stream=True来获取流式响应
        stream = client.chat(
            model='deepseek-r1:14b',
            messages=st.session_state.messages,
            stream=True,
            options={
                'temperature': temperature
            }
        )
        
        # 逐字显示回复
        for chunk in stream:
            if chunk.message and chunk.message.content:
                full_response += chunk.message.content
                message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # 保存AI回复
    st.session_state.messages.append({"role": "assistant", "content": full_response}) 