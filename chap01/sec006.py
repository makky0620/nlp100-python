# coding: utf-8
def n_gram(input, N=2):
    # 文字 n-gram (引数 str)
    l = len(input)
    output = []
    if type(input) == str:
        input = input.replace(" ", "")
        for i in range(len(input)):
             output.append(input[i:i+N])
        output = [ li for li in output if len(li) == N]
    if type(input) == list:
        output = [[input[i+n] for n in range(N) if i+n < len(input)] for i in range(len(input))]
        output = [ word for word in output if len(word) == N]

    return set(output)

s1 = "paraparaparadise"
s2 = "paragraph"

s1_bi_gram = n_gram(s1)
s2_bi_gram = n_gram(s2)

print(s1_bi_gram | s2_bi_gram)
print(s1_bi_gram & s2_bi_gram)
print(s1_bi_gram - s2_bi_gram)