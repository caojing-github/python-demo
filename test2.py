# 高楼扔鸡蛋 https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/gao-lou-reng-ji-dan-wen-ti
def superEggDrop(K: int, N: int) -> int:
    memo = dict()

    def dp(K, N):
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]

        # for 1 <= i <= N:
        #     res = min(res,
        #             max(
        #                     dp(K - 1, i - 1),
        #                     dp(K, N - i)
        #                 ) + 1
        #             )

        res = float('INF')
        # 用二分搜索代替线性搜索
        lo, hi = 1, N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1)  # 碎
            not_broken = dp(K, N - mid)  # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)

        memo[(K, N)] = res
        return res

    return dp(K, N)


# 直接调用方法
if __name__ == '__main__':
    print(superEggDrop(2, 10))
    print(superEggDrop(2, 11))
    print(superEggDrop(2, 12))
    print(superEggDrop(2, 13))
    print(superEggDrop(2, 14))
    print(superEggDrop(2, 15))
    print(superEggDrop(2, 16))
    print(superEggDrop(2, 17))
    print(superEggDrop(2, 18))
    print(superEggDrop(2, 19))
    print(superEggDrop(2, 20))
