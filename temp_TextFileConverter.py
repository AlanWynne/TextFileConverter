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
test_conversion_file_config_fn  =  os.path.join(path, ('file_conversion_configuration_template' + '.fc.json'))
test_absent_file_sffn_fn        =  os.path.join(path, 'test_absent_file_sffn_fn.dat')
test_absent_file_sffn_cfn       =  os.path.join(path, 'test_absent_file_sffn_fn.fc.json')
test_absent_file_sfn_fn         =  'test_absent_file_sffn_fn.dat'
test_absent_file_sfn_cfn        =  'test_absent_file_sffn_cfn.fc.json'
test_empty_file_sffn_fn         =  os.path.join(path, 'test_empty_file_sffn_fn.dat')
test_empty_file_sffn_cfn        =  os.path.join(path, 'test_empty_file_sffn_fn.fc.json')
test_empty_file_sfn_fn          =  'test_empty_file_sfn_fn.dat'
test_empty_file_sfn_cfn         =  'test_empty_file_sfn_fn.fc.json'
test_source_file_sffn_0001_fn   =  os.path.join(path, 'test_source_file_sffn_0001_fn.dat')
test_source_file_sffn_0001_cfn  =  os.path.join(path, 'test_source_file_sffn_0001_fn.fc.json')
test_source_file_sfn_0001_fn    =  'test_source_file_sfn_0001_fn.dat'
test_source_file_sfn_0001_cfn   =  'test_source_file_sfn_0001_fn.fc.json'

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

    delete_file_no_exception(test_conversion_file_config_fn)
    delete_file_no_exception(test_absent_file_sffn_fn)     
    delete_file_no_exception(test_absent_file_sffn_cfn)     
    delete_file_no_exception(test_absent_file_sfn_fn)       
    delete_file_no_exception(test_absent_file_sfn_cfn)      
    delete_file_no_exception(test_empty_file_sffn_fn)       
    delete_file_no_exception(test_empty_file_sffn_cfn)      
    delete_file_no_exception(test_empty_file_sfn_fn)        
    delete_file_no_exception(test_empty_file_sfn_cfn)       
    delete_file_no_exception(test_source_file_sffn_0001_fn) 
    delete_file_no_exception(test_source_file_sffn_0001_cfn)
    delete_file_no_exception(test_source_file_sfn_0001_fn) 
    delete_file_no_exception(test_source_file_sfn_0001_cfn)
    
    # Act 

    # Assert
    # Ensure that files deleted correctly
    assert not os.path.isfile(test_conversion_file_config_fn)
    assert not os.path.isfile(test_absent_file_sffn_fn      )
    assert not os.path.isfile(test_absent_file_sffn_cfn     )
    assert not os.path.isfile(test_absent_file_sfn_fn       )
    assert not os.path.isfile(test_absent_file_sfn_cfn      )
    assert not os.path.isfile(test_empty_file_sffn_fn       )
    assert not os.path.isfile(test_empty_file_sffn_cfn      )
    assert not os.path.isfile(test_empty_file_sfn_fn        )
    assert not os.path.isfile(test_empty_file_sfn_cfn       )
    assert not os.path.isfile(test_source_file_sffn_0001_fn )
    assert not os.path.isfile(test_source_file_sffn_0001_cfn)
    assert not os.path.isfile(test_source_file_sfn_0001_fn  )
    assert not os.path.isfile(test_source_file_sfn_0001_cfn )
    
def test_instance_no_parms():
    """Create instance without parameters"""

    # Expectation :
    # Invoke pySimpleGui popup for user to select a file,
    #       user to cancel
    #       NoFileSelectedError should be raised
    
    # Arrange --- # Nothing to arrange

    # Act
    
    with pytest.raises(tfc.NoParametersError):
        tfc.cls_text_file(log = log)

    # Assert

    assert os.path.isfile(test_conversion_file_config_fn)
        
def test_absent_file_sffn():
    """Create instance source full file name provided but file does not exist"""
    
    # Expectation :
    # Invoke pySimpleGui popup for user to select a file,
    # from directory of source file full name provided.
    #       user to cancel
    #       NoFileSelectedError should be raised
    
    # Arrange --- #

    # Act
    with pytest.raises(tfc.NoFileSelectedError):
        tfc.cls_text_file(sfn = test_absent_file_sffn_fn, log = log)

    # Assert
    assert not os.path.isfile(test_absent_file_sffn_fn)
    assert not os.path.isfile(test_absent_file_sffn_cfn)

def test_absent_file_sfn():
    """Create instance source file name provided but file does not exist"""

    # Expectation :
    # Invoke pySimpleGui popup for user to select a file,
    # from current Working directory.
    #       user to cancel
    #       NoFileSelectedError should be raised

    # Arrange --- # 

    # Act
    with pytest.raises(tfc.NoFileSelectedError):
        tfc.cls_text_file(sfn = test_absent_file_sfn_fn, log = log)

    # Assert
    assert not os.path.isfile(test_absent_file_sfn_fn)
    assert not os.path.isfile(test_absent_file_sfn_cfn)

def test_empty_file_sffn():
    """Create instance source file full name provided but file is empty"""

    # Expectation :
    # Source file Confiuration file created in current working directory
    # Open the file, if it is empty SourceFileEmptyError raised
    
    # Arrange --- # ensure the source file is empty

    source_file       = open(test_empty_file_sffn_fn,"w", encoding='utf-8')
    source_file.close()
        
    # Act
    with pytest.raises(tfc.SourceFileEmptyError):
        tfc.cls_text_file(sfn = test_empty_file_sffn_fn, log = log)

    # Assert

    assert      os.path.isfile(test_empty_file_sffn_fn)
    assert      os.path.isfile(test_empty_file_sffn_cfn)

def test_empty_file_sfn():
    """Create instance source file name provided but file is empty"""

    # Expectation :
    # Source file Confiuration file created in current working directory
    # Open the file, if it is empty SourceFileEmptyError raised
    
    # Arrange --- # ensure the source file is empty

    source_file       = open(test_empty_file_sfn_fn,"w", encoding='utf-8')
    source_file.close()
        
    # Act
    with pytest.raises(tfc.SourceFileEmptyError):
        tfc.cls_text_file(sfn = test_empty_file_sfn_fn, log = log)

    # Assert
    assert      os.path.isfile(test_empty_file_sfn_fn)
    assert      os.path.isfile(test_empty_file_sfn_cfn)

def test_source_file_sffn_0001():
    """Create instance source file full name provided file has data"""

    # Expectation :
    # Source file Confiuration file created in current working directory
    # theOpen the file, if it is empty SourceFileEmptyError raised
    
    # Arrange --- # Crete a source file with a particular structure
    source_file         = open(test_source_file_sffn_0001_fn,"w", encoding='utf-8')
    for i in range(0, 10):
        record          = f'record{i:04}' 
        for j in range (0, 15):
            if (j % 2)  == 0:
                record  = record + f'field{j:>4}'
            else:
                record  = record + f'field{j:04}'

        record      = record + f'\n'
        source_file.write(record)            
    
    source_file.close()
    
    # Act
    tfc.cls_text_file(sfn = test_source_file_sffn_0001_fn, log = log)

    # Assert
    assert      os.path.isfile(test_source_file_sffn_0001_fn)
    assert      os.path.isfile(test_source_file_sffn_0001_cfn)

def test_source_file_sfn_0001():
    """Create instance source file full name provided file has data"""

    # Expectation :
    # Source file Confiuration file created in current working directory
    # theOpen the file, if it is empty SourceFileEmptyError raised
    
    # Arrange --- # Crete a source file with a particular structure
    source_file         = open(test_source_file_sfn_0001_fn,"w", encoding='utf-8')
    for i in range(0, 10):
        record          = f'record{i:04}' 
        for j in range (0, 15):
            if (j % 2)  == 0:
                record  = record + f'field{j:>4}'
            else:
                record  = record + f'field{j:04}'

        record      = record + f'\n'
        source_file.write(record)            
    
    source_file.close()
    
    # Act
    tfc.cls_text_file(sfn = test_source_file_sfn_0001_fn, log = log)

    # Assert
    assert      os.path.isfile(test_source_file_sfn_0001_fn)
    assert      os.path.isfile(test_source_file_sfn_0001_cfn)

# class test_TFC_MasterData():

def test_MasterDataTestFileCopy001():
    """Create instance source file full name provided file has data"""

    # Expectation :
    # Source file Confiuration file created in current working directory
    # theOpen the file, if it is empty SourceFileEmptyError raised
    
    # Arrange --- # Crete a source file with a particular structure

    delete_file_no_exception(test_conversion_file_config_fn)
    
    
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

if __name__ == "__main__":
    print("Done")
