# Build from existing train/test/dev splits given in required format
Guide to creating the NYT, RCV1 and Yelp corpora in: Investigating Active Learning Sampling Strategies for Extreme Multi Label Text Classification (Fromme et. al. 2022).
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
