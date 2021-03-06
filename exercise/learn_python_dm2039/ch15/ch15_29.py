# ch15_29.py
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug("程式開始")

def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(n + 1):
        ans *= i
        logging.debug('i = ' + str(i) + ', ans = ' + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans

num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug("程式結束")




