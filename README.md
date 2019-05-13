# Coding Assessment
## TextShuttle Summer Internship 2019

### Getting started

You have 60 minutes to work on this assignment. Don't worry should you not
manage to complete all tasks.

Clone this repository and edit any code on your own machine. After 60 minutes,
compress your local repository (with your modified code) into a zip or .tar.gz
archive and send it to laeubli@textshuttle.ai.

Please complete the tasks in order, i.e., do not work on task 3 before having completed task 2, etc.

### Task 1: Corpus Preprocessing

A parallel corpus is a collection of translations. Each translation consists of two strings: the original sentence in the source language, and its translation in the target language. They are referred to as source side and target side, respectively.

On disk, parallel corpora are often stored in line-delimited plain text files: one for the source side, and another for the target side. Each file contains one sentence per line, and sentences on the same line are translations. For example, line 31 in `data/corpus.en` is a translation of line 31 in `data/corpus.de`, etc.

Before training machine translation models, parallel corpora – often crawled from the web and thus containing noise – must be preprocessed. Your task is to implement two preprocessing methods: ratio cleaning and whitespace normalisation. Implement the `clean` and `normalise_whitespace` methods in `preprocess_corpus.py` according to their docstring specifications. You may use the files stored in `data/` folder for testing.

### Task 2: Use of REST API

`translate.py` is a script meant to translate sentences using an online machine translation service. Implement the `translate` function such that the following API is used for translation:

* Endpoint: https://mintzberg.textshuttle.ai/api/v1
* Specification: https://mintzberg.textshuttle.ai/docs/

We recommend using the [`requests` module](https://pypi.org/project/requests/) to retrieve translations from the online service. This module is not part of Python's standard library; you may need to install it.

### Task 3: Command Line Interface

Implement a command line interface (CLI) in `preprocess_corpus.py` to conveniently apply the preprocessing functionality implemented in task 1 to a parallel corpus stored on disk. The CLI should load a parallel corpus from two files, apply ratio cleaning and whitespace normalisation (as implemented in task 1), and write the filtered corpus to disk.

Example:

```bash
python3 preprocess_corpus.py -source data/corpus.en -target data/corpus.de
```

You may either add CLI arguments for target file locations, or derive them by adding a suffix to the original file names, such as `data/corpus.en.filtered` and `data/corpus.de.filtered`.
