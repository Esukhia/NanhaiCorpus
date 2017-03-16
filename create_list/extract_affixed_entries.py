import PyTib
from PyTib.common import open_file, write_file


parts = PyTib.getSylComponents()


def split_word(word):
    parts = word.split('་')
    start = '་'.join(parts[:-1])+'་'
    end = parts[-1]
    return start, end

lexicon = open_file('build_corpus_lexicon_output/corpus_vocab_tib_order.txt').strip().split('\n')

# initialize full lexicon
s = PyTib.Segment()
s.include_user_vocab(local_vocab=lexicon)

affixed = []
non_affixed = []
for word in lexicon:
    print(word, end=' : ')
    if word != '':
        start, last_syl = split_word(word)
        print(start, last_syl, end = ' , ')
        syl_parts = parts.get_parts(last_syl)
        if syl_parts and len(syl_parts) == 2:
            root, suffix = syl_parts
            print(root, suffix)
            if suffix == 'ར' or suffix == 'ས' or suffix == 'འི':
                if start+root in s.lexicon:
                    affixed.append(word+','+start+root)
                if start+root+'འ' in s.lexicon:
                    affixed.append(word+','+start+root+'འ')
        else:
            non_affixed.append(word)

write_file('extract_affixed_output/corpus_vocab_affixed.csv', '\n'.join(affixed))
write_file('extract_affixed_output/corpus_vocab_non_affixed.txt', '\n'.join(non_affixed))
