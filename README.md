수리논리학
==========
## 개요
논리학은 AI의 핵심.
논리학은 프로그래밍 언어.
2040년에는 Python보다 논리 언어가 더 유행할 것이다.

## 지식의 표현법
### Michael Jackson은 키가 180이다.  
~~Michael Jackson은 키가 180~~  
~~The height of Michael Jackson is 180~~  
~~height(Michael Jackson) = 180~~  
__height(Michael Jackson, 180)__   

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
|~coffee          : | 내가 커피를 줄게요.|
  
## 논리적 귀결

```
소크라테스는 사람이다.  
모든 사람은 죽는다. 
-> 소크라테스는 죽는다. 
```

1 p and q => q 
0 p and q => r 
1 p => p or q 
0 p or q => p 
0 p => ~p 
1 (p->q and p) => q 
0 p->q => q->p
1 p => p and p

## 논리학적 승자/패자의 개념

| | 가게에서 커피를 만든 경우 | 가게에서 커피를 만들지 못한 경우 |
| --- | --- | --- |
| Cashier | 승 | 패 |
| Customer  | 패 | 승 |

## 무한 지식의 표현
### 모든 사람은 죽는다.
0 ∀x mortal(x)  
1 ∀x∈사람 mortal(x)  
1 ∀x(사람(x) -> mortal(x))  
∀x P(x) = P(t1)∧P(t2)∧...  
∃x P(x) = P(t1)∨P(t2)∨...  

∀ == All  
∃  == Exist  

- 한국에는 대머리가 있다.
∃x(대머리(x) ∧ Korean(x))

ex)
1 p(a) -> ∃x p(x)
1 소수인 A가 있다 -> 소수인 x가 존재한다.
0 p(a) -> ∀x p(x)
0 소수인 a가 있다 -> 모든 x는 소수이다.
1 ∀ xp(x) -> ∃ xp(x)
1 모든 x가 xp이다 -> xp인 x가 존재한다.

### factorial을 프로그래밍하시오.

[1, 1, 2, 6, 24, 120]
무한 -> 유한하게 압축 ∀x
f(n) = f(n-1) * n
∀x∀y (f(x,y) -> f(x+1, xy+y))
xy+y == y(x + 1)
f(x+1, xy+y) == f(x+1, y(x + 1))

## 질의법

∃x fact(5,x)


##### problem) fibonacci를 프로그래밍하시오
fib(n) == fib(n-1) + fib(n-2)  

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  

∀x∀y∀z (fib(x, y) ∧ fib(x+1, z) -> fib(x + 2, y + z)  
fib(0) == 1  
fib(1) == 1  
fib(10) == 89  

and, or, ~, imply
all, some 

짝수(2) ∧ ∀x 짝수(x) -> 짝수(x+2)
홀수(1) ∧ ∀x 홀수(x) -> 홀수(x+2)
