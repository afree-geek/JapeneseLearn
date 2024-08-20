import random

fiftySoundQingPing={'あ':'a','い':'i','う':'u','え':'e','お':'o','か':'ka','き':'ki','く':'ku','け':'ke','こ':'ko',
      'さ':'sa','し':'xi','す':'su','せ':'se','そ':'so','た':'ta','ち':'qi','つ':'ci','て':'te','と':'to',
      'な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no','は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho',
      'ま':'ma','み':'mi','む':'mu','め':'me','も':'mo','や':'ya','ゆ':'yu','よ':'yo','ら':'ra','り':'ri',
      'る':'ru','れ':'re','ろ':'ro','わ':'wa','を':'o','ん':'n'}

fiftySoundQingPian={'ア':'a','イ':'i','ウ':'u','エ':'e','オ':'o','カ':'ka','キ':'ki','ク':'ku','ケ':'ke','コ':'ko',
      'サ':'sa','シ':'xi','ス':'su','セ':'se','ソ':'so','タ':'ta','チ':'qi','ツ':'ci','テ':'te','ト':'to',
      'ナ':'na','ニ':'ni','ヌ':'nu','ネ':'ne','ノ':'no','ハ':'ha','ヒ':'hi','フ':'fu','ヘ':'he','ホ':'ho',
      'マ':'ma','ミ':'mi','ム':'mu','メ':'me','モ':'mo','ヤ':'ya','ユ':'yu','ヨ':'yo','ラ':'ra','リ':'ri',
      'ル':'ru','レ':'re','ロ':'ro','ワ':'wa','ヲ':'o','ン':'n'}

total,error=0,0
mode=input("请选择练习科目(1.平假名清音，2.片假名清音):")
if mode=='1':
      while True:
            randomKey = random.sample(list(fiftySoundQingPing.keys()), 1)
            print(randomKey[0])
            whetherSee = input("请输入读音:")
            if whetherSee!=fiftySoundQingPing[randomKey[0]]:
                  error+=1
                  print("\033[31m"+fiftySoundQingPing[randomKey[0]]+"\033[0m")
            total+=1
            print("当前得分率:"+"\033[32m"+str('%.2f'%((1-error/total)*100))+"%"+"\033[0m"+"      (总回答次数:"+str(total)+")")
elif mode=='2':
      while True:
            randomKey = random.sample(list(fiftySoundQingPian.keys()), 1)
            print(randomKey[0])
            whetherSee = input("请输入读音:")
            if whetherSee!=fiftySoundQingPian[randomKey[0]]:
                  error+=1
                  print("\033[31m"+fiftySoundQingPian[randomKey[0]]+"\033[0m")
            total+=1
            print("当前得分率:"+"\033[32m"+str('%.2f'%((1-error/total)*100))+"%"+"\033[0m"+"      (总回答次数:"+str(total)+")")