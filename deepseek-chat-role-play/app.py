import streamlit as st
from ollama import Client
import os
from roles import ROLE_TEMPLATES
from styles import set_think_style

# 页面配置
st.set_page_config(
    page_title="DeepSeek Chat",
    page_icon="🤖",
    layout="wide"
)

# 应用样式
set_think_style()

# 初始化Ollama客户端
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
client = Client(host=OLLAMA_HOST)

# 获取可用模型列表
@st.cache_data(ttl=300)  # 缓存5分钟
def get_available_models():
    try:
        models = client.list()
        return [model['model'] for model in models['models']]
    except Exception as e:
        st.error(f"获取模型列表失败: {str(e)}")
        return ['deepseek-r1:14b']  # 默认模型

# 设置页面标题
st.title("🤖 DeepSeek Chat")

# 侧边栏配置
with st.sidebar:
    st.markdown("## 模型设置")
    
    # 模型选择
    available_models = get_available_models()
    selected_model = st.selectbox(
        "选择模型",
        options=available_models,
        index=available_models.index('deepseek-r1:14b') if 'deepseek-r1:14b' in available_models else 0
    )
    
    st.markdown("## 角色选择")
    
    # 角色选择下拉菜单
    selected_role = st.selectbox(
        "选择AI助手的角色",
        options=list(ROLE_TEMPLATES.keys()),
        format_func=lambda x: f"{ROLE_TEMPLATES[x]['icon']} {ROLE_TEMPLATES[x]['name']}"
    )
    
    # 显示角色介绍
    role = ROLE_TEMPLATES[selected_role]
    st.markdown(f"""
    **当前角色**: {role['icon']} {role['name']}  
    **简介**: {role['description']}
    """)
    
    # 其他配置
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7)
    
    if st.button("清空对话", type="primary"):
        st.session_state.messages = [{
            "role": "system",
            "content": ROLE_TEMPLATES[selected_role]["prompt"]
        }]
        st.rerun()

# 初始化对话历史
if "messages" not in st.session_state or not st.session_state.messages:
    st.session_state.messages = [{
        "role": "system",
        "content": ROLE_TEMPLATES[selected_role]["prompt"]
    }]

# 显示聊天历史
for message in st.session_state.messages[1:]:  # 跳过system prompt
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 用户输入处理
if prompt := st.chat_input("说点什么吧..."):
    # 检查是否需要切换角色
    current_role = st.session_state.messages[0]["content"]
    if current_role != ROLE_TEMPLATES[selected_role]["prompt"]:
        st.session_state.messages = [{
            "role": "system",
            "content": ROLE_TEMPLATES[selected_role]["prompt"]
        }]
    
    # 添加用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 显示AI思考状态
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # 使用stream=True来获取流式响应
            stream = client.chat(
                model=selected_model,  # 使用选择的模型
                messages=st.session_state.messages,
                stream=True,
                options={
                    'temperature': temperature
                }
            )
            
            # 逐字显示回复，支持思考过程
            for chunk in stream:
                if chunk.message and chunk.message.content:
                    content = chunk.message.content
                    # 特殊标记转换
                    if content == "<think>":
                        content = "```think\n"
                    elif content == "</think>":
                        content = "\n```"
                    full_response += content
                    # 实时显示
                    message_placeholder.markdown(full_response + "▌")
            
            # 最终显示
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            error_message = f"发生错误: {str(e)}"
            message_placeholder.error(error_message)
            full_response = error_message
    
    # 保存AI回复
    st.session_state.messages.append({"role": "assistant", "content": full_response}) 