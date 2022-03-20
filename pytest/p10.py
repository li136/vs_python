# with open('p10.txt') as file_object:
#     contents =file_object.read()
# qwe=float(contents)
# print(contents)
# print(qwe)

with open('p10.txt') as file_object:
    for p in file_object:
        # rstrip()去回车符号
        print(f"{p.rstrip()}---next")

with open('p10.txt') as file_object:        
    file_p10=file_object.readlines()
    print(file_p10)

# 写文件
with open('p10.txt','w') as file1:
    file1.write("覆盖test\n")

with open('p10.txt','a') as file1:
    file1.write("附加test")