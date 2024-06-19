
def seperate_input(input: str) -> dict:

    data_list = []
    data_list = input.split('\\')

    data_list[0] = data_list[0].removeprefix('2124/')
    data_list[1] = data_list[1].removeprefix('F240')
    data_list[2] = data_list[2].removeprefix('F400')
    data_list[3] = data_list[3].removeprefix('F7240')

    output_dict = {'serialnumber':data_list[0],'articlenumber':data_list[1],'ordernumber':data_list[2],'certificat':data_list[3]}
    
    return output_dict
    # print('')
    # print(output_dict)

def search_file(directory:str, file) -> str:

    ...


if __name__ == '__main__':
    seperate_input('2124/109314\F240123456789\F40047110815\F724032188')