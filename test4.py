# 动态规划之正则表达 https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-zhi-zheng-ze-biao-da#er-chu-li-dian-hao-tong-pei-fu
# 暴力递归
def isMatch(text, pattern) -> bool:
    if not pattern: return not text
    # bool() 字符串为空返回False
    first = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        # \ 在行尾时表示做续行符使用
        return isMatch(text, pattern[2:]) or \
               first and isMatch(text[1:], pattern)
    else:
        return first and isMatch(text[1:], pattern[1:])


# 带备忘录的递归
def isMatch2(text, pattern) -> bool:
    memo = dict()  # 备忘录

    def dp(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if j == len(pattern): return i == len(text)

        first = i < len(text) and pattern[j] in {text[i], '.'}

        if j <= len(pattern) - 2 and pattern[j + 1] == '*':
            ans = dp(i, j + 2) or \
                  first and dp(i + 1, j)
        else:
            ans = first and dp(i + 1, j + 1)

        memo[(i, j)] = ans
        return ans

    return dp(0, 0)


if __name__ == '__main__':
    print(bool(''))
    print(isMatch2('abcda', 'a.*'))
    print(isMatch2('abcda', 'a*'))
    print(isMatch2('abcda', 'a.*a'))
