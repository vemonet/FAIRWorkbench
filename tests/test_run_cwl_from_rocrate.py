from fairworkflows.config import TESTS_RESOURCES
from fairworkflows.ro_crate import ROCrate

SAMPLE_ROCRATE = TESTS_RESOURCES / 'test_crate.crate.zip'

def test_run_cwl_from_rocrate():

    crate = ROCrate(SAMPLE_ROCRATE)
    crate.run({'message': 'helloworld'})

    assert len(crate.run_log) > 0
