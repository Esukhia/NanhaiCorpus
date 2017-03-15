import os


def open_file(file_path):
    try:
        with open(file_path, 'r', -1, 'utf-8-sig') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', -1, 'utf-16-le') as f:
            return f.read()

path = '../../CORPUS_TEXT_UTF8SIG'
corpus_files = [a for a in os.listdir(path)]
for f in corpus_files:
    content = open_file('{}/{}'.format(path, f))
    if 'པར་སྐྲུན་རྐྱང་ཕྱག' in content:
        print(f)