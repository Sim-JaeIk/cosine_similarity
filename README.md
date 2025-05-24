# 🤖 Korean NLP Demo for AI Education

![Python](https://img.shields.io/badge/python-3.8+-blue?logo=python)
![Colab Compatible](https://img.shields.io/badge/Run%20on-Google%20Colab-orange?logo=googlecolab)
![NLP Task](https://img.shields.io/badge/task-NLP--Education-lightgrey)
![Korean NLP](https://img.shields.io/badge/lang-Korean-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/project-Demo%20Ready-yellowgreen)


## 🤖 Korean NLP Demo for AI Education

**한국어 자연어 처리 기반 문장 유사도 분석 데모 (AI 교육용)**

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Google Colab](https://img.shields.io/badge/runs-on-Colab-yellow)
![NLP](https://img.shields.io/badge/NLP-교육용_데모-lightgrey)

> 이 프로젝트는 **AI 교육용 데모**로 제작된 프로그램으로, 한국어 텍스트 데이터에서 문장을 추출하고, \*\*자연어 처리 전처리 과정(TFIDF, Word2Vec)\*\*과 \*\*문장 유사도 계산(Cosine Similarity)\*\*을 직접 체험할 수 있도록 구성되었습니다.

---

### 🧠 이 데모의 목적

* **자연어 처리의 기초 흐름**을 실습 중심으로 이해합니다.
* 텍스트 전처리 → 형태소 분석 → 벡터화 → 유사도 계산의 전체 흐름을 경험합니다.
* **TF-IDF와 Word2Vec의 차이점과 사용 목적**을 실제 데이터를 통해 학습합니다.
* 한국어 문장 처리를 위한 라이브러리 사용법을 익힙니다 (`KoNLPy`, `gensim`, `sklearn` 등).

---

### 📂 입력 파일 형식 예시 (`train_data.txt`)

```python
[history 2] = [
  ('수학은 영어와 친구다', '수학과 영어는 서로 도와주는 과목이지! 재미있어 보인다!'),
  ('수학은 과학의 도구 학문이다', '맞아! 수학은 과학을 이해하는데 중요한 도구야! 멋진 말이야!'),
  ('과학은 체육을 발전시키고 있어', '정확해! 과학이 체육 기술과 훈련을 발전시켜! 흥미로운 연결이네!')
]
```

* 작은 따옴표 `'` 안의 문장을 추출해 분석 대상으로 사용합니다.

---

### 🧪 실행 흐름 요약

| 단계             | 설명                                      |
| -------------- | --------------------------------------- |
| 📤 파일 업로드      | 사용자가 `.txt` 파일을 업로드하거나 GitHub에서 자동 다운로드 |
| 🧾 문장 추출       | 정규표현식으로 작은 따옴표 안 문장만 필터링                |
| 🪄 형태소 분석      | `Okt` 분석기로 명사만 추출 (TF-IDF에 적합한 토큰 생성)   |
| 📊 TF-IDF 변환   | 명사 기반 문장을 벡터로 전환                        |
| 🔍 코사인 유사도 계산  | 각 문장 간 의미적 유사도를 수치로 확인                  |
| 🧬 Word2Vec 학습 | 명사 기반 단어 임베딩 생성 (추후 활용 가능)              |

---

### 🎯 출력 예시

```text
[<1.00>] [<0.35>] [<0.42>]
[<0.35>] [<1.00>] [<0.29>]
[<0.42>] [<0.29>] [<1.00>]
```

* `[<유사도>]` 형태로 문장 간의 유사도가 행렬로 표시됩니다.
* 유사도가 1.00에 가까울수록 내용이 유사한 문장입니다.

---

### ⚙️ 실행 환경 (Google Colab 기준)

```python
!pip install konlpy
!apt-get install -y openjdk-11-jdk
```

* `KoNLPy`, `gensim`, `scikit-learn`, `re`, `requests` 사용
* `Google Colab`에서 바로 실행 가능
