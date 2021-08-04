from __future__ import print_function

import getopt
import json
import os
import requests

import swagger_client
import sys
import yaml

from swagger_client.rest import ApiException
from pprint import pprint
from swagger_client.configuration import Configuration

cli_configuration = Configuration()
verbose: bool = False
MANDATORY_FIELDS = ['name', 'repository_url', 'sut_tosca_path', 'ti_tosca_path',
                    'result_destination_path', 'test_id']
api_client = swagger_client.ApiClient(cli_configuration)


def config_is_multi(config_yaml) -> bool:
    if 'test_id' in config_yaml:
        return False
    else:
        return True


def config_is_valid(config_yaml) -> bool:
    for field in MANDATORY_FIELDS:
        found: bool = False
        for entry in config_yaml:
            if field == entry:
                found = True
                break
        if not found:
            error_msg = f'''Mandatory field {field} is not set in configuration file.'''
            raise ValueError(error_msg)
    return True


def read_config(config_path: str):
    ctt_conf = {}
    if os.path.isfile(config_path):
        with open(config_path, 'r') as config_file:
            config_yaml = yaml.safe_load(config_file)
            if config_is_multi(config_yaml):
                for entity in config_yaml:
                    if config_is_valid(entity):
                        ctt_conf[entity['test_id']] = entity
            elif config_is_valid(config_yaml):
                ctt_conf[config_yaml['test_id']] = config_yaml

            # for field in MANDATORY_FIELDS:
            #     found: bool = False
            #     for entry in ctt_conf:
            #         if field == entry:
            #             found = True
            #             break
            #     if not found:
            #         error_msg = f'''Mandatory field {field} is not set in configuration file.'''
            #         raise ValueError(error_msg)
            if verbose:
                print(f'Successfully read configuration file:')
                pprint(config_yaml)
    return ctt_conf


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


def trigger_workflow(conf: Configuration, config_file):
    url = f'''{conf.host}/workflow'''
    data = {'workflow_data': open(config_file, 'rb').read()}
    headers = {'Content-Type': 'application/octet-stream', 'accept': '*/*'}
    response = requests.post(url=url, data=data, headers=headers)
    json_data = response.json()
    if 'logs' in json_data and 'results' in json_data:
        return json_data['logs'], json_data['results']
    else:
        return None


def main(argv):
    usage: str = '''ctt-cli.py [PARAMS]
    Mandatory parameters:
        -u, --url=CTT_SERVER_URL    URL of the CTT server (e.g., http://localhost:18080/RadonCTT)
        -c, --config=CTT_CONFIG     Path to the CTT configuration file
        
    Other parameters:    
        -r, --remote                Run (multiple) configurations remotely
        -v, --verbose               Be verbose
        -h, --help                  Print this help
    '''

    global cli_configuration
    global verbose
    remote: bool = False
    config_file = ''
    try:
        opts, args = getopt.getopt(argv, 'u:c:vhr', ['url=', 'config=', 'verbose', 'help', 'remote'])
        for option, argument in opts:
            if option in ('-u', '--url'):
                cli_configuration.host = argument
            elif option in ('-c', '--config'):
                config_file = argument
            elif option in ('-v', '--verbose'):
                verbose = True
            elif option in ('-r', '--remote'):
                remote = True
            elif option in ('-h', '--help'):
                print(usage)
                sys.exit()
            else:
                raise SystemExit(usage)
        if not cli_configuration.host or not config_file:
            raise SystemExit(usage)

    except ValueError:
        raise SystemExit(usage)

    ctt_conf = read_config(config_file)

    if remote:
        logs, results = trigger_workflow(cli_configuration, config_file)
        for key in ctt_conf.keys():
            results_uuid = results[key]
            results_destination = ctt_conf[key]['result_destination_path']
            cur_logs = logs[key]
            print(f'''{key}: {results_uuid} -> {results_destination} {cur_logs}''')
            download_result(cli_configuration, results_uuid, results_destination)
    else:
        # read_config(config_file)
        for entry in ctt_conf:
            config_entry = ctt_conf[entry]
            project_uuid = create_project(cli_configuration, config_entry['name'], config_entry['repository_url'])
            test_artifact_uuid = create_test_artifact(cli_configuration, project_uuid,
                                                      config_entry['sut_tosca_path'],
                                                      config_entry['ti_tosca_path'],
                                                      config_entry.get('sut_inputs_path'),
                                                      config_entry.get('ti_inputs_path'))
            deployment_uuid = create_deployment(cli_configuration, test_artifact_uuid)
            execution_uuid = create_execution(cli_configuration, deployment_uuid)
            result_uuid = create_result(cli_configuration, execution_uuid)
            download_result(cli_configuration, result_uuid, config_entry.get('result_destination_path'))


if __name__ == "__main__":
    main(sys.argv[1:])
