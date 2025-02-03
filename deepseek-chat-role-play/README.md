# DeepSeek Chat Role Play

一个支持角色扮演的DeepSeek聊天界面。

## 功能特点

- 支持多种预设角色（程序员、文案师、老师、段子手）
- 实时切换角色，自动重置对话上下文
- 思考过程可视化，支持优雅的展开/收起
- 流式输出，打字机效果
- 可调节temperature参数

## 安装使用

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 确保Ollama服务已启动且已下载deepseek-r1:14b模型：
```bash
ollama run deepseek-r1:14b
```

3. 启动应用：
```bash
streamlit run app.py
```

## 自定义角色

编辑 `roles.py` 文件，按照已有模板添加新的角色定义即可。

## 注意事项

- 需要确保有足够的系统资源运行DeepSeek模型
- 建议使用较新版本的Python (3.8+)
- 如果使用远程Ollama服务，请通过环境变量设置OLLAMA_HOST

## License

MIT 