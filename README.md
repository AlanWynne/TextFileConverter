# TextFileConverter

## Introduction
TextFileConverter is a python project to convert Structured Text or data flat file into csv or json files. Other formats might be explored later.

This is currently a work in progress, and still is not delivering any results.

I am doing this in an effort to learn about Python Programming and TDD with Python Programming. 

---

## What is a Structured Text or data flat file? 

A Structured Text or data flat file, is a file of data of known structure, but the structure metadata is not part of the file.

## What is structure metadata? 

The Structure metadata is the information about the records in the structured text or data file. 

It is assumed that the text or data file will be a file of data of one or more record structures. These record structures need to be provided to the text file converter in a json or Excel file. This file will be assumed to have the same name as the source text file with one of the following suffixes/extension  'fc.json' or 'fc.xlsx'.

## How does the process work?

On invoking the TextFileConverter Application the following needs to be provided:

1. Source file name:  If source file name is not provided the program will request it.
2. Destination Format: If the conversion process is not provided csv will be assumed.
3. Field Delimiter: If the field delimiter is not provided, comma will be assumed.
4. Text qualifier: If text qualifier is not provided single quote will be assumed.   

Once the process starts it will look for the metadata of the text or data file structure. It will look for this information in a file named the same as the Source file name, but with one of the following extensions "fc.json" or "fc.xlsx". If no such file is found, a template file will be created and the process will end in failure. It is up to the user to then edit the template according to the file structure, or provide the correct metadata file.  

### Scenario:

    a_text_file.dat   to be converted to csv.

   Execute the text file converter as follows: 
   
   textFileConverter sfn=a_text_file.dat ot=csv fd=, tq='

   The program will first ensure that the file  "a_text_file.dat" exists in the current directory or in the path specified if it is provided. 
   it will then look for the files "a_text_file.fc.json" or "a_text_file.fc.xlsx" if not found it will create the file "a_text_file.fc.json" and then the user will have to edit it to have the appropriate metadata for the file "a_text_file.dat".

   Assuming everything is in place, the program should then create a file "a_text_file.csv" which should represent the file "a_text_file.dat" but with the fields in the file separated with the appropriate Field delimiter , text fields appropriately enclosed with the relevant Text Qualifier (Relevant to csv only), also the Metadata field configuration will be overwritten with the current settings and metadata. 

---

# Things to do:  (so much but so little time!)

- What about XML
- What about yaml
