count={}
with open("moby_01.txt") as infile:
    for line in infile:
        # 將所有字元轉成小寫
        cleaned_line = line.lower()
        
        # 刪除所有標點符號
        punct = str.maketrans("!.,:;-?", "       ")
        cleaned_line = cleaned_line.translate(punct)
        
        # 依照單字切割
        for word in cleaned_line.split():
        # 計算單字個數，並加入字典
            count[word]=count.get(word,0)+1 

# 定義排序方式
# 此時 x 為一 tuple. x[0]為 key、x[1]為 value
# 以字典的 value 排序，故需回傳 value
def sort(x):
    return x[1]

# .items()會回傳字典的 key、value，以 tuple 表示
word_list = list(count.items())
word_list.sort(key=f)

print("Most common words:")

#取出倒數5個，並反轉，即從大排到小
for word in reversed(word_list[-5:]):
    print(word)

print("\nLeast common words:")
for word in word_list[:5]:
    print(word)