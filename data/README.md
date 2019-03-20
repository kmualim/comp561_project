# Dataset 

Here lies the files for the data used for the final classification task - a simple clinical test 
The dataset comes from the european bioinformatics database: http://www.ebi.ac.uk 
and holds a comprehensive human expression map. 

## Requirements 

## Download dataset 
This repo contains a script - download.py that can be used to download the data using the following command: 
` python download.py `

## Structure of dataset 
E-MTAB-3732.sdrf.txt holds various characteristics for the derivation of a sample 
- labels were extracted from this text file
![](images/structure.png)
Figure 1: Structure of E-MTAB-3732.sdrf.txt 

processedMatrix.Aurora.july2015.txt holds 24 GB of expression values corresponding to these samples. 
- inputs were extracted from this text file

## Preprocessing Data
The preprocessing of this dataset involved extracting the a series of labels. 
Due to lack of computing power, I looked at ~9300 samples for both normal and other labels. 
These other labels constitute different forms of cancer: glioblastoma, carcinoma, myeloma, cancer, adenocarcinoma to make up ~9300 samples. <br>

normal labels can be found in <b> neg_labels.txt </b> which stores the sample numbers for normal samples <br>
cancer labels can be found in <b> cancer_labels.txt </b> which stores the sample numbers for cancerous samples <br>

Extracting the expression values for the individual samples was then performed using the following script and command: <br>
`bash reduce_labels.sh` <br>
- outputs a txt file for every sample <br>

Transposing and concatenating normal/cancerous samples was then performed using the following script and command:  <br>
`bash transpose.sh ` <br>
- transpose.sh is dependent on tsk.awk, so ensure that tsk.awk is present in the same directory <br>
- tsk.awk : works to transpose the individual files <br> 

## Final Dataset 
output.txt (cancerous), output_normal.txt (normal)


