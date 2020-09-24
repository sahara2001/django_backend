import requests
import json

def test_get_answer1():
    data={"questionCode": "1","answerText": "yes"}
    r = requests.get("http://127.0.0.1:8000/api/get_question/", data=data)
    # 
    print(json.loads(r.text)['questionString'])

def test_get_movies1():
    data={"questionCode": "1","answerText": "yes"}
    r = requests.get("http://127.0.0.1:8000/api/get_movies/", data=data)
    # 
    print(json.loads(r.text)['movieList'])

def test_post1():
    data={"questionCode": "1","answerText": "yes"}
    r = requests.post("http://127.0.0.1:8000/api/post_answer/", data=data)
    # 
    print(json.loads(r.text)['nextQuestionString'])
    


if __name__ == '__main__':
    test_get_movies1()
    test_get_answer1()
    test_post1()