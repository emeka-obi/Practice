 

test_dict ={'fwbilly5@blinkfw.com': [{'err': 6, 'tot': 1121}, {'liveview': 1, 'clip': 1, 'status_bw': 1, 'sm_table_update(delete)': 1, 'fw_update(sm)': 1, 'config_set(update)': 1}]}
def total_function(test_dict:dict) -> int:   
    for i in test_dict:
        first_key = i
        for j in range(len(test_dict[i])-1):
            for k in test_dict[first_key][j]:
                total = test_dict[first_key][j].get('tot')
    return total


def update(test_dict:dict):
    total = total_function(test_dict)
    for i in test_dict:
        first_key = i
        for j in range(1, len(test_dict[i])):
            for k in test_dict[first_key][j]:
                change_to = round((100 * test_dict[first_key][j][k])/total, 2)
                test_dict[first_key][j][k] = change_to
    
    return test_dict
    

               
                


if __name__ == "__main__":
    print(update(test_dict))

            
       
       
        
        
    