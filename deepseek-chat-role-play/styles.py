import streamlit as st

def set_think_style():
    st.markdown("""
    <style>
        code.language-think  {
            white-space: pre-wrap !important;      
            display: block;                        
            overflow: hidden;                      
            max-height: 200px;                     
            transition: max-height 0.3s ease-out;  
            cursor: pointer;                       
            position: relative;                    
            padding-top: 25px !important;          
            border-left: 3px solid #6c757d !important; 
            margin: 10px 0 !important;             
        }
        
        code.language-think::before {
            content: "思考过程";                   
            position: absolute;                   
            left: 3px;                            
            top: 1px;                             
            background: #f3f4f6;                  
            padding: 2px 8px;                     
            border-radius: 4px;                   
            font-size: 12px;                      
            color: #6b7280;                       
        }
        
        code.language-think::after {
            content: "悬停查看更多👇";                
            position: absolute;                    
            left: 50%;                             
            bottom: 5px;                           
            transform: translateX(-50%);           
            background: #f3f4f6;                   
            padding: 2px 8px;                      
            border-radius: 4px;                    
            font-size: 12px;                       
            color: #6b7280;                        
            opacity: 0.8;                          
        }
        
        code.language-think:hover::after {
            display: none;                         
        }
        
        code.language-think:hover {
            max-height: none;                     
            box-shadow: 0 2px 5px rgba(0,0,0,0.1); 
        }
    </style>
    """, unsafe_allow_html=True) 