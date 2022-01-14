# Guide to creating the NYT, RCV1 and Yelp corpora in: Investigating Active Learning Sampling Strategies for Extreme Multi Label Text Classification (Fromme et. al. 2022).

# Build NYT, RCV1 and Yelp datasets from source

We use train/test/val splits as given by the source dataset.

The required target data format is .csv with the following columns:
text,label_1,label_2,...,label_n

"text" contains the input text, "label_i" is either 0 or 1.

In order to create the label columns, we first crawl all labels from the dataset
and organize them in a hierarchy. Hierarchies are stored in a .csv with the following columns:
parent_class,child_class

Please check
https://drive.google.com/file/d/11ikCpcdnvGuZsnigTZkT3BC8Ab4Z7cYk/view?usp=sharing (arXiv dataset)
or
https://drive.google.com/file/d/1CM6ybPQk2ZKZWAiHen2gogoO3wDeUzjf/view?usp=sharing (EurLex dataset)
for examples of file format.

We use only leaf classes - that means we omit all labels that occur on the left side as parents 
and remove them from the dataset. If a sentence will have 0 labels as a result of this process
we remove it from the dataset entirely.


# Build NYT, RCV1 and Yelp datasets from available splits

If you have the following file structures available or are willing to create them, you can also use the script
format_transform_from_hierarchical.py to create the datasets. In any case, the script is included for your
reference on how to build the datasets.

Required are the following:

1)
train.csv test.csv and val.csv files in a folder, seperate for each dataset. Example file structure:
NYT
--train.csv
--test.csv
--val.csv

Files need to be in .csv format with the following fields:
labels,text
OR
labels,title,abstract

labels in the "labels" field need to be separated by the "|" character:
label1|label2|label3....

Splits are used as given in the datasets. 

2)
The Label hierarchy in a .csv file. This file is created by the corresponding script in https://github.com/morningmoni/HiLAP.

3)
run the python script:
python format_transform_from_hierarchical.py path/to/data-folder path/to/hierarchy-file --outname desired-output-name
