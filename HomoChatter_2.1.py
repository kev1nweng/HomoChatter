import os
import random

os.system('title HomoChatter 2.1')
os.system('cls')
part1 = ["你是一个一个一个","食","我事","脱出","快点端上来罢","我在撅homochatter的时候，","十分甚至九分","兄啊，","戳啦，","wxy撅","sd食","五班事","这这布隆……","哼，哼，哼，"]
part2 = ["恶臭的","撅撅子的","都是男的","正撅的","中出的","一针见雪的","homosexual","脱出的","食雪的","急不可耐的","小鬼的","自裁的","114514的"]
part3 = ["……有什么存在的必要吗","我等不及力","野獣先辈","——淳平","？我修院！","快点端上来罢","快点端下去罢","啊啊啊啊啊啊啊啊啊啊啊啊","雪崩","极霸矛嘛","你有在偷看罢？","1919810"]
emotion = ["（喜","（悲","（恼","（疑惑","（智将","（大喜","（全恼","（无慈悲","（确信","（直球","（警撅","（并感","（乐","（半恼","（）", "（心虚", "意味深"]
tips = ["猜猜最多可以输入几位数（喜", "HomoChatter的开发者头发已经只剩十根甚至是九根力（悲", "震惊！今日一名为HomoChatter的人机聊天软件成功通过图灵测试！", "冷知识：输入的不是整数不会真的被撅（心虚", "我现在就要和HomoChatter聊天，三回啊三回", "假如HomoChatter在Github上开源会发生什么？", "据报道，我校homo浓度已达到惊人的114%", "学校食堂的秘制酱料面很好吃，赶紧去尝尝（喜", "homo特色社会主义", "近日，两学生在教室里公然开撅"]

撅=input
脱出=print
rc=random.choice

while True:
    脱出("输入一个整数，输对了有奖励，输错了有惩罚（意味深")
    
    while True:
        try:
            inputnum=int(撅("快点端上来罢（喜："))
            break
        except ValueError:
            os.system('cls')
            print("[错误]让你输入整数，再乱输小心被撅（恼")  
            continue

    random.seed(inputnum + random.randint(0, 114514))
    
    脱出("\n======================================================")
    脱出(rc(part1),sep="",end="")
    脱出(rc(part2),sep="",end="")
    脱出(rc(part3),sep="",end="")
    脱出(rc(emotion),sep="",end="\n")
    脱出("======================================================\n")
    脱出("Tip: ", tips[random.randint(0, 9)],sep="",end="\n")
    脱出("\n*点击任意键再次对话", sep="",end="\n")
    
    
    os.system('pause>nul')
    os.system('cls')
