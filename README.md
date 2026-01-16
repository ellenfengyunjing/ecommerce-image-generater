# 电商图片自动套版生成工具 - 前端

这是一个纯 HTML + JavaScript 的前端应用，用于电商图片的自动套版生成。

## 功能特性

- 🎨 支持多张参考图批量生成
- 📤 上传产品图和参考图
- ✏️ 可选的卖点文案输入
- 📐 可配置图片尺寸（1K/2K/4K）
- 🎯 可配置清晰度（标准/高清/超高清）
- ⬇️ 支持单张图片下载

## 技术栈

- 纯 HTML + CSS + JavaScript（无框架依赖）
- 响应式设计，支持移动端
- 使用 Fetch API 与后端通信

## 安全说明

✅ **本前端代码不包含任何 API Key 或敏感信息**

- API Key 安全保存在后端服务器（`server.py`）
- 前端只包含后端 API 地址配置
- 所有敏感操作都在后端完成

## 使用方法

### 1. 本地开发

直接在浏览器中打开 `index.html` 文件即可。

**注意**：需要确保后端服务器已启动并运行在 `http://localhost:8000`

### 2. 配置后端 API 地址

#### 方式一：直接修改代码（简单但不推荐用于生产）

编辑 `index.html` 文件中的以下部分：

```javascript
const BACKEND_API_URL = "http://localhost:8000/api/generate";
```

#### 方式二：使用配置文件（推荐用于生产环境）

1. 复制 `config.example.js` 为 `config.js`
2. 修改 `config.js` 中的 `API_URL` 为实际的后端服务器地址
3. 在 `index.html` 的 `<head>` 标签中添加：
   ```html
   <script src="config.js"></script>
   ```

**⚠️ 重要**：`config.js` 文件已添加到 `.gitignore`，不会被提交到 Git。

### 3. 部署到服务器

可以将 `frontend` 文件夹部署到任何静态文件服务器：

- **Nginx**: 将 `frontend` 文件夹内容放到网站根目录
- **Apache**: 将 `frontend` 文件夹内容放到 `htdocs` 目录
- **GitHub Pages**: 将 `frontend` 文件夹内容推送到 GitHub Pages
- **Vercel/Netlify**: 直接部署 `frontend` 文件夹

**重要**：部署到生产环境时，记得修改 `BACKEND_API_URL` 为实际的后端服务器地址。

## 文件结构

```
frontend/
├── index.html          # 主页面（包含所有 HTML、CSS、JavaScript）
├── config.example.js  # 配置文件示例
├── .gitignore         # Git 忽略文件配置
└── README.md          # 本说明文件
```

## 浏览器兼容性

- Chrome/Edge (推荐)
- Firefox
- Safari
- 移动端浏览器

## 注意事项

1. **后端依赖**：前端需要后端服务器支持，确保后端已启动
2. **CORS 配置**：如果前后端不在同一域名，需要后端配置 CORS
3. **API 地址**：生产环境需要修改 `BACKEND_API_URL` 为实际地址
4. **安全性**：API Key 只保存在后端，前端不包含任何敏感信息

## 开发说明

这是一个单文件应用，所有代码都在 `index.html` 中：
- CSS 样式在 `<style>` 标签中
- JavaScript 逻辑在 `<script>` 标签中
- 无需构建工具，直接打开即可使用

## License

MIT
