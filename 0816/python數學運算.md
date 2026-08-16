# Python 數學運算筆記（國中~高中程度）

## 1. 基本資料型態

| 型態 | 中文 | 例子 |
|------|------|------|
| `int` | 整數 | `50`, `-3`, `0` |
| `float` | 浮點數（小數） | `3.14`, `-0.5` |
| `str` | 字串（文字） | `"hello"`, `'中文'` |
| `bool` | 布林值（真/假） | `True`, `False` |

```python
print(type(50))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type("abc"))   # <class 'str'>
print(type(True))    # <class 'bool'>
```

可以用 `int()`、`float()`、`str()` 轉換型態：

```python
print(int("5") + 5)      # 10，把字串 "5" 轉成整數
print(float(10))         # 10.0，把整數轉成浮點數
print(str(50) + "歲")    # 50歲，把整數轉成字串
```

## 2. 算術運算子

| 運算子 | 功能 | 例子 | 結果 |
|--------|------|------|------|
| `+` | 加法 | `3 + 5` | `8` |
| `-` | 減法 | `10 - 4` | `6` |
| `*` | 乘法 | `3 * 5` | `15` |
| `/` | 除法（結果是小數） | `7 / 2` | `3.5` |
| `//` | 整除（只取整數部分） | `7 // 2` | `3` |
| `%` | 取餘數 | `7 % 2` | `1` |
| `**` | 指數（次方） | `2 ** 3` | `8` |

```python
print(3 + 5)          # 8
print(3 * 5)          # 15
print(7 / 2)          # 3.5
print(7 // 2)         # 3
print(7 % 2)          # 1
print(2 ** 3)         # 8
```

### 取餘數的小妙用
判斷奇數／偶數：

```python
n = 7
print(n % 2 == 0)     # False，不是偶數，所以是奇數
```

## 3. 運算子優先順序

和數學課本一樣：**先乘除後加減，有括號先算**。

```python
print(3 + 5 * 2)      # 13，先算 5*2
print((3 + 5) * 2)    # 16，括號優先
print(2 ** 3 * 2)     # 16，指數優先於乘法
```

優先順序（高到低）：
1. `()` 括號
2. `**` 指數
3. `* / // %` 乘、除、整除、取餘數
4. `+ -` 加、減

## 4. 和數學課本對應的例子

### 4.1 圓面積公式 `A = πr²`
```python
import math

radius = 10
area = math.pi * radius ** 2
print(area)    # 314.1592653589793
```

### 4.2 一元二次方程式 `ax² + bx + c = 0`
解 `x = (-b ± √(b² - 4ac)) / 2a`

```python
import math

a, b, c = 1, -3, 2          # x² - 3x + 2 = 0
disc = b ** 2 - 4 * a * c   # 判別式 D = b² - 4ac

x1 = (-b + math.sqrt(disc)) / (2 * a)
x2 = (-b - math.sqrt(disc)) / (2 * a)
print(x1, x2)   # 2.0 1.0
```

### 4.3 等差級數和 `S = n(a₁ + aₙ) / 2`
```python
n = 100                 # 有 100 項
a1 = 1                  # 第一項
an = 100                # 第 100 項
total = n * (a1 + an) / 2
print(total)            # 5050.0
```

### 4.4 直角三角形斜邊 `c = √(a² + b²)`
```python
import math

a, b = 3, 4
c = math.sqrt(a ** 2 + b ** 2)
print(c)    # 5.0（剛好是 3-4-5 三角形）
```

## 5. math 模組常用函式

```python
import math

math.sqrt(16)        # 4.0        開根號
math.pi              # 3.14159... 圓周率
math.e               # 2.71828... 自然對數底
math.pow(2, 3)       # 8.0        次方（等同 2**3）
math.fabs(-5)        # 5.0        絕對值
math.floor(3.7)      # 3          無條件捨去
math.ceil(3.2)       # 4          無條件進位
math.factorial(5)    # 120        5!
math.gcd(12, 18)     # 6          最大公因數
math.radians(180)    # 3.14159... 度轉弧度
math.sin(math.radians(90))   # 1.0  sin 90°
math.cos(math.radians(0))    # 1.0  cos 0°
```

## 6. 小練習

1. 計算 `(3 + 4) * 5 - 10 / 2` 的答案。
2. 寫程式計算 1 到 100 所有奇數的和。
3. 輸入一個三位數，用 `//` 和 `%` 分別印出百位、十位、個位數。
4. 判斷一個數是不是質數。
5. 用公式 `F = C * 9 / 5 + 32` 把攝氏轉成華氏。

### 解答

**練習 2：**
```python
total = 0
for i in range(1, 101, 2):   # 1, 3, 5, ..., 99
    total += i
print(total)    # 2500
```

**練習 3：**
```python
n = 523
print(n // 100)        # 5  百位
print(n // 10 % 10)    # 2  十位
print(n % 10)          # 3  個位
```

**練習 4：**
```python
n = 29
is_prime = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)    # True
```
