#pythonの基本文法
#対応するC言語での記述はクオーテーション内で記述
#Cでは、プログラムの本体は一番先に処理されるmain関数内に書く必要があるが、以下では省略する。


###############################################
#初期的な設定(モジュールなど)
###############################################

#モジュールをインポート
import numpy

#モジュール名に別名をつけてインポート
import matplotlib.pyplot as plt

#モジュール内の特定の機能だけをインポート
from collections import defaultdict, Counter

#モジュールの関数を使うときは、関数の前に"モジュール名."をつける

"""
ヘッダーファイルのインクルード。
#include <iostream>

スコープ解決演算子を用いる名前空間名の省略
using namespace std;							
"""

###############################################
#関数の定義
###############################################

#"def <関数名>:"で宣言。"return"で値を返す
def double(x):	
	return x * 2

#関数fを変数とする関数apply
def apply(f):
	f(1)
	
#関数である変数my_doubleをapply関数に代入
my_double = double
x = apply(my_double)

#名前を持たない短い関数(ラムダ式)を宣言。"lambda <変数名>:式"
y = apply(lambda x: x + 4)

#デフォルト引数を持つ関数。引数を指定しないときに、デフォルトの値が渡される。
def my_print(string="defalt message"):
	print(string)

#defalt message と出力される
my_print()

"""
Cでは上記のようにいきなり変数x,yを出してはならない。必ず型名とともに宣言してから使う。
仮引数は宣言の必要なし。ただし、仮引数に型名の指定が必要。
int y;

必ず型名を宣言する。セミコロンを忘れずにする。仮引数の型名も忘れずに。
int double(int x) {
	return x * 2;
}

インライン関数の宣言。"inline <型名> <関数名>(型名 引数){};"
短い処理のみ可。呼び出し部分に埋め込まれ、処理速度向上。
inline int apply(int x){x + 4};

デフォルト引数を持つ関数。プロトタイプ宣言時にも、通常の関数宣言時にも指定可。
int number(int x = 4);
int number(int x){
	return x + 4;
}
"""

###############################################
#文字列の扱い
###############################################

#まず標準出力についてpythonでは
x = 3;
print(x)
#C++ではつぎのようになる。
"""
#include <iostream>
using namespace std;
int x = 3;
cout << x << "\n";
"""

#文字列の変数
string_A = "test messageA"
string_B = 'test messageB'

#特殊文字と文字列の長さを取得
tab_string = "\t"
len_string = len(tab_string)

#バックスラッシュとして認識させる。(この場合、文字長は2)
tab_string = r"\t"
len_string = len(tab_string)

#複数行の文字列を定義
multi_line_string = """一行目
二行目
三行目"""

#文字列の連結。いづれも"test messageA test messageB" 
name1_AB = string_A + " " + string_B
name2_AB = "{0} {1}".format(string_A, string_B)
name3_AB = f"{string_A} {string_B}"

"""
C言語では文字列を記憶できる型はない。一つの変数につき一文字(1byte)。
文字列は配列を用いて扱う。文字列は" "で囲み、文字は' 'で囲む。
文字配列では、最後にNULL文字を格納する。
char string_A[14] = {'t', 'e', 's', 't', ' ', 'm', 'e', 's', 's', 'a', 'g', 'e', 'A', '\0'};
char string_A[] = {'t', 'e', 's', 't', ' ', 'm', 'e', 's', 's', 'a', 'g', 'e', 'A', '\0'};
char string_B[14] = "test messageB";
char string_B[] = "test messageB";

文字長を取得するには標準ライブラリをインクルードする必要がある。(別にforループなどで取得可能ではあるが手間)
#include <cstring>
size_t strlen(const cahr* <文字配列>);

複数行の文字配列は改行の特殊文字を使用する
char multi_line_string[] = "Hello\nWorld";

文字列の連結は上の標準ライブラリを用いれば簡単である。
include <cstring>
char* strcat(char* string_A, const char* string_B);

C++での文字列の出力は
#include <iostream>
using namespace std;
cout << string_A << '\n';

文字列を配列で宣言した場合、あとから別の文字列を代入して変更することができない。
配列のかわりにポインタで扱うと変更可能である。
const char* string_A = "test messageA";
cout << string_A << '\n';
string_A = "changed string_A";
"""

###############################################
#リストについて
###############################################

#複数の要素を格納できるリスト
intger_list = [1, 2, 3]
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#任意の型を格納できる
some_list = ["string", 0.1, True]

#リストの長さと合計値を取得
list_length = len(intger_list)
list_sum = sum(intger_list)

#リストの要素をインデックスを用いて取り出す
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]

#リスト内の一部を切り出すスライス
first_three = x[:3]
three_to_end = x[3:]
one_to_three = x[1:3]
last_three = x[-3:]

#0番目から10番目の要素を歩幅2でとりだす。(0,2,4,6,8)
zero_ten_stride2 = x[0:10:2]

#2番目から最後までの要素を歩幅3でとりだす。(2,5,8)
two_end_stride3 = x[2::3]

#リストの先頭から最後まで歩幅3で取り出す。(0,3,6,9)
all_string3 = x[::3]

#リストの末尾から逆順でとりだす。(8,7,6,5,4,3)#末尾から2番目の要素から8個の要素を逆順にとってくる
back_stride1 = x[-2:-8:-1]

#同様の表記で要素を削除
del x[9]

#リストの末尾に要素を追加
x.append(9)
x.extend([10,11,12,13,14,15])
y = x + [16,17,18,19,20]

#リスト任意の要素を変更する。(この場合、偶数だけ10倍した値に変更)
y[2::2] = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

#リストの要素の有無を確認(上からTrue, False)
print(1 in x)
print(100 in x)

#同時にリストから要素をとりだす
number_one, number_two = [5, 10]

#全要素を取りだす。リストのコピー。
copy_of_x = x[:]




