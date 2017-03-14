import os
from collections import defaultdict


def is_tibetan_letter(char):
    """
    :param char: caracter to check
    :return: True or False
    """
    if (char >= 'ༀ' and char <= '༃') or (char >= 'ཀ' and char <= 'ྼ'):
        return True
    else:
        return False


def non_tib_chars(string):
    """
    :param string:
    :return: list of non-tibetan non-tibetan-pre_process characters found within a orig_list
    """
    punct = ['༄', '༅', '།', '་', '༌', '༑', '༎', '༏', '༐', '༔']
    chars = []
    for character in string:
        if not is_tibetan_letter(character) and character not in chars and character not in punct:
            chars.append(character)
    return chars


def tib_sort(l):
    """
    sorts a list according to the Tibetan order
    code from https://github.com/eroux/tibetan-collation/blob/master/implementations/Unicode/rules-icu52.txt
    :param l: list to sort
    :return: sorted list
    """
    from icu import RuleBasedCollator
    rules = '\n# Rules for Sanskrit ordering\n# From Bod rgya tshig mdzod chen mo pages 9 - 11, 347, 1153, 1615, 1619, 1711, 1827, 2055, 2061, 2840, 2920, 3136 and 3137\n# Example: ཀར་ལུགས།  < ཀརྐ་ཊ།\n&ཀར=ཀར\n&ཀལ=ཀལ\n&ཀས=ཀས\n&གཉྫ=གཉྫ\n&ཐར=ཐར\n&པུས=པུས\n&ཕལ=ཕལ\n&བིལ=བིལ\n&མཉྫ=མཉྫ\n&མར=མར\n&ཤས=ཤས\n&སར=སར\n&ཨར=ཨར\n&ཨས=ཨས\n# Marks (seconadry different, with low equal primary weight after Lao)\n&[before 1]ཀ<།<<༎<<༏<<༐<<༑<<༔<<༴<་=༌\n&ཀ<<ྈྐ<ཫ<དཀ<བཀ<རྐ<ལྐ<སྐ<བརྐ<བསྐ\n&ཁ<<ྈྑ<མཁ<འཁ\n&ག<དགག<དགང<དགད<དགན<དགབ<དགཝ<དགའ<དགར<དགལ<དགས<དགི<དགུ<དགེ<དགོ<དགྭ<དགྱ<དགྲ<བགག<བགང<བགད<བགབ<བགམ<<<བགཾ<བགཝ<བགའ\n		<བགར<བགལ<བགི<བགུ<བགེ<བགོ<བགྭ<བགྱ<བགྲ<བགླ<མགག<མགང<མགད<མགབ<མགའ<མགར<མགལ<མགི<མགུ<མགེ<མགོ<མགྭ<མགྱ<མགྲ<འགག<འགང<འགད<འགན<འགབ<འགམ<<<འགཾ\n		<འགའ<འགར<འགལ<འགས<འགི<འགུ<འགེ<འགོ<འགྭ<འགྱ<འགྲ<རྒ<ལྒ<སྒ<བརྒ<བསྒ\n&ང<<<ྂ<<<ྃ<དངག<དངང<དངད<དངན<དངབ<དངའ<དངར<དངལ<དངི<དངུ<དངེ<དངོ<མངག<མངང<མངད<མངན<མངབ<མངའ<མངར<མངལ<མངི<མངུ<མངེ<མངོ<རྔ<ལྔ<སྔ<བརྔ<བསྔ\n&ཅ<གཅ<བཅ<ལྕ<བལྕ\n&ཆ<མཆ<འཆ\n&ཇ<མཇ<འཇ<རྗ<ལྗ<བརྗ\n&ཉ<<ྋྙ<གཉ<མཉ<རྙ=ཪྙ<སྙ<བརྙ=བཪྙ<བསྙ\n&ཏ<ཊ<ཏྭ<ཏྲ<གཏ<བཏ<རྟ<ལྟ<སྟ<བརྟ<བལྟ<བསྟ\n&ཐ<ཋ<མཐ<འཐ\n&ད<ཌ<གདག<གདང<གདད<གདན<གདབ<གདམ<<<གདཾ<གདའ<གདར<གདལ<གདས<གདི<གདུ<གདེ<གདོ<གདྭ<བདག<བདང<བདད<བདབ<བདམ<<<བདཾ<བདའ\n		<བདར<བདལ<བདས<བདི<བདུ<བདེ<བདོ<བདྭ<མདག<མདང<མདད<མདན<མདབ<མདའ<མདར<མདལ<མདས<མདི<མདུ<མདེ<མདོ<མདྭ<འདག<འདང<འདད<འདན<འདབ<འདམ<<<འདཾ\n		<འདཝ<འདའ<འདར<འདལ<འདས<འདི<འདུ<འདེ<འདོ<འདྭ<འདྲ<རྡ<ལྡ<སྡ<བརྡ<བལྡ<བསྡ\n&ན<ཎ<གནག<གནང<གནད<གནན<གནབ<གནམ<<<གནཾ<གནཝ<གནའ<གནར<གནལ<གནས<གནི<གནུ<གནེ<གནོ<གནྭ<མནག<མནང<མནད<མནན<མནབ<མནམ<<<མནཾ<མནའ\n		<མནར<མནལ<མནས<མནི<མནུ<མནེ<མནོ<མནྭ<རྣ<སྣ<བརྣ<བསྣ\n&པ<<ྉྤ<དཔག<དཔང<དཔད<དཔབ<དཔའ<དཔར<དཔལ<དཔས<དཔི<དཔུ<དཔེ<དཔོ<དཔྱ<དཔྲ<ལྤ<སྤ\n&ཕ<<ྉྥ<འཕ\n&བ<དབག<དབང<དབད<དབན<དབབ<དབའ<དབར<དབལ<དབས<དབི<དབུ<དབེ<དབོ<དབྱ<དབྲ<འབག<འབང<འབད<འབན<འབབ<འབམ\n	<<<འབཾ<འབའ<འབར<འབལ<འབས<འབི<འབུ<འབེ<འབོ<འབྱ<འབྲ<རྦ<ལྦ<སྦ\n&མ<<<ཾ<དམག<དམང<དམད<དམན<དམབ<དམཝ<དམའ<དམར<དམལ<དམས<དམི<དམུ<དམེ<དམོ<དམྭ<དམྱ<རྨ<སྨ\n&ཙ<གཙ<བཙ<རྩ<སྩ<བརྩ<བསྩ\n&ཚ<མཚ<འཚ\n&ཛ<མཛ<འཛ<རྫ<བརྫ\n# &ཝ\n&ཞ<གཞ<བཞ\n&ཟ<གཟ<བཟ\n# &འ\n&ཡ<གཡ\n&ར<<<ཪ<ཬ<བརླ=བཪླ\n# &ལ\n&ཤ<ཥ<གཤ<བཤ\n&ས<གསག<གསང<གསད<གསན<གསབ<གསའ<གསར<གསལ<གསས<གསི<གསུ<གསེ<གསོ<གསྭ<བསག<བསང<བསད<བསབ<བསམ<<<བསཾ<བསའ<བསར\n		<བསལ<བསས<བསི<བསུ<བསེ<བསོ<བསྭ<བསྲ<བསླ\n&ཧ<ལྷ\n&ཨ\n# Explicit vowels\n<ཱ<ི<ཱི<ྀ<ཱྀ<ུ<ཱུ<ེ<ཻ=ེེ<ོ<ཽ=ོོ\n# Post-radicals\n	<ྐ<ྑ<ྒ<ྔ<ྕ<ྖ<ྗ<ྙ<ྟ<ྚ<ྠ<ྛ<ྡ<ྜ<ྣ<ྞ<ྤ<ྥ<ྦ<ྨ<ྩ<ྪ<ྫ<ྭ<<<ྺ<ྮ<ྯ<ྰ<ྱ<<<ྻ<ྲ<<<ྼ<ླ<ྴ\n	<ྵ<ྶ<ྷ<ྸ\n# Combining marks and signs (secondary weight)\n&༹<<྄<<ཿ<<྅<<ྈ<<ྉ<<ྊ<<ྋ<<ྌ<<ྍ<<ྎ<<ྏ\n# Treatༀ,  ཷand ,ཹ as decomposed\n&ཨོཾ=ༀ\n&ྲཱྀ=ཷ\n&ླཱྀ=ཹ'
    collator = RuleBasedCollator('[normalization on]\n' + rules)
    return sorted(l, key=collator.getSortKey)


def write_file(file_path, content):
    with open(file_path, 'w', -1, 'utf-8-sig') as f:
        f.write(content)


def open_file(file_path):
    try:
        with open(file_path, 'r', -1, 'utf-8-sig') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', -1, 'utf-16-le') as f:
            return f.read()


def find_corpus_non_tib(file_list):
    all_non_tib = defaultdict(int)
    for f in file_list:
        content = open_file(f).strip().split()
        for c in content:
            non_tib = non_tib_chars(c)
            for n in non_tib:
                all_non_tib[n] += 1
    write_file('non_tib_characters.txt', '\n'.join(['{}: {}'.format(k, v) for k, v in all_non_tib.items()]))
    return all_non_tib


def extract_vocab_with_freq(files_list):
    total = defaultdict(int)
    non_tib_total = find_corpus_non_tib(files_list)
    for f in files_list:
        content = open_file(f).strip().split()
        for c in content:
            clean = c
            for a in non_tib_total:
                clean = clean.replace(a, '')
                clean = clean.strip('་')
            total[clean] += 1
    return total


def compare_lists(base_list, to_compare_list):
    base = extract_vocab_with_freq(base_list)
    to_compare = extract_vocab_with_freq(to_compare_list)

    only_in_to_compare = []
    shared_words = []
    for word in to_compare:
        if word not in base:
            only_in_to_compare.append(word)
        else:
            shared_words.append(word)
    return only_in_to_compare, shared_words


def main():
    raw_corpus_path = '../CORPUS_TEXT_UTF8SIG'
    raw_corpus_files = ['{}/{}'.format(raw_corpus_path, a) for a in os.listdir(raw_corpus_path)]
    corpus_vocab = extract_vocab_with_freq(raw_corpus_files)
    write_file('corpus_vocab_tib_order.txt', '\n'.join(tib_sort(corpus_vocab)))
    freq_sorted = sorted([(k, v) for k, v in corpus_vocab.items()], key=lambda x: x[1], reverse=True)
    write_file('corpus_vocab_freq_order.txt', '\n'.join(['{},{}'.format(a[0], a[1]) for a in freq_sorted]))

main()
