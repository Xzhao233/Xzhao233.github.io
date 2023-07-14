﻿
# 打开文件并写入内容
FileTxt = open("file.txt", "w")
FileTxt.write('''#用以下方式添加：xxx(英文代码):xxx(对应中文)
abs:取绝对值
all:判断是否全为True
any:判断是否存在True
bin:转二进制
bool:转布尔
bytearray:可变字节数组
bytes:不可变字节数组
chr:Unicode转字符
dict:字典
del:删除
enumerate:枚举函数
eval:返回值执行代码
exec:执行代码
filter:过滤集合
float:转浮点数
format:格式化
frozenset:不可变集合
getattr:获取对象属性
globals:全局命名空间
global:声明
hasattr:判断属性
hash:哈希值
hex:转十六进制
id:标识符
input:输入
int:转整数
import:导入库
isinstance:判断类型
issubclass:判断类关系
iter:创建迭代器
len:获取长度
list:列表
locals:局部命名空间
map:映射
max:获取最大值
min:获取最小值
next:获取下一个元素
object:所有类的基类
oct:转八进制
open:打开文件
ord:转Unicode
pow:幂运算
print:输出
range:数字序列
repr:转可打印字符串形式
reversed:反转序列
round:四舍五入
set:集合
setattr:设置属性
slice:切片操作
sorted:排序集合
str:字符串
sum:求和
super:获取父类方法
tuple:元组
type:获取类型
vars:返回对象属性和属性值
zip:合并
findcode:查找代码
''')

# 关闭文件
FileTxt.close()

import turtle

turtle = turtle.Turtle()
turtle.write("↓在下方输出区写代码↓", font=("Arial",14, "normal"))
turtle.hideturtle()

def GetCode_S1(ZhInput):
    checksfilelist = []
    checksfile = ''
    for checks in ZhInput:
        checksfilelist.append(checks)
        if checks == ' ':
            del checksfilelist[-1]
            #删除最后一个字符，也就是空格
            break
    #获取空格前的文段，并保存在列表checksfilelist中
    checksfile = ''.join(checksfilelist)
    #转化成字符串
    return checksfile

def GetCode_S2(ZhInput):
    GeS1 = GetCode_S1(ZhInput)
    LenGeS1 = len(GeS1)
    #获取GeS1的长度
    GeS2 = ZhInput[LenGeS1+1:]
    #获取GetCodeS1后后面内容
    return GeS2
def getconv(file = 'file.txt'):
    result = {}
    with open(file, 'r') as f:
        lines = f.readlines()
        #读取文件：file.txt
    for line in lines[1:]:
        name, value = line.strip().split(':')
        result[value] = name
        #获取文件中的信息
    return result
result = getconv()
def findcode(codename:str,result = result) -> str:
    for key, value in result.items():
        if codename == value:
            print('你要查找的代码名为：',key)
            return key
            break
    print('你要查找的代码名为：','未找到')
    return '未找到'
def convcode(chicode,chicode2,result = result):
    if chicode.startswith("【") == True:
        start = chicode.find("【")
        end = chicode.find("】")
        #查找【和】的位置
        if start != -1 and end != -1:
            # 找到了指定的字符
            content = chicode[start+1:end]
            rest = chicode[end+1:]
            for key, value in result.items():
            #遍历result字典
                if rest == key:
                    if rest == '导入库' or rest == '声明' or rest == '删除':
                        retcode = content + value+' '+chicode2
                        return retcode
                        break
                    
                    else:
                        retcode = content + value+'('+chicode2+')'
                        return retcode
                        break
                #如果在字典中找到对应值，则输出转化后的代码（转化函数名）
    for key, value in result.items():
        #遍历result字典
        if chicode == key:
            if chicode == '导入库' or chicode == '声明' or chicode == '删除':
                retcode = value+' '+chicode2
                return retcode
                break
            else:
                retcode = value+'('+chicode2+')'
                return retcode
                break
        #如果在字典中找到对应值，则输出转化后的代码（转化函数名）
    retcode = chicode+'('+chicode2+')'
    print('Warning:未找到对应代码，将使用输入的代码')
    return retcode
    #如果没有在字典中找到对应值，则输出转化后的代码（不转化函数名）
willPrintTrip = True
while True:
    willRun = True
    if willPrintTrip == True:
        willPrintTrip = False
        code = input('您可以输入“输出代码字典”获取代码字典\n您可以输入“查找代码”+空格+英文代码名（需要加引号）查找对应中文代码\n您可以输入“帮助”获取代码帮助\n输入中文代码：')
    else:
        willPrintTrip = False
        code = input('输入中文代码：')
    #根据willPrintTrip的值决定是否输出提示
    if code == '输出代码字典':
        for key, value in result.items():
            print(key, ':', value)
            willRun = False
            #如果用户输入输出代码字典，则输出代码字典，且将willRun设置为False
    if code == '帮助':
        print('代码示例：\n输出 "你好,世界！"\n这行代码将输出你好世界\n合并 [1,2],[3,4]\n将合并列表')
        input('按回车（Enter）继续...')
        print('=======================\n【】内的代码为保留代码，如：【a=】转整数 "13"\n不要在【】里写空格！')
        input('按回车（Enter）继续...')
        print('=======================\n提示：不要使用可读性差的代码，如【a=】转整数 输入 "请输入："\n会导致报错')
        input('按回车（Enter）继续...')
        print('=======================\n如果一定要输入，请把后面级的代码写成普通py代码的形式')
        input('按回车（Enter）继续...')
        print('=======================\n功能分别为：获取代码前半段，获取代码后半段，获取对应代码列表、转换代码、查找代码\n由Xzhao（黄楚钊）一人制作，未加入任何工作室')
        input('按回车（Enter）继续...')
        print('=======================\n使用库：turtle（绘制舞台区内容）\n目前版本：Xpy For GaotuCode Beta 3.1')
        willRun = False
        #如果用户输入帮助，则输出帮助，且将willRun设置为False
    if willRun == True:
        willRunCode = convcode(GetCode_S1(code),GetCode_S2(code))
        print('Info:您执行的代码转换后：')
        print(willRunCode)
        try:
            exec(willRunCode)
        except Exception as e:
            print("Error:", e)
        #如果willRun为True，则运行转换后的代码
