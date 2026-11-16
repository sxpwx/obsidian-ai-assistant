# DuoAI Assistant

An Obsidian plugin that lets you use any custom OpenAI-compatible LLM API. Configure your own endpoint, API key, and model, then generate continuations, summaries, translations, and polished text right inside your notes.

## Features

- Bring your own model: custom API base URL, API key, model name, temperature, max tokens, system prompt, and timeout
- Built-in provider presets: OpenAI, DeepSeek, Qwen, Kimi, Zhipu GLM, local Ollama, or fully custom
- Text actions on selection: summarize, translate, polish, and explain
- Continue writing from the text before the cursor
- Ghost-text completion: after the cursor rests for a configurable delay, a semi-transparent suggestion appears at the cursor. Press `Tab` to accept or `Esc` to dismiss. Any typing or cursor move clears it.
- Custom prompts with a `{{text}}` placeholder for the selected text
- Ask AI: a dialog for free-form questions; copy or insert the answer into the current note
- A "Test connection" button in settings

## Installation

Install from Obsidian Community Plugins: open **Settings → Community plugins**, browse for **DuoAI Assistant**, then install and enable it.

Manual installation:

1. In Obsidian, open **Settings → Community plugins → Open plugins folder** (this is `<vault>/.obsidian/plugins/`).
2. Create a subfolder named `duoai-assistant`.
3. Copy `main.js`, `manifest.json`, and `styles.css` from this repository into it.
4. Restart Obsidian and enable **DuoAI Assistant** under Community plugins.

## Configuration

Open **Settings → Community plugins → DuoAI Assistant**:

1. Pick a provider preset (or choose **Custom** to fill everything manually).
2. Enter the API base URL (**without** the `/chat/completions` suffix).
3. Enter your API key.
4. Enter the model name.
5. Click **Test connection** to verify.

Common base URLs (may change; check the provider's official docs):

| Provider | Base URL | Example model |
| --- | --- | --- |
| OpenAI | `https://api.openai.com/v1` | `gpt-4o-mini` |
| DeepSeek | `https://api.deepseek.com/v1` | `deepseek-chat` |
| Qwen | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus` |
| Kimi | `https://api.moonshot.cn/v1` | `moonshot-v1-8k` |
| Zhipu GLM | `https://open.bigmodel.cn/api/paas/v4` | `glm-4-flash` |
| Ollama (local) | `http://localhost:11434/v1` | `llama3` |

When using local Ollama, you can put any placeholder value in the API key field (for example `ollama`) and make sure `ollama serve` is running.

## Usage

- **Command palette** (`Ctrl/Cmd + P`): search `AI:` for summarize, translate, polish, explain, continue writing, custom prompt, and ask AI.
- **Context menu**: right-click anywhere to get **AI: Continue writing** (no selection needed, uses the text before the cursor). With text selected, you'll also get summarize, translate, polish, explain, and custom prompt.
- **Ghost-text completion**: in edit mode, rest the cursor at a spot. After the configured delay (10 seconds by default), a semi-transparent suggestion appears; `Tab` inserts it and `Esc` dismisses it. In settings, the **Auto-completion wait time** row has a toggle to enable/disable and a field to set the delay. Changes apply immediately.
- **AI: Test ghost completion now**: trigger a completion immediately instead of waiting, to verify the feature.
- **AI: Diagnose ghost completion**: writes step-by-step status to `ghost-diag.txt` in the plugin folder for troubleshooting.
- **Custom prompt**: use `{{text}}` for the selected text. If you don't include the placeholder, the selection is appended automatically.
- **Hotkeys**: search `AI:` under Settings → Hotkeys to bind your favorites.

## FAQ

- **401**: API key is wrong, or the key has no access to the selected model.
- **404**: API base URL is incorrect. Do not include the `/chat/completions` suffix.
- **Request timeout**: increase the timeout setting, or check your network/proxy.
- **No response**: make sure the plugin is enabled and the API URL and key are filled in.

## Files

| File | Purpose |
| --- | --- |
| `main.js` | Plugin entry point |
| `manifest.json` | Plugin metadata |
| `styles.css` | Styles |
| `versions.json` | Plugin-to-Obsidian version compatibility map |
| `install.py` | Optional local install helper (not required for community install) |

## License

MIT
