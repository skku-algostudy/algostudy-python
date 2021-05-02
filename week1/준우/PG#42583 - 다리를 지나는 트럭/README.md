# PG#42583 - 다리를 지나는 트럭

## 느낀점
* 무한루프 돌아서 뭔가 하고 봤는데, 무게가같은트럭이 있다는 것을 간과함.
* enumerate로 해결
* 이 문제는 함 다시 풀어보자.

## notes
* asdf

## input
```
bride_length: 2
weight: 10
truck_weights: [7,4,5,6]
```

## output
```
8
```

## strategy
* truck_weights는 큐를 쓰자. while q로 돌리면 됨.
* truck_time_dict는 딕셔너리이되, time을 1씩 쭉 늘려주자
  * time이 bride_length가 되면 팝
* 
