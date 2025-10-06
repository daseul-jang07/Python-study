python = "Python is Amazing"
print(python.lower()) # 모든 문자를 소문자로 출력
print(python.upper()) # 모든 문자를 대문자로 출력
print(python[0].isupper()) # 원하는 자리의 알파벳이 대문자인지 확인
print(python[0].islower())
print(len(python)) # 길이
print(python.replace("Python", "Java")) # 원하는 단어를 찾은 다음 다른 단어로 바꾸기

index = python.index("n") # 글자 위치 확인
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # find -> 문자가 없어도 다음 단계 진행
# print(python.index("Java")) # index -> 문자가 없으면 오류 -> 종료
print("hi")

print(python.count("n")) # 등장 횟수