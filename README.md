## Dictionary scripts
This repository contains sources for dictionaries and scripts that converts them to plain .csv files with 2 values: word and translation. These converted files can be imported into LinguaCafe and used with its built-in dictionary search function. Please make sure you use the dictionaries according to their Terms of Use, some only allow personal use.

I will add direct support for importing some of these dictionaries, and this process won't be necessary in the future.

## Prerequisites
Make sure you have these python libraries installed before running the script:

> pip install pandas

## <span>Dict.</span>cc  

Tested for Norwegian, German and Spanish dictionaries. The German dictionary has over a million entries, and it may take a few minutes to convert and import.  

Step 1: Download <span>dict.</span>cc dictionaries from [here](https://www1.dict.cc/translation_file_request.php?l=e).  

Step 2: Unzip the file and copy it next to the script.  

Step 3: Use the <span>convert.</span>py script to convert the dictionary. It needs 2 arguments, the input file and the output.  

> python3 ./convert.py ./abcabcabcd-124154256-2aoaib.txt ./output.csv

Step 4: Now you can import the output.csv file into LinguaCafe on the Admin->Dictionaries page. Make sure you use "," character as a delimiter.