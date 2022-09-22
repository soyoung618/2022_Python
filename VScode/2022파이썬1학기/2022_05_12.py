    # [:]를 이용한 얕은 복사
import copy  # copy 모듈 불러오기
import copy
import imp
from pkgutil import extend_path
print('#'*50)
arr1 = [4, 5, 6, [2, 4, 8, ]]
arr2 = arr1[:]  # 여기에 복사
print("1. 전체 복사")
print(f"arr1 : {arr1} , add : {hex(id(arr1))}")
print(f"arr2 : {arr2} , add : {hex(id(arr2))}")

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)
print('arr2.append(22)')
print(f"arr1 : {arr1} , add : {hex(id(arr1))}")
print(f"arr2 : {arr2} , add : {hex(id(arr2))}")

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f"arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}")

print("\n4. 리스트 내부 리스트")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f"arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}")

print("\n5. 리스트 전체 다시 확인")
print(f"arr1 : {arr1} , add : {hex(id(arr1))}")
print(f"arr2 : {arr2} , add : {hex(id(arr2))}")

# copy 메서드를 이용한 얕은 복사
print('a'*100)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1.copy()  # 여기서 복사 copy 메서드 사용
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')
print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2에 값 추가
print('arr2.append(22)')
print(f"arr1 : {arr1} , add : {hex(id(arr1))}")
print(f"arr2 : {arr2} , add : {hex(id(arr2))}")
# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f"arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}")
print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f"arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}")
print("\n5. 리스트 전체 다시 확인")
print(f"arr1 : {arr1} , add : {hex(id(arr1))}")
print(f"arr2 : {arr2} , add : {hex(id(arr2))}")


# copy 모듈의 copy 함수를 이용한 얕은 복사
print("import copy")
print('a'*100)
arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = copy.copy(arr1)  # 여기서 복사 copy 메서드 사용
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')
print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2에 값 추가
print('arr2.append(22)')
print(f"arr1 : {arr1} , add : {hex(id(arr1))}")
print(f"arr2 : {arr2} , add : {hex(id(arr2))}")
# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f"arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}")
print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f"arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}")
print(f"arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}")
print("\n5. 리스트 전체 다시 확인")
print(f"arr1 : {arr1} , add : {hex(id(arr1))}")
print(f"arr2 : {arr2} , add : {hex(id(arr2))}")
# 얕은복사
# 1.=주소동일
# 2. [:] 주소 다름. 내부 주소 동일
#3. .copy
# 4.copy.copy(주소)

# copy 모듈의 copy 함수를 이용한 얕은 복사 (dictionnary)
print('a'*50)
d1 = {'a': 'Mirim',  'b': [1, 2, 3]}
d2 = copy.copy(d1)  # copy 모듈 얕은 복사
print("1. 전체 출력")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')
print("\n2. 딕셔너리에 새 key,value 추가")
d2['c'] = 'kimchi'
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')

# 딕셔너리 내부에 리스트 value
print("\n3. 딕셔너리 내부 리스트")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n4. 딕셔너리 내부 리스트에 갑 추가")
d1['b'].append('No')
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n5. 딕셔너리 전체 다시 확인")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')

# 깊은 복사 copy.deepcopy
print('a'*50)
arr1 = [1, 2, [99, 88, 77], 3]
arr2 = copy.deepcopy(arr1)  # copy 모듈 깊은 복사
print("1. 전체 출력")
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')
print("\n2. 딕셔너리에 새 key,value 추가")
arr1.append(0)
print('arr1.append(0)')
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')
print("\n3. 리스트 내부 리스트")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}")
print("\n4. 리스트 내부 리스트에 값 추가")
arr1[2].append(10)
print("arr1[2].append(10)")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}")
print("\n5. 리스트 전체 다시 확인")
print(f"arr1 : {arr1} , address : {hex(id(arr1))}")
print(f"arr2 : {arr2} , address : {hex(id(arr2))}")


# 문자열
# 홍길동 씨의 주민번호는 881120-1069234이다. 주민등록 번호를 연원일부분과 뒤의 숫자 부분으로 나누어 출력해보자.
a = "881120-1069234"
print("연월일 :", a[0:6])
print("숫자 :", a[7:14])

# 주민등록번호 뒷자리의 맨 첫번째 숫자는 성별을 타나낸다. 홍길동씨의 주민등록번호에서 성별을 나타내는 숫자를 출력해보자
a = "881120-1069234"
print("성별:", a[7])

# 리스트1
# [1,3,5,4,2]라는 리스트를 [5,4,3,2,1]로 만들어보자
l = [1, 3, 5, 4, 2]
print("원본:", l)
l.sort()
l.reverse()
print("결과:", l)
# 'Life', 'is', 'too', 'short' 를 Lifeistooshort 로 만들시오
l = ['Life', 'is', 'too', 'short']
for i in l:
    print(i, end="")
print()
# (1,2,3)이라는 튜플에 4라는 값으 ㄹ추가하여 1,2,3,4처럼 만들어 출력
t = (1, 2, 3)
t += (4, )
print(t)

# 디셔너리 a에서 'B'에 해당되는 값을 추출하고 삭제해보자
a = {'A': 90, 'B': 80, 'C': 70}
print("원본 딕셔너리:", a)
b = a.pop('B')
print("'B' 추출 후 딕셔너리:", a)
print("추출된 B의 값:", b)
