# Radon CTT CLI

Command-line interface (CLI) for interacting with the Radon CTT server.

| Items | Contents |
| --- | --- |
| **Description** | The Continuous Testing Tool Command-line interface allows to execute CTT workflows on a [CTT Server](https://github.com/radon-h2020/radon-ctt) based on the information from configuration files. |
| **Licence**| Apache License, Version 2.0: https://opensource.org/licenses/Apache-2.0 |
| **Maintainers**| <ul><li>Thomas F. Düllmann ([@duelle](https://github.com/duelle)) </li><li>Andre van Hoorn ([@avanhoorn](https://github.com/avanhoorn)) </li></ul> |


## Installation

* Clone repository
* (Optional) Install Python environment (e.g., `virtualenv .` and `source bin/activate`)
* Install package requirements: `pip install -r requirements.txt`


## Usage
```
ctt-cli.py [PARAMS]
    Mandatory parameters:
        -u, --url=CTT_SERVER_URL    URL of the running CTT server (e.g., http://localhost:18080/RadonCTT)
        -c, --config=CTT_CONFIG     Path to the CTT configuration file
        
    Other parameters:   
        -r, --remote                Run (multiple configurations remotely)
        -v, --verbose               Be verbose
        -h, --help                  Print this help
```

## Configuration File

The configuration file is expected to be in the YAML format, containing the following fields:

### Mandatory:
* **name**: The name of the project to create
* **repository_url**: The URL of the git repository or, in case the server runs in CHE-mode, the folder name of the project
* **sut_tosca_path**: The relative path to the SUT CSAR
* **ti_tosca_path**: The relative path to the TI CSAR
* **result_destination_path**: Path where the results should be saved
* **test_id**: ID of the test to execute (not fully implemented, can be any string at the moment)

### Optional:
* **sut_inputs_path**: The relative path to the SUT inputs 
* **ti_inputs_path**: The relative path to the TI inputs

### Example 
```
{
  'name': 'ToDoListAPI',
  'repository_url': 'demo-ctt-todolistapi',
  'sut_tosca_path': 'todolist.csar',
  'ti_tosca_path': 'deploymentTestAgent.csar',
  'ti_inputs_path': 'inputs.yaml',
  'result_destination_path': '/tmp/results.zip',
  'test_id': 'deploymentTest_01',
}
```
