import json_data_process as jdp
import os

def seperate_input(input: str) -> dict:

    data_list = []
    data_list = input.split('\\')

    data_list[0] = data_list[0].removeprefix('2124/')
    data_list[1] = data_list[1].removeprefix('F240')
    data_list[2] = data_list[2].removeprefix('F400')
    data_list[3] = data_list[3].removeprefix('F7240')

    output_dict = {'serialnumber':data_list[0],'articlenumber':data_list[1],'ordernumber':data_list[2],'certificat':data_list[3]}
    
    return output_dict

def search_file(serialnumber: str, certificate: str) -> str:

    name_scheme = jdp.read_JSON_Data('config.json', 'Parameter', 'Filescheme')
    path_to_certificate = jdp.read_JSON_Data('config.json', 'Parameter', 'Path_to_certificate')
    file_type = jdp.read_JSON_Data('config.json', 'Parameter', 'Filetype')

    name = replace_Config(name_scheme, [serialnumber, certificate])
    name = f'{name}{file_type}'

    file_path = os.path.join(path_to_certificate,name)

    if os.path.exists(file_path):
        return file_path
    else:
        return None

def replace_Config(input: str, new_data: list) -> str:

    parameters = input.count('<')

    for parameter in range(0, parameters):

        index_start = input.find('<')
        index_stop = input.find('>')
        output = input[:index_start] + str(new_data[parameter]) + input[index_stop+1:]
        input = output

    return output

if __name__ == '__main__':
    # seperate_input('2124/109314\F240123456789\F40047110815\F724032188')
    replace_Config("Serienummer_<Serienummer>_Eichschein_<Eichschein>", [1234,5678])
    print(search_file(1234, 5678))