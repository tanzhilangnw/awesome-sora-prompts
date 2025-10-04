#!/usr/bin/env python3
"""
Sora2 视频统计工具
用于统计和管理生成的视频文件
"""

import os
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class VideoStats:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.videos_dir = self.project_root / 'generated_videos'
        self.stats = {
            'total_videos': 0,
            'categories': {},
            'total_size': 0,
            'quality_ratings': [],
            'date_range': {'earliest': None, 'latest': None}
        }
    
    def scan_videos(self):
        """扫描所有视频文件"""
        if not self.videos_dir.exists():
            print("视频目录不存在")
            return
        
        # 扫描各分类目录
        for category_dir in self.videos_dir.iterdir():
            if category_dir.is_dir() and category_dir.name not in ['raw', 'processed', 'thumbnails', 'metadata']:
                category_name = category_dir.name
                self.stats['categories'][category_name] = {
                    'count': 0,
                    'size': 0,
                    'videos': []
                }
                
                # 扫描该分类下的视频文件
                for video_file in category_dir.glob('*.mp4'):
                    video_info = self.get_video_info(video_file, category_name)
                    if video_info:
                        self.stats['categories'][category_name]['videos'].append(video_info)
                        self.stats['categories'][category_name]['count'] += 1
                        self.stats['categories'][category_name]['size'] += video_info['size']
                        self.stats['total_videos'] += 1
                        self.stats['total_size'] += video_info['size']
                        
                        # 更新日期范围
                        if video_info['date']:
                            if not self.stats['date_range']['earliest'] or video_info['date'] < self.stats['date_range']['earliest']:
                                self.stats['date_range']['earliest'] = video_info['date']
                            if not self.stats['date_range']['latest'] or video_info['date'] > self.stats['date_range']['latest']:
                                self.stats['date_range']['latest'] = video_info['date']
                        
                        # 收集质量评分
                        if video_info['quality_rating']:
                            self.stats['quality_ratings'].append(video_info['quality_rating'])
    
    def get_video_info(self, video_file: Path, category: str) -> Dict[str, Any]:
        """获取视频文件信息"""
        try:
            stat = video_file.stat()
            size_mb = stat.st_size / (1024 * 1024)  # 转换为MB
            
            # 尝试读取元数据文件
            metadata_file = self.videos_dir / 'metadata' / f"{video_file.stem}.json"
            metadata = {}
            if metadata_file.exists():
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
            
            return {
                'filename': video_file.name,
                'path': str(video_file.relative_to(self.project_root)),
                'size': size_mb,
                'date': metadata.get('generation_date'),
                'duration': metadata.get('duration'),
                'resolution': metadata.get('resolution'),
                'quality_rating': metadata.get('quality_rating'),
                'category': category
            }
        except Exception as e:
            print(f"读取视频文件 {video_file} 时出错: {e}")
            return None
    
    def generate_report(self) -> str:
        """生成统计报告"""
        report = f"""
# Sora2 视频统计报告

> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 总体统计
- **总视频数量**: {self.stats['total_videos']}
- **总存储大小**: {self.stats['total_size']:.2f} MB
- **平均质量评分**: {sum(self.stats['quality_ratings'])/len(self.stats['quality_ratings']):.1f} (共{len(self.stats['quality_ratings'])}个评分)

## 📅 时间范围
- **最早生成**: {self.stats['date_range']['earliest'] or '无数据'}
- **最新生成**: {self.stats['date_range']['latest'] or '无数据'}

## 📁 分类统计

"""
        
        # 按视频数量排序
        sorted_categories = sorted(
            self.stats['categories'].items(),
            key=lambda x: x[1]['count'],
            reverse=True
        )
        
        for category_name, category_info in sorted_categories:
            report += f"### {category_name.title()}\n"
            report += f"- 视频数量: {category_info['count']}\n"
            report += f"- 存储大小: {category_info['size']:.2f} MB\n"
            if category_info['count'] > 0:
                avg_size = category_info['size'] / category_info['count']
                report += f"- 平均大小: {avg_size:.2f} MB\n"
            report += "\n"
        
        # 质量评分分布
        if self.stats['quality_ratings']:
            report += "## 📈 质量评分分布\n\n"
            quality_ranges = {
                '优秀 (9-10)': len([r for r in self.stats['quality_ratings'] if 9 <= r <= 10]),
                '良好 (7-8)': len([r for r in self.stats['quality_ratings'] if 7 <= r < 9]),
                '一般 (5-6)': len([r for r in self.stats['quality_ratings'] if 5 <= r < 7]),
                '较差 (1-4)': len([r for r in self.stats['quality_ratings'] if 1 <= r < 5])
            }
            
            for range_name, count in quality_ranges.items():
                percentage = (count / len(self.stats['quality_ratings'])) * 100
                report += f"- {range_name}: {count} 个 ({percentage:.1f}%)\n"
        
        return report
    
    def save_report(self, report: str):
        """保存报告到文件"""
        report_file = self.project_root / 'video_stats_report.md'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"统计报告已保存到: {report_file}")

def main():
    """主函数"""
    stats = VideoStats('.')
    stats.scan_videos()
    report = stats.generate_report()
    print(report)
    stats.save_report(report)

if __name__ == '__main__':
    main()
