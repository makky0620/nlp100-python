
input = "I am an NLPer"

def n_gram(input, N=2):
    # 文字 n-gram (引数 str)
    l = len(input)
    output = []
    if type(input) == str:
        input = input.replace(" ", "")
        for i in range(len(input)):
             output.append(input[i:i+N])
    if type(input) == list:
        output = [[input[i+n] for n in range(N) if i+n < len(input)] for i in range(len(input))]
        output = [ list for list in output if len(list) == N]
    return output

if __name__ == "__main__":
    output = n_gram(input)              # 文字 n-gram
    print(output)
    input = input.split()
    output = n_gram(input, 3)         
    print(output)