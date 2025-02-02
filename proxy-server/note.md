# 反向代理服务器说明文档

## 项目概述
这是一个使用 Go 语言实现的反向代理服务器，支持将请求动态转发到不同的后端服务器，并同时支持 HTTP 和 HTTPS 协议。

## 技术栈
- Go 1.21
- 仅使用标准库实现
  - net/http
  - net/http/httputil
  - crypto/tls

## 功能特性

### 1. 基础配置
- 服务端口：8080
- 支持协议：HTTP 和 HTTPS
- 动态目标服务器

### 3. 使用示例

#### HTTP 转发
访问地址：http://localhost:8080/localhost:5000/api/users
实际转发：http://localhost:5000/api/users

#### HTTPS 转发
访问地址：http://localhost:8080/localhost:443/api/users
实际转发：https://localhost:443/api/users

#### 支持协议解析
访问地址：http://localhost:8080/https://www.baidu.com/api/users
实际转发：https://www.baidu.com/api/users

### 4. 核心功能
- **自动协议选择**
  - 检测目标端口 443 自动使用 HTTPS
  - 其他端口默认使用 HTTP

- **请求转发**
  - 保留原始查询参数
  - 完整转发请求头
  - 自动设置正确的 Host 头

- **SSL/TLS 支持**
  - 支持 HTTPS 后端服务
  - 开发环境可忽略证书验证

### 5. 错误处理
- 400 Bad Request：目标地址格式错误
- 服务启动失败时输出错误日志

## 使用说明

### 1. 启动服务
```bash
go run main.go
```

### 2. 测试连接
```bash
# 测试 HTTP 转发
curl http://localhost:8080/localhost:5000/test

# 测试 HTTPS 转发
curl http://localhost:8080/api.example.com:443/v1/data
```

## 注意事项

### 安全考虑
1. 开发环境
   - 当前配置忽略 SSL 证书验证
   - 适合快速开发和测试

2. 生产环境建议
   - 配置proper的SSL证书验证
   - 添加请求来源验证
   - 实现访问控制策略

### 性能优化建议
1. 考虑添加连接池
2. 实现请求限流
3. 添加缓存机制

## 后续优化方向
1. 添加负载均衡功能
2. 实现健康检查
3. 支持配置文件
4. 添加监控指标
5. 实现路由规则配置
6. 支持多级代理