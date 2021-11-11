# newsTopicClassification  
  
한글뉴스기사 주제분류AI  
국립국어원 신문 말뭉치(Ver.2) sampling Dataset를 이용    
skt AI KoGPT2 fine-tuning 사용    
뉴스 내용을 보고 토픽을 예측    
  
  
### Data  
국립국어원 신문 말뭉치(Ver.2) sampling Dataset  
- Label  
    - 0: ITscience  
    - 1: culture  
    - 2: economy  
    - 3: entertainment  
    - 4: health  
    - 5: life  
    - 6: politic  
    - 7: social  
    - 8: sport  
- train  
    각 라벨별로 500개의 뉴스 문장+내용  
- test  
    각 라벨별로 50개의 뉴스 문장+내용  
 ### Model  
 SKT에서 만든 KoGPT2모델을 fine-tuning  
 - 선정이유  
    - 대용량 한글 데이터 학습 모델  
    한국어 위키 백과, 뉴스, 모두의 말뭉치 v1, 청와대 국민청원 학습  
    - 최신 모델  
        GPT2 발매년도: 2019  
        KoGPT2 발매년도: 2021.5
 - GPT2  
    적은 모델 파라미터로 높은 성능을 내는 자연어처리 특화 모델  
    ![](https://github.com/seawavve/newsTopicClassification/blob/main/img/gpt2_compute_graph.jpg)  
 - KoGPT2  
    SKT에서 제공하는 대용량 한글 데이터셋 학습 GPT2 모델  
    한국어 위키 백과, 뉴스, 모두의 말뭉치 V1, 청와대 국민청원 학습  
 ### Result  
 - classification report  
 ![](https://github.com/seawavve/newsTopicClassification/blob/main/img/classification_report.jpg)  
 - confusion matrix  
 ![](https://github.com/seawavve/newsTopicClassification/blob/main/img/confusion_matrix.jpg)  
life,  social, culture가 서로 혼동  
라벨을 통합하거나 데이터를 더 늘린다면 개선 가능  
### Feedback  
- 한자, 특수문자를 제거  
- sampling data ⇒ full data  
  
### 참고자료  
- SKT KoGPT2 repository  
[https://github.com/SKT-AI/KoGPT2](https://github.com/SKT-AI/KoGPT2)  
- GPT2 Visualization  
[https://jalammar.github.io/illustrated-gpt2/](https://jalammar.github.io/illustrated-gpt2/)  
