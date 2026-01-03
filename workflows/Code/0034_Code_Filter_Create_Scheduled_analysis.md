# 0034_Code_Filter_Create_Scheduled 工作流分析

## 工作流概述

该工作流是一个自动化的Spotify月度播放列表生成器，主要功能是将用户最近喜欢的歌曲自动添加到当月的Spotify播放列表中。工作流采用模块化设计，包含30个节点，集成了Spotify和NocoDB服务。

## 工作流逻辑描述

该工作流被划分为四个独立的玻璃平台，节点通过发光管道相互连接：

### 阶段1：触发与初始化（黄色平台）

- **Schedule Trigger**（节点712）：作为工作流的起点，定时触发整个工作流执行。
- **Get current date**（节点18）：执行JavaScript代码获取当前日期，并格式化输出为播放列表名称（如"January '26"）。

### 阶段2：歌曲管理（橙色平台）

- **Get last 10 liked tracks**（节点48）：从Spotify获取用户最近喜欢的10首歌曲。
- **For each tracks in liked song**（节点561）：将歌曲列表拆分为单个歌曲进行处理。
- **Check if track is saved**（节点68）：在NocoDB数据库中检查当前歌曲是否已存在。
- **Is not saved**（节点99）：条件判断，确定歌曲是否需要添加到数据库。
- **Create song entry**（节点133）：如果歌曲不存在，则将其添加到NocoDB数据库中，记录歌曲URI、添加时间和播放列表名称。

### 阶段3：播放列表管理（蓝色平台）

- **Get all user playlist**（节点172）：获取用户所有的Spotify播放列表。
- **Get monthly playlist**（节点210）：筛选出与当前月份匹配的播放列表。
- **Monthly playlist exist in Spotify?**（节点273）：条件判断播放列表是否存在。
- **Get playlist in DB**（节点245）：在NocoDB数据库中检查播放列表是否已记录。
- **Playlist exist in DB?**（节点307）：条件判断数据库中是否已有播放列表记录。
- **Create playlist in Spotify**（节点341）：如果播放列表不存在，则在Spotify中创建新的月度播放列表。
- **Create playlist in DB1**（节点366）：将新创建的Spotify播放列表信息添加到数据库。
- **Create playlist in DB**（节点405）：如果播放列表已存在于Spotify但不存在于数据库，则将其添加到数据库。

### 阶段4：数据同步（绿色平台）

- **Merge**（节点444）：合并来自不同分支的执行结果。
- **Get this month playlist in DB**（节点483）：从数据库获取当月的播放列表信息。
- **Get this month tracks in DB**（节点510）：从数据库获取当月添加的所有歌曲。
- **For each monthly tracks in DB**（节点576）：将当月歌曲列表拆分为单个歌曲进行处理。
- **Get this month tracks in Spotify**（节点590）：获取Spotify当月播放列表中的所有歌曲。
- **Filter1**（节点614）：检查当前歌曲是否已存在于Spotify播放列表中。
- **Song is not present in the playlist?**（节点650）：条件判断歌曲是否需要添加到播放列表。
- **Add song to the playlist**（节点537）：如果歌曲不存在于播放列表，则将其添加到Spotify当月播放列表中。
- **End**（节点732）：工作流结束节点。

## 关键技术特点

1. **条件判断与分支处理**：工作流包含多个条件判断节点，用于处理各种场景（播放列表存在/不存在、歌曲存在/不存在等）

2. **分批处理**：使用SplitInBatches节点对歌曲列表进行分批处理，确保API调用的稳定性

3. **错误处理机制**：包含专门的Error Handler节点，用于捕获和处理工作流执行过程中的错误

4. **模块化设计**：将功能划分为清晰的阶段，便于维护和扩展

5. **数据持久化**：使用NocoDB数据库记录播放列表和歌曲信息，确保数据一致性

6. **定时执行**：通过Schedule Trigger节点实现工作流的自动定时执行

## 工作流执行流程

1. 定时触发工作流
2. 获取当前日期，生成播放列表名称
3. 获取用户最近喜欢的10首歌曲
4. 遍历歌曲，检查并添加到数据库
5. 检查并管理月度播放列表
6. 获取数据库中当月的所有歌曲
7. 遍历歌曲，检查并添加到Spotify播放列表
8. 工作流执行完成

## 输入输出示例

### 输入
- 无直接输入，工作流通过API自动获取数据

### 输出
- 在Spotify中创建或更新月度播放列表
- 在NocoDB中记录播放列表和歌曲信息

## 注意事项

1. 工作流需要有效的Spotify OAuth2凭证
2. 需要配置NocoDB API令牌
3. 工作流默认使用UTC时区
4. 包含错误重试机制（最多重试3次，每次间隔1秒）
5. 最大执行时间为3600秒（1小时）

## 总结

该工作流是一个功能完整的自动化音乐管理工具，通过集成Spotify和NocoDB服务，实现了用户喜欢歌曲到月度播放列表的自动同步。工作流采用模块化设计，包含完善的错误处理机制，适合在生产环境中使用。