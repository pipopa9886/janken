
import random as r
import time


#変数宣言タイム
a=0
total=0
win=0
lose=0
draw=0
player=0
while player==0:
    with open("name.txt","r",encoding="utf-8") as re:
        name=re.read()
#pcのname.txtを読み込む

    print("あなたは{}さんですか？".format(name))
    print("はい:0,いいえ:1")
    choise=int(input())
    if choise==1:
        print("こんにちはじゃんけんゲームへようこそ")
        print("あなたの名前を教えてください")
        name=input()
        print("ようこそ{}さん。楽しんでいってください。それではスタートします".format(name))
        time.sleep(2)
    else:
        with open("result.txt","r",encoding="utf-8") as rea:
            youresult=rea.read()
        print("前回あなたは{}でした。".format(youresult))
    while a==0:
        cpu=r.randint(0,2)#0-グー 1-チョキ 2-バー
        print("じゃんけんをします。0:グー,1:チョキ,2:パーを数字で選んでください")
        me=int(input())
        print("----------------------------------------------------------")
        if me>=0 and me<=2:
            total+=1
            print("第{}回戦".format(total))
            if cpu==0:
                if cpu==0 and me==0:

                    print("相手はグーを出して{}さんもグーだから".format(name))
                    print("あいこだね")
                    draw+=1
                elif cpu==0 and me==1:

                    print("相手はグーを出して{}さんはチョキだから".format(name))
                    print("負けちゃった")
                    lose+=1
                elif cpu==0 and me==2:

                    print("相手はグーを出して{}さんはパーだから".format(name))
                    print("勝ち！")
                    win+=1
                else:
                    pass
            elif cpu==1:
                if cpu==1 and me==0:

                    print("相手はチョキを出して{}さんはグーだから".format(name))
                    print("勝ち！")
                    win+=1
                elif cpu==1 and me==1:

                    print("相手はチョキを出して{}さんもチョキだから".format(name))
                    print("あいこだね")
                    draw+=1
                elif cpu==1 and me==2:

                    print("相手はチョキを出して{}さんはパーだから".format(name))
                    print("負けちゃった")
                    lose+=1
                else:
                    pass
            elif cpu==2:
                if cpu==2 and me==0:

                    print("相手はパーを出して{}さんはグーだから".format(name))
                    print("負けちゃった")
                    lose+=1
                elif cpu==2 and me==1:

                    print("相手はパーを出して{}さんはチョキだから".format(name))
                    print("勝ち!")
                    win+=1
                elif cpu==2 and me==2:

                    print("相手はパーを出して{}さんもパーだから".format(name))
                    print("あいこだね")
                    draw+=1
                else:
                    pass
            else:
                pass

        else:
            print("正しい数字を入力してね。")
            continue
        time.sleep(1)
        #もう一回やる?
        print("----------------------------------------------------------")
        print("もう一回やる？")
        print("0:やる,1:やらない")
        a=int(input())
        if a==1:
            print("今回の対戦は{}戦{}勝{}敗{}分でした".format(total,win,lose,draw))
            hij=("今回の対戦は{}戦{}勝{}敗{}分でした".format(total,win,lose,draw))
            percentage=int(win/total*100)
            print("勝率は{}%です".format(percentage))
            print("ご利用ありがとうございました。")
            time.sleep(0.5)
            with open("name.txt","w",encoding="utf-8") as w:
                w.write(name)
            with open("result.txt","w",encoding="utf-8")as wr:
                wr.write(hij)
        print("----------------------------------------------------------")
    #違うプレイヤーでやる?
    print("----------------------------------------------------------")
    print("違うプレイヤーでプレイする?")
    print("0:やる,1:やらない")
    player=int(input())
    print("----------------------------------------------------------")
    a=0
    total=0
    win=0
    lose=0
    draw=0
