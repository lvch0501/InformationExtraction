import os
import xml.dom.minidom as xmldom
import io
import requests
import tempfile

count = 0
num = 0

def extract_xml(file_dir, save_dir):
    global count
    global num
    try:
        domobj = xmldom.parseString(file_dir)
    except:
        print("file")
        return
    elementobj = domobj.documentElement
    PMID_elementobj = elementobj.getElementsByTagName("PMID")
    try:
        final_sentence = PMID_elementobj[0].firstChild.data + '\t'
    except:
        print("PMID")
        count+=1
        return

    # date_elemntobj = elementobj.getElementsByTagName("PubMedPubDate")
    # for i in range(len(date_elemntobj)):
    #     if date_elemntobj[i].getAttribute("PubStatus") == "pubmed":
    #         date = date_elemntobj[i].childNodes[1].firstChild.nodeValue
    #         if int(date_elemntobj[i].childNodes[3].firstChild.nodeValue) < 10:
    #             date = date + "0" + date_elemntobj[i].childNodes[3].firstChild.nodeValue
    #         else:
    #             date = date + date_elemntobj[i].childNodes[3].firstChild.nodeValue
    #         if int(date_elemntobj[i].childNodes[5].firstChild.nodeValue) < 10:
    #             date = date + "0" +date_elemntobj[i].childNodes[5].firstChild.nodeValue
    #         else:
    #             date = date + date_elemntobj[i].childNodes[5].firstChild.nodeValue
    #         final_sentence = final_sentence + date + '\t'

    title_elmentobj = elementobj.getElementsByTagName("ArticleTitle")
    try:
        title = title_elmentobj[0].firstChild.data
    except:
        print("title")
        count+=1
        return
    final_sentence = final_sentence+title + '\t'
    abstract_elementobj = elementobj.getElementsByTagName("AbstractText")
    abstract = ''
    for i in range(len(abstract_elementobj)):
        try:
            childNodes = abstract_elementobj[i].childNodes
            for j in range(len(childNodes)):
                if childNodes[j].nodeType==1:
                    abstract=abstract.rstrip(' ')+'('+childNodes[j].firstChild.data+')'
                elif childNodes[j].nodeType==3:
                    abstract+=childNodes[j].data +' ' # 标点符号后面加空格
        except:
            print("abstract")
            count+=1
            continue
    abstract=abstract.rstrip(' ')# 去除最后一次加的无用的空格
    final_sentence = final_sentence + abstract + '\t'
    # IOS_elementobj = elementobj.getElementsByTagName("ISOAbbreviation")
    # try:
    #     IOS = IOS_elementobj[0].firstChild.data
    # except:
    #     count+=1
    #     return
    # final_sentence = final_sentence + IOS + '\t'
    # publication_element = elementobj.getElementsByTagName("PublicationType")
    # for i in range(len(publication_element)):
    #     final_sentence = final_sentence + " " +publication_element[i].getAttribute("UI") + '\t'
    #reference_element = elementobj.getElementsByTagName("Reference")
    #for i in range(len(reference_element)):
        #final_sentence = final_sentence + " " +reference_element[i].childNodes[3].childNodes[1].firstChild.data
    print(final_sentence)
    with open(save_dir, 'a', encoding="utf-8") as f:
        f.writelines(final_sentence+'\n')
        num+=1


def get_neg_list(file):
    data = list(io.open(file, "r", encoding='latin-1').readlines())
    data = [s.strip() for s in data]
    data = [x for x in data if x is not '']
    return data

def main():
    global count
    global num
    dirname = 'new_data/train_pmid.txt'
    save_dir = 'new_data/test_data.txt'
    # dirname = 'data/GWAS/2018_divided_unprocess/2018_2019_test_neg_GWAS.txt'
    # save_dir = './new_dataset/GWAS/gwas_test_neg.txt'
    #for maindir, subdir, file_name_list in os.walk(dirname):
    #    for i in file_name_list:
    #        print(i)
    #        extract_xml(os.path.join(dirname,i), save_dir)
    PMID_list = get_neg_list(dirname)
    for i in PMID_list:
        if num>5000:
            break
        print(i)
        url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?' \
              'db=pubmed&id=' + i + '&retmode=xml&key=c885ac65aae4e2ee21685f672e41be296308 '
        try:
            f = requests.get(url)
        except:
            count += 1
            print("can not get the xml file")
            continue
        extract_xml(f.text, save_dir)
    print(count)


if __name__ == '__main__':
    main()