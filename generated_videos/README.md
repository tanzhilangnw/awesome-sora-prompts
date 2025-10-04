# Sora2 生成视频存储

这个目录用于存储和管理通过Sora2生成的视频文件。

## 📁 目录结构

```
generated_videos/
├── cinematic/              # 电影风格视频
├── documentary/            # 纪录片风格视频
├── animation/              # 动画风格视频
├── experimental/           # 实验性视频
├── artistic/               # 艺术风格视频
├── commercial/             # 商业用途视频
├── educational/            # 教育内容视频
├── entertainment/          # 娱乐内容视频
├── sports/                 # 体育相关视频
├── nature/                 # 自然景观视频
├── urban/                  # 城市景观视频
├── historical/             # 历史题材视频
├── futuristic/             # 未来科幻视频
├── abstract/               # 抽象艺术视频
├── character_driven/       # 角色驱动视频
├── raw/                    # 原始生成视频
├── processed/              # 后期处理视频
├── thumbnails/             # 视频缩略图
└── metadata/               # 视频元数据
```

## 📝 文件命名规范

### 视频文件命名格式
```
[分类]_[提示词ID]_[日期]_[版本].mp4

示例:
- cinematic_epic_battle_20251004_v1.mp4
- documentary_nature_wildlife_20251004_v2.mp4
```

**注意**: 当前Sora2支持生成10秒视频，所有提示词都按10秒时长设计。

### 元数据文件命名格式
```
[视频文件名].json

示例:
- cinematic_epic_battle_20251004_v1.json
```

## 🗂️ 分类存储说明

### 按分类存储
- 每个分类目录存储对应类型的生成视频
- 便于按主题查找和管理
- 支持分类统计和分析

### 特殊目录
- **raw/**: 存储Sora2直接生成的原始视频
- **processed/**: 存储经过后期处理的视频
- **thumbnails/**: 存储视频缩略图（用于快速预览）
- **metadata/**: 存储视频的元数据信息

## 📊 元数据格式

每个视频应包含对应的JSON元数据文件：

```json
{
  "video_id": "cinematic_epic_battle_20251004_v1",
  "prompt_id": "epic_battle_scene",
  "category": "cinematic",
  "generation_date": "2025-10-04",
  "duration": 60,
  "resolution": "4K",
  "frame_rate": 24,
  "aspect_ratio": "16:9",
  "file_size": "125MB",
  "prompt_text": "An epic medieval battle unfolds...",
  "parameters": {
    "style": "realistic",
    "lighting": "dramatic",
    "camera_work": "cinematic"
  },
  "quality_rating": 8.5,
  "notes": "Good epic scale, lighting could be improved",
  "tags": ["war", "epic", "medieval", "action"]
}
```

## 🔧 管理工具

### 视频统计脚本
```bash
# 统计各分类视频数量
python tools/video_stats.py

# 生成视频索引
python tools/generate_video_index.py
```

### 批量处理脚本
```bash
# 批量生成缩略图
python tools/generate_thumbnails.py

# 批量提取元数据
python tools/extract_metadata.py
```

## 📋 使用建议

1. **及时分类**: 生成视频后立即放入对应分类目录
2. **规范命名**: 使用统一的命名格式便于管理
3. **保存元数据**: 记录生成参数和效果评价
4. **定期整理**: 定期清理低质量或重复的视频
5. **备份重要**: 对重要视频进行备份

## 🚀 快速开始

1. 生成视频后，根据提示词分类放入对应目录
2. 创建对应的元数据文件
3. 生成缩略图用于快速预览
4. 定期使用工具脚本进行统计和管理

## 📈 统计信息

- 总视频数量: [自动统计]
- 各分类分布: [自动统计]
- 存储空间使用: [自动统计]
- 质量评分分布: [自动统计]

---

**注意**: 请定期清理不需要的视频文件，避免占用过多存储空间。
