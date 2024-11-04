# 필요한 라이브러리 설치
!pip install konlpy
!apt-get install -y openjdk-11-jdk

import re
from gensim.models import Word2Vec
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google.colab import files
import requests

# 파일 업로드 시도
uploaded = files.upload()

if uploaded:
    # 사용자가 파일을 업로드한 경우
    file_path = list(uploaded.keys())[0]  # 업로드된 파일의 경로 사용
    print(f"사용자가 업로드한 파일 '{file_path}'로 유사성 분석을 시작합니다.")
else:
    # 업로드가 취소된 경우 GitHub에서 파일 다운로드
    github_url = "https://raw.githubusercontent.com/Sim-JaeIk/cosine_similarity/main/train_data.txt"
    file_path = "train_data.txt"
    
    # GitHub에서 파일 다운로드
    response = requests.get(github_url)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"'{file_path}' 파일을 GitHub에서 다운로드했습니다.")
    else:
        print("GitHub에서 파일을 다운로드할 수 없습니다. 링크를 확인해주세요.")
        raise FileNotFoundError("train_data.txt 파일이 없습니다.")

# 파일 내용 읽기
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 작은 따옴표 안에 있는 문장 또는 작은 따옴표 안에 온점으로 끝나는 문장 추출
sents = re.findall(r"'([^']+?[\.\!\?]?)'", text)

# 추출한 문장들을 word2vec.txt 파일에 저장
with open("word2vec.txt", "w", encoding="utf-8") as f:
    for sent in sents:
        clean_sent = sent.strip()
        if clean_sent:
            f.write(clean_sent + "\n")

print("모든 문장 추출 및 word2vec.txt 파일에 저장 완료")

# 형태소 분석기
tokenizer = Okt()

# word2vec.txt 파일에서 문장 불러오기
with open("word2vec.txt", "r", encoding="utf-8") as f:
    sents = f.readlines()

# 각 문장에 대해 모든 명사 추출 및 토큰화
tokens = []
for sent in sents:
    words = tokenizer.pos(sent, stem=True)  # 어간 추출 적용
    # 명사 태그(Noun)만 추출
    nouns = [word for word, tag in words if tag == 'Noun']
    if nouns:
        tokens.append(" ".join(nouns))  # TF-IDF를 위해 공백 기준으로 단어 구분

# Word2Vec 모델 학습
w2v = Word2Vec(sentences=[tok.split() for tok in tokens], vector_size=100, window=5, min_count=1, sg=0)

# TF-IDF 행렬 생성
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(tokens)

# 코사인 유사도 계산
cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# 유사도 결과 출력 (소수점 둘째 자리까지 반올림하여 [<벡터 값>] 형식으로 출력)
formatted_cos_sim = [[f"[<{sim:.2f}>]" for sim in row] for row in cos_sim]

for row in formatted_cos_sim:
    print(" ".join(row))
