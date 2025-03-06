files = ["input.txt", "output.txt", "출력예시.txt", "test.py"]

for file in files:
    with open(file, "w") as f:
        pass  # 빈 파일로 만들기

print("파일 초기화 완료!")
