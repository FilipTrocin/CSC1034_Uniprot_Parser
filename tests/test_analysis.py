import pytest

def test_hello_world():
    """Testing code"""
    assert True

import uniplot.analysis
import uniplot.parse


TEST_UNIPROT="./resources/uniprot_sprot_small.xml.gz"

def test_average():
    """Testing correctness of the average lengths of proteins"""
    assert uniplot.analysis.average_len(
        uniplot.parse.uniprot_seqrecords(TEST_UNIPROT)
    ) == 302.72222222222223
