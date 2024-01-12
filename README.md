# DocVQA

This repository contains the dataset and code for reproducing results of the DocVQA paper, an exploration into Document Visual Question Answering using advanced models like BERT and M4C.

For an in-depth understanding of the original methodologies and findings, please refer to the paper, [DocVQA: A Dataset for VQA on Document Images,](https://arxiv.org/abs/2007.00398).

Furthermore, you can access a detailed Technical Report, which provides more insight into the specifics of this project - [Technical Report](https://www.overleaf.com/project/6523e0bb952b3bf78d627861).

## Dataset

The DocVQA dataset includes over 12,000 document images with more than 50,000 questions designed for Visual Question Answering tasks.

## Code

The codebase includes scripts for training and evaluating BERT and M4C models on the DocVQA dataset.

### Installation

Instructions for setting up the environment and installing dependencies.

```bash
pip install -r requirements.txt

## Citation

If you find this work useful, please consider citing the following:

```bibtex
@InProceedings{docvqa_wacv,
    author    = {Mathew, Minesh and Karatzas, Dimosthenis and Jawahar, C.V.},
    title     = {DocVQA: A Dataset for VQA on Document Images},
    booktitle = {WACV},
    year      = {2021},
    pages     = {2200-2209}
}
