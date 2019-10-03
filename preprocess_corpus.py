#!/usr/bin/env python3


class ParallelCorpus:
    """A sentence-level parallel corpus."""

    def __init__(self, source_file: str, target_file: str):
        """Loads translations (source and target side) from two files, each
        containing one sentence per line.
        """
        with open(source_file, encoding='utf-8') as src, \
             open(target_file, encoding='utf-8') as trg:
            self.translations = list(zip(src, trg))

    def clean(self):
        """Removes all translations where one side (source, target) is more
        than twice as long as the other side. Length is measured in number of
        characters.
        """
        self.translations[:] = [tup for tup in self.translations if not
                                (len(tup[0]) * 2 < len(tup[1]) or len(tup[1]) * 2 < len(tup[0]))]

    def normalise_whitespace(self):
        """Replaces non-breaking whitespace (U+00A0) with regular whitespace
        (U+0020) in the source and target side of all translations.
        """
        indices = set()
        for i, tup in enumerate(self.translations):
            for k, sentence in enumerate(tup):
                if u"\u00A0" in sentence:
                    indices.add((i, k))

        for index in indices:
            source, target = self.translations[index[0]]
            if index[1] == 0:
                self.translations[index[0]] = (source.replace(u"\u00A0", ' '), target)
            else:
                self.translations[index[0]] = (source, target.replace(u"\u00A0", ' '))


if __name__ == "__main__":
    new_corpus = ParallelCorpus('data/corpus.de', 'data/corpus.en')
    new_corpus.clean()
    new_corpus.normalise_whitespace()

    pass # TODO Task 3
