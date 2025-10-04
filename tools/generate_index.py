#!/usr/bin/env python3
"""
Sora2 提示词索引生成工具
自动生成项目的索引文件和统计信息
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

class IndexGenerator:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.categories = {}
        self.prompts = []
    
    def scan_categories(self):
        """扫描所有分类目录"""
        categories_dir = self.project_root / 'categories'
        if not categories_dir.exists():
            return
        
        for category_dir in categories_dir.iterdir():
            if category_dir.is_dir():
                category_name = category_dir.name
                self.categories[category_name] = {
                    'path': str(category_dir),
                    'prompts': [],
                    'count': 0
                }
                
                # 扫描该分类下的提示词文件
                for prompt_file in category_dir.glob('*.md'):
                    if prompt_file.name != 'README.md':
                        prompt_info = self.extract_prompt_info(prompt_file)
                        if prompt_info:
                            self.categories[category_name]['prompts'].append(prompt_info)
                            self.categories[category_name]['count'] += 1
                            self.prompts.append(prompt_info)
    
    def extract_prompt_info(self, file_path: Path) -> Dict[str, Any]:
        """从文件中提取提示词信息"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            info = {
                'file': str(file_path.relative_to(self.project_root)),
                'title': '未命名',
                'category': '未知',
                'difficulty': '未知',
                'duration': '未知',
                'tags': [],
                'created_date': '未知',
                'last_updated': '未知'
            }
            
            # 提取标题
            title_match = re.search(r'\*\*标题\*\*:\s*\[([^\]]+)\]', content)
            if title_match:
                info['title'] = title_match.group(1)
            
            # 提取分类
            category_match = re.search(r'\*\*分类\*\*:\s*\[([^\]]+)\]', content)
            if category_match:
                info['category'] = category_match.group(1)
            
            # 提取难度
            difficulty_match = re.search(r'\*\*难度\*\*:\s*\[([^\]]+)\]', content)
            if difficulty_match:
                info['difficulty'] = difficulty_match.group(1)
            
            # 提取时长
            duration_match = re.search(r'\*\*时长\*\*:\s*\[([^\]]+)\]', content)
            if duration_match:
                info['duration'] = duration_match.group(1)
            
            # 提取标签
            tags_match = re.search(r'\*\*标签\*\*:\s*\[([^\]]+)\]', content)
            if tags_match:
                tags_str = tags_match.group(1)
                info['tags'] = [tag.strip() for tag in tags_str.split(',')]
            
            # 提取创建日期
            created_match = re.search(r'## 创建日期\s*\n\[([^\]]+)\]', content)
            if created_match:
                info['created_date'] = created_match.group(1)
            
            # 提取最后更新日期
            updated_match = re.search(r'## 最后更新\s*\n\[([^\]]+)\]', content)
            if updated_match:
                info['last_updated'] = updated_match.group(1)
            
            return info
            
        except Exception as e:
            print(f"读取文件 {file_path} 时出错: {e}")
            return None
    
    def generate_main_index(self) -> str:
        """生成主索引文件"""
        index_content = f"""# Sora2 提示词项目索引

> 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 项目统计
- 总分类数: {len(self.categories)}
- 总提示词数: {len(self.prompts)}

## 分类概览

"""
        
        for category_name, category_info in self.categories.items():
            index_content += f"### {category_name.title()}\n"
            index_content += f"- 提示词数量: {category_info['count']}\n"
            index_content += f"- 目录: [{category_name}/](categories/{category_name}/)\n\n"
        
        index_content += """## 快速导航

### 按难度分类
- [初级提示词](#初级)
- [中级提示词](#中级)  
- [高级提示词](#高级)

### 按类型分类
"""
        
        for category_name in self.categories.keys():
            index_content += f"- [{category_name.title()}](categories/{category_name}/)\n"
        
        index_content += """
## 最新提示词
"""
        
        # 按创建日期排序，显示最新的5个
        sorted_prompts = sorted(self.prompts, 
                               key=lambda x: x.get('created_date', ''), 
                               reverse=True)
        
        for prompt in sorted_prompts[:5]:
            index_content += f"- [{prompt['title']}]({prompt['file']}) - {prompt['category']}\n"
        
        return index_content
    
    def generate_category_index(self, category_name: str) -> str:
        """生成分类索引文件"""
        if category_name not in self.categories:
            return ""
        
        category_info = self.categories[category_name]
        prompts = category_info['prompts']
        
        index_content = f"""# {category_name.title()} 提示词集合

> 提示词数量: {len(prompts)}

## 提示词列表

"""
        
        # 按难度分组
        difficulty_groups = {'初级': [], '中级': [], '高级': []}
        
        for prompt in prompts:
            difficulty = prompt.get('difficulty', '未知')
            if difficulty in difficulty_groups:
                difficulty_groups[difficulty].append(prompt)
            else:
                difficulty_groups['中级'].append(prompt)
        
        for difficulty, prompt_list in difficulty_groups.items():
            if prompt_list:
                index_content += f"### {difficulty}\n\n"
                for prompt in prompt_list:
                    index_content += f"- [{prompt['title']}]({Path(prompt['file']).name}) - {prompt.get('duration', '未知时长')}\n"
                index_content += "\n"
        
        return index_content
    
    def generate_all_indices(self):
        """生成所有索引文件"""
        # 生成主索引
        main_index = self.generate_main_index()
        with open('INDEX.md', 'w', encoding='utf-8') as f:
            f.write(main_index)
        
        # 为每个分类生成索引
        for category_name in self.categories.keys():
            category_index = self.generate_category_index(category_name)
            category_path = self.project_root / 'categories' / category_name / 'README.md'
            with open(category_path, 'w', encoding='utf-8') as f:
                f.write(category_index)
        
        print("索引文件生成完成!")
        print(f"- 主索引: INDEX.md")
        print(f"- 分类索引: categories/*/README.md")

def main():
    """主函数"""
    generator = IndexGenerator('.')
    generator.scan_categories()
    generator.generate_all_indices()

if __name__ == '__main__':
    main()
