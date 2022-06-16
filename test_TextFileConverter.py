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
#from TextFileConverter import * as tfc
import pytest

#===============================================================================
# Global Data

TITLE   = 'Test of TextFileConverter.py'
version = '0000.0000'

#===============================================================================
# Classes

# class test_TextFileConverter(unittest.TestCase):

def test_instance_no_parms():
    """Test the class without parameters"""

    # Arrange --- # Nothing to arrange

    # Act
    with pytest.raises(tfc.SourceFileAbsentError):
        source_file = tfc.cls_text_file()

    # Assert
        
def test_source_file_absent():
    """Test the class with using non exist file name"""
      
    # Arrange --- # Ensure that a particular file does not exist:
    path = os.getcwd()
    test_file_NO_FILE = os.path.join(path, 'testTextFileConverter.DELETE_THIS_FILE.dat')
    try:
        os.remove(test_file_NO_FILE)
    except FileNotFoundError:
        pass

    # Act
    with pytest.raises(tfc.SourceFileAbsentError):
        source_file = tfc.cls_text_file(source_file_name=test_file_NO_FILE)

    # Assert

def test_empty_file():
    """Test the class with an empty file."""

    # Arrange --- # Create an empty file to test with
    path = os.getcwd()
    test_file_0000_name  = os.path.join(path, 'testTextFileConverter.0000.dat')
    try:
        os.remove(test_file_0000_name)
    except FileNotFoundError:
        pass
    
    test_file_0000       = open(test_file_0000_name,"w", encoding='utf-8')
    test_file_0000.close()
 
    # Act
    with pytest.raises(tfc.SourceFileEmptyError):
        source_file = tfc.cls_text_file( source_file_name=test_file_0000_name)
      
    # Assert
        
    assert  isinstance(source_file, cls_text_file)
    assert  source_file.source_file_name == test_file_0000_name

def test_source_file_test_0001():
    """Test the class with a file (not Empty)."""

    # Arrange --- # Create a text file and put some data into it.
    path = os.getcwd()
    test_file_0001_name  = os.path.join(path, 'testTextFileConverter.0001.dat')
    try:
        os.remove(test_file_0001_name)
    except FileNotFoundError:
        pass

    test_file_0001       = open(test_file_0001_name,"w", encoding='utf-8')
    for i in range(0, 20):
        record = f'record{i:04}' 
        for j in range (0, 15):
            if (j % 2) == 0:
                record = record + f'field{j:>4}'
            else:
                record = record + f'field{j:04}'

            record = record + f'\n'
            test_file_0001.write(record)
            
        test_file_0001.close()
        
        # Act

        test_file_0001 = tfc.cls_text_file(test_file_0001_name)
              
        # Assert

        assert  isinstance(test_file_0001, tfc.cls_text_file)
        assert  test_file_0001.source_file_name == test_file_0001_name
        
if __name__ == "__main__":
    print("Done")
