#!/usr/bin/env python3

def print_square(x):
	print(x*x)

print(print_square(3))


#3~4번째 줄은 함수에 대한 정의이므로 넘어갑니다.
#6번째 줄이 실행됩니다. print(print_square(3)) 내부에 있는 print_square(3)이 실행됩니다.
#3번째 줄의 함수가 불려지고, 파라미터 x가 3으로 대체됩니다.
#4번째 줄이 실행됩니다. print(3 * 3)이므로, 9가 출력됩니다.
#6번째 줄로 다시 돌아옵니다. print(함수) 꼴이므로, 함수의 리턴값이 함수 부분에 대체되어야 합니다.
#print_square 함수는 리턴값이 없으므로, None이 리턴됩니다.
#print(print_square(3))의 print_square(3) 부분이 None으로 대체되어, print(None)과 동일해져 None이 출력됩니다.
