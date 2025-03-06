files = ["연습장/input.txt", "연습장/output.txt", "연습장/출력예시.txt", "연습장/test.py"]

for file in files:
    with open(file, "w") as f:
        pass  # 빈 파일로 만들기

print("파일 초기화 완료!")
