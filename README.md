# SA-IS_LCP_Suffix_Array-Induced_Sort-Longgest_Common_Prefix-EN-JP-

Japanese follows after English. 日本語の説明は英語の説明のあとに続く。


## Environment
Ubuntu18.04


## Purpose
This sa-is algorithm is used for assignment in the class of algorithms in University of Tokyo by Professor Aida Hitoshi. 
The assignment was about finding the Longest Common Prefix(LCP) in the long data of string(reformed genom data).
Moreover, do it in small order as possible. 
The SA-IS algorithm is used to find the LCP in O(n), Linear order.

The content of the assignment was like following

Find the answer of longest common prefix. if the i th and j th prefix had k alphbets in common and that k was the maximum value of all. print the i j k in the result

## Data
The data used in this assignment will be provided in the data directory.
it will be provided with space between every 10 alphabets.

License : This data is a reformed version of human genom data which is open to the public in NCBI(National Center for Biotechnology Information) at NIH(National Institutes of Health) in United State of America.

## execution method/result
1. For example if you want to only compare 50 alphabets from the start, you would enter

$ python sa-is_lcp.py 50

time 0.0002448558807373047

4 10 32

First line shows the time of execution and the second line means that starting from 4th alphabet and 10th alphabet, there is a Longest common prefix and its lenth is 32.

To be specific, 50 words from start will be like following

ZZZCTAACCC TAACCCTAAC CCTAACCCTA ACCCTAACCC TCTGAAAGTG

4 10 32 means 32 alphabets from 4th and 10th alphabet is the same (CTAACCCTAACCCTAACCCTAACCCTAACCCT) and it is the longest of all prefix

2. To use the Text data as standart input, enter

$ python sa-is_lcp.py < X1M.txt

time 6.033958196640015

47941 48002 7051


米国NIHのNCBIで公開されているヒトゲノムデータの一部を本課題向けに改良したものです。
