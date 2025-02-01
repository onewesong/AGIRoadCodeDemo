import streamlit as st

def set_think_style():
    st.markdown("""
    <style>
        code.language-think  {
            white-space: pre-wrap !important;      /* 让文字乖乖换行 */
            display: block;                        /* 霸占一整行 */
            overflow: hidden;                      /* 先藏起来 */
            max-height: 200px;                     /* 露出小脑袋 */
            transition: max-height 0.3s ease-out;  /* 优雅地展开 */
            cursor: pointer;                       /* 变身小手手 */
            position: relative;                    /* 准备好定位 */
            padding-top: 25px !important;          /* 给标签腾位置 */
            border-left: 3px solid #6c757d !important; /* 点缀一下左边 */
            margin: 10px 0 !important;             /* 上下留点空间 */
        }
        
        code.language-think::before {
            content: "思考过程";                   /* 告诉大家这是什么 */
            position: absolute;                   /* 固定位置 */
            left: 3px;                            /* 靠左站 */
            top: 1px;                             /* 靠上站 */
            background: #f3f4f6;                  /* 标签底色 */
            padding: 2px 8px;                     /* 撑开点 */
            border-radius: 4px;                   /* 圆润的角 */
            font-size: 12px;                      /* 文字要小巧 */
            color: #6b7280;                       /* 低调的颜色 */
        }
        
        code.language-think::after {
            content: "悬停查看更多👇";                /* 友好的提示 */
            position: absolute;                    /* 固定位置 */
            left: 50%;                             /* 居中 */
            bottom: 5px;                           /* 靠下 */
            transform: translateX(-50%);           /* 完美居中 */
            background: #f3f4f6;                   /* 和上面配套 */
            padding: 2px 8px;                      /* 撑开点 */
            border-radius: 4px;                    /* 圆润 */
            font-size: 12px;                       /* 小巧 */
            color: #6b7280;                        /* 协调 */
            opacity: 0.8;                          /* 半透明 */
        }
        
        code.language-think:hover::after {
            display: none;                         /* 展开时藏起提示 */
        }
        
        code.language-think:hover {
            max-height: none;                     /* 完全展开 */
            box-shadow: 0 2px 5px rgba(0,0,0,0.1); /* 加个投影 */
        }
    </style>
    """, unsafe_allow_html=True)