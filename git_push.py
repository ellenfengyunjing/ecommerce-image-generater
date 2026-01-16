#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Git 推送脚本 - 用于处理中文路径问题
"""
import os
import subprocess
import sys

# 设置工作目录
work_dir = r"d:\Ellen工作资料\AI项目\电商参考图生图网页\frontend"
os.chdir(work_dir)

print("当前工作目录:", os.getcwd())
print("\n正在执行 Git 操作...\n")

# 1. 配置 Git 用户信息
print("[1/5] 配置 Git 用户信息...")
subprocess.run(["git", "config", "user.name", "ellenfengyunjing"], check=False)
subprocess.run(["git", "config", "user.email", "ellenfengyunjing@users.noreply.github.com"], check=False)
print("✓ Git 用户信息已配置\n")

# 2. 添加所有文件
print("[2/5] 添加所有文件到 Git...")
result = subprocess.run(["git", "add", "."], capture_output=True, text=True, encoding='utf-8')
if result.returncode != 0:
    print(f"警告: {result.stderr}")
else:
    print("✓ 文件已添加\n")

# 3. 检查状态
print("[3/5] 检查 Git 状态...")
result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, encoding='utf-8')
if result.stdout.strip():
    print("待提交的文件:")
    print(result.stdout)
else:
    print("没有待提交的文件")
print()

# 4. 提交
print("[4/5] 提交更改...")
result = subprocess.run(
    ["git", "commit", "-m", "Initial commit: Frontend code for ecommerce image generator"],
    capture_output=True,
    text=True,
    encoding='utf-8'
)
if result.returncode != 0:
    if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
        print("⚠ 没有需要提交的更改")
    else:
        print(f"错误: {result.stderr}")
        sys.exit(1)
else:
    print("✓ 提交成功\n")

# 5. 推送到 GitHub
print("[5/5] 推送到 GitHub...")
result = subprocess.run(
    ["git", "push", "-u", "origin", "main"],
    capture_output=True,
    text=True,
    encoding='utf-8'
)
if result.returncode != 0:
    print(f"错误: {result.stderr}")
    if "src refspec main does not match any" in result.stderr:
        print("\n提示: 没有提交记录，请先确保有文件被提交")
    elif "Authentication" in result.stderr or "fatal" in result.stderr:
        print("\n提示: 可能需要身份验证，请使用 Personal Access Token")
    sys.exit(1)
else:
    print("✓ 推送成功！")
    print(result.stdout)

print("\n完成！")
