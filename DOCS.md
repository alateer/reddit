## reddit

一个类reddit的咨询讨论社区

### 相关链接

> reddit：https://www.reddit.com/
> reddit github：https://github.com/reddit-archive/reddit
> Fastapi：https://fastapi.org.cn/
> Reddit Api Document: https://www.reddit.com/dev/api

### 项目背景

名称由来与英文过去式 "Read It" 发音相同
是一个娱乐、社交及资讯网站，属于一个电子布告栏系统
国内相对做的比较好的咨询社区模式都过度臃肿，且Reddit的帖子模式以及投票方式都相对非常完善高效。
很多的模块都非常的互联网风格，且应用场景多
作为自己练手的项目在难度上有挑战，并且上限很高

### 核心模块

> Post (帖子)

包括标题和内容，可选tag，可选community。

> Community (社区)

一类Post的集合。
包含成员，名称，描述，规则等。
可被用户自行创建
用户可加入或退出社区

> Common (评论)

用户可在Post下进行内容评论。
用户可回复评论内容。
Common可以被投票。

> Vote (投票)

用户可对帖子或评论进行正投票或反投票。
投票无法成为负数。
当存在正投票时，负投票会使总票数-1。
投票决定默认排序。

> User (用户)

用户个人页面及相关信息

### 其他模块

> 私信和频道（Chat & Channel）

和其他用户单独聊天
在一个群聊中聊天

### 技术方案

架构：前后端分离
前端：React
后端语言：Python
后端Web框架：Fastapi
关系数据库：Mysql
非关系数据库：Redis
MQ：待定
定时任务：待定或自己实现
容器化部署（Docker）

### 开发流程

> 服务端开发

1. 服务及功能划分
2. 数据库、API设计
3. 开发

> 前端开发

1. 页面设计
2. 开发

### 服务端服务及功能划分

> 用户服务

- 用户信息
- 设置
- 安全
- 通知

> 投票服务

- 查询
- 更新

> 帖子服务（包含Community）

- 创建
- 查询
- 组合

> 评论服务

- 创建
- 查询

> 分布式ID服务

- 查询

### 数据模型设计

> 分布式ID服务


