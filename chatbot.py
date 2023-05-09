import urllib3, json
from konlpy.tag import Okt

openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
accessKey = "your key"

src = open('info.txt', 'r', encoding='utf-8').readlines()
passage = ''.join(src)
http = urllib3.PoolManager()
okt = Okt()

# def action(q):
#     requestJson = {"argument": { "question": q, "passage": passage }}
#     response = http.request("POST", openApiURL, headers={"Content-Type": "application/json; charset=UTF-8","Authorization": accessKey}, body=json.dumps(requestJson))
#     response = json.loads(str(response.data,"utf-8"))

#     print(response)

#     answer = response['return_object']['MRCInfo']['answer']
#     print('변경전:', answer)

#     if '[END]' in answer:
#         answer = answer[:answer.index('[END]')]

#     answer = passage[passage.index(answer): passage.index('[END]', passage.index(answer))]
#     print('변경후:', answer)

#     return answer

def action(q):
    q = okt.normalize(q)

    if len(okt.nouns(q)):
        # print(okt.pos(q))
        requestJson = {"argument": { "question": q, "passage": passage }}
        response = http.request("POST", openApiURL, headers={"Content-Type": "application/json; charset=UTF-8","Authorization": accessKey}, body=json.dumps(requestJson))
        response = json.loads(str(response.data,"utf-8"))

        # print(response)

        if float(response['return_object']['MRCInfo']['confidence']) > 0.10:
            answer = response['return_object']['MRCInfo']['answer']
            print('변경전:', answer)

            if '[END]' in answer:
                answer = answer[:answer.index('[END]')]

            answer = passage[passage.index(answer): passage.index('[END]', passage.index(answer))]
            print('변경후:', answer)

            return answer
        
    
    # print(q)
    # end_word = [word for word in q if '가'<=word<='힣'][-1]
    # josa = '이' if (ord(end_word)-ord("가")) % 28 > 0 else ''

    josa = ''
    return '"' + q + '"' + josa + '라는 문장은 아직 제대로 이해하지 못했습니다. 이 사항은 챗봇 응답에 추가될 예정입니다.'
