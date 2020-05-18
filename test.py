import re

def process():
    text = []
    new_text = []
    with open("data/new_data_test.txt", "r", encoding="latin-1") as f:
        text = f.readlines()

    new_text = []
    for i in text:
        new_text.append(i.split("\t"))
    print(text[0])


def compile_pmid(string):
    pattern = re.compile(r'rs[0-9]+[a-zA-Z-_]*')
    result = pattern.findall(string)
    return  result

def compile_p_value(string):
    s = "30102696	A genome-wide association study identifies a susceptibility locus for biliary atresia on 2p16.1 within the gene EFEMP1.	Biliary atresia (BA) is a rare pediatric cholangiopathy characterized by fibrosclerosing obliteration of the extrahepatic bile ducts, leading to cholestasis, fibrosis, cirrhosis, and eventual liver failure. The etiology of BA remains unknown, although environmental, inflammatory, infectious, and genetic risk factors have been proposed. We performed a genome-wide association study (GWAS) in a European-American cohort of 343 isolated BA patients and 1716 controls to identify genetic loci associated with BA. A second GWAS was performed in an independent European-American cohort of 156 patients with BA and other extrahepatic anomalies and 212 controls to confirm the identified candidate BA-associated SNPs. Meta-analysis revealed three genome-wide significant BA-associated SNPs on 2p16.1 (rs10865291, rs6761893, and rs727878; P < 5 ×10-8), located within the fifth intron of the EFEMP1 gene, which encodes a secreted extracellular protein implicated in extracellular matrix remodeling, cell proliferation, and organogenesis. RNA expression analysis showed an increase in EFEMP1 transcripts from human liver specimens isolated from patients with either BA or other cholestatic diseases when compared to normal control liver samples. Immunohistochemistry demonstrated that EFEMP1 is expressed in cholangiocytes and vascular smooth muscle cells in liver specimens from patients with BA and other cholestatic diseases, but it is absent from cholangiocytes in normal control liver samples. Efemp1 transcripts had higher expression in cholangiocytes and portal fibroblasts as compared with other cell types in normal rat liver. The identification of a novel BA-associated locus, and implication of EFEMP1 as a new BA candidate susceptibility gene, could provide new insights to understanding the mechanisms underlying this severe pediatric disorder."

    #pattern = re.compile(r'[0-9]+[.][0-9]+\s*[x|×|*]\s*[0-9]+[\(]{0,1}[0-9-]+[\)]{0,1}')
    pattern = re.compile(r'[0-9]+[.]?[0-9]*\s*[x|×]\s*[0-9]+[\(]{0,1}-[0-9\s]+[\)]{0,1}')
    #pattern = re.compile(r'[0-9]+[.][0-9]+\s*[x|×|*]\s*[0-9]+\(*[0-9-]+\)*')
    #pattern = re.compile(r'\u202f')
    pattern2 = re.compile(r'[0-9.]+[e|E][\(]{0,1}[0-9-]+[\)]{0,1}')
    # result = pattern.findall(s)
    # result2 = pattern2.findall(s)
    result = pattern.findall(string)
    result2 = pattern2.findall(string)
    for i in result+result2:
        tempStr = str(i).replace("(", "").replace(")", "")
        b = tempStr.split()
        print("".join(b), end="      ")
    print()
    return result+result2

def count_pmid():
    text_url = "clean_data/test_data.txt"
    text = []
    with open(text_url, "r", encoding="utf-8") as f:
        text = f.readlines()
    s=""
    count = 0
    for i in text:
        result = compile_p_value(i.strip().split("\t")[2])
        if(len(result)==0):
            count+=1
    print(count)
    #with open("clean_data/train_data.txt", "w", encoding="utf-8") as f:
        #f.write(s)

def find_err():
    texts = list()
    with open("train_data.txt", "r", encoding="utf-8") as f:
        texts = f.readlines()
    new_text = list()
    for i in texts:
        new_text.append(i.strip().split("\t"))
    count = 0
    s = ""
    for i in new_text:
        print("line: "+str(new_text.index(i)+1), end="   ")
        result = compile_p_value(i[2])
        if(len(result)==0):
            count+=1
    print(count)

if __name__ == '__main__':
    #process()
    #count_pmid()
    #compile_p_value("")
    find_err()
