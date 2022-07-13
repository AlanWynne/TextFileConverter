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

import os
import TextFileConverter as tfc
import pytest
import shutil

#===============================================================================
# Global Data

TITLE   = 'Test of TextFileConverter.py'
version = '0000.0000'

path                            =  os.getcwd()
log                             =  False

def delete_file_no_exception(file):

    try:
        os.remove(file)
    except FileNotFoundError:
        pass 
        
#===============================================================================
# Classes

# class test_TFC_000():

def test_setup ():

    # Remove    everything that should not exist before testing.
    # Arrange

    files = os.listdir(os.getcwd())

    for f in files:
        if 'TextFileConverter' in f:
            if '.log' in f:
                delete_file_no_exception(f)

    # Act 

    # Assert
    # Ensure that files deleted correctly

def test_MasterDataTestFileCopy001_csv():
    """Create instance source file full name provided file has data"""

    # Expectation :
    # Source file Confiuration file created in current working directory
    # theOpen the file, if it is empty SourceFileEmptyError raised
    
    # Arrange --- # Crete a source file with a particular structure
   
    original                = os.path.join(os.getcwd(), 'MasterDataTestFile.fc.json') 
    new_copy                = os.path.join(os.getcwd(), 'MasterDataTestFile.copy001.fc.json')
    
    delete_file_no_exception(new_copy)
    shutil.copyfile(original, new_copy) 
    assert                  os.path.isfile(new_copy)

    original                = os.path.join(os.getcwd(), 'MasterDataTestFile.dat') 
    new_copy                = os.path.join(os.getcwd(), 'MasterDataTestFile.copy001.dat')
    
    delete_file_no_exception(new_copy)
    shutil.copyfile(original, new_copy)   
    assert                  os.path.isfile(new_copy)
    
    source_file             = new_copy
    destination_file        = os.path.join(os.getcwd(), 'MasterDataTestFile.copy001.csv')
    
    delete_file_no_exception(destination_file)
    
    assert                  os.path.isfile(source_file)
    assert not              os.path.isfile(destination_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'csv', fd = '|' , tq = '"',  log = True )

    # Assert
    assert                  os.path.isfile(source_file)
    assert                  os.path.isfile(destination_file)

def test_MasterDataTestFileCopy002_json():
    """Create instance source file full name provided file has data"""

    # Expectation :
    # Source file Confiuration file created in current working directory
    # theOpen the file, if it is empty SourceFileEmptyError raised
    
    # Arrange --- # Crete a source file with a particular structure
   
    original                = os.path.join(os.getcwd(), 'MasterDataTestFile.fc.json') 
    new_copy                = os.path.join(os.getcwd(), 'MasterDataTestFile.copy002.fc.json')
    
    delete_file_no_exception(new_copy)
    shutil.copyfile(original, new_copy) 
    assert                  os.path.isfile(new_copy)

    original                = os.path.join(os.getcwd(), 'MasterDataTestFile.dat') 
    new_copy                = os.path.join(os.getcwd(), 'MasterDataTestFile.copy002.dat')
    
    delete_file_no_exception(new_copy)
    shutil.copyfile(original, new_copy)   
    assert                  os.path.isfile(new_copy)
    
    source_file             = new_copy
    destination_file        = os.path.join(os.getcwd(), 'MasterDataTestFile.copy002.json')
    
    delete_file_no_exception(destination_file)
    
    assert                  os.path.isfile(source_file)
    assert not              os.path.isfile(destination_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'json', fd = '|' , tq = '"',  log = True )

    # Assert
    assert                  os.path.isfile(source_file)
    assert                  os.path.isfile(destination_file)

def test_MasterDataTestFileCopy003_dat():
    """Create instance source file full name provided file has data"""

    # Expectation :
    # Source file Confiuration file created in current working directory
    # theOpen the file, if it is empty SourceFileEmptyError raised
    
    # Arrange --- # Crete a source file with a particular structure
   
    original                = os.path.join(os.getcwd(), 'MasterDataTestFile.fc.json') 
    new_copy                = os.path.join(os.getcwd(), 'MasterDataTestFile.copy003.fc.json')
    
    delete_file_no_exception(new_copy)
    shutil.copyfile(original, new_copy) 
    assert                  os.path.isfile(new_copy)

    original                = os.path.join(os.getcwd(), 'MasterDataTestFile.dat') 
    new_copy                = os.path.join(os.getcwd(), 'MasterDataTestFile.copy003.dat')
    
    delete_file_no_exception(new_copy)
    shutil.copyfile(original, new_copy)   
    assert                  os.path.isfile(new_copy)
    
    source_file             = new_copy
    destination_file        = os.path.join(os.getcwd(), 'MasterDataTestFile.copy003.out.dat')
    
    delete_file_no_exception(destination_file)
    
    assert                  os.path.isfile(source_file)
    assert not              os.path.isfile(destination_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'dat', fd = '|' , tq = '"',  log = True )

    # Assert
    assert                  os.path.isfile(source_file)
    assert                  os.path.isfile(destination_file)


if __name__ == "__main__":
    print("Done")
