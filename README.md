# collect_genbank
For beginners, you can download genbank files from NCBI using this programm.  

# Requirement
* Biopython

# Installation
Down load **collect_genbank.py** locally 

# Preparation
For performing this programm, prepare a csv file or text file (csv file is recommended).   
The file contains list of accession number.  
You can obtain the list of accession number to be downloaded from NCBI or the result of Blast.  
  
Format of content is as below and example of the file is available in this repository (example.csv, example.txt).  

```
AA000001.1
AB000001.1
AC000001.1
```

# Usage
When downloading genbank files, ***you must write your email address collectly***. Otherwise, this programm does not work.

* at directory collect_genbank.py is downloaded
```bash
python collect_genbank.py -e < your email address > -f < list of accession numbers > -o < location of directory to store if necessary >
```

* example
```bash
python collect_genbank.py -e thisisnotcollectemail001(at)aaa.com -f list.csv
```
```bash
python collect_genbank.py -e thisisnotcollectemail001(at)aaa.com -f list2.csv -o result
```

# Options
```
-e, --email      write your email address (required)
-f, --infile     a csv or text file containing list of accession numbers to be downloaded
-o, --outdir     location for directory to store downloaded genbank files if necessary
```
# License
MIT License

# Reference


# Author
* Yusuke Tsuda
* Bacteriology, Nagoya University Graduated School of Medicine
* tsuda.yusuke@med.nagoya-u.ac.jp
