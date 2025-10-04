# Sora2 提示词项目

一个专门为Sora2视频生成模型收集、整理和优化提示词的开源项目。

## 📁 项目结构

```
sora2/
├── categories/                 # 提示词分类目录
│   ├── cinematic/             # 电影风格提示词
│   ├── documentary/           # 纪录片风格提示词
│   ├── animation/             # 动画风格提示词
│   ├── experimental/          # 实验性提示词
│   ├── artistic/              # 艺术风格提示词
│   ├── commercial/            # 商业用途提示词
│   ├── educational/           # 教育内容提示词
│   ├── entertainment/         # 娱乐内容提示词
│   ├── sports/                # 体育相关提示词
│   ├── nature/                # 自然景观提示词
│   ├── urban/                 # 城市景观提示词
│   ├── historical/            # 历史题材提示词
│   ├── futuristic/            # 未来科幻提示词
│   ├── abstract/              # 抽象艺术提示词
│   └── character_driven/      # 角色驱动提示词
├── templates/                 # 模板文件
│   ├── prompt_template.md     # 提示词模板
│   └── category_template.md   # 分类模板
├── examples/                  # 示例文件
│   └── README.md              # 示例说明
├── tools/                     # 工具脚本
│   ├── validate_prompts.py    # 提示词验证工具
│   └── generate_index.py     # 索引生成工具
├── docs/                      # 文档目录
│   └── README.md              # 项目文档
├── assets/                    # 资源文件
│   ├── images/                # 图片资源
│   ├── videos/                # 视频资源
│   └── audio/                 # 音频资源
└── README.md                  # 项目说明
```

## 🚀 快速开始

### 1. 添加新提示词
1. 选择合适的分类目录
2. 复制 `templates/prompt_template.md` 模板
3. 填写完整的提示词信息
4. 保存到对应的分类目录

### 2. 创建新分类
1. 在 `categories/` 目录下创建新文件夹
2. 复制 `templates/category_template.md` 模板
3. 填写分类信息
4. 更新主 README.md

### 3. 使用工具
```bash
# 验证所有提示词
python tools/validate_prompts.py

# 生成索引文件
python tools/generate_index.py
```

## 📝 提示词分类说明

### 🎬 电影风格 (Cinematic)
专业的电影级视频生成提示词，适用于剧情片、动作片等。

### 📺 纪录片 (Documentary)
纪实风格的视频提示词，适用于新闻、教育、历史等题材。

### 🎨 动画 (Animation)
各种动画风格的提示词，包括2D、3D、卡通等。

### 🧪 实验性 (Experimental)
前沿的实验性提示词，探索Sora2的新可能性。

### 🎭 艺术 (Artistic)
艺术创作相关的提示词，包括绘画、雕塑、装置艺术等。

### 💼 商业 (Commercial)
商业用途的提示词，适用于广告、宣传、产品展示等。

### 📚 教育 (Educational)
教育内容相关的提示词，适用于教学视频、科普内容等。

### 🎪 娱乐 (Entertainment)
娱乐内容提示词，包括综艺、游戏、音乐等。

### ⚽ 体育 (Sports)
体育相关的提示词，适用于运动赛事、健身、户外活动等。

### 🌿 自然 (Nature)
自然景观相关的提示词，包括风景、动植物、天气等。

### 🏙️ 城市 (Urban)
城市景观提示词，包括建筑、街道、人群、交通等。

### 🏛️ 历史 (Historical)
历史题材提示词，适用于历史重现、古装、文物等。

### 🚀 未来 (Futuristic)
科幻未来风格的提示词，包括太空、机器人、未来城市等。

### 🎨 抽象 (Abstract)
抽象艺术风格的提示词，包括几何、色彩、概念等。

### 👤 角色驱动 (Character Driven)
以角色为中心的提示词，包括人物、表情、动作等。

## 🛠️ 工具说明

### 提示词验证工具
- 检查提示词文件格式
- 验证必需字段
- 生成验证报告

### 索引生成工具
- 自动生成项目索引
- 统计提示词数量
- 按分类组织内容

## 🤝 贡献指南

1. Fork 本项目
2. 创建新的功能分支
3. 添加新的提示词或改进现有内容
4. 提交 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢所有为这个项目贡献提示词的社区成员！

---

**注意**: 这是一个开源项目，欢迎社区贡献和反馈。如果您有好的提示词或改进建议，请随时提交 Issue 或 Pull Request。
