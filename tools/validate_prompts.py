#!/usr/bin/env python3
"""
Sora2 提示词验证工具
用于验证提示词文件的格式和内容完整性
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any

class PromptValidator:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.errors = []
        self.warnings = []
    
    def validate_prompt_file(self, file_path: Path) -> Dict[str, Any]:
        """验证单个提示词文件"""
        result = {
            'file': str(file_path),
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查必需的部分
            required_sections = [
                '## 基本信息',
                '## 提示词内容',
                '## 参数设置',
                '## 预期效果'
            ]
            
            for section in required_sections:
                if section not in content:
                    result['errors'].append(f"缺少必需部分: {section}")
                    result['valid'] = False
            
            # 检查提示词内容格式
            if '```' in content:
                code_blocks = re.findall(r'```[\s\S]*?```', content)
                if not code_blocks:
                    result['warnings'].append("未找到代码块格式的提示词内容")
            
            # 检查分类是否有效
            valid_categories = [
                'cinematic', 'documentary', 'animation', 'experimental',
                'artistic', 'commercial', 'educational', 'entertainment',
                'sports', 'nature', 'urban', 'historical', 'futuristic',
                'abstract', 'character_driven'
            ]
            
            category_match = re.search(r'\*\*分类\*\*:\s*\[([^\]]+)\]', content)
            if category_match:
                category = category_match.group(1)
                if category not in valid_categories:
                    result['warnings'].append(f"未知分类: {category}")
            
        except Exception as e:
            result['errors'].append(f"读取文件失败: {str(e)}")
            result['valid'] = False
        
        return result
    
    def validate_all_prompts(self) -> Dict[str, Any]:
        """验证所有提示词文件"""
        results = {
            'total_files': 0,
            'valid_files': 0,
            'invalid_files': 0,
            'files': []
        }
        
        # 遍历所有分类目录
        categories_dir = self.project_root / 'categories'
        if categories_dir.exists():
            for category_dir in categories_dir.iterdir():
                if category_dir.is_dir():
                    for prompt_file in category_dir.glob('*.md'):
                        if prompt_file.name != 'README.md':
                            results['total_files'] += 1
                            file_result = self.validate_prompt_file(prompt_file)
                            results['files'].append(file_result)
                            
                            if file_result['valid']:
                                results['valid_files'] += 1
                            else:
                                results['invalid_files'] += 1
        
        return results
    
    def generate_report(self, results: Dict[str, Any]) -> str:
        """生成验证报告"""
        report = f"""
# 提示词验证报告

## 总体统计
- 总文件数: {results['total_files']}
- 有效文件: {results['valid_files']}
- 无效文件: {results['invalid_files']}

## 详细结果
"""
        
        for file_result in results['files']:
            status = "✅ 有效" if file_result['valid'] else "❌ 无效"
            report += f"\n### {file_result['file']} {status}\n"
            
            if file_result['errors']:
                report += "**错误:**\n"
                for error in file_result['errors']:
                    report += f"- {error}\n"
            
            if file_result['warnings']:
                report += "**警告:**\n"
                for warning in file_result['warnings']:
                    report += f"- {warning}\n"
        
        return report

def main():
    """主函数"""
    validator = PromptValidator('.')
    results = validator.validate_all_prompts()
    report = validator.generate_report(results)
    
    print(report)
    
    # 保存报告到文件
    with open('validation_report.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n验证报告已保存到: validation_report.md")

if __name__ == '__main__':
    main()
