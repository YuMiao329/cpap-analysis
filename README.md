# CPAP Analysis Assignment

The file `cpap_cal.py` could be used to generate personalized informations based on the O2 level and average events.

There are four different results could be generated based on the information entered:

`Hypoxia`,`Hypoxia Apnea`,`Normal Sleep`,`Apnea`

Which could be analyzed based on table:
  |  | All O2 values 93 and above | Any O2 value below 93
  | --- | --- | --- |
  | __Average Events <= 5.0__ | normal sleep | hypoxia |
  | __Average Events > 5.0__ | apnea | hypoxia apnea |
  
 The default information is based on the file `sample_data.txt`
 
 ## Usage
 
 Simply run the file `cpap_cal.py` you will be able to automatically load data from the `sample_data.txt`
 
 Since there are ten patients in the file, ten JSON file will be ouput to the current directory.
 
 Each of the JSON file contains the information of the name shown as the file name.
