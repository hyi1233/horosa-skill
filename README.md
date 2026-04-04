[简体中文](./README.zh-CN.md) | **English**

<div align="center">
  <h1>Horosa Skill</h1>
  <p><strong>Offline-first AI infrastructure for Xingque / Horosa.</strong></p>
  <p>Install once, run real Xingque methods locally, expose them to Claude, Codex, Open WebUI, or OpenClaw through MCP, and persist every result as structured memory.</p>

  <p>
    <a href="https://github.com/Horace-Maxwell/horosa-skill">
      <img src="https://img.shields.io/badge/Browse-Repository-0f172a?style=for-the-badge&logo=github" alt="Browse Repository" />
    </a>
    <a href="https://github.com/Horace-Maxwell/horosa-skill/releases">
      <img src="https://img.shields.io/badge/Browse-Releases-1d4ed8?style=for-the-badge&logo=github" alt="Browse Releases" />
    </a>
    <a href="./README.zh-CN.md">
      <img src="https://img.shields.io/badge/Read%20in-Chinese-0f766e?style=for-the-badge" alt="Read in Chinese" />
    </a>
  </p>

  <p>
    <img src="https://img.shields.io/github/stars/Horace-Maxwell/horosa-skill?style=for-the-badge" alt="GitHub stars" />
    <img src="https://img.shields.io/github/v/release/Horace-Maxwell/horosa-skill?display_name=tag&style=for-the-badge" alt="Release" />
    <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows-0f766e?style=for-the-badge" alt="Platforms" />
    <img src="https://img.shields.io/badge/runtime-offline%20first-111827?style=for-the-badge" alt="Offline first runtime" />
    <img src="https://img.shields.io/badge/MCP-ready-111827?style=for-the-badge" alt="MCP ready" />
    <img src="https://img.shields.io/badge/structured-JSON%20artifacts-111827?style=for-the-badge" alt="Structured JSON artifacts" />
  </p>
</div>

![Horosa Skill hero](./docs/media/hero-banner.svg)

## Why This Repo Exists

Xingque already has deep metaphysical logic, rich export content, and a serious local runtime story. What it did not have was a GitHub-first delivery layer that modern AI tools can call cleanly.

Horosa Skill is that delivery layer:

- offline runtime install from GitHub Releases
- local MCP server plus JSON-first CLI
- stable structured envelopes instead of loose text
- machine-readable Xingque export protocol
- local SQLite plus JSON artifact storage for retrieval and reuse

If the goal is "clone the repo, install once, and let AI call real Horosa methods locally without a remote service," this repo is built for exactly that.

## What Ships Today

### Directly callable methods

| Domain | Methods available now |
| --- | --- |
| Export + orchestration | `export_registry`, `export_parse`, `horosa_dispatch` |
| Core astrology | `chart`, `chart13`, `hellen_chart`, `guolao_chart`, `india_chart`, `relative`, `germany` |
| Predictive astrology | `solarreturn`, `lunarreturn`, `solararc`, `givenyear`, `profection`, `pd`, `pdchart`, `zr`, `firdaria`, `decennials` |
| Chinese metaphysics | `ziwei_birth`, `ziwei_rules`, `bazi_birth`, `bazi_direct`, `liureng_gods`, `liureng_runyear`, `qimen`, `taiyi`, `jinkou`, `tongshefa`, `sanshiunited`, `suzhan`, `sixyao`, `jieqi_year`, `nongli_time`, `gua_desc`, `gua_meiyi` |
| Other occult modules | `otherbu` |

### Export protocol domains already modeled

Horosa Skill does not only expose tools. It also models Xingque's AI export registry as a machine-readable protocol surface, including:

- `astrochart`, `indiachart`, `astrochart_like`, `relative`
- `primarydirect`, `primarydirchart`, `zodialrelease`, `firdaria`, `profection`, `solararc`, `solarreturn`, `lunarreturn`, `givenyear`, `decennials`
- `bazi`, `ziwei`, `suzhan`, `sixyao`, `tongshefa`, `liureng`, `jinkou`, `qimen`, `sanshiunited`, `taiyi`
- `guolao`, `germany`, `jieqi`, `jieqi_meta`, `jieqi_chunfen`, `jieqi_xiazhi`, `jieqi_qiufen`, `jieqi_dongzhi`
- `otherbu`, `generic`

### Explicit shipping exclusion

- `fengshui`

## What Makes This Repo Different

| Capability | What it means |
| --- | --- |
| Real offline runtime | The calculation stack, ephemeris, export logic, and MCP surface can run locally after install |
| Structured result contract | Every tool returns `ok`, `tool`, `version`, `input_normalized`, `data`, `summary`, `warnings`, `memory_ref`, `error` |
| Export-aware outputs | Supported methods also attach `export_snapshot` and `export_format` so AI can consume the same semantic structure every time |
| Retrieval-ready memory | Results land in SQLite and JSON artifacts for later search, replay, and chaining |
| Release-based distribution | The repo stays lightweight while full runtimes ship through GitHub Releases |

## Quick Start

```bash
cd horosa-skill
uv sync
uv run horosa-skill install
uv run horosa-skill doctor
uv run horosa-skill serve
```

Default MCP endpoint:

```text
http://127.0.0.1:8765/mcp
```

For stdio clients such as Claude Desktop:

```bash
cd horosa-skill
uv run horosa-skill serve --transport stdio
```

## Least Confusing Workflow

If you only want the shortest path, use these 4 steps:

1. Install and verify the offline runtime

```bash
cd horosa-skill
uv sync
uv run horosa-skill install
uv run horosa-skill doctor
```

2. Let the dispatcher choose methods for you

```bash
echo '{
  "query":"Please use qimen, liureng, and chart methods to analyze the current situation",
  "birth":{"date":"1990-01-01","time":"12:00","zone":"8","lat":"31n14","lon":"121e28"},
  "save_result": true
}' | uv run horosa-skill ask --stdin
```

3. Inspect one exact record

```bash
uv run horosa-skill memory show <run_id>
```

4. Write the AI's final answer back into that record

```bash
echo '{
  "run_id":"<run_id>",
  "user_question":"What does this mean for my career next?",
  "ai_answer":"The pattern is cautious first, then gradually upward.",
  "ai_answer_structured":{"trend":"up_later"}
}' | uv run horosa-skill memory answer --stdin
```

## Example Flows

Run the export registry:

```bash
cd horosa-skill
uv run horosa-skill export registry
```

Parse Xingque export text into structured JSON:

```bash
cd horosa-skill
echo '{
  "technique": "qimen",
  "content": "[起盘信息]\n参数\n\n[八宫]\n八宫内容\n\n[演卦]\n演卦内容"
}' | uv run horosa-skill export parse --stdin
```

Run a tool directly:

```bash
echo '{"date":"1990-01-01","time":"12:00","zone":"8","lat":"31n14","lon":"121e28"}' \
  | uv run horosa-skill tool run chart --stdin
```

Run a Phase 2 local method directly:

```bash
echo '{"taiyin":"巽","taiyang":"坤","shaoyang":"震","shaoyin":"震"}' \
  | uv run horosa-skill tool run tongshefa --stdin
```

Run the dispatcher:

```bash
echo '{
  "query":"Please use qimen, liureng, and chart methods to analyze the current situation",
  "birth":{"date":"1990-01-01","time":"12:00","zone":"8","lat":"31n14","lon":"121e28"},
  "save_result": true
}' | uv run horosa-skill dispatch --stdin
```

## AI Client Integrations

- [Claude Desktop config](./horosa-skill/examples/clients/claude_desktop_config.json)
- [Codex config](./horosa-skill/examples/clients/codex-config.toml)
- [Open WebUI setup](./horosa-skill/examples/clients/openwebui-streamable-http.md)
- [OpenClaw setup](./horosa-skill/examples/clients/openclaw-mcp.md)

## Runtime Model

This project keeps three layers separate on purpose:

| Layer | Lives where | Why |
| --- | --- | --- |
| Public repo | GitHub repository | code, docs, CLI, MCP surface, examples, release scripts |
| Maintainer packaging input | local `vendor/runtime-source/` | large runtime sources needed to build release assets |
| End-user runtime | `~/.horosa/runtime/current` on macOS or `%LOCALAPPDATA%/Horosa/runtime/current` on Windows | installed offline runtime used by real tool execution |

That separation keeps the repository reviewable without making runtime builds depend on random sibling directories.

## Local Storage Model

Structured results are stored locally by default:

- macOS / Linux: `~/.horosa-skill/`
- Windows: `%APPDATA%/HorosaSkill/`

Each saved run can persist:

- run metadata
- tool call records
- entity references
- JSON artifacts under `runs/<YYYY>/<MM>/<DD>/`
- one `run manifest` for easier per-run inspection and management

Each record can now also keep:

- the original query / user question
- every tool result for that run
- the AI's final answer
- optional `ai_answer_structured` JSON

Recommended pattern for external AI clients:

1. call `ask` or `tool run`
2. keep the returned `memory_ref.run_id`
3. write the final AI answer with `memory answer`
4. inspect the full record later with `memory show <run_id>`

## Repository Layout

| Path | Role |
| --- | --- |
| [`horosa-skill/`](./horosa-skill) | Python package, CLI, MCP server, tests, examples, and release scripts |
| [`docs/`](./docs) | Runtime specs, coverage docs, release notes, and maintainership docs |
| [`vendor/`](./vendor) | Local runtime source area for offline packaging |

Useful docs:

- [Repo Layout](./docs/REPO_LAYOUT.md)
- [Offline Runtime Releases](./docs/OFFLINE_RUNTIME_RELEASES.md)
- [Runtime Manifest Spec](./docs/RUNTIME_MANIFEST_SPEC.md)
- [Algorithm Coverage](./docs/ALGORITHM_COVERAGE.md)
- [Vendored Runtime Sources](./vendor/README.md)

## Current Status

Implemented now:

- offline runtime install, doctor, serve, and stop flow
- macOS and Windows runtime release assets
- local MCP plus JSON-first CLI
- full export registry and export parser
- structured storage with SQLite plus JSON artifacts
- fixed export contracts across supported methods
- headless local engines for `qimen`, `taiyi`, `jinkou`, and `tongshefa`
- local aggregator support for `sanshiunited`
- direct support for `hellen_chart`, `guolao_chart`, `germany`, `firdaria`, `decennials`, `suzhan`, `sixyao`, and `otherbu`
- full self-check coverage for call, output, storage, and retrieval

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
