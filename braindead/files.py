import os
import shutil
from glob import iglob
from itertools import chain
from typing import Generator, Iterable, TextIO

from braindead.constants import DIST_DIR, TEMPLATE_DIR


def find_all_posts(directory: str = "posts") -> Iterable[str]:
    """ All the md posts - both extensions .markdown and .md"""
    return find_all_markdown_and_md_files(directory=directory)


def find_all_pages(directory: str = "pages") -> Iterable[str]:
    """ Similar to the one above, but searches for posts - another directory. Both .md and .markdown """
    return find_all_markdown_and_md_files(directory=directory)


def find_all_markdown_and_md_files(directory: str) -> Iterable[str]:
    """ Base method that finds both .md and .markdown recursively in a given directory and it's children. """
    md_files: Generator = iglob(os.path.join(directory, "**", "*.md"), recursive=True)
    markdown_files: Generator = iglob(os.path.join(directory, "**", "*.markdown"))
    return chain(md_files, markdown_files)


def save_output(original_file_name: str, output: str) -> str:
    """ Saves a given output based on the original filename in the dist folder"""
    new_location: str = os.path.splitext(os.path.join(DIST_DIR, original_file_name))[0] + ".html"
    new_directory, _ = os.path.split(new_location)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    output_file: TextIO = open(new_location, "w")
    output_file.write(output)
    return new_location


def gather_statics() -> None:
    template_statics = os.path.join(TEMPLATE_DIR, "static")
    if os.path.exists(template_statics):
        shutil.copytree(template_statics, os.path.join(DIST_DIR, "static"), dirs_exist_ok=True)
