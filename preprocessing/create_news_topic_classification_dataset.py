# -*- coding: utf-8 -*-
import json
import os
from collections import OrderedDict

def data_to_json(data):
    file_data=OrderedDict()
    file_data['chars']=list(data)
    print(json.dumps(file_data,ensure_ascii=False))
    with open('rr.json','w',encoding='utf-8') as make_file:
        json.dump(file_data,make_file,ensure_ascii=False)

def get_every_filename():
    filenames=[]

    for i in range(1,10):
        filenames.append('NIRW190000000'+str(i))
    for i in range(10,31):
        filenames.append('NIRW19000000'+str(i))
    
    for i in range(1,10):
        filenames.append('NLRW190000000'+str(i))
    for i in range(10,100):
        filenames.append('NLRW19000000'+str(i))
    for i in range(100,162):
        filenames.append('NLRW1900000'+str(i))

    for i in range(1,10):
        filenames.append('NPRW190000000'+str(i))
    for i in range(10,71):
        filenames.append('NPRW19000000'+str(i))

    for i in range(1,10):
        filenames.append('NWRW190000000'+str(i))
    for i in range(10,61):
        filenames.append('NWRW19000000'+str(i))

    filenames.append('NZRW1900000001')
    return filenames

#################---MAIN---###################
if __name__=="__main__":
    topic={
        '정치':'politic',
        '경제':'economy',
        '사회':'social',
        '생활':'life',
        'IT/과학':'ITscience',
        '연예':'entertainment',
        '스포츠':'sport',
        '문화':'culture',
        '미용/건강':'health'
    }

    filenames=get_every_filename()
    idx=0


    for filename in filenames:
        print('now '+filename+' is running...')

        with open('./'+filename+'.json', 'r',encoding="utf-8") as f:
            json_data = json.load(f)
        for news_idx in range(len(json_data['document'])):
            #News Identification
            news_data=json_data['document'][news_idx]
            id=news_data['id'].replace('.','_')
            topic_eng=topic[news_data['metadata']['topic']]
            content=''
            for line in news_data['paragraph']:
                content+=( line['form'] + '\n' )
            print('id: ',id)
            print('topic: ',topic_eng)
            print('content: ',content)

            output_path='./data/'+topic_eng+'/'+id+'.txt'
            with open(output_path,'w',encoding='UTF-8') as file:
                file.write(content)






        
