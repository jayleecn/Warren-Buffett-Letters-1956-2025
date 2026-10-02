[English](README.md) | [中文](README.zh-CN.md)

# 沃伦·巴菲特致股东信（1956–2025）

由沃伦·E·巴菲特（Warren E. Buffett）撰写的 **91 份文档**精选合集，聚焦价值投资理念与方法论。

## 阅读入口

- [INDEX.md](INDEX.md)：可直接打开 Markdown/PDF 的信件索引，包含财年、签署日期和来源。
- [catalog.json](catalog.json)：机器可读的元数据与路径，覆盖 91 份巴菲特文档和单独分类的 6 份非巴菲特文档。
- [多语言知识库](https://github.com/jayleecn/Warren-Buffett-Letters-Vault)：译文与概念/公司/人物导航；本仓库保存原始来源资料。

## 收录范围

- **巴菲特合伙企业协议（1956）**：创始文件
- **巴菲特合伙企业致有限合伙人信（1957–1969）**：致 Buffett Partnership, Ltd. 有限合伙人的 32 封信
- **伯克希尔·哈撒韦致股东信（1970–2025）**：致 Berkshire Hathaway Inc. 股东的 58 封信

## 策展原则

本合集优先收录含有**实质性投资讨论**的信件——投资理念、估值方法、组合管理、企业分析与市场评论。纯行政类信件（例如报税说明）不予收录。

### 未收录信件

以下 2 封来自 [rbcpa.com](https://www.rbcpa.com/warren-e-buffett/buffett-letters-1959-present/) 的信件**未收录**，因其仅含报税说明、无投资内容：

- **1962-12-24** — 致有限合伙人的税务信息信
- **1963-12-26** — 致有限合伙人的税务信息信

有兴趣的读者可在此查阅：https://www.rbcpa.com/warren-e-buffett/buffett-letters-1959-present/

## 目录结构

```
Warren Buffett Letters(1956-2025)/
├── letters-en-source/   # 原始来源文件（HTML、PDF、EPUB 摘录）
├── letters-en-pdf/      # 全部信件的 PDF 版本（可全文检索）
├── letters-en-md/       # 全部信件的 Markdown 版本
├── referance/           # 参考资料与来源索引
├── INDEX.md             # 全部信件完整索引表
└── README.md
```

## 文件命名约定

```
{FiscalYear}_Letter({N})_{SigningDate}.{ext}
```

- **FiscalYear**：信件所覆盖的财年（例如 `1957`、`2024`）
- **Letter(N)**：同一财年有多封信时的序号（仅一封时可省略）
- **SigningDate**：信件签署日期，格式为 `YYYYMMDD`；若仅知月份则用 `YYYYMM`

示例：
- `1958_Letter_19590211.pdf` — 1958 财年年信，签署于 1959 年 2 月 11 日
- `1962_Letter(2)_19621101.pdf` — 1962 财年第二封信，签署于 1962 年 11 月 1 日
- `1957_Letter_195802.pdf` — 1957 财年年信，签署于 1958 年 2 月（具体日期不详）

> **关于签署日期的说明**：签署日期取自每封信中明确的日期行或签名栏。有两封信没有明确日期，仅记录到年月：
>
> - `1957_Letter_195802` — 信中完全没有日期；“1958 年 2 月”是根据相邻年份的模式推断的
> - `1975_Letter_197604` — 信末仅有 “Warren E. Buffett, Chairman”，无日期；信中引用截至 1976 年 3 月 31 日的数据，因此写作时间不早于 1976 年 4 月
>
> 另有一封信 `2014_Letter(2)_20150227`（50 周年纪念文章 *"Berkshire – Past, Present and Future"*）本身没有日期；2015 年 2 月 27 日取自同一年报中一并发布的配套信件。

## 来源

| 来源 | 数量 | 时期 |
|--------|-------|--------|
| [gurufocus.com](https://www.gurufocus.com/news/126451/original-warren-buffett-partnership-agreement-found-here) | 1 | 1956 |
| [1957-1969 Complete Buffett Partnership Letters (PDF)](https://www.ivey.uwo.ca/media/2975913/buffett-partnership-letters.pdf) | 29 | 1957–1969 |
| [rbcpa.com](https://www.rbcpa.com/warren-e-buffett/buffett-letters-1959-present/) | 3 | 1966–1968 |
| [1965-2012 BH Letters to Shareholders (EPUB)](referance/1965-2012_Berkshire_Hathaway_Letters_to_Shareholders.epub) | 8 | 1970–1977 |
| [berkshirehathaway.com](https://www.berkshirehathaway.com/letters/letters.html) | 50 | 1978–2025 |

## 版权声明

本合集中的信件版权归沃伦·E·巴菲特和/或伯克希尔·哈撒韦公司所有。本合集仅基于合理使用原则，用于**教育与研究目的**。

原始信件可从上述来源公开获取。

## 策展人 / 联系方式

策展人：**@jayleecn**

如有版权问题或更正建议，请联系：

- X (Twitter)：[@jayleecn](https://x.com/jayleecn)
- 微信公众号：**太白钓雪**，主要记录些价值投资的笔记和思考

![微信公众号二维码|150](curator/qrcode.jpg)

## 非巴菲特信件

非巴菲特本人撰写的信件单独存放在 `letters-en-*/non-buffett/`：

- **Kenneth V. Chace**（伯克希尔·哈撒韦总裁）：5 封早期伯克希尔年信（1965–1969）
- **Charles T. Munger**（伯克希尔·哈撒韦副董事长）：1 封特别信函（2014）

## 维护与检索

先检索 `letters-en-md/`，需要核对排版或来源时再读 PDF/原始文件。这些目录保存同一文档的不同表示，同时搜索会产生重复结果。`referance/` 保存来源合集和原始索引，不是策展后的阅读集合。

`catalog.json` 是索引元数据的统一来源：`primary`/`author` 区分作者，`fiscal_year` 与 `signing_date` 区分财年和签署日期，`signing_date_precision` 保留只知月份的情况。每条记录包含 Markdown/PDF 路径、原始文件路径和已记录的来源。

修改目录数据或新增文档后，运行：

```bash
python3 scripts/catalog.py --write
python3 scripts/catalog.py --check
```

检查器核对全部 Markdown/PDF 配对、作者分类、财年、签署日期、来源路径、生成索引及两份 README 的来源统计；不校验外部来源是否在线或信件正文的学术准确性。

按一个财年或签署日期取元数据，避免读取整个目录：

```bash
python3 scripts/catalog.py --year 2024
python3 scripts/catalog.py --date 2025-02-22
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

查询输出 JSON，并保留作者/primary 分类；财年查询可能包含单独分类的非巴菲特文档。
