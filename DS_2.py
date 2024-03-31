def check_brackets(input_string):
    stack = []  # 初始化一个空栈，用于存储左括号的索引
    output = ""  # 初始化输出字符串

    # 遍历输入字符串的每个字符
    for i, char in enumerate(input_string):
        if char == "(":  # 如果当前字符是左括号
            stack.append(i)  # 将左括号的索引压入栈中
            output += " "  # 在输出字符串中添加空格以便对齐
        elif char == ")":  # 如果当前字符是右括号
            if not stack:  # 如果栈为空，说明没有匹配的左括号
                output += "?"  # 在输出字符串中标记问号
            else:
                stack.pop()  # 如果栈不为空，弹出一个匹配的左括号的索引
                output += " "  # 在输出字符串中添加空格以便对齐
        else:
            output += " "  # 如果当前字符不是括号，则在输出字符串中添加空格以便对齐

            
    # 处理栈中剩余的左括号，它们没有匹配的右括号
    for index in stack:
        output = output[:index] + "x" + output[index+1:]
    
    output = input_string + "\n" + output
    
    return output  # 返回处理后的结果字符串

def process_test_cases(test_cases):
    result = ""  # 初始化结果字符串
    for test_case in test_cases:
        result += check_brackets(test_case) + "\n"  # 对每个测试用例调用check_brackets函数，并将结果添加到结果字符串中
    return result  # 返回最终的结果字符串

# 输入测试用例
test_cases = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]

# 输出结果
print(process_test_cases(test_cases))
