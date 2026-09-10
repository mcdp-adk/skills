# 语法中的中文排版

嵌入内容里的中文可能是显示文字，也可能是标识符或数据。只在能够确定用途的文字区域应用正文约定；遇到不熟悉的扩展，保留原文，修改前查目标格式的文档。

## Markdown

空格应加在显示文字的边界，保持语法定界符完整。例如：

```markdown
请从 [SDK 下载页](https://example.org/sdk)获取文件。
执行 `tool --check` 后查看结果。
```

链接的显示文字可以整理，地址保持原样。引用式链接的文字有时兼作引用标识符；标题也可能决定自动生成的锚点。修改这两类内容时检查引用关系，必要时同步引用处。

缩进、空行和行末空格可能决定列表、代码块或硬换行。保留它们的结构作用，不把清除全部行末空格当作中文排版步骤。强调标记内侧也不能随意加空格，否则可能显示为普通星号。

GFM 表格中的 `|` 即使放在行内代码中，也需要按表格规则转义。整理单元格文字时保留分隔行、列结构和已有转义。

依据：[CommonMark 的强调规则](https://spec.commonmark.org/0.31.2/#emphasis-and-strong-emphasis)、[链接](https://spec.commonmark.org/0.31.2/#links)、[硬换行](https://spec.commonmark.org/0.31.2/#hard-line-breaks)、[GFM 表格](https://github.github.com/gfm/#tables-extension-)。

## Mermaid

Flowchart 的节点 ID 与显示标签分开处理。新建节点时可使用简短的 ASCII ID，将中文放入带 ASCII 双引号的标签：

```mermaid
flowchart LR
    source["读取 CSV 文件"] --> preview["预览前 5 行"]
```

标签中的空格是正常文字。整理已有图时保留 ID、连线和语法引号，只修改任务涉及的显示文字。标签需要包含引号等特殊字符时，按该图类型的规则转义；其他 Mermaid 图类型使用各自的标签语法。

依据：[Mermaid Flowchart 的 Unicode 文本与特殊字符](https://mermaid.js.org/syntax/flowchart.html)。

## 公式、HTML 和 front matter

| 内容 | 可以整理的位置 | 需要保持的部分 |
| --- | --- | --- |
| 数学公式 | 任务要求修改、且已确认语法的说明文字 | 公式分隔符、命令、运算符和转义；源代码空格不等于显示间距。 |
| HTML | 任务涉及的文本节点或明确用于显示的属性值 | 标签、属性名、外层 ASCII 引号、实体和脚本。 |
| YAML front matter | 任务涉及的标题、摘要等文字字段 | 键名、值的类型、缩进、引号及块标量规则。 |

这些区域默认原样保留。显示文字也受所在格式约束，例如给 YAML 值加入冒号或换行，可能需要调整其引号或写法。修改时同时满足正文排版和目标语法。

依据：[GitHub 数学表达式](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)、[HTML 语法](https://html.spec.whatwg.org/multipage/syntax.html)、[YAML 规范](https://yaml.org/spec/1.2.2/)。
