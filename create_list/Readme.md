# 1. build_corpus_lexicon.py

Builds a list of all the words found in CORPUS_TEXT_UTF8SIG.

Filters all non-Tibetan characters that it finds in the corpus files and strips the tseks(initial and final) before adding it to the list.

Output (build_corpus_lexicon_output):
- xxx_freq_order.txt : the lexicon ordered by frequency in the raw corpus
- xxx_tib_order.txt : the lexicon ordered alphabetically.
- non_tib_characters.txt : all the non-Tibetan characters found in the corpus + their respective frequency.

# 2. Filter.py

## compare_lists()

- Input: compare_lists([<list of files from which to compare\>], [<list of files to compare\>]) 
- Output: two lists: words only in [<list of files to compare\>], words found in both lists of files.