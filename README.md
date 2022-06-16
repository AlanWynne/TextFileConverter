# TextFileConverter
TextFileConverter is a python project to convert Structured Text flat file 
into csv or json files. 

This is currently a work in progress, and still is not delivering any resutls.

I am doing this in an effort to learn about Python Programming and TDD with 
Python Programming. 

===============================================================================
In order to do this conversion, we first need to understand the structure of
the text file. The assumption been made that this information is available.
This information needs to be imported into the program and stored in a usable
format. The structure will be saved in a json file, so that it can be used 
again.

Scenario:

    a_text_file.dat   to be converted to csv.

        When the program runs, it needs to be provided with the source file 
        to be converted, the conversion process (csv, json) the field 
        delimiter and the text qulifier. All parameters are optional. 

        if source file name is not provided the program will request it.
        if the conversion process is not provided csv will be defaulted
        if the field delimiter is not provided it will be defaulted to comma
        if text qualifier is not provided it will be defaulted to single quote        

        The final settings for the file will be saved in a json file that can be
        reused to do a simialr task on a new version of the source file name.
        The json file storing this information will be called "a_text_file.fi.json"

        Each time the program runs it will look foir files endign with "fi.json"
        and list them for selection to be used to re-apply the same conversion
        process.
        
        The "a_text_file.fi.json" file will also contain a data dicitionary 
        of record structures for each record type in the file. The data dictioanry 
        will stipulate the field name and value that will identify how to select
        records for that particular structure.  
        
        a record structure will have a name and will be save in a seperate
        record structure json file called "a_record_structure_name.rs.json" 
        keeping it out sideof the "fi.json" file means it could be used for
        other file's as well.

        The record structure will be defined as a data dictionary, the 
        primary key of the record structure data dictionary will be the 
        record structure name the Value of the Record structure key will be 
        another data dictionary of the Fields that make up the record.
        Each Field name will be a key of this data dictionary and it will 
        have a data dictionary of the Record attributes. The record attributes
        are, starting offset, field length, ending offset (always staring 
        offset + length), and optionaly a value for the field that will identify
        the record as this record strcuture. 

===============================================================================
 Things to do:  (so much but so little time!)
    
    Build code to get source_file_name of the file to be converted, what 
    format we wish to convert too.
    
    Once we have the file name, we need to check if there is existing file 
    structure information availble.
    
    Exsiting file structure information is available: Load it and use it.
    
    No existing file structure information available: Create it.
    
    Read the input file and convert it to the desired output format and 
    save it.

