# Sora2 提示词项目文档

## 项目概述
这是一个专门为Sora2视频生成模型收集、整理和优化提示词的开源项目。

## 目录结构说明

### categories/ - 提示词分类目录
- **cinematic/**: 电影风格提示词
- **documentary/**: 纪录片风格提示词
- **animation/**: 动画风格提示词
- **experimental/**: 实验性提示词
- **artistic/**: 艺术风格提示词
- **commercial/**: 商业用途提示词
- **educational/**: 教育内容提示词
- **entertainment/**: 娱乐内容提示词
- **sports/**: 体育相关提示词
- **nature/**: 自然景观提示词
- **urban/**: 城市景观提示词
- **historical/**: 历史题材提示词
- **futuristic/**: 未来科幻提示词
- **abstract/**: 抽象艺术提示词
- **character_driven/**: 角色驱动提示词

### templates/ - 模板文件
- **prompt_template.md**: 单个提示词模板
- **category_template.md**: 分类目录模板

### examples/ - 示例文件
存放各种类型的示例提示词和生成结果

### tools/ - 工具脚本
用于提示词管理、验证和优化的工具

### assets/ - 资源文件
- **images/**: 相关图片资源
- **videos/**: 示例视频
- **audio/**: 音频资源

## 使用指南

### 如何添加新提示词
1. 选择合适的分类目录
2. 复制 `templates/prompt_template.md` 模板
3. 填写完整的提示词信息
4. 提交到对应的分类目录

### 如何创建新分类
1. 在 `categories/` 目录下创建新文件夹
2. 复制 `templates/category_template.md` 模板
3. 填写分类信息
4. 更新主 README.md

## 贡献指南
[详细的贡献指南和规范]

## 许可证
[项目许可证信息]
