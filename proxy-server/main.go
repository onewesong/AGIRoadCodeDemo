package main

import (
	"crypto/tls"
	"log"
	"net/http"
	"net/http/httputil"
	"strings"
)

func main() {
	// 注册所有请求都由 proxyHandler 处理
	http.HandleFunc("/", proxyHandler)

	log.Println("反向代理服务器启动于 :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal("服务器启动失败:", err)
	}
}

func proxyHandler(w http.ResponseWriter, r *http.Request) {
	// 解析请求路径：格式为 /目标服务器地址/路径
	path := strings.TrimPrefix(r.URL.Path, "/")
	parts := strings.SplitN(path, "/", 2)
	if len(parts) < 1 || parts[0] == "" {
		http.Error(w, "目标地址错误", http.StatusBadRequest)
		return
	}

	targetHost := parts[0]
	targetPath := "/"
	if len(parts) == 2 {
		targetPath += parts[1]
	}

	// 根据端口号判断是否使用 HTTPS
	scheme := "http"
	if strings.Contains(targetHost, ":443") {
		scheme = "https"
	}

	// 定义反向代理的 director 函数，重写请求的 URL 和 Host
	director := func(req *http.Request) {
		req.URL.Scheme = scheme
		req.URL.Host = targetHost
		req.URL.Path = targetPath
		req.URL.RawQuery = r.URL.RawQuery
		req.Host = targetHost
	}

	proxy := &httputil.ReverseProxy{
		Director: director,
		Transport: &http.Transport{
			TLSClientConfig: &tls.Config{
				InsecureSkipVerify: true, // 忽略 SSL 证书验证，仅用于测试
			},
		},
	}
	proxy.ServeHTTP(w, r)
}
