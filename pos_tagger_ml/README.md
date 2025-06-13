# POS Tagging Project

## Overview

This project implements various Part-of-Speech (POS) tagging approaches using Python and NLTK. It explores multiple taggers including Unigram, Bigram, and Trigram taggers, as well as different modifications of the Viterbi algorithm to handle unknown words effectively.

The main goal is to analyze, compare, and improve the tagging accuracy on a given dataset, ultimately building a robust POS tagger combining statistical and rule-based techniques.

---

## Project Structure

pos_tagging_project/                                                                                                                                             
│                                                                                                                                                       
├── data/                                                                                                                      
│ ├── train.txt # Training dataset (tagged sentences)                                                                                                         
│ ├── test.txt # Test dataset (tagged sentences)                                                                                                                      
│                                                                                                                                                                   
├── notebooks/                                                                                                                                                            
│ ├── pos_tagging_exploration.ipynb # Main Jupyter Notebook containing experiments, implementations, and evaluations                                                      
│                                                                                                                                                                        
├── src/                                                                                                                                                                   
│ ├── taggers.py # Implementation of various taggers (Unigram, Bigram, Trigram)                                                                                          
│ ├── viterbi.py # Viterbi algorithm and its modified versions for unknown words handling                                                                                  
│ ├── utils.py # Utility functions such as dataset loading, preprocessing, and evaluation metrics                                                                           
│                                                                                                                                                                         
├── tests/                                                                                                                                                                                                                                                                                               
│ ├── test_taggers.py # Unit tests for tagger implementations                                                                                                      
│ ├── test_viterbi.py # Unit tests for Viterbi algorithm functions                                                                                                        
│                                                                                                                                                                      
├── README.md # This file, project overview and instructions                                                                                                                
├── requirements.txt # Python dependencies and versions                                                                                                                     
└── setup.py # Setup file if packaging the project                                                                                                                          

---

## Detailed Explanation of Components

### 1. Data

- `train.txt` and `test.txt` contain tagged sentences used to train and test the taggers.
- Each line usually contains word-tag pairs or sentences formatted for easy tokenization.

### 2. Notebooks

- `pos_tagging_exploration.ipynb`: The core file where all code experiments, model building, and evaluation are done.
- Contains implementations of:
  - Unigram, Bigram, Trigram taggers (with backoff strategies)
  - Vanilla Viterbi algorithm
  - Modified Viterbi approaches to handle unknown words (including weighted transition probabilities)
  - Combination of rule-based regex tagger and trigram tagger
- Step-by-step explanations and accuracy comparisons are presented here.

### 3. Source Code (`src/`)

- **taggers.py**  
  Houses implementations for different statistical taggers:
  - UnigramTagger
  - BigramTagger
  - TrigramTagger (with backoff to simpler taggers)
  - Regex-based tagger patterns

- **viterbi.py**  
  Contains implementations of:
  - Vanilla Viterbi algorithm for POS tagging
  - Modified Viterbi for unknown words using transition probabilities
  - Modified Viterbi adding tag occurrence probability weights
  - Viterbi integrated with Trigram and regex tagger for improved accuracy

- **utils.py**  
  Utility functions for:
  - Loading and preprocessing datasets
  - Calculating emission and transition probabilities
  - Tokenization helpers
  - Evaluation functions for tagging accuracy

### 4. Tests (`tests/`)

- Contains unit tests for the tagger and Viterbi implementations to ensure correctness and robustness.
- Use `pytest` or `unittest` framework to run tests:
  ```bash
  pytest tests/
  ```
## How to Run
## Setup environment
#### Install dependencies:
```bash
pip install -r requirements.txt
```
#### Run the notebook
- Open and run notebooks/pos_tagging_exploration.ipynb to see the implementations, experiment with code, and observe results interactively.

#### Run scripts
 - You can also import modules and run taggers from scripts in src/, for example:
```python
from src.taggers import TrigramTagger
from src.viterbi import VanillaViterbi
Run tests
```
 - To validate code correctness:
```bash
pytest tests/
```
### Key Learnings and Observations
 - Combining statistical taggers with rule-based taggers improves overall accuracy, especially on unknown or rare words.
 - Modified Viterbi algorithms that consider transition probabilities and tag occurrence frequencies handle unknown words better than vanilla Viterbi.
 - The trigram tagger backed by regex-based tagger achieves the highest accuracy (~97%) in the experiments.
 - Several real-world examples demonstrate how modified taggers correct errors made by simpler models.

#### Future Work
 - Extend to bigger datasets and more complex tagsets.
 - Explore deep learning approaches such as BiLSTM-CRF models.
 - Build an end-to-end pipeline for real-time POS tagging.
 - Create a web interface or API for interactive tagging.
#### Contact and Contributions
    Feel free to open issues or pull requests for improvements, bug fixes, or new features.


