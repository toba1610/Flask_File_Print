import json

def read_JSON_Data(file, topic, parameter=None):

    with open(file, encoding='utf-8') as config:                  
        config_data = json.load(config)         

    data_type = type(config_data)

    if data_type == dict:

        data_type = type(config_data[topic])

        if data_type == dict:

            data = config_data[topic]

            return data[parameter]               
        
        elif data_type == list:

            return config_data[topic]

def read_JSON_Topic(file, topic):

    with open(file, encoding='utf-8') as config:                  
        config_data = json.load(config)         

    return config_data[topic]                   

def save_JSON_Data(file, topic, parameter, value):

    with open(file, encoding='utf-8') as target:                      
        target_data = json.load(target)             

    target_data[topic][parameter] = value

    with open(file, encoding='utf-8', mode= 'w') as config:                 
        json.dump(target_data, config, indent=2, ensure_ascii=False)    

def create_new_json_entry(file, Result_Type, result):
    
    with open(file, encoding='utf-8') as target:                      
        target_data = json.load(target)             
    
    target_data[Result_Type].append(result)         
   
    with open(file, encoding='utf-8', moder= 'w') as config:                 
        json.dump(target_data, config, indent=2, ensure_ascii=False)


 