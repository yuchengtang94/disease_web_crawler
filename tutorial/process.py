import json

files = ['rare_disease.json', 'disease.json']
# files = ['rare_disease.json']
# files = ['disease.json']
dict = {}
i = 0;
for file_str in files:

    file = open(file_str, encoding='utf-8').read()
    json_data = json.loads(file)
    #
    #
    for data in json_data:
        # if data.strip() != '\n':
        i = i + 1
        dict[str(i)] = data

    # dict = json_data
        # print('***** '+ str(i) + ' *******')
json_file_result = open('Final_disease.json', 'w+', encoding='utf-8')
json.dump(dict, json_file_result, indent=4, separators=(',', ': '))
json_file_result.close()