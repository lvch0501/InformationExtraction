import re


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()
def process_title():
    text_list = list
    with open("clean_data/train_data.txt", encoding="utf-8", mode="r") as f:
        text_list = f.readlines()
    title_text = [i.strip().split("\t")[1] for i in text_list]

    s = ""
    for i in title_text:
        s += i+"\n"

    with open("title_data/train_title.txt", mode="w", encoding="utf-8") as f:
        f.write(s)
    print()


if __name__ == '__main__':
    process_title()