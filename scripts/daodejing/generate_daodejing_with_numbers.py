#!/usr/bin/env python3
import os
import re

from fonts import ArticleProducer


def read_daodejing_chapters():
    """读取道德经各章节内容"""
    with open('daodejing.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    # 按章节分割
    chapters = []
    lines = content.strip().split('\n\n')

    for line in lines:
        if line.strip():
            parts = line.strip().split('\n')
            if len(parts) >= 2:
                chapter_num = parts[0].strip()
                chapter_text = ''.join(parts[1:]).strip()
                chapters.append((chapter_num, chapter_text))

    return chapters


def generate_chapter_pdf(chapter_num, chapter_text):
    """生成单个章节的字帖，在内容前添加章节序号"""
    print(f"正在生成 {chapter_num}...")

    # 在内容前添加章节序号
    numbered_text = f"{chapter_num}{chapter_text}"

    # 创建ArticleProducer实例
    producer = ArticleProducer(article=chapter_num, text=numbered_text)

    # 生成字帖
    producer.paint()

    # 合并PDF
    producer.merge_pdf()

    print(f"{chapter_num} 生成完成")


def main():
    """主函数"""
    print("开始生成带序号的道德经字帖...")

    # 读取章节
    chapters = read_daodejing_chapters()
    print(f"共找到 {len(chapters)} 个章节")

    # 重新生成所有章节（带序号）
    for chapter_num, chapter_text in chapters:
        try:
            generate_chapter_pdf(chapter_num, chapter_text)
        except Exception as e:
            print(f"生成 {chapter_num} 时出错: {e}")

    print("带序号的道德经字帖生成完成！")


if __name__ == "__main__":
    main()