# -*- coding: utf-8 -*-
"""将 AI 助手插件自动安装到本机 Obsidian 的 Vault 中。"""
import json
import os
import shutil
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

PLUGIN_ID = 'ai-assistant'
FILES = ['main.js', 'manifest.json', 'styles.css']
SRC_DIR = os.path.dirname(os.path.abspath(__file__))


def find_config():
    appdata = os.environ.get('APPDATA')
    if not appdata:
        return None
    path = os.path.join(appdata, 'obsidian', 'obsidian.json')
    return path if os.path.isfile(path) else None


def get_vaults(config_path):
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print('读取 Obsidian 配置失败：', e)
        return []
    vaults = []
    for info in data.get('vaults', {}).values():
        path = info.get('path')
        if path and os.path.isdir(path):
            vaults.append((path, bool(info.get('open'))))
    return vaults


def choose_vault(vaults):
    if not vaults:
        return None
    if len(vaults) == 1:
        return [vaults[0][0]]
    print('检测到多个 Vault：')
    for i, (path, opened) in enumerate(vaults, 1):
        mark = '（当前打开）' if opened else ''
        print('  {}. {}{}'.format(i, path, mark))
    print('  0. 全部安装')
    while True:
        choice = input('请选择要安装的序号（默认 1）：').strip() or '1'
        if choice == '0':
            return [path for path, _ in vaults]
        if choice.isdigit() and 1 <= int(choice) <= len(vaults):
            return [vaults[int(choice) - 1][0]]
        print('输入无效，请重新输入。')


def install(vault):
    target = os.path.join(vault, '.obsidian', 'plugins', PLUGIN_ID)
    os.makedirs(target, exist_ok=True)
    for name in FILES:
        src = os.path.join(SRC_DIR, name)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(target, name))
        else:
            print('缺少文件：', name)
            return False
    print('已安装到：', target)
    return True


def main():
    print('=== AI 助手插件安装程序 ===')
    missing = [n for n in FILES if not os.path.isfile(os.path.join(SRC_DIR, n))]
    if missing:
        print('插件文件不完整，缺少：', ', '.join(missing))
        return
    config = find_config()
    if not config:
        print('未找到 Obsidian 配置文件（%APPDATA%\\obsidian\\obsidian.json）。')
        print('请手动把本文件夹中的 main.js / manifest.json / styles.css 复制到')
        print('Vault 目录下的 .obsidian/plugins/ai-assistant/ 文件夹中。')
        return
    vaults = get_vaults(config)
    chosen = choose_vault(vaults)
    if not chosen:
        print('未找到可用的 Vault，请手动安装。')
        return
    ok = 0
    for vault in chosen:
        if install(vault):
            ok += 1
    print('')
    print('安装完成，共 {} 个 Vault。'.format(ok))
    print('请重新启动 Obsidian，在「设置 → 第三方插件」中启用本插件。')


if __name__ == '__main__':
    main()
