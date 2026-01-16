@echo off
chcp 65001 >nul
cd /d "d:\Ellen工作资料\AI项目\电商参考图生图网页\frontend"

echo ========================================
echo 推送到 GitHub
echo ========================================
echo.

echo [1/4] 检查 Git 配置...
git config user.name >nul 2>&1
if errorlevel 1 (
    echo 未配置 Git 用户信息，请先配置：
    echo git config user.name "你的名字"
    echo git config user.email "你的邮箱"
    pause
    exit /b 1
)

echo [2/4] 添加文件到 Git...
git add .
if errorlevel 1 (
    echo 添加文件失败！
    pause
    exit /b 1
)

echo [3/4] 提交更改...
git commit -m "Initial commit: Frontend code for ecommerce image generator"
if errorlevel 1 (
    echo 提交失败！可能是没有更改需要提交。
)

echo [4/4] 推送到 GitHub...
git push -u origin main
if errorlevel 1 (
    echo.
    echo 推送失败！可能的原因：
    echo 1. 需要身份验证（请使用 Personal Access Token）
    echo 2. 远程仓库已有内容（需要先拉取）
    echo.
    echo 请查看错误信息并参考 推送说明.md
    pause
    exit /b 1
)

echo.
echo ========================================
echo 推送成功！
echo ========================================
echo.
pause
