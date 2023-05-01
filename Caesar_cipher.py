# Caesar_chipher

alp_list = []

# 0~25 : a~z
for i in range(97, 123):
    alp_list.append(chr(i))

cipher_list = []

for i in range(26):
    if i < 23:
        cipher_list.append(alp_list[i + 3])
    elif i >= 23:
        cipher_list.append(alp_list[i - 23])

# 문자 입력
a = input('문자 입력')

# 함수
new_list = []
index_list = []
collect_list = []


for i in range(len(a)):
    # 문자열 리스트만들기
    new_list = list(a)
    
    #알파벳 별 인덱스 구하기
    index_list.append(alp_list.index(new_list[i]))
    
    #암호화 리스트에 넣기
    collect_list.append(cipher_list[index_list[i]])
    
    
collect = ''.join(collect_list)
print(collect)
