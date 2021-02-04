#pythonの基本文法
#対応するC言語での記述はクオーテーション内で記述


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
#ヘッダーファイルのインクルード。このシャープはコメントを意味するものではない。
#include <iostream>

#スコープ解決演算子を用いる名前空間名の省略
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
#Cでは上記のようにいきなり変数x,yを出してはならない。必ず型名とともに宣言してから使う。
#仮引数は宣言の必要なし。ただし、仮引数に型名の指定が必要。
int y;

#必ず型名を宣言する。セミコロンを忘れずにする。仮引数の型名も忘れずに。
int double(int x) {
	return x * 2;
}

#インライン関数の宣言。"inline <型名> <関数名>(型名 引数){};"
#短い処理のみ可。呼び出し部分に埋め込まれ、処理速度向上。
inline int apply(int x){x + 4};

#デフォルト引数を持つ関数。プロトタイプ宣言時にも、通常の関数宣言時にも指定可。
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
name2_AB = "{0} {1}".format(string_A, strig_B)
name3_AB = f"{string_A} {string_B}"

"""
#C言語では文字列を記憶できる型はない。一つの変数につき一文字(1byte)。
#文字列は配列を用いて扱う。文字列は" "で囲み、文字は' 'で囲む。
#文字配列では、最後にNULL文字を格納する。
char string_A[14] = {'t', 'e', 's', 't', ' ', 'm', 'e', 's', 's', 'a', 'g', 'e', 'A', '\0'};
char string_A[] = {'t', 'e', 's', 't', ' ', 'm', 'e', 's', 's', 'a', 'g', 'e', 'A', '\0'};
char string_B[14] = "test messageB";
char string_B[] = "test messageB";

#文字長を取得するには標準ライブラリをインクルードする必要がある。(別にforループなどで取得可能ではあるが手間)
#include <cstring>
size_t strlen(const cahr* <文字配列>);

#複数行の文字配列は改行の特殊文字を使用する
char multi_line_string[] = "Hello\nWorld";

#文字列の連結は上の標準ライブラリを用いれば簡単である。
#include <cstring>
char* strcat(char* string_A, const char* string_B);

#C++での文字列の出力は
#include <iostream>
using namespace std;
cout << string_A << '\n';

#文字列を配列で宣言した場合、あとから別の文字列を代入して変更することができない。
#配列のかわりにポインタで扱うと変更可能である。
const char* string_A = "test messageA";
cout << string_A << '\n';
string_A = "changed string_A";
"""

