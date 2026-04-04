[简体中文](./README.zh-CN.md) | [English](./README.md)

<div align="center">
  <h1>Horosa Skill</h1>
  <p><strong>面向星阙 / Horosa 的离线优先 AI 基础设施层。</strong></p>
  <p>让 Claude、Codex、Open WebUI、OpenClaw 这类 AI 在本机直接调用真正的星阙算法、完整 AI 导出协议和离线 runtime，并把每次结果写成可检索的结构化记忆。</p>

  <p>
    <a href="https://github.com/Horace-Maxwell/horosa-skill">
      <img src="https://img.shields.io/badge/查看-仓库-0f172a?style=for-the-badge&logo=github" alt="查看仓库" />
    </a>
    <a href="https://github.com/Horace-Maxwell/horosa-skill/releases">
      <img src="https://img.shields.io/badge/查看-Releases-1d4ed8?style=for-the-badge&logo=github" alt="查看 Releases" />
    </a>
    <a href="./README.md">
      <img src="https://img.shields.io/badge/Read%20in-English-0f766e?style=for-the-badge" alt="Read in English" />
    </a>
  </p>

  <p>
    <img src="https://img.shields.io/github/stars/Horace-Maxwell/horosa-skill?style=for-the-badge" alt="GitHub stars" />
    <img src="https://img.shields.io/github/v/release/Horace-Maxwell/horosa-skill?display_name=tag&style=for-the-badge" alt="Release" />
    <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows-0f766e?style=for-the-badge" alt="Platforms" />
    <img src="https://img.shields.io/badge/runtime-离线优先-111827?style=for-the-badge" alt="Offline first runtime" />
    <img src="https://img.shields.io/badge/MCP-ready-111827?style=for-the-badge" alt="MCP ready" />
    <img src="https://img.shields.io/badge/structured-JSON%20artifacts-111827?style=for-the-badge" alt="Structured JSON artifacts" />
  </p>
</div>

![Horosa Skill hero](./docs/media/hero-banner.svg)

## 这个仓库到底是干什么的

星阙本身已经有很强的玄学算法、本地运行链路和 AI 导出能力。Horosa Skill 做的事情，是把这些能力整理成现代 AI 真正能稳定调用的交付层。

它解决的是这几个问题：

- runtime 怎么离线安装
- AI 怎么通过 MCP 或 CLI 调真实算法
- 输出怎么从自由文本变成稳定 JSON
- 本地结果怎么落库、复查、再检索
- GitHub 仓库怎么保持轻量，同时又不牺牲完整离线分发

如果你的目标是“别人 clone 仓库后，装一次，就能让 AI 在自己机器上直接调用真正的星阙方法”，这个仓库就是为这个目标做的。

## 当前已经能直接调用的方法

### 已上线的直接工具层

| 领域 | 当前可直接调用的方法 |
| --- | --- |
| 导出与调度 | `export_registry`、`export_parse`、`horosa_dispatch` |
| 核心星盘 | `chart`、`chart13`、`hellen_chart`、`guolao_chart`、`india_chart`、`relative`、`germany` |
| 推运方法 | `solarreturn`、`lunarreturn`、`solararc`、`givenyear`、`profection`、`pd`、`pdchart`、`zr`、`firdaria`、`decennials` |
| 中文术数 | `ziwei_birth`、`ziwei_rules`、`bazi_birth`、`bazi_direct`、`liureng_gods`、`liureng_runyear`、`qimen`、`taiyi`、`jinkou`、`tongshefa`、`sanshiunited`、`suzhan`、`sixyao`、`jieqi_year`、`nongli_time`、`gua_desc`、`gua_meiyi` |
| 其他模块 | `otherbu` |

### 已建模的 AI 导出协议面

Horosa Skill 不只是能跑工具，还已经把星阙 AI 导出协议整理成机器可读表面，覆盖：

- `astrochart`、`indiachart`、`astrochart_like`、`relative`
- `primarydirect`、`primarydirchart`、`zodialrelease`、`firdaria`、`profection`、`solararc`、`solarreturn`、`lunarreturn`、`givenyear`、`decennials`
- `bazi`、`ziwei`、`suzhan`、`sixyao`、`tongshefa`、`liureng`、`jinkou`、`qimen`、`sanshiunited`、`taiyi`
- `guolao`、`germany`、`jieqi`、`jieqi_meta`、`jieqi_chunfen`、`jieqi_xiazhi`、`jieqi_qiufen`、`jieqi_dongzhi`
- `otherbu`、`generic`

### 明确不纳入本次发布

- `fengshui`

## 这个仓库真正强的地方

| 能力 | 意义 |
| --- | --- |
| 真离线 runtime | 安装后可以在本机直接跑算法、星历、导出协议，不依赖外部服务 |
| 稳定结构化返回 | 每个工具统一返回 `ok`、`tool`、`version`、`input_normalized`、`data`、`summary`、`warnings`、`memory_ref`、`error` |
| 导出协议固化 | 支持的方法会自动带 `export_snapshot` 和 `export_format`，方便 AI 稳定消费 |
| 本地记忆可检索 | 结果进入 SQLite 和 JSON artifact，可复查、可复用、可检索 |
| 轻仓库 + 重 Release | GitHub 仓库保持干净，完整 runtime 通过 Releases 分发 |

## 快速开始

```bash
cd horosa-skill
uv sync
uv run horosa-skill install
uv run horosa-skill doctor
uv run horosa-skill serve
```

默认 MCP 地址：

```text
http://127.0.0.1:8765/mcp
```

如果要给 Claude Desktop 这类 stdio 客户端使用：

```bash
cd horosa-skill
uv run horosa-skill serve --transport stdio
```

## 最不容易混淆的用法

如果你只是第一次上手，直接记这 4 条就够了：

1. 安装并检查 runtime

```bash
cd horosa-skill
uv sync
uv run horosa-skill install
uv run horosa-skill doctor
```

2. 让 AI 自己选工具

```bash
echo '{
  "query":"请综合奇门、六壬和星盘分析当前状态",
  "birth":{"date":"1990-01-01","time":"12:00","zone":"8","lat":"31n14","lon":"121e28"},
  "save_result": true
}' | uv run horosa-skill ask --stdin
```

3. 精确查看某一条记录

```bash
uv run horosa-skill memory show <run_id>
```

4. 把 AI 最终回答回写到那条记录

```bash
echo '{
  "run_id":"<run_id>",
  "user_question":"我接下来事业走势如何？",
  "ai_answer":"先稳后升，宜先整理资源再扩张。",
  "ai_answer_structured":{"trend":"up_later"}
}' | uv run horosa-skill memory answer --stdin
```

## 典型调用示例

输出完整星阙 AI export registry：

```bash
cd horosa-skill
uv run horosa-skill export registry
```

把星阙 AI 导出文本转为结构化 JSON：

```bash
cd horosa-skill
echo '{
  "technique": "qimen",
  "content": "[起盘信息]\n参数\n\n[八宫]\n八宫内容\n\n[演卦]\n演卦内容"
}' | uv run horosa-skill export parse --stdin
```

直接跑一个工具：

```bash
echo '{"date":"1990-01-01","time":"12:00","zone":"8","lat":"31n14","lon":"121e28"}' \
  | uv run horosa-skill tool run chart --stdin
```

直接跑一个 Phase 2 本地方法：

```bash
echo '{"taiyin":"巽","taiyang":"坤","shaoyang":"震","shaoyin":"震"}' \
  | uv run horosa-skill tool run tongshefa --stdin
```

运行总调度器：

```bash
echo '{
  "query":"请综合奇门、六壬和星盘做当前状态分析",
  "birth":{"date":"1990-01-01","time":"12:00","zone":"8","lat":"31n14","lon":"121e28"},
  "save_result": true
}' | uv run horosa-skill dispatch --stdin
```

## AI 客户端接入

- [Claude Desktop 配置](./horosa-skill/examples/clients/claude_desktop_config.json)
- [Codex 配置](./horosa-skill/examples/clients/codex-config.toml)
- [Open WebUI 接入说明](./horosa-skill/examples/clients/openwebui-streamable-http.md)
- [OpenClaw 接入说明](./horosa-skill/examples/clients/openclaw-mcp.md)

## Runtime 放置模型

这个项目故意把三层分开：

| 层 | 放在哪里 | 为什么 |
| --- | --- | --- |
| 公共仓库层 | GitHub 仓库 | 代码、文档、CLI、MCP、示例、发布脚本 |
| 维护者打包输入层 | 本地 `vendor/runtime-source/` | 打 runtime 包时需要的大体积源 |
| 最终用户运行层 | macOS 在 `~/.horosa/runtime/current`，Windows 在 `%LOCALAPPDATA%/Horosa/runtime/current` | 安装后真正执行算法的离线 runtime |

这样做的目的，就是让仓库看起来专业、轻量、可审查，同时又不牺牲离线打包能力。

## 本地存储模型

结构化结果默认落在本地：

- macOS / Linux：`~/.horosa-skill/`
- Windows：`%APPDATA%/HorosaSkill/`

每次运行会写入：

- run 元信息
- tool call 记录
- entity 索引
- `runs/<YYYY>/<MM>/<DD>/` 下的 JSON artifact
- 一份 `run manifest`，方便按一次完整调用来查看和管理

每条记录现在默认同时保存：

- 原始 query / user question
- 每个 tool 的结构化结果
- 最终 AI answer
- 可选的 `ai_answer_structured`

如果你的 AI 先调工具、再自己生成最终回答，推荐流程是：

1. 先调用 `ask` 或 `tool run`
2. 记下返回里的 `memory_ref.run_id`
3. 用 `memory answer` 把 AI 最终回答写回去
4. 用 `memory show <run_id>` 查看完整记录

## 仓库结构

| 路径 | 作用 |
| --- | --- |
| [`horosa-skill/`](./horosa-skill) | Python 包、CLI、MCP server、测试、示例配置、发布脚本 |
| [`docs/`](./docs) | runtime 规范、覆盖矩阵、发布说明、维护文档 |
| [`vendor/`](./vendor) | 本地离线打包所需的 runtime source 区域 |

建议顺手看的文档：

- [Repo Layout](./docs/REPO_LAYOUT.md)
- [Offline Runtime Releases](./docs/OFFLINE_RUNTIME_RELEASES.md)
- [Runtime Manifest Spec](./docs/RUNTIME_MANIFEST_SPEC.md)
- [Algorithm Coverage](./docs/ALGORITHM_COVERAGE.md)
- [Vendored Runtime Sources](./vendor/README.md)

## 当前状态

已经完成：

- 离线 runtime install、doctor、serve、stop
- macOS 和 Windows runtime release 资产
- 本地 MCP 和 JSON-first CLI
- 完整 export registry 与 export parser
- SQLite + JSON artifact 记忆层
- 支持方法的固定 export contract
- `qimen`、`taiyi`、`jinkou`、`tongshefa` 的本地 headless engine
- `sanshiunited` 的本地聚合层
- `hellen_chart`、`guolao_chart`、`germany`、`firdaria`、`decennials`、`suzhan`、`sixyao`、`otherbu`
- 面向调用、输出、存储、检索的全量自检

## Contributing

见 [CONTRIBUTING.md](./CONTRIBUTING.md)。
