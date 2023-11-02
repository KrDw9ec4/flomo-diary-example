## Flomo-Diary

首先使用 [Flomo](https://flomoapp.com/) 导出**当天**记录的 memos，然后使用 [Flomo-Importer](https://github.com/jia6y/flomo-to-obsidian) 将导出的 `.zip` 文件导入到 Obsidian 中，运行 **Flomo-Diary.py** 输入要汇总的日期 `YYYYMMDD`，最后会生成一个 `YYYY-MM-DD.md` 的日记在指定文件夹中。

即：

```
Flomo --- Flomo-Importer & Flomo-Diary.py ---> Obsidian
```

### 日期输入：支持多种格式的识别

```regex
(\d{4})[-|.|/]?(\d{2})[-|.|/]?(\d{2})
```

目前支持 `YYYY-MM-DD` `YYYY.MM.DD` `YYYY/MM/DD` `YYYYMMDD` 四种格式的日期输入。

### 文件合理归档：将导入后生成的文件按照相同规则存放

将导入后生成的 memos, canvas, diary 按照相同规则存放。

- **memos**: `Z20-Flomo/Memos/YYYYMM/YYYY-MM-DD/`
- **canvas**: `Z20-Flomo/Canvas/YYYYMM/YYYY-MM-DD.canvas`
- **diary**: `Z10-Diary/YYYY/YYYYMM/YYYY-MM-DD.md`

### 日记 YAML 区：创建日期、前后日期、往年今日

保存创建日期，匹配生成前后日期，往年今日。

```yaml
---
created: 2023-09-17T22:24:43
Recently:
  - "[[2023-09-16]]"
  - "[[2023-09-18]]"
Today:
  - "[[2021-09-17]]"
---
```

// *以 `2023-09-17.md` 作为示例*

### 日记形成：嵌入生成当天日记

通过嵌入来汇总当天的 memo。

```markdown
## 今日日志

###### 00:39:24

![[memo@2023_09_17_00_39_24_1.md]]

###### 00:39:25

![[memo@2023_09_17_00_39_25_2.md]]
```

### 生成“夜间日志”：个人需求

```markdown
## 夜间日志

早起:: 
早睡:: 
学习时间:: 
阅读时间:: 
今日总评:: 
```

### 版本备份：提交到 GitHub

建立 Python 的 git 指令模块，汇总结束后提交修改到 GitHub。

## Process-Memo

对导入后的 memo 文件进行处理，优化在 Obsidian 中的体验。

定义一些识别语法，实现在 Flomo 快捷输入，在 Obsidian 中生成特定的格式。

### memos 创建日期进 YAML 区

```yaml
---
Flomo: 2023-09-17T00:39:24
---
```

将 Flomo-Importer 导入后生成的创建日期时间放入 YAML 区。

### `Key:: Value` 识别：生成 Properties

在 flomo 记录时使用 `Key:: Value` 的形式，等汇总时将其更改格式放入 YAML 区。

也支持将标签放入 YAML 区。

**Flomo**：

```text
FRM:: 张三，李四，王五
tags:: #Copy #Resourse #Technology
```

**Obsidian**：

```yaml
---
FRM: 
  - 张三
  - 李四
  - 王五
tags: 
  - Copy
  - Resourse
  - Technology
---
```

// *FRM:: Friend Relationship Management*

### 回应样式：回应已有的 memo

在 Flomo 中输入 `Reply to > YYYY-MM-DD HH:mm:ss`，在汇总时会在该 memo 用 CallOut + 嵌入内容作为回应样式。

**Flomo**：

```text
Reply to > YYYY-MM-DD HH:mm:ss
```

**Process-Memo**：

1. 识别回应格式；
2. 捕获到日期和时间；
3. 到相应的 memos 文件夹中搜索匹配**已存在**的笔记（末尾有序号）；
4. 转换为以下的格式保存（**嵌入 + CallOut**）；
5. 在被回应的笔记末尾追加跳转当前回应的链接，而不是通过双链关系来找（**多重嵌套 CallOut + 嵌入**）。

**Obsidian**：

当前笔记：

```markdown
> [!quote]- Reply to
> ![[memo@YYYY_MM_DD_HH_mm_ss_N]]
```

被回应笔记：

```markdown
> [!abstract]- Refer to
> 
> > [!quote]- YYYY-MM-DD HH:mm:ss
> > ![[memo@YYYY_MM_DD_HH_mm_ss_N]]
> 
> > [!quote]- YYYY-MM-DD HH:mm:ss
> > ![[memo@YYYY_MM_DD_HH_mm_ss_N]]
```

### 修改导入后语法错误

- 删除 Flomo 中的列表导入后的额外空行：`^ +$\n`
- 删除多余的转义字符：`\`

## Append-Memo

有时候汇总当天的 memos 之后，会有一些想要补充的内容，比如一些想要记录的想法，或者是一些想要回应的内容，这时候就可以使用 **Append-Memo.py** 来追加 memo。

- 发送到 Flomo：通过 api 发送到 Flomo。 // *需要在**用户环境变量**创建一个键为 "FLOMO_API_URL"，值为 api 链接的变量*
- 保存到 Obsidian：按照正常流程生成的 memo 文件一样生成追加的 memo 文件。