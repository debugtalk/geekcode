# coding: utf-8

################################################################
# 思考题 Python 实现
################################################################

import copy
import math

def get_product_factors(n):
    """ get product factors of n
    """
    if n <= 0:
        return []
    else:
        product_factors = []
        for i in range(1, math.ceil(math.sqrt(n)) + 1):
            if i > 0 and n % i == 0:
                product_factors.append(i)
                product_factors.append(int(n / i))

        return sorted(list(set(product_factors)))

def get_multiply_combo(product, result=[]):
    """ 使用函数的递归（嵌套）调用，找出所有可能的乘积组合

    Args:
        product: 乘积结果
        result: 保存当前的解

    Returns: void

    """
    product_factors = get_product_factors(product)
    for i in product_factors:
        new_result = copy.copy(result)
        new_result.append(i)
        divisor = product // i
        if i == 1 or i == product:
            new_result.append(divisor)
            print(new_result)
        else:
            get_multiply_combo(divisor, new_result)


if __name__ == "__main__":
    product_factors = get_product_factors(4)
    print(product_factors)
    # [1, 2, 4]

    get_multiply_combo(6)
    # [1, 6]
    # [2, 1, 3]
    # [2, 3, 1]
    # [3, 1, 2]
    # [3, 2, 1]
    # [6, 1]

    get_multiply_combo(8)
    # [1, 8]
    # [2, 1, 4]
    # [2, 2, 1, 2]
    # [2, 2, 2, 1]
    # [2, 4, 1]
    # [4, 1, 2]
    # [4, 2, 1]
    # [8, 1]