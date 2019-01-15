##Code to triage email

import sys

#make each paper an object
class paper(object):
    def __init__(self,text):
        self.text = text

    def score(self,keywords):
        self.val = 0
        for word in keywords:
            self.val += self.text.count(word)
        return self.val

def get_arxiv_num(line):
    ## Extract arXiv number
    parts = line.partition(':')
    part = parts[2].split()
    
    if type(part) == str:
        arxiv_num = part
    else:
        arxiv_num = part[0]
    
#need a list of keywords
keywords = []
with open('/Users/brendanretter/Documents/Triage_ArXiv/keywords.txt','r') as file:
    for word in file:
        keywords.append(word[:-1])

#intiate object list
papers = []

#initiate variables
fields = ['arXiv:','Date:','Title:','Authors:','Categories:','Comments:']
start_line = 'arXiv:'
end_line = '\\\\ ('
end_email = '%%%---%%%---%%%---%%%---%%%---%%%---%%%---%%%---%%%---%%%---%%%---%%%---%%%---'
sep = '------------------------------------------------------------------------------\n'
paper_count = 0

with open(sys.argv[1]) as file:
    #Extract papers.
    #Step 1. Extract preamble
    preamble = ''
    while True:
        line = file.readline()
        if '\\\\' in line:
            break
        else:
            preamble += line

    #Step 2. Extract all papers
    while end_email not in line:
        line = file.readline()
        if start_line in line:
            p_text = ''
            while end_line not in line:
                p_text += line
                line = file.readline()

            papers.append(paper(p_text))

papers.sort(reverse=True,key= lambda x: x.score(keywords))
full_email = ''
for p in papers:
    full_email+='SCORE {:d}\n'.format(p.val)
    full_email+=p.text
    full_email+=sep

file = open('sorted_email.txt','w+')
file.write(full_email)
file.close()

exit()
