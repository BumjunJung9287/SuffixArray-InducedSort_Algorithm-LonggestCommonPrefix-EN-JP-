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
it will be provided with space or enter between every 10 alphabets. but ignore it when processing

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

$ python sa-is_lcp.py < X10M.txt

time 70.56135487556458

3543341 3581770 9435

## 目的
東京大学の相田仁先生のアルゴリズム授業でのレポート問題のためsa-is法を使いました。
この問題は長い文字列が与えられその中から、先頭からi文字目からi + k文字目までの文字
列と先頭からj文字目からj + k文字目までの文字列が完全に一致するような組
み合わせ(ただしi < jとする)のうち、kが最大となるようなi, j, kの値をなるべく小さいオーダーで導出する問題でした。
そこで、sa-is法を使い、LCPを求め普通に解くにはO(n^2logn)のかかる問題をなるべくO(n)のオーダーで収まるようにすることが目的です。

## データ
課題で使用されたデータはdataディレクトリに入っています。
これらのデータには文字数がわかりやすいように 10 文字ご
とに空白文字または改行文字が挿入されていますが、処理を行う際には無
視します。

ライセンス :米国NIHのNCBIで公開されているヒトゲノムデータの一部を本課題向けに改良したものです。

## 実行方法/結果
1. 例えば先頭から５０文字だけをinputにしたいのなら

$ python sa-is_lcp.py 50

time 0.0002448558807373047

4 10 32

のようにする。１行目は実行時間を表し、２行目にi,j,kの値が出力される。

具体的に説明すると、先頭から５０文字は次のようになるが、

ZZZCTAACCC TAACCCTAAC CCTAACCCTA ACCCTAACCC TCTGAAAGTG

4 10 32 とは４番目、１０番目から始まる文字列の相田に共通する３２文字の部分列があって(CTAACCCTAACCCTAACCCTAACCCTAACCCT)その長さが最大であることを意味する。

2. 与えられたデータをinputにするには次のようにする。

$ python sa-is_lcp.py < X1M.txt

time 6.033958196640015

47941 48002 7051



$ python sa-is_lcp.py < X10M.txt

time 70.56135487556458

3543341 3581770 9435



