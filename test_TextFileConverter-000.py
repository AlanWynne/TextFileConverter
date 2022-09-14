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


import pytest

import os
import shutil

from GitHub.TextFileConverter import TextFileConverter as tfc

#===============================================================================
# Global Data

TITLE   = 'Test of TextFileConverter.py'
version = '0000.0000'

path                            =  os.getcwd()
log                             =  False

parent_dir       = os.getcwd()
test_dir_name    = 'TextFileConverter/TestDirectory'
root_file_name   = 'TDD_MasterTestFile_Customers_Accounts'

test_dir         = os.path.join(os.getcwd(), test_dir_name)

test_input_dat   = root_file_name + '.dat'
test_config_json = root_file_name + '.fc.json'
test_config_xlsx = root_file_name + '.fc.xlsx'
test_output_csv  = root_file_name + '.csv'
test_output_json = root_file_name + '.json'
test_output_dat  = root_file_name + '.out.dat'
    
def delete_file_obj_no_exception(obj):

    if os.path.isfile(obj):
        try:
            os.remove(obj)
        except FileNotFoundError:
            pass 

    if os.path.isdir(obj):
        try:
            shutil.rmtree(obj)
        except FileNotFoundError:
            pass 
            
#===============================================================================
# Classes

# class test_TFC_000():

def test_setup ():

    # Do everything to cleanup and setup the testing environment
    # Remove everything that should not exist before testing.
    # Copy test file to the testing directory.
 
    while test_dir_name in os.getcwd():
        os.chdir("..")

    parent_dir       = os.getcwd()
    test_dir         = os.path.join(os.getcwd(), test_dir_name)

    delete_file_obj_no_exception(test_dir)
    os.mkdir(test_dir)        # Create new empty test directory
    os.chdir(test_dir)        # Make new Test Directory the current Directory
    
    shutil.copy(os.path.join(parent_dir, test_input_dat ) , os.path.join(test_dir, test_input_dat ))
    shutil.copy(os.path.join(parent_dir, test_config_json ) , os.path.join(test_dir, test_config_json ))
    shutil.copy(os.path.join(parent_dir, test_config_xlsx ) , os.path.join(test_dir, test_config_xlsx ))
    
    # Assert
    
    assert os.path.isfile(os.path.join(test_dir, test_input_dat ))
    assert os.path.isfile(os.path.join(test_dir, test_config_json ))
    assert os.path.isfile(os.path.join(test_dir, test_config_xlsx ))
    
    os.chdir("..")
    
def test_dat_to_csv_use_json():
    """Convert Dat file to CSV using Config Described in JSON"""

    # Expectation :
    # A csv version of the source file is created

    # Arrange --- # copy template files to directory to convert to csv
    
    os.chdir(test_dir)      
    test_case_dir_name      = 'TestCase_001_dat_to_csv_using_json'
    test_case_dir           = os.path.join(os.getcwd(), test_case_dir_name)
    
    delete_file_obj_no_exception(test_case_dir)

    os.mkdir(test_case_dir)        # Create new empty test directory
    os.chdir(test_case_dir)        # Make new Test Directory the current Directory

    source_file             = os.path.join(test_case_dir, test_input_dat )
    config_file             = os.path.join(test_case_dir, test_config_json)
    dest_file               = os.path.join(test_case_dir, test_output_csv)

    assert not os.path.isfile(source_file)
    assert not os.path.isfile(config_file)
    assert not os.path.isfile(dest_file)

    shutil.copy(os.path.join(parent_dir, test_input_dat ) , source_file)
    shutil.copy(os.path.join(parent_dir, test_config_json ) , config_file)

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'csv', fd = '|' , tq = '"',  log = True )

    # Assert

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    assert os.path.isfile(dest_file)

    os.chdir("..")
    
def test_dat_to_csv_use_xlsx():
    """Convert Dat file to CSV using Config Described in XLSX"""

    # Expectation :
    # A csv version of the source file is created

    # Arrange --- # Copy template files to directory to convert to csv

    os.chdir(test_dir)      
    test_case_dir_name      = 'TestCase_002_dat_to_csv_using_xlsx'
    test_case_dir           = os.path.join(os.getcwd(), test_case_dir_name)
    
    delete_file_obj_no_exception(test_case_dir)

    os.mkdir(test_case_dir)        # Create new empty test directory
    os.chdir(test_case_dir)        # Make new Test Directory the current Directory

    source_file             = os.path.join(test_case_dir, test_input_dat )
    config_file             = os.path.join(test_case_dir, test_config_xlsx)
    dest_file               = os.path.join(test_case_dir, test_output_csv)

    assert not os.path.isfile(source_file)
    assert not os.path.isfile(config_file)
    assert not os.path.isfile(dest_file)

    shutil.copy(os.path.join(parent_dir, test_input_dat ) , source_file)
    shutil.copy(os.path.join(parent_dir, test_config_xlsx ) , config_file)

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'csv', fd = '|' , tq = '"',  log = True )

    # Assert

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    assert os.path.isfile(dest_file)
    
    os.chdir("..")
    
def test_dat_to_json_use_json():
    """Convert Dat file to CSV using Config Described in JSON"""

    # Expectation :
    # A csv version of the source file is created

    # Arrange --- # copy template files to directory to convert to csv

    os.chdir(test_dir)      
     
    test_case_dir_name      = 'TestCase_003_dat_to_json_using_json'
    test_case_dir           = os.path.join(os.getcwd(), test_case_dir_name)
    
    delete_file_obj_no_exception(test_case_dir)

    os.mkdir(test_case_dir)        # Create new empty test directory
    os.chdir(test_case_dir)        # Make new Test Directory the current Directory

    source_file             = os.path.join(test_case_dir, test_input_dat)
    config_file             = os.path.join(test_case_dir, test_config_json)
    dest_file               = os.path.join(test_case_dir, test_output_json)

    assert not os.path.isfile(source_file)
    assert not os.path.isfile(config_file)
    assert not os.path.isfile(dest_file)

    shutil.copy(os.path.join(parent_dir, test_input_dat ) , source_file)
    shutil.copy(os.path.join(parent_dir, test_config_json ) , config_file)

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'json', fd = '|' , tq = '"',  log = True )

    # Assert

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    assert os.path.isfile(dest_file)

    os.chdir("..")
    
def test_dat_to_json_use_xlsx():
    """Convert Dat file to CSV using Config Described in XLSX"""

    # Expectation :
    # A csv version of the source file is created

    # Arrange --- # Copy template files to directory to convert to csv

    os.chdir(test_dir)      

    test_case_dir_name      = 'TestCase_004_dat_to_json_using_xlsx'
    test_case_dir           = os.path.join(os.getcwd(), test_case_dir_name)
    
    delete_file_obj_no_exception(test_case_dir)

    os.mkdir(test_case_dir)        # Create new empty test directory
    os.chdir(test_case_dir)        # Make new Test Directory the current Directory

    source_file             = os.path.join(test_case_dir, test_input_dat )
    config_file             = os.path.join(test_case_dir, test_config_xlsx)
    dest_file               = os.path.join(test_case_dir, test_output_json)

    assert not os.path.isfile(source_file)
    assert not os.path.isfile(config_file)
    assert not os.path.isfile(dest_file)

    shutil.copy(os.path.join(parent_dir, test_input_dat ) , source_file)
    shutil.copy(os.path.join(parent_dir, test_config_xlsx ) , config_file)

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'json', fd = '|' , tq = '"',  log = True )

    # Assert

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    assert os.path.isfile(dest_file)

    os.chdir("..")
    
def test_dat_to_dat_use_json():
    """Convert Dat file to Dat using Config Described in json"""

    # Expectation :
    # A csv version of the source file is created

    # Arrange --- # Copy template files to directory to convert to csv

    os.chdir(test_dir)      

    test_case_dir_name      = 'TestCase_005_dat_to_dat_using_json'
    test_case_dir           = os.path.join(os.getcwd(), test_case_dir_name)
    
    delete_file_obj_no_exception(test_case_dir)

    os.mkdir(test_case_dir)        # Create new empty test directory
    os.chdir(test_case_dir)        # Make new Test Directory the current Directory

    source_file             = os.path.join(test_case_dir, test_input_dat)
    config_file             = os.path.join(test_case_dir, test_config_json)
    dest_file               = os.path.join(test_case_dir, test_output_dat)

    assert not os.path.isfile(source_file)
    assert not os.path.isfile(config_file)
    assert not os.path.isfile(dest_file)

    shutil.copy(os.path.join(parent_dir, test_input_dat ) , source_file)
    shutil.copy(os.path.join(parent_dir, test_config_json ) , config_file)

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'dat', fd = '|' , tq = '"',  log = True )

    # Assert

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    assert os.path.isfile(dest_file)

    os.chdir("..")
    
def test_dat_to_dat_use_xlsx():
    """Convert Dat file to Dat using Config Described in xlsx"""

    # Expectation :
    # A csv version of the source file is created

    # Arrange --- # Copy template files to directory to convert to csv

    os.chdir(test_dir)      

    test_case_dir_name      = 'TestCase_006_dat_to_dat_using_xlsx'
    test_case_dir           = os.path.join(os.getcwd(), test_case_dir_name)
    
    delete_file_obj_no_exception(test_case_dir)

    os.mkdir(test_case_dir)        # Create new empty test directory
    os.chdir(test_case_dir)        # Make new Test Directory the current Directory

    source_file             = os.path.join(test_case_dir, test_input_dat)
    config_file             = os.path.join(test_case_dir, test_config_xlsx)
    dest_file               = os.path.join(test_case_dir, test_output_dat)

    assert not os.path.isfile(source_file)
    assert not os.path.isfile(config_file)
    assert not os.path.isfile(dest_file)

    shutil.copy(os.path.join(parent_dir, test_input_dat ) , source_file)
    shutil.copy(os.path.join(parent_dir, test_config_xlsx ) , config_file)

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    
    # Act
    tfc.cls_text_file(sfn = source_file, ot = 'dat', fd = '|' , tq = '"',  log = True )

    # Assert

    assert os.path.isfile(source_file)
    assert os.path.isfile(config_file)
    assert os.path.isfile(dest_file)
    
    os.chdir("..")
    
if __name__ == "__main__":

    print("Done")
