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

#関数fを引数とする関数apply
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
int main(){
	int x = 3;
	cout << x << "\n";
}
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

#文字列のアンパック。(シーケンス型はアンパック可能)
a,b,c = 'str'
print(a)	#a = s

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

#リストの要素をインデックスを用いて取り出す。(インデックスで要素にアクセスできる=シーケンス型)
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

#リスト展開を使い、同時に指定
number_one, number_two = [5, 10]

#全要素を取りだす。リストのコピー。
copy_of_x = x[:]

"""
Cでは配列がpythonでのリストの役割を果たす。一つの配列に複数の型の変数を格納できない。
必ず配列は宣言または初期化をし、型名も記す。
int test_score[5];
test_score[0] = 60; test_score[1] = 70; test_score[3] = 80; test_score[4] = 90; test_score[5] = 100;
test_score[] = {60, 70, 80, 90, 100};

配列の要素を取り出す。
first_score = test_score[0];
third_score = test_score[3];

Cには容易に特定の範囲のみを取りだしたり、削除する機能はない。また、配列の要素数を取得するものもない。(ひと手間必要)
C言語では配列を戻り値にすることができない。
pythonは参照渡しだが、Cでは値渡しなので、直接アドレスを操作してポインタを用いる必要がある。

以下、与えられたint型配列を逆順にソートするプログラム例。
int test[] = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };
void array_return(int* list, int range) {
	for (int i = 0; i < range / 2; i++) {
		int tmp = list[i];
		list[i] = list[range - i - 1];
		list[range - i - 1] = tmp;
	}
}
int main() {
	array_return(test, sizeof(test) / sizeof(test[0])); //二つ目の引数は配列の大きさを渡す
	return 0;
}

普通には配列の要素数を変更することができない。stdlibをインクルードし、malloc関数でメモリの動的確保を行う。
以下、配列から特定の要素を取り出した新たな配列を作るプログラム例(改良の余地あり)。
#include <stdlib.h>
#include <iostream>
int test[] = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };
int* new_array;
void array_cut(int* list, int start=0, int end = 0, int stride=1) {
	if (end == 0) {
		end = start;                                              //もしendが指定されなかったら1要素だけ切り出す
	}
	int new_range = (end - start + 1) / stride; 　　　　　　　　　//新しい配列の要素数
	new_array = (int *)malloc(sizeof(int) * new_range);　　　　　 //新しい配列のメモリー領域
	for (int i = 0; i < new_range; i++) {
		new_array[i] = list[start + stride * i];
		std::cout << new_array[i] << "\n";
	}
}
int main() {
	array_cut(test,0,9,2); 　//0~9までを歩幅2で取り出す。(10,30,50,70,90)
	array_cut(test, 2, 5); 　//2~5までを歩幅1で取り出す。(30,40,50,60)
	array_cut(test, 6);　　　// 6のみを取り出す。(70)

	free(new_array);         //メモリの解放
	return 0;
}
一回だけ行うならば、関数化せず、定数型でnew_arrayの要素数を定義すれば楽である。

配列の中に、指定した数が含まれているか判定する簡単な機能はない。例えば次のようなプログラムで判定できる。
#include <iostream>
int test[] = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };
bool judge(int* Array, int value, int size) {
	int test = 1;
	for (int i = 0; i < size; i++) {
		if (Array[i] == value) { test *= 0; }
		else { test *= 1; }
	}
	if (test == 0) { return true; }
	else { return false; }
}
int main() {
	std::cout << judge(test, 10, 10) << '\n'; //True
	std::cout << judge(test, 15, 10) << '\n'; //False
	std::cout << judge(test, 20, sizeof(test) / sizeof(test[0])) << 'n'; //True
	return 0;
}

配列のコピーについても、pythonのように一度に配列をコピーすることはできない。forループなどで各要素を一つずつコピーしなければならない。
int test[10] = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };
int main() {
	const int size = sizeof(test) / sizeof(test[0]);
	int cp_test[size];
	for (int i = 0; i < size; i++) {
		cp_test[i] = test[i];
	}
}
"""
###############################################
#タプル
###############################################
#リストと似ているが、要素の変更ができない。

#タプルの宣言
my_tuple1 = (1,2)
my_tuple2 = 3, 4
my_list = [1, 2, 3]
my_list2 = [4, 5, 6]
list_tuple = my_list, my_list2

#空のタプルを生成
empty_tuple = ()

#一要素のみのタプル。コンマを忘れずにつける。
one_tuple = ("only,")
one_tuple = "only",

#型の確認(<class 'tuple'>)
print(type(one_tuple))

#タプルを用いて複数の値を返す関数
def sum_and_product(x,y):
	return (x + y), (x * y)
sp = sum_and_product(2,3)	#sp = (5, 6)
s, p = sum_and_product(4, 8)	#s = 12, p = 32

#値の交換
s, p = p, s

#タプル関数を用いてタプルを生成
emptytuple = tuple()  #空のタプルを作成
mylist = [0, 1, 2, 3] 
mytuple = tuple(mylist)  #リストを基にタプルを作成
anothertuple = tuple(iter(mylist))  #イテレータを基にタプルを作成(イテレータについては後述)

#インデックスでタプルの要素にアクセス
tp1 = mytuple[1]
print(mytuple[2])

#要素の変更はできないが、変数に別のタプルを代入可能
mytuple = 1, 2, 3
mytuple = 4, 5, 6
list_tuple[0][1] = 20

###############################################
#辞書
###############################################
#キーと値を関連付けて格納する。キーに対する値を即座に取り出せる。

#空の辞書
empty_dict = {}
empyt_dict2 = dict()

#辞書のリテラル表現
test_score = {"A": 80, "B": 65}

#キーに対する値を取り出す。
A_score = test_score["A"]

#辞書内にキーが存在するか
exsistence_A = "A" in test_score #True
exsistence_B = "C" in test_score #False

#getメソッドを用いて、キーなしのときデフォルト値を返す
C_score = test_score.get("C", 0)	#0になる
D_score = test_score.get("D")       #Noneになる

#キーの値を書き換える
test_score["A"] = 100


profile = {
	"name" : "Tom",
	"age" : 19,
	"height" : 170,
	"weight" : 60,
	"Univ" : "Okayama",
	"Country" : "Japan",
	"food" : ["Apple", "Banana", "Orange", "Grape"]
}

#各要素のキーを取得
profile_keys = profile.keys()
print(profile_keys)	#dict_keys(['name', 'age', 'height', 'weight', 'Univ', 'Country', 'food'])

#各要素の値を取得
profile_values = profile.values()
print(profile_values)	#dict_values(['Tom', 19, 170, 60, 'Okayama', 'Japan', ['Apple', 'Banana', 'Orange', 'Grape']])

#各要素のタプルを取得
profile_items = profile.items()
print(profile_items)	#dict_items([('name', 'Tom'), ('age', 19), ('height', 170), ('weight', 60), ('Univ', 'Okayama'), ('Country', 'Japan'), ('food', ['Apple', 'Banana', 'Orange', 'Grape'])])

#辞書内にキーがあるキーが含まれているか確認
"name" in profile_keys	#python的でない
"name" in profile	#python的

#辞書内にある値が含まれているか確認
"Tom" in profile_values	#唯一の方法だが低速

#文章中の単語数を辞書に登録する
document = ["Hello", "Hello", "Yes", "Yes", "Good", "Bye", "Hello"]
word_counts = {}
for word in document:
	if word in word_counts:		#すでに辞書内に登録されていれば、値を+1する
		word_counts[word] += 1
	else:
		word_counts[word] = 1		#辞書内に登録されていなければ、値を1とする
print(word_counts)	#{'Hello': 3, 'Yes': 2, 'Good': 1, 'Bye': 1}

#defaultdictクラスを用いる
#デフォルトの値を設定できる辞書型リスト。辞書に登録されていなくてもその時点でその値をデフォルト(初期値)として認知する。
#登録されていないキーにアクセスした場合にもエラーにならない。
from collections import defaultdict
word_count_a = defaultdict(int)		#defaultdict()で引数で渡した関数が返す値を初期値とする。この場合は0
for word in document:
	word_count_a[word] += 1
print(word_count_a)		#defaultdict(<class 'int'>, {'Hello': 3, 'Yes': 2, 'Good': 1, 'Bye': 1})
#空のリストを初期値とする
dict_list = defaultdict(list)
dict_list[2].append(1)
print(dict_list)	#defaultdict(<class 'list'>, {2: [1]})
#空の辞書を初期値とする
dict_list = defaultdict(dict)
dict_list["math"]["NumberTheory"] = "ok"
print(dict_list)	#defaultdict(<class 'dict'>, {'math': {'NumberTheory': 'ok'}})
#無名関数lambdaを用いて初期値を1とする(各keyが1多くカウントされる)
word_count_b = defaultdict(lambda:1)
for word in document:
	word_count_b[word] += 1
print(word_count_b)		#defaultdict(<function <lambda> at 0x000001BFB22F9940>, {'Hello': 4, 'Yes': 3, 'Good': 2, 'Bye': 2})

#Counterクラスを用いる
#ひとつづきの値をキーとその出現数に展開する
numlist = [1, 3, 5, 6, 6, 4, 3, 3, 1, 1, 7, 4, 3, 3, 2, 2, 3]
from collections import Counter
c = Counter(numlist)
print(c)	#Counter({3: 6, 1: 3, 6: 2, 4: 2, 2: 2, 5: 1, 7: 1})
c = Counter(document)
print(c)	#Counter({'Hello': 3, 'Yes': 2, 'Good': 1, 'Bye': 1})

###############################################
#集合
###############################################
#重複しない値の集まり
primes = {2, 3, 5, 7}	#中括弧で集合の宣言
primes = set()	#空の集合
primes.add(2)	#要素2を追加 {2}
primes.add(3)	#要素3を追加 {2, 3}
primes.add(3)	#{2, 3}のまま
n = len(primes)		#n=2
tf = 2 in primes	#tf=True 
tf = 4 in primes	#tf=False
numlist = [1, 3, 5, 6, 6, 4, 3, 3, 1, 1, 7, 4, 3, 3, 2, 2, 3]
num_set = set(numlist)	#重複が取り除かれる
print(num_set)	#{1, 2, 3, 4, 5, 6, 7}
num_list = list(num_set)	#重複のないリストを生成

###############################################
#真偽とループ
###############################################
#ifによる真偽
if 2 > 1:
	print("2が1より大きい")		#実行される
elif 3 > 2:
	print("3が2より大きい")		#実行されない
if 1 > 2:
	print("1が2より大きい")		#実行されない
elif 3 > 2:
	print("3が2より大きい")		#実行される
else:
	print("その他の処理")		#実行されない

#一行でif-elif-elseを処理
x = 2
sol = "even" if x % 2 == 0 else "odd"	#xの余りが0ならsol=even,その他はsol=even
x = 0
sol = 'negative' if x < 0 else 'positive' if x > 0 else 'zero'	#x<0ならnegative.それ以外でx>0ならpositive.それ以外ならzero
print(sol)	#zero

#while文
x = 0
while x < 10:
	print(x, end=', ')	#0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
	x += 1
print()

#while文で無限ループ
x = 0
while True:
	key = input()	#キーボード入力待機
	if key == "exit":	#exitと入力されたらbreakでループを抜け出す
		break	

#for文
for x in range(10):		#0から9の範囲
	print(x, end=', ')	#0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
print()

#continueとbreak文
for x in range(10):
	if x == 1 or x == 5:
		continue
	elif x == 7:
		break
	print(x, end=', ')	#0, 2, 3, 4, 6,
print()






