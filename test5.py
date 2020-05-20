# 动态规划之四键键盘 https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-zhi-si-jian-jian-pan
def maxA(N: int) -> int:
    # 对于 (n, a_num, copy) 这个状态，
    # 屏幕上能最终最多能有 dp(n, a_num, copy) 个 A
    def dp(n, a_num, copy):
        # base case
        if n <= 0: return a_num;
        # 几种选择全试一遍，选择最大的结果
        return max(
            dp(n - 1, a_num + 1, copy),  # A
            dp(n - 1, a_num + copy, copy),  # C-V
            dp(n - 2, a_num, a_num)  # C-A C-C
        )

    # 可以按 N 次按键，屏幕和剪切板里都还没有 A
    return dp(N, 0, 0)


def dp(n, a_num, copy):
    # base case
    if n <= 0: return a_num;
    # 几种选择全试一遍，选择最大的结果
    return max(
        dp(n - 1, a_num + 1, copy),  # A
        dp(n - 1, a_num + copy, copy),  # C-V
        dp(n - 2, a_num, a_num)  # C-A C-C
    )


if __name__ == '__main__':
    print(maxA(7))
    print(dp(7, 0, 0))
    print(dp(6, 1, 0))
    print(dp(3, 4, 0))
