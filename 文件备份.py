odd_name = input("输入原来的文件名")
#对例如 a.txt , b.txt ,c.txt d.txt.txt
name_index = odd_name.rfind(".")
try:
    if name_index>0:
        porfix = odd_name[name_index:]

except Exception as e:
    print(e)

new_name = odd_name[:name_index]+"备份"+porfix
old_f = open(odd_name,"rb")
new_f = open(new_name,"wb")
while True:
    context = old_f.read(1024)
    if len(context) == 0:
        break
    new_f.write(context)
old_f.close()
new_f.close()


