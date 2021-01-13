# arxiv_triage
Short and simple code to arrange papers in daily arXiv email by relevance.

Triage_ArXiv can called from command line with 
  > python triage_python.py [text file]
 
where [text file] is a .txt file containing the ArXiv email.
 The output is a text file sorted_email.txt which contains the papers from the arXiv email sorted in decending order of relevance.

Alternate use is the bash script 'triage'.
1. First, copy the arXiv email to your clipboard

2. Triage_ArXiv can called from command line with
  > triage

'triage' first pastes the contents of your clipboard to a text file 'arxiv.txt' which is then passed to 'triage_python.py', and finally opens the sorted email in your default text editor.  

notes:
'triage' will need to be edited to point to the directory containing 'triage_python.py'.
 
Files:
triage_python.py is a python script which sorts the papers in the email.
keywords.txt contains a list of keywords that the user is looking for.
triage is a bash script which automates some of the process. 
 
 
 
