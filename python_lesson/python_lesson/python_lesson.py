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
#ヘッダーファイルのインクルード
include <iostream>				
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
