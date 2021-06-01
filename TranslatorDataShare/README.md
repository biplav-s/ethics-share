# Resources for rating translator data

This repository is intended to share data related to rating of translators
for gender-bias. A list of professions were used to generate
input sentences which were fed to commercial translators (anonymized
as T1, T2, ...). The translation is conducted from English to a language 
(called middle language) and then back to English. The performance of the 
translators are assessed for discrepency in gender in the sentences.


Description of directories:
  * input: 
    - Profession.txt: list of professions used to generate 
          input sentences
    - biasTestParameter: used to generate sentences. See explanation
          and parser in ./BiasSpecReusabledata" directory
  * output:
    - Result - {true/false} - <translator> - <language>.json
           where true: 1st step of rating method
                 false: 2nd step of rating method
    - Result - <translator> - summary.csv
           contains the discrepency in gender when unbiased (u1) or
           biased data (b1 or b2)  is given as input.           
    
