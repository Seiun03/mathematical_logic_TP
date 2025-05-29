import streamlit as st

db_query = "SELECT * FROM"
bool_list = ["log_in"]
infor_list = ["department", "name", "tel"]

def clear_state():
    #ID
    if "id" not in st.session_state:
        st.session_state.id = ""
    #담당부서
    if "department" not in st.session_state:
        st.session_state.department = ""
    #이름
    if "name" not in st.session_state:
        st.session_state.name = ""
    #전화번호
    if "tel" not in st.session_state:
        st.session_state.tel = ""
    #포맷
    if "format" not in st.session_state:
        st.session_state.format = ""
    #일단 LLM 모델
    if "llm_model" not in st.session_state:
        st.session_state.llm_model = "llama3:latest"
    if "main" not in st.session_state:
        st.session_state.main = None
    #폐기 예정 사항
    if "current_dialog" not in st.session_state:
        st.session_state.current_dialog = True
    #로그인 체크
    if "log_in" not in st.session_state:
          st.session_state.log_in = False
    #민원 양식, 최종 민원
    if "answer" not in st.session_state:
          st.session_state.answer = ""
    #민원 양식 선택 함수
    if "answer_format" not in st.session_state:
        st.session_state.answer_format = "None"
    #답변
    if "response" not in st.session_state:
        st.session_state.response = "답변이 생성되지 않았습니다."
    #현재 페이지 위치 체크
    if "page" not in st.session_state:
        st.session_state['page'] = "home"
    #다이얼로그 버그 임시 체크용
    if "dialog" not in st.session_state:
        st.session_state.dialog_check = False
    #데이터프레임 선택
    if "selected_row" not in st.session_state:
        st.session_state.selected_row = None
    if "choice" not in st.session_state:
        st.session_state.choice = "수리논리학"
    
    if "write_mode" not in st.session_state:
        st.session_state.write_mode = True

    if "view_post" not in st.session_state:
        st.session_state['view_post'] = ""

    if "board" not in st.session_state:
        st.session_state['board'] = "글 목록"

if "logical_1" not in st.session_state:

    st.session_state.logical_1 = """
    ## 개요
    > **논리학**은 AI의 핵심.
    > **논리언어**는 프로그래밍 언어.
    > 2040년에는 Python보다 **논리 언어**가 더 유행할 것이다.
    >   
    > *권기항 교수님*

    ## 지식의 표현법
    ### Michael Jackson은 키가 180이다. 
    | 진릿값 | 표현                               | 형식       | 설명                                  |
    | :----: | ---------------------------------- | ---------- | ------------------------------------- |
    |   F    | Michael Jackson은 키가 180         | 자연어     | 문법적으로는 문장이지만 모호함        |
    |   F    | The height of Michael Jackson is 180 | 자연어   | 서술형 문장이지만 논리식은 아님       |
    |   F    | height(Michael Jackson) = 180      | 함수 표현  | 수학적 함수처럼 보이지만 관계가 아님  |
    |   T    | height(Michael Jackson, 180)       | 관계 표현  | 논리적으로 관계가 참(True)임          |

    #### 추가 예제
    - 3 더하기 1은 4이다.  
        plus(3, 1, 4)  
    - A와 B는 친구이다.  
        friend(A, B)  
    
    ## 지식의 Size
    | 지식 | 지식의 Size |
    | :--: | :--: |
    | Michael Jackson은 가수이다. | 1 |
    | Michael Jackson는 가수이고 Prince도 가수이다. | 2 |
    | Michael Jackson은 가수, 또는 조인성은 가수이다. | 2 |
    | 동아대 컴퓨터 공학과에는 대머리가 있다. | 컴퓨터 공학과 소속 인원 수 |

    ## 복잡한 지식의 표현법
    ### and, or, imply, not을 사용
    | 기호/키워드 | 의미         | 기호 표현 |
    |-------------|--------------|-----------|
    | and         | 논리곱       | ∧         |
    | or          | 논리합       | ∨         |
    | not         | 부정         | ¬ 또는 ~  |
    | imply       | 함의         | →         |

    짝수(2) ∧ ∀x 짝수(x) -> 짝수(x+2)
    홀수(1) ∧ ∀x 홀수(x) -> 홀수(x+2)

    - bong is smart and funny  
    funny(bong) and smart(bong)  
    - bong is smart but not funny  
    smart(bong) and ~funny(bong)  
    - bong is smart or married  
    smart(bong) od married(bong)

    - 봉준호는 부자이므로 봉준호는 좋은 집에서 산다.  
    rich(bong) -> nicehouse(bong) `(C의 if문 형태)`  
    - n이 짝수이면 n * n은 짝수이다.  
    even(n) -> even(n * n)  
    - 비가 오면 땅이 젖는다.  
    rain -> wet(ground)
    - 문이 잠겨 있으면 문을 열 수 없다.  
    door locked -> ~open()


    |starbucks :  | |
    | :--- | --- |
    |coffee and cappu : | 둘 다 주세요.|
    |coffee or  cappu : | 적어도 하나는 주세요.|
    |coffee ->  cappu : | 내가 커피를 주면, 카푸치노를 주세요.|
    |~coffee          : | 내가 커피를 줄게요.|"""

if "logical_2" not in st.session_state:
    st.session_state.logical_2 = '''
    ## 논리적 귀결

    ```
    소크라테스는 사람이다.  
    모든 사람은 죽는다. 
    -> 소크라테스는 죽는다. 
    ```

    ### 예제

    | 진릿값 | 명제 |
    | :--: | :--- |
    T | p and q => q 
    F | p and q => r 
    T | p => p or q 
    F | p or q => p 
    F | p => ~p 
    T | (p->q and p) => q 
    F | p->q => q->p
    T | p => p and p

    ## 논리학적 승자/패자의 개념

    | | 가게에서 커피를 만든 경우 | 가게에서 커피를 만들지 못한 경우 |
    | --- | --- | --- |
    | Cashier | 승 | 패 |
    | Customer  | 패 | 승 |
'''
if "logical_3" not in st.session_state:
    st.session_state.logical_3 = '''
    ## 무한 지식의 표현
    #### 기호 ∀과 ∃
    > "and, or, not, imply은 **amateur의 영역**. all, some을 잘 다뤄야 **pro의 영역**으로 갈 수 있다."
    >   
    > *권기항 교수님*

    | 기호 | 의미   | 설명               | 사용 예시                        |
    | :--: | :----: | ------------------ | ------------------------------- |
    | ∀    | 모든   | All, for all       | ∀x ∈ ℝ, x² ≥ 0                  |
    | ∃    | 존재   | Exist, there exists| ∃x ∈ ℝ, x² = 4 (x = ±2 존재함)  |

    ### 예제

    | 진릿값 | 명제                            | 자연어 예시                                 | 해설 |
    |--------|----------------------------------|---------------------------------------------|------|
    | 1      | p(a) → ∃x p(x)                  | 소수인 A가 있다 → 소수인 x가 존재한다       | a가 존재하면 ∃x는 참 |
    | 0      | p(a) → ∀x p(x)                  | 소수인 a가 있다 → 모든 x는 소수이다         | 한 명이 만족해도 전체는 아님 |
    | 1      | ∀x p(x) → ∃x p(x)               | 모든 x가 소수이다 → 소수인 x가 존재한다     | 전칭이면 당연히 존재 |

    ### 모든 사람은 죽는다. 를 명제로 나타내기
    | 진릿값 | 명제 |
    | :--: | :--- |
    F | ∀x mortal(x)  
    T | ∀x∈사람 mortal(x)  
    T | ∀x(사람(x) -> mortal(x))  
    T |∀x P(x) = P(t1)∧P(t2)∧...  
    T |∃x P(x) = P(t1)∨P(t2)∨...  

    ### 추가 예제
    - 한국에는 대머리가 있다.  
    ∃x(대머리(x) ∧ Korean(x))

    ### factorial을 프로그래밍하시오.

    [1, 1, 2, 6, 24, 120]  
    무한 -> 유한하게 압축 $$∀x$$
                    
    $$f(n) = f(n-1) * n$$ 
                    
    $$∀x∀y (f(x,y) → f(x+1, xy+y))$$
                    
    $$xy+y == y(x + 1)$$
                    
    $$f(x+1, xy+y) == f(x+1, y(x + 1))$$

    ### fibonacci를 프로그래밍하시오
    $$fib(n) == fib(n-1) + fib(n-2)$$  

    $$[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]$$  

    $$∀x∀y∀z (fib(x, y) ∧ fib(x+1, z) -> fib(x + 2, y + z)$$  

    $$fib(0) == 1$$  

    $$fib(1) == 1$$  
                    
    $$fib(10) == 89$$  

    ## 질의법

    #### 표현:
    ```
    ∃x fact(5, x)
    ```

    #### 의미 (질의형 논리 관점):
    - "어떤 x가 존재하는가? 그것이 fact(5, x)를 만족하는가?"
    - "5의 팩토리얼을 만족시키는 x는 무엇인가?"
    - 이는 **정보를 구성하는 지식 기반에 질의**하는 방식   
'''



def logout_state():
    st.session_state.log_in = False
    st.session_state.answer = ""
    st.session_state.answer_format = "None"
    st.session_state.departname = ""
    st.session_state.tel = ""
    st.session_state.name =""
    st.session_state.id = ""