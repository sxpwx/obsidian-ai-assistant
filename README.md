# DuoAI Assistant

An Obsidian plugin that lets you use any custom LLM API. Configure your own endpoint, key, and model, then generate continuations, summaries, translations, and polished text right inside your notes. Works with OpenAI-compatible APIs as well as Anthropic Claude's native Messages API.

一款 Obsidian 插件，可接入任意自定义大模型 API。填写自己的接口地址、密钥和模型，即可在笔记中续写、总结、翻译和润色。支持 OpenAI 兼容接口，也原生支持 Anthropic Claude 的 Messages API。

## Features

- Bring your own model: custom API base URL, API key, model name, temperature, max tokens, system prompt, and timeout
- Built-in presets: OpenAI, Anthropic Claude, xAI Grok, DeepSeek, Qwen, Kimi, Zhipu GLM, local Ollama, or fully custom
- Text actions on selection: summarize, translate, polish, and explain
- Continue writing from the text before the cursor
- Ghost-text completion: after the cursor rests for a configurable delay, a semi-transparent suggestion appears at the cursor. Press `Tab` to accept or `Esc` to dismiss. Any typing or cursor move clears it
- Custom prompts with a `{{text}}` placeholder for the selected text
- Ask AI: a dialog for free-form questions; copy or insert the answer into the current note
- Bilingual settings panel (Chinese and English)
- A "Test connection" button in settings

## 功能

- 自带模型：可自定义 API 地址、密钥、模型名、温度、最大 Token、系统提示词和超时时间
- 内置服务商预设：OpenAI、Anthropic Claude、xAI Grok、DeepSeek、通义千问、Kimi、智谱 GLM、本地 Ollama，或完全自定义
- 选中文本处理：总结、翻译、润色、解释
- 续写：基于光标前的内容继续生成
- 光标停留自动续写：光标静止达到设定时间后，在光标处显示半透明建议；按 `Tab` 接受、`Esc` 放弃，打字或移动光标即消失
- 自定义提示词：用 `{{text}}` 代表选中文本
- AI 问答：弹窗提问，可复制回答或插入当前笔记
- 设置面板中英双语
- 设置内提供「测试连接」按钮

## Installation / 安装

Install from Obsidian Community Plugins: open **Settings → Community plugins**, browse for **DuoAI Assistant**, then install and enable it.

从 Obsidian 社区插件安装：打开**设置 → 第三方插件**，搜索 **DuoAI Assistant**，安装并启用。

Manual installation / 手动安装:

1. Open **Settings → Community plugins → Open plugins folder** (`<vault>/.obsidian/plugins/`).
   打开**设置 → 第三方插件 → 打开插件文件夹**（即 `<vault>/.obsidian/plugins/`）。
2. Create a subfolder named `duoai-assistant`.
   新建名为 `duoai-assistant` 的文件夹。
3. Copy `main.js`, `manifest.json`, and `styles.css` into it.
   把 `main.js`、`manifest.json`、`styles.css` 复制进去。
4. Restart Obsidian and enable **DuoAI Assistant**.
   重启 Obsidian，在第三方插件中启用 **DuoAI Assistant**。

## Configuration / 配置

Open **Settings → Community plugins → DuoAI Assistant**:

打开**设置 → 第三方插件 → DuoAI Assistant**：

1. Pick a provider preset (or **Custom** to fill everything manually).
   选择服务商预设（或「自定义」手动填写）。
2. Enter the API base URL (**without** the `/chat/completions` or `/messages` suffix).
   填写 API 根地址（**不要**包含 `/chat/completions` 或 `/messages`）。
3. Enter your API key.
   填写 API Key。
4. Enter the model name.
   填写模型名称。
5. Click **Test connection** to verify.
   点「测试连接」验证。

Common base URLs (may change; check the provider's official docs):

常用地址（可能调整，以服务商官方文档为准）：

| Provider / 服务商 | Base URL | Example model / 示例模型 |
| --- | --- | --- |
| OpenAI | `https://api.openai.com/v1` | `gpt-4o-mini` |
| Anthropic Claude | `https://api.anthropic.com/v1` | `claude-sonnet-5-5` |
| xAI Grok | `https://api.x.ai/v1` | `grok-4.6` |
| DeepSeek | `https://api.deepseek.com/v1` | `deepseek-chat` |
| Qwen / 通义千问 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus` |
| Kimi / 月之暗面 | `https://api.moonshot.cn/v1` | `moonshot-v1-8k` |
| Zhipu GLM / 智谱 | `https://open.bigmodel.cn/api/paas/v4` | `glm-4-flash` |
| Ollama (local / 本地) | `http://localhost:11434/v1` | `llama3` |

Anthropic uses the native Messages API (`/v1/messages`) automatically; no extra configuration is needed. For local Ollama, any placeholder value works as the API key (for example `ollama`), just make sure `ollama serve` is running.

Anthropic 会自动使用原生 Messages API（`/v1/messages`），无需额外设置。使用本地 Ollama 时，API Key 可填任意占位值（例如 `ollama`），并确保 `ollama serve` 已启动。

## Usage / 使用

- **Command palette** (`Ctrl/Cmd + P`): search `AI:` for summarize, translate, polish, explain, continue writing, custom prompt, and ask AI.
- **Context menu**: right-click anywhere for **AI: Continue writing** (no selection needed, uses the text before the cursor). With text selected, you also get summarize, translate, polish, explain, and custom prompt.
- **Ghost-text completion**: in edit mode, rest the cursor at a spot. After the configured delay (10 seconds by default), a semi-transparent suggestion appears; `Tab` inserts it and `Esc` dismisses it. The **Auto-completion delay** row in settings has a toggle and a delay field; changes apply immediately.
- **AI: Test ghost completion now**: trigger a completion immediately instead of waiting.
- **AI: Diagnose ghost completion**: writes step-by-step status to `ghost-diag.txt` in the plugin folder for troubleshooting.
- **Custom prompt**: use `{{text}}` for the selected text. If you omit the placeholder, the selection is appended automatically.
- **Hotkeys**: search `AI:` under Settings → Hotkeys to bind your favorites.

- **命令面板**（`Ctrl/Cmd + P`）：搜索 `AI:`，可执行总结、翻译、润色、解释、续写、自定义提示词和 AI 问答。
- **右键菜单**：在编辑区任意位置右键都有 **AI: 续写**（无需选中文字，基于光标前内容）。选中文字后还会出现总结、翻译、润色、解释和自定义提示词。
- **自动续写**：编辑模式下把光标停住，达到设定时间（默认 10 秒）后光标处出现半透明建议；按 `Tab` 插入、`Esc` 放弃。设置里的「自动续写等待时间」一行含开关和毫秒输入框，修改立即生效。
- **AI: 立即测试幽灵续写**：不等延迟，马上触发一次，便于验证功能。
- **AI: 诊断自动续写**：把每一步状态写入插件目录下的 `ghost-diag.txt`，用于排查问题。
- **自定义提示词**：用 `{{text}}` 代表选中文本；若省略占位符，选中文本会自动附在提示词末尾。
- **快捷键**：在「设置 → 快捷键」搜索 `AI:` 可为常用命令绑定快捷键。

## FAQ / 常见问题

- **401**: API key is wrong, or the key has no access to the selected model. / 密钥错误，或该密钥无权访问所选模型。
- **404**: API base URL is incorrect. Remove the `/chat/completions` or `/messages` suffix. / 地址不正确，请去掉 `/chat/completions` 或 `/messages` 后缀。
- **Request timeout**: increase the timeout setting, or check your network/proxy. / 超时，请调大超时时间或检查网络与代理。
- **No response**: make sure the plugin is enabled and the API URL and key are filled in. / 无回复，请确认插件已启用且地址与密钥已填写。
- **Anthropic 400**: make sure the model name is valid for your account, for example `claude-sonnet-5-5`. / 若返回 400，请确认模型名在你的账号下可用，例如 `claude-sonnet-5-5`。

## Files / 文件

| File | Purpose / 用途 |
| --- | --- |
| `main.js` | Plugin entry point / 插件主程序 |
| `manifest.json` | Plugin metadata / 插件元数据 |
| `styles.css` | Styles / 样式 |
| `versions.json` | Plugin-to-Obsidian version compatibility map / 版本兼容映射 |
| `install.py` | Optional local install helper (not required for community install) / 可选的本地安装脚本（社区安装无需此文件） |

## License / 许可证

MIT
