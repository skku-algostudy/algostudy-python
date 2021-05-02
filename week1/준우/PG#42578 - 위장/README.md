# PG#42578 - 위장

## 느낀점


## notes
* 스파이는 매일 다른 조합의 옷을 입음.
* 하루에 최소 한 개의 의상은 입는다고 함.
* ['의상이름', '종류']
* 같은 이름의 의상은 존재하지 않음 -> 의상이름은 관심없고 숫자로 가자.

## input
```
clothes : [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
```

## output
```
5
```

## strategy
* 각 의상종류수 + 1을 싹 곱한다음에
* 아무것도 안입는 경우 빼주면 될듯
* 딕셔너리 사용
