from __future__ import print_function
import getopt
import json
import swagger_client
import sys

from swagger_client.rest import ApiException
from pprint import pprint
from swagger_client.configuration import Configuration

cli_configuration = Configuration()
ctt_conf = {}
verbose: bool = False
MANDATORY_FIELDS = ['name', 'repository_url', 'sut_tosca_path', 'ti_tosca_path',
                    'result_destination_path', 'test_id']
api_client = swagger_client.ApiClient(cli_configuration)


def read_config(config_path: str):
    import os
    import yaml
    if os.path.isfile(config_path):
        with open(config_path, 'r') as config_file:
            config_yaml = yaml.safe_load(config_file)
            global ctt_conf
            ctt_conf = config_yaml
            for field in MANDATORY_FIELDS:
                found: bool = False
                for entry in ctt_conf:
                    if field == entry:
                        found = True
                        break
                if not found:
                    error_msg = f'''Mandatory field {field} is not set in configuration file.'''
                    raise ValueError(error_msg)
            global cli_configuration
            cli_configuration.host = ctt_conf['host']
            if verbose:
                print(f'Successfully read configuration file:')
                pprint(config_yaml)


def create_project(config: Configuration, project_name: str, repository_url: str) -> str:
    project_api_instance = swagger_client.ProjectApi(swagger_client.ApiClient(config))
    body = swagger_client.POSTProject(name=project_name,
                                      repository_url=repository_url)
    try:
        project_api_instance.create_project(body=body)
        response_data = project_api_instance.api_client.last_response.data
        json_data = json.loads(response_data)
        if 'uuid' in json_data:
            if verbose:
                print(f'''Created project: {json_data}''')
            return json_data['uuid']
    except ApiException as e:
        print("Exception when calling ProjectAPI->create_project: %s\n" % e)


def create_test_artifact(config: Configuration, project_uuid: str,
                         sut_tosca_path: str, ti_tosca_path: str,
                         sut_inputs_path: str = '', ti_inputs_path: str = '') -> str:
    test_artifact_api_instance = swagger_client.TestArtifactApi(swagger_client.ApiClient(config))
    body = swagger_client.POSTTestArtifact(project_uuid=project_uuid,
                                           sut_tosca_path=sut_tosca_path,
                                           sut_inputs_path=sut_inputs_path,
                                           ti_tosca_path=ti_tosca_path,
                                           ti_inputs_path=ti_inputs_path)
    try:
        test_artifact_api_instance.create_testartifact(body=body)
        response_data = test_artifact_api_instance.api_client.last_response.data
        json_data = json.loads(response_data)
        if 'uuid' in json_data[0]:
            if verbose:
                print(f'''Created test artifact: {json_data[0]}''')
            return json_data[0]['uuid']
    except ApiException as e:
        print("Exception when calling TestArtifactAPI->create_test_artifact: %s\n" % e)


def create_deployment(config: Configuration, test_artifact_uuid: str) -> str:
    deployment_api_instance = swagger_client.DeploymentApi(swagger_client.ApiClient(config))
    body = swagger_client.POSTDeployment(testartifact_uuid=test_artifact_uuid)
    try:
        deployment_api_instance.create_deployment(body=body)
        response_data = deployment_api_instance.api_client.last_response.data
        json_data = json.loads(response_data)
        pprint(json_data)
        if 'uuid' in json_data:
            if verbose:
                print(f'''Created deployment: {json_data}''')
            return json_data['uuid']
    except ApiException as e:
        print("Exception when calling DeploymentAPI->create_deployment: %s\n" % e)


def create_execution(config: Configuration, deployment_uuid: str) -> str:
    execution_api_instance = swagger_client.ExecutionApi(swagger_client.ApiClient(config))
    body = swagger_client.POSTExecution(deployment_uuid=deployment_uuid)
    try:
        execution_api_instance.create_execution(body=body)
        response_data = execution_api_instance.api_client.last_response.data
        json_data = json.loads(response_data)
        pprint(json_data)
        if 'uuid' in json_data:
            if verbose:
                print(f'''Created execution: {json_data}''')
            return json_data['uuid']
    except ApiException as e:
        print("Exception when calling ExecutionAPI->create_execution: %s\n" % e)


def create_result(conf: Configuration, execution_uuid: str) -> str:
    result_api_instance = swagger_client.ResultApi(swagger_client.ApiClient(conf))
    body = swagger_client.POSTResult(execution_uuid=execution_uuid)
    try:
        result_api_instance.create_result(body=body)
        response_data = result_api_instance.api_client.last_response.data
        json_data = json.loads(response_data)
        pprint(json_data)
        if 'uuid' in json_data:
            if verbose:
                print(f'''Created result: {json_data}''')
            return json_data['uuid']
    except ApiException as e:
        print("Exception when calling ResultAPI->create_result: %s\n" % e)


def download_result(conf: Configuration, result_uuid: str, result_destination_path: str):
    import urllib.request
    url = f'''{conf.host}/result/{result_uuid}/download'''
    urllib.request.urlretrieve(url, result_destination_path)
    if verbose:
        print(f'''Downloaded results to: {result_destination_path}''')


def main(argv):

    usage: str = '''ctt-cli.py [PARAMS]
    Mandatory parameters:
        -u, --url=CTT_SERVER_URL    URL of the CTT server (e.g., http://localhost:18080/RadonCTT)
        -c, --config=CTT_CONFIG     Path to the CTT configuration file
        
    Other parameters:    
        -v, --verbose               Be verbose
        -h, --help                  Print this help
    '''

    global cli_configuration
    global verbose
    config_file = ''
    try:
        opts, args = getopt.getopt(argv, 'u:c:vh', ['url=', 'config=', 'verbose', 'help'])
        for option, argument in opts:
            if option in ('-u', '--url'):
                cli_configuration.host = argument
            elif option in ('-c', '--config'):
                config_file = argument
            elif option in ('-v', '--verbose'):
                verbose = True
            elif option in ('-h', '--help'):
                print(usage)
                sys.exit()
            else:
                raise SystemExit(usage)
    except ValueError:
        raise SystemExit(usage)

    read_config(config_file)
    project_uuid = create_project(cli_configuration, ctt_conf['name'], ctt_conf['repository_url'])
    test_artifact_uuid = create_test_artifact(cli_configuration, project_uuid,
                                              ctt_conf['sut_tosca_path'], ctt_conf['ti_tosca_path'],
                                              ctt_conf.get('sut_inputs_path'), ctt_conf.get('ti_inputs_path'))
    deployment_uuid = create_deployment(cli_configuration, test_artifact_uuid)
    execution_uuid = create_execution(cli_configuration, deployment_uuid)
    result_uuid = create_result(cli_configuration, execution_uuid)
    download_result(cli_configuration, result_uuid, ctt_conf.get('result_destination_path'))


if __name__ == "__main__":
    main(sys.argv[1:])
