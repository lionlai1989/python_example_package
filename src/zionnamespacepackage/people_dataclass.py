import pandas as pd
from typing import List
from dataclasses import dataclass, fields


@dataclass
class People:
    Name: str
    Age: int
    Score: List[int]
    Location: List[str]
    Skills: List[str]


def write_people_df_to_csv(df, path):
    people_df["Score"] = df["Score"].apply(lambda x: " ".join([str(i) for i in x]))
    df["Location"] = df["Location"].apply(lambda x: " ".join(x))
    df["Skills"] = df["Skills"].apply(lambda x: " ".join(x))
    df.to_csv(
        path,
        index=False,
        sep=",",
        lineterminator="\n",
        header=True,
        columns=[f.name for f in fields(People)],
    )


def read_people_df_from_csv(path):
    df = pd.read_csv(path, sep=",", header=0, index_col=False)
    df["Score"] = df["Score"].apply(lambda x: [int(i) for i in str(x).split(" ")])
    df["Location"] = df["Location"].apply(lambda x: x.split(" "))
    df["Skills"] = df["Skills"].apply(lambda x: x.split(" "))
    return df


data_list = []
data_dict = {
    "Name": "John",
    "Age": 25,
    "Score": [100, 200],
    "Location": ["New", "York"],
    "Skills": ["Python", "SQL"],
}
data_list.append(data_dict)
data_dict = {
    "Name": "Jane",
    "Age": 30,
    "Score": [150],
    "Location": ["London"],
    "Skills": ["Java", "C++"],
}
data_list.append(data_dict)
data_dict = {
    "Name": "Bob",
    "Age": 35,
    "Score": [120, 200],
    "Location": ["Paris"],
    "Skills": ["R", "MATLAB"],
}
data_list.append(data_dict)
people_list = [People(**d) for d in data_list]
print(people_list)
people_df = pd.DataFrame([p.__dict__ for p in people_list])
print(people_df)

write_people_df_to_csv(people_df, "./people.csv")
read_df = read_people_df_from_csv("./people.csv")
print(read_df)


for _, row in read_df.iterrows():
    data_dict = {key: row[key] for key in row.keys()}
    # run_batch(imagery_table, StereoScene(**data_dict), tmp_stereo_dir)
    print(data_dict)
    print(People(**data_dict))
