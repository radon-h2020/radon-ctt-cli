# Radon CTT CLI

Command-line interface (CLI) for interacting with the Radon CTT server.

## Usage

ctt-cli.py [PARAMS]
    Mandatory parameters:
        -u, --url=CTT_SERVER_URL    URL of the CTT server (e.g., http://localhost:18080/RadonCTT)
        -c, --config=CTT_CONFIG     Path to the CTT configuration file
        
    Other parameters:    
        -v, --verbose               Be verbose
        -h, --help                  Print this help


## Configuration File

The configuration file is expected to be in the YAML format, containing the following fields:

### Mandatory:
* name: The name of the project to create
* repository_url: The URL of the git repository or, in case the server runs in CHE-mode, the folder name of the project
* sut_tosca_path: The relative path to the SUT CSAR
* ti_tosca_path: The relative path to the TI CSAR
* result_destination_path: Path where the results should be saved
* test_id: ID of the test to execute (not fully implemented, can be any string at the moment)

### Optional:
* sut_inputs_path: The relative path to the SUT inputs 
* ti_inputs_path: The relative path to the TI inputs

### Example 
{
  'name': 'ToDoListAPI',
  'repository_url': 'demo-ctt-todolistapi',
  'sut_tosca_path': 'todolist.csar',
  'ti_tosca_path': 'deploymentTestAgent.csar',
  'ti_inputs_path': 'inputs.yaml',
  'result_destination_path': '/tmp/results.zip',
  'test_id': 'deploymentTest_01',
}
