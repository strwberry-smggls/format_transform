import pandas as pd
import sys
import pickle
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("data_path", type=str)
parser.add_argument("hierarchy_path", type=str)
parser.add_argument("--do_hierarchy", type=bool, default=True)
parser.add_argument("--outname", type=str, default="XMTC")
args = parser.parse_args()
files = ["train.csv", "val.csv", "test.csv"]
hierarchy_path = args.hierarchy_path

train = pd.read_csv(f"{args.data_path}/train.csv")
dev = pd.read_csv(f"{args.data_path}/val.csv")
test = pd.read_csv(f"{args.data_path}/test.csv")

all_df = [train, dev, test]

if args.do_hierarchy == "1":
    hierarchy = pd.read_csv(f"{args.hierarchy_path}")

    #collect all leafs from hierarchy
    parents = hierarchy["parent_id"].to_list()
    children = []
    for c in hierarchy["child_id"]:

        if c not in parents:
            children.append(c) 

    for df in all_df:
        labels = df["labels"]
        new_labels = []
        for l in labels:
            l = l.split("|")
            l_new = [x for x in l if x in children]
            if l_new == []:
                l_new = l
            new_labels.append(l_new)

        df["labels"] = new_labels

all_labels = []
for df in all_df:
    for labels in df["labels"]:
        if type(labels) == str:
            labels = labels.split("|")
        all_labels.extend(labels)

all_labels = sorted(list(set(all_labels)))


label_index = {}
for l in all_labels:
    label_index[l] = len(label_index)

col = ["comment_text"]
col.extend(list(label_index.keys()))

col_str = ",".join(col)
di = 0
for df in all_df:
    outname = f"{args.outname}_{files[di]}"

    new_df = pd.DataFrame(columns=col)
    label_col = df["labels"]
    index = 0
    for labels in label_col:
        if type(labels) == str:
            labels = labels.split("|")
        l_row = ["0" for i in range(len(label_index))]
        l = labels
        for ls in l:
            l_row[label_index[ls]] = "1"
        try:
            row = [df["text"][index]]
        except:
            txt = df["title"][index]
            txt += " "
            txt += df["abstract"][index].strip("[").strip("]")
            row = [txt]

        row.extend(l_row)
        new_df.loc[index] = row
        index += 1
        print(f"{index/len(df)*100}%", end="\r")

    new_df.to_csv(outname, sep=",")
    di += 1