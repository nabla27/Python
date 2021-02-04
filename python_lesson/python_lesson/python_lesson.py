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

"""
#必ず型名を宣言する。セミコロンを忘れずにする。
int double(x) {										
	return x * 2;									
}
"""
