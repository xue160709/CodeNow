#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX Pro Max 检索 — 面向 UI/UX 指南的 BM25 搜索

用法：
  python search.py "<查询>" [--domain <领域>] [--stack <技术栈>] [--max-results 3]
  python search.py "<查询>" --design-system [-p "项目名称"]
  python search.py "<查询>" --design-system --persist [-p "项目名称"] [--page "dashboard"]

领域：style、color、chart、landing、product、ux、typography、google-fonts 等（见 CSV_CONFIG）
技术栈：react、nextjs、vue、svelte、astro、swiftui、react-native、flutter 等

持久化（主文件 + 页面覆盖）：
  --persist    将设计系统写入 design-system/<项目>/MASTER.md
  --page       同时在 design-system/<项目>/pages/ 下生成页面覆盖文件
"""

import argparse
import sys
import io
from core import CSV_CONFIG, AVAILABLE_STACKS, MAX_RESULTS, search, search_stack
from design_system import generate_design_system, persist_design_system

# Windows 默认 cp1252 下强制 stdout/stderr 为 UTF-8，避免 emoji 等字符报错
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_output(result):
    """格式化检索结果（便于模型消费、控制 token）"""
    if "error" in result:
        return f"错误：{result['error']}"

    output = []
    if result.get("stack"):
        output.append(f"## UI Pro Max 技术栈指南")
        output.append(f"**技术栈：** {result['stack']} | **查询：** {result['query']}")
    else:
        output.append(f"## UI Pro Max 检索结果")
        output.append(f"**领域：** {result['domain']} | **查询：** {result['query']}")
    output.append(f"**数据源：** {result['file']} | **命中：** {result['count']} 条\n")

    for i, row in enumerate(result['results'], 1):
        output.append(f"### 结果 {i}")
        for key, value in row.items():
            value_str = str(value)
            if len(value_str) > 300:
                value_str = value_str[:300] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UI Pro Max 检索")
    parser.add_argument("query", help="检索查询字符串")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="检索领域（domain）")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help=f"按技术栈检索。可选：{', '.join(AVAILABLE_STACKS)}")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="最多返回条数（默认 3）")
    parser.add_argument("--json", action="store_true", help="以 JSON 输出")
    # 设计系统生成
    parser.add_argument("--design-system", "-ds", action="store_true", help="生成完整设计系统推荐")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="设计系统输出中的项目名称")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="设计系统输出格式：ascii 或 markdown")
    # 持久化（主文件 + 页面覆盖）
    parser.add_argument("--persist", action="store_true", help="将设计系统写入 design-system/<项目>/（分层目录）")
    parser.add_argument("--page", type=str, default=None, help="同时在 design-system/<项目>/pages/ 生成页面覆盖文件")
    parser.add_argument("--output-dir", "-o", type=str, default=None, help="持久化输出根目录（默认当前工作目录）")

    args = parser.parse_args()

    # 设计系统模式优先
    if args.design_system:
        result = generate_design_system(
            args.query, 
            args.project_name, 
            args.format,
            persist=args.persist,
            page=args.page,
            output_dir=args.output_dir
        )
        print(result)
        
        # 持久化成功后的终端说明
        if args.persist:
            project_slug = args.project_name.lower().replace(' ', '-') if args.project_name else "default"
            print("\n" + "=" * 60)
            print(f"✅ 设计系统已写入 design-system/{project_slug}/")
            print(f"   📄 design-system/{project_slug}/MASTER.md（全局规则）")
            if args.page:
                page_filename = args.page.lower().replace(' ', '-')
                print(f"   📄 design-system/{project_slug}/pages/{page_filename}.md（页面覆盖）")
            print("")
            print(f"📖 使用方式：实现某页时先看 design-system/{project_slug}/pages/[页面].md。")
            print(f"   若存在，则其中规则覆盖 MASTER.md；否则仅使用 MASTER.md。")
            print("=" * 60)
    # 技术栈检索
    elif args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
    # 领域检索
    else:
        result = search(args.query, args.domain, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
