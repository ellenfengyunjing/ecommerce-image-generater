/**
 * 前端配置文件示例
 * 
 * 使用方法：
 * 1. 复制此文件为 config.js
 * 2. 修改 API_URL 为实际的后端服务器地址
 * 3. 在 index.html 中引入 config.js（在 index.html 的 <head> 中添加：<script src="config.js"></script>）
 * 
 * ⚠️ 注意：config.js 文件包含敏感配置，不要提交到 Git
 */

// 后端 API 地址配置
window.APP_CONFIG = {
  // 本地开发环境
  // API_URL: "http://localhost:8000/api/generate",
  
  // 生产环境（示例）
  API_URL: "https://your-backend-domain.com/api/generate",
  
  // 其他配置项可以在这里添加
  // TIMEOUT: 60000,
  // MAX_RETRIES: 3,
};
