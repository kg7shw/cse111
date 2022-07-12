from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Grant", "Call") == "Call; Grant"
    assert make_full_name("Ny", "Ang") == "Ang; Ny"
    assert make_full_name("Jose", "Del-Silvio") == "Del-Silvio; Jose"
    assert make_full_name("Aaron", "McDougal") == "McDougal; Aaron"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Call; Grant") == "Call"
    assert extract_family_name("Ang; Ny") == "Ang"
    assert extract_family_name("Del-Silvio; Jose") == "Del-Silvio"
    assert extract_family_name("McDougal; Aaron") == "McDougal"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    assert extract_given_name("Call; Grant") == "Grant"
    assert extract_given_name("Ang; Ny") == "Ny"
    assert extract_given_name("Del-Silvio; Jose") == "Jose"
    assert extract_given_name("McDougal; Aaron") == "Aaron"
    assert extract_given_name("; ") == ""










# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])