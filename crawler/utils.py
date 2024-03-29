import os
import json
import re


def ensure_file_directory(file):
    inception(os.path.dirname(os.path.realpath(file)))


def inception(directory):
    parent_directory = os.path.dirname(directory)
    if not os.path.exists(parent_directory):
        inception(parent_directory)
    if not os.path.exists(directory):
        os.makedirs(directory)


def dump_json(json_object,output_file):
    ensure_file_directory(output_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_object, ensure_ascii=False))


def extract_domain(url):
    result = re.sub(r'(.*://)?([^/?]+).*', '\g<2>', url)
    return result
