# PG#42746 - 가장 큰 수

## 느낀점
* 

## input
```
numbers
[6,10,2]
```

## output
```
저 세개를 이어붙여서 만들 수 있는 가장 큰 수
"6210"
```

## notes
* 문자열로 리턴
* 1000 이하의 상황.

## strategy
* 방법 1 : 단순 줄세우기 후 가장 큰 값 리턴
* 방법 2 : 각 숫자 자릿수를 모두 맞추면(10을 곱해서), 큰걸수록 앞에 가는 게 좋을것.
  * 다만 9랑 90이 있다고 하면, 9가 훨씬 유리함.
  * 그렇다면 앞에 가야 하는 순위는
    * 앞숫자가 커야함
    * 앞숫자가 같은 경우, 더 적은 자릿수가 유리함
    * 그다음 숫자가 커야함
    * 그 다음 숫자가 같은 경우, 더 적은 자릿수가 유리함
    * ...
  * 6, 10, 2, 1, 50, 5 -> (6000, -1), (1000, -2), (2000, -1), (1000, -1), (5000, -2), (5000, -1)
  * 자릿수 n이면 point 2n-1개 달림.
* 자릿수 시바