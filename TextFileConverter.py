# -*- coding: utf-8 -*-
# Copyright (C) 2022 Alan Wynne
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Pu blic
# License as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Contributor(s): Alan Wynne
#

__doc__="""Use OpenDocument to generate your documents."""

#===============================================================================
# import statements

import sys
import os
import PySimpleGUI as sg

#===============================================================================
# Global Data

TITLE   = 'Flat Text file to csv, json conversion'
version = '0000.0000'

#===============================================================================
# Classes

class SourceFileAbsentError(Exception):
    """An exception class for empty Source files"""
    
class SourceFileEmptyError(Exception):
    """An exception class for empty Source files"""
    
class cls_record:
    """ Record class
        Handle flat records in a file with a particular structure, and get them
        into a python usable format.
    """

    #===========================================================================
    # Class Attributes

    CLASS_NAME                  = 'cls_record_structure'
    version                     = '0000.0000'

    # =============================================================================
    # @staticmethod decorator:  Add a Function to a class
    # Class Static methods refer to :
    # the generic cls rather than to self or a particular instances. nothing in
    # the static method should refer to an instance

    # =============================================================================
    # @classmethod decorator:  Add a Custom Constructor to the Class
    # determines Class methods and refer to class rather. Static Methods are used
    # to ammend settings created in __init__

    # =============================================================================
    # Instance methods do not have particular instance decorators. Instance methods
    # are relevant to a particular instnace

    def __init__(self):
        """ constructor method for cls_record_structure """

        pass

class cls_text_file:
    """ Text File class
        Handle text files,
    """
    #===========================================================================
    # Class Attributes

    CLASS_NAME                  = 'cls_text_file'
    version                     = '0000.0000'


    SUPPORTED_INPUT             = ('*.*', '*')
    SUPPORTED_INPUT_DESCRIP     = 'All files'

    SUPPORTED_OUTPUT            = ('csv', 'json')
    SUPPORTED_OUTPUT_DESCRIP    = str(SUPPORTED_OUTPUT)

    CHAR_COMMA                  = ','
    CHAR_QUOTE_SINGLE           = "'"
    CHAR_QUOTE_DOUBLE           = '"'

    dd_text_file_structure      = {}   # data dicitonay defining the input file attributes
    record_structures           = []   # list of record structures pertaining to the file

    # =============================================================================
    # @staticmethod decorator:  Add a Function to a class
    # Class Static methods refer to :
    # the generic cls rather than to self or a particular instances. nothing in
    # the static method should refer to an instance

    @staticmethod # print out help on how to use this function
    def display_help(cls):

        """ Text file Conmverter Help function.
        """

        help_text = """
            TextFileConverter.py usage.

                TextFileConverter.py self, (source_file_name = None, output_type = None, delim = None, text_qualifier = None)

                Source_file_name: The name of the source file name to be converted to the desired output.
                output_type     : The desired convertion process, currently csv or json
                delim           : Applicable for csv is the field seperator or delimiter
                text_qualifier  : The character desired to be used to enclose char, text or string fields

        """
        print(help_text)
        return

    @staticmethod # Get and validate a file_name
    def get_file_name(cls, file_name = None, file_types = None , message = None):

        message             = ''
        path                = os.getcwd()

        if file_name        == None:
            file_name       = ''

        if file_name        == '':     # provided file name is empty get file name
            message         = 'No File name provided!'
        else:                          # provided file name to be verified.
            if not os.path.isfile(file_name):
                if os.path.isdir(file_name):
                    path            = file_name
                    os.chdir(path)
                    message         = 'Provided file names is a path!'
                    file_name       = ''
                else:
                    message         = 'Provided file name does not exist!'
                    file_name        = ''

        if file_types               == None:
            file_types_descrip      =  cls_text_file.SUPPORTED_INPUT_DESCRIP
            file_types              =  cls_text_file.SUPPORTED_INPUT

        if isinstance(file_types, str):
           file_types_descrip        = file_type
           file_types                = tuple(map(file_types.split(', ') ))  # convert file types to tupple

        if isinstance(file_types, tuple):
            if file_types           == ():
                file_types_descrip  =  cls_text_file.SUPPORTED_INPUT_DESCRIP
                file_types          =  cls_text_file.SUPPORTED_INPUT
            else:
                if file_types           == cls_text_file.SUPPORTED_INPUT:
                    file_types_descrip  =  cls_text_file.SUPPORTED_INPUT_DESCRIP
                else:
                    file_types_descrip  =  str(file_types)

        if file_name                == '':          # no file_name provided, get file_name.
            message                 = message + ' ' + 'Please select a file?'
            file_name          = sg.popup_get_file(message ,
                title               = TITLE,
                default_path        = path,
                default_extension   = ".txt",
                file_types          = ((file_types_descrip, file_types),),
                )

        if not file_name:
            # sg.popup("Cancel", "No file_name selected")
            raise SourceFileAbsentError("Quiting: no source_file_name selected!")

        return(file_name)

    # =============================================================================
    # @classmethod decorator:  Add a Custom Constructor to the Class
    # determines Class methods and refer to class rather. Static Methods are used
    # to ammend settings created in __init__

    # =============================================================================
    # Instance methods do not have particular instance decorators. Instance methods
    # are relevant to a particular instnace

    def set_field_delim(self, delim):
        """ Set Field delimiter """

        if delim == '':
            delim               = cls_text_file.CHAR_COMMA
            self.fd             = cls_text_file.CHAR_COMMA
            self.field_delim    = self.fd
        else:
            self.fd             = delim
            self.field_delim    = self.fd
        return(delim)

    def set_text_qualifier(self, text_qualifier):
        """ Set text Qualifier """

        if text_qualifier == '':
            text_qualifier      = cls_text_file.CHAR_QUOTE_SINGLE
            self.tq             = cls_text_file.CHAR_QUOTE_SINGLE
            self.text_qualifier = self.tq
        else:
            self.tq             = text_qualifier
            self.text_qualifier = self.tq

        return(text_qualifier)

    def __init__(self, source_file_name = None, output_type = None, delim = None, text_qualifier = None):
        """ constructor method """

        if source_file_name == None:
            source_file_name      = ''
            self.source_file_name = ''

        if isinstance(source_file_name, str):
            self.source_file_name = cls_text_file.get_file_name(cls_text_file, file_name = source_file_name, file_types = cls_text_file.SUPPORTED_INPUT)

        if output_type in cls_text_file.SUPPORTED_OUTPUT:
            self.output_type    = output
        else:
            self.output_type    = cls_text_file.SUPPORTED_OUTPUT[0]

        self.fd                 = self.set_field_delim(delim)
        self.tq                 = self.set_text_qualifier(text_qualifier)

        return

    def print(self):
        """ print the instance attributes. """

        import json

        cls_text_file_attributes_dd = {
            'CLASS_NAME':               cls_text_file.CLASS_NAME,
            'Attributes':               {
                'version':                  cls_text_file.version,
                'CHAR_COMMA':               cls_text_file.CHAR_COMMA,
                'CHAR_QUOTE_SINGLE':        cls_text_file.CHAR_QUOTE_SINGLE,
                'CHAR_QUOTE_DOUBLE':        cls_text_file.CHAR_QUOTE_DOUBLE,
                'source_file_name':           self.source_file_name,
                'field_delim':              self.field_delim,
                'text_qualifier':           self.text_qualifier,
                'SUPPORTED_OUTPUT':         cls_text_file.SUPPORTED_OUTPUT,
                'output_type':              self.output_type
                }
            }

        print(json.dumps(cls_text_file_attributes_dd, indent=4, sort_keys=False))
        return(0)

#===============================================================================
# Main Processing

"""
    Flat Text file to csv, json conversion.
"""
print(f"Start of Main Program: {__name__}")
print(f"Name of the script      : {sys.argv[0]=}")
print(f"Arguments of the script : {sys.argv[1:]=}")

args                    = ''
source_file_name_parm   = '' 
output_type_parm        = ''
delim_parm              = ''
text_qualifier_parm     = ''

i = 1
for arg in args:
    print(f'\t Argument {i}:<{arg}>')
    if 'source_file_name' in arg:
        source_file_name_parm = arg
    if 'output_type=' in arg:
        output_type_parm = arg
    if 'delim=' in arg:
        delim_parm = arg
    if 'text_qualifier=' in arg:
        text_qualifier_parm = arg
    i += 1

# text_file = cls_text_file(source_file_name_parm, output_type_parm, delim_parm, text_qualifier_parm)

#===============================================================================
# In order to do this conversion, we first need to understand the structure of
# the text file. The assumption been made that this information is available.
# This information needs to be imported into the program and stored in a usable
# format.

#===============================================================================
# It is assumed that the flat file is made up of flat text that has no delimiters
# or text enclosures, and may have more than one record type on the file.
# The hiarchy will be assumed to be as follows:
# For each file_name, there could be numerous record structures.
# Each record structure will have a structure name, record identifier field name
# and a record identifier field value.
#
# Each Record Structure will also have a list of fields that make up the record.
# The field in the list of fields will contain a field name, field start offset,
# field lenght, and field end offset. End field offset will always be
# field start offset + field length.

#===============================================================================
# Things to do:
#   1:  Build code to get file_name of the file to be converted, and what format
#       we wish to convert too.
#   2:  Once we have the file name, we need to check if there is existing
#       file structure information availble.
#   3:  Exsiting file structure information is available: Load it.
#   4:  No existing file structure information available: Create it.
#   5:  Read the input file and convert it to the desired output format
#       and save it.

# source_file_name  = 'D:/Users/A142367/OneDrive - Standard Bank/WIP/Python/test_TextFileConverter.txt'
