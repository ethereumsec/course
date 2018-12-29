"""
compile.py

Run this to 'compile' Ethereum Security course from Markdown to HTML
"""

import markdown2
import os

PATH_TO_CURRICULUM = '.' + os.sep + 'curriculum'

curriculum_part_directories = [x[0] for x in os.walk(PATH_TO_CURRICULUM)][1:]
for i, curriculum_part_directory in enumerate(curriculum_part_directories):
    markdown_files_here = [x for x in os.listdir(curriculum_part_directory) if x.endswith('.md')]
    curriculum_part_name = curriculum_part_directory.split(os.sep)[-1][3:]
    this_directory = '..' + os.sep + curriculum_part_name
    os.mkdir(this_directory)
    for this_markdown_file in markdown_files_here:
        this_file_path = curriculum_part_directory + os.sep + this_markdown_file
        this_html = '<p>Something went wrong generating HTML - this is placeholder text!</p>'
        with open(this_file_path, 'r') as this_file:
            this_files_contents = this_file.read()
            this_html = markdown2.markdown(this_files_contents)
        target_output_html_file = this_directory + os.sep + this_markdown_file[:-3] + '.html'
        with open(target_output_html_file, 'w') as this_output_file:
            this_output_file.write(this_html)
            this_output_file.close()
        
