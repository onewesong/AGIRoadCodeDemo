import streamlit as st

def set_think_style():
    st.markdown("""
    <style>
        code.language-think  {
            white-space: pre-wrap !important;      /* 自动换行 */
            display: block;                        /* 块级显示 */
            overflow: hidden;                      /* 溢出隐藏 */
            max-height: 200px;                     /* 初始最大高度 */
            transition: max-height 0.3s ease-out;  /* 添加过渡动画 */
            cursor: pointer;                       /* 鼠标指针样式 */
            position: relative;                    /* 相对定位 */
            padding-top: 25px !important;          /* 为标签留出空间 */
        }
        
        code.language-think::before {
            content: "思考过程";                   /* 提示文字 */
            position: absolute;                    /* 绝对定位 */
            left: 3px;                           /* 左侧距离 */
            top: 1px;                             /* 顶部距离 */
            background: #f3f4f6;                  /* 背景色 */
            padding: 2px 5px;                     /* 内边距 */
            border-radius: 4px;                   /* 圆角 */
            font-size: 12px;                      /* 字体大小 */
            color: #6b7280;                       /* 字体颜色 */
            opacity: 0.8;                         /* 透明度 */
        }
        
        code.language-think::after {
            content: "悬停查看更多 ↓";             /* 展开提示文字 */
            position: absolute;                    /* 绝对定位 */
            left: 50%;                            /* 水平居中 */
            bottom: 5px;                          /* 底部距离 */
            transform: translateX(-50%);           /* X轴偏移实现完全居中 */
            background: #f3f4f6;                  /* 背景色 */
            padding: 2px 8px;                     /* 内边距 */
            border-radius: 4px;                   /* 圆角 */
            font-size: 12px;                      /* 字体大小 */
            color: #6b7280;                       /* 字体颜色 */
            opacity: 0.7;                         /* 透明度 */
        }
        
        code.language-think:hover::after {
            display: none;                        /* 悬停时隐藏展开提示 */
        }
        
        code.language-think:hover {
            max-height: none;                      /* 悬停时展开全部 */
        }
    </style>
    """, unsafe_allow_html=True) 