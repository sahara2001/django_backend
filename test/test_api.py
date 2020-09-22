import requests
import json

def test_post1():
    data={"questionCode": "1","answerText": "yes"}
    r = requests.post("http://127.0.0.1:8000/api/post_answer/", data=data)
    # 
    print(json.loads(r.text))
    


if __name__ == '__main__':
    test_post1()