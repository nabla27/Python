#pythonの基本文法
#対応するC言語での記述はクオーテーション内で記述


#############################
#初期的な設定(モジュールなど)
#############################
import numpy										#モジュールをインポート
import matplotlib.pyplot as plt						#モジュール名に別名をつけてインポート
from collections import defaultdict, Counter		#モジュール内の特定の機能だけをインポート
													#モジュールの関数を使うときは、関数の前に"モジュール名."をつける

"""
include <iostream>									#ヘッダファイルをインクルード
using namespace std;								#スコープ解決演算子を用いる名前空間名の省略
"""

###########
#関数の定義
###########
def double(x):										#def <関数名>: で宣言
	return x * 2									#return で返す

def apply(f):
	f(1)											#

my_double = double
x = apply(my_double)

"""
int double(x) {										#必ず戻り値の型名を宣言
	return x * 2;									#セミコロンを忘れずに
}
"""
