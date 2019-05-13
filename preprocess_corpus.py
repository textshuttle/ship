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
        pass # TODO Task 1

    def normalise_whitespace(self):
        """Replaces non-breaking whitespace (U+00A0) with regular whitespace
        (U+0020) in the source and target side of all translations.
        """
        pass # TODO Task 1


if __name__ == "__main__":
    pass # TODO Task 3
