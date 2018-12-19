> 题目：假设有四种面额的钱币，1元、2元、5元和10元，而您一共给我10元，那您可以奖赏我1张10元，或者10张1元，或者5张1元外加1张5元等等。如果考虑每次奖赏的金额和先后顺序，那么最终一共有多少种不同的奖赏方式呢？
>
> 极客时间版权所有: [https://time.geekbang.org/column/article/73511](QRcode.jpeg)


```java
// Java implementation

import java.util.ArrayList;

public class Lesson5_1 {

    public static long[] rewards = {1, 2, 5, 10};    // 四种面额的纸币

    /**
    * @Description:    使用函数的递归（嵌套）调用，找出所有可能的奖赏组合
    * @param totalReward- 奖赏总金额，result- 保存当前的解
    * @return void
    */

    public static void get(long totalReward, ArrayList<Long> result) {

        // 当 totalReward = 0 时，证明它是满足条件的解，结束嵌套调用，输出解
        if (totalReward == 0) {
            System.out.println(result);
            return;
        }
        // 当 totalReward < 0 时，证明它不是满足条件的解，不输出
        else if (totalReward < 0) {
            return;
        } else {
            for (int i = 0; i < rewards.length; i++) {
                // 由于有 4 种情况，需要 clone 当前的解并传入被调用的函数
                ArrayList<Long> newResult = (ArrayList<Long>)(result.clone());
                // 记录当前的选择，解决一点问题
                newResult.add(rewards[i]);
                // 剩下的问题，留给嵌套调用去解决
                get(totalReward - rewards[i], newResult);
            }
        }

    }

}
```

```python
# Python implementation

import copy

rewards = [1, 2, 5, 10]    # 四种面额的纸币

def get(total_reword, result):
    """ 使用函数的递归（嵌套）调用，找出所有可能的奖赏组合

    Args:
        totalReward: 奖赏总金额
        result: 保存当前的解

    Returns: void

    """
    if total_reword == 0:
        print(result)
        return
    elif total_reword < 0:
        return
    else:
        for i in range(len(rewards)):
            new_result = copy.copy(result)
            new_result.append(rewards[i])
            get(total_reword - rewards[i], new_result)


if __name__ == "__main__":
    result = []
    get(2, result)
    # [1, 1]
    # [2]
    get(3, result)
    # [1, 1, 1]
    # [1, 2]
    # [2, 1]
```