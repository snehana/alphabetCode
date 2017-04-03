import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = 'lib/x64' if sys.maxsize > 2**32 else 'lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
import os
import math
import copy
import pygame
import pickle
class SampleListener(Leap.Listener):
    cnt = 0                                                                                         
    count = 0
    flg_main = 0
    flg = 0
    fr1 = [0, 0, 0, 0, 0]                                                                           
    fr2 = [0, 0, 0, 0, 0]                                                                           
    def on_frame(self, controller):
        if SampleListener.flg == 1:                                                                 
            if SampleListener.cnt == 300:
                for i in range(0, 5):
                    SampleListener.fr1[i] /= 300                                                    
                    SampleListener.fr2[i] /= 300
                 
                print("-------------------------------------------------------------------")
                SampleListener.cnt = 0                                                              
                SampleListener.flg = 0
                SampleListener.flg_main = 1
            else:
                frame = controller.frame()
                hand = frame.hands[0]
                pointables = hand.pointables
                i = -1
                for pointable in pointables:
                    i = i + 1
                    SampleListener.fr1[i] += math.sqrt((pointable.direction[0]) ** 2 + (pointable.direction[2]) ** 2)
                    SampleListener.fr2[i] += math.sqrt((pointable.stabilized_tip_position[0]-hand.stabilized_palm_position[0]) ** 2 + (pointable.stabilized_tip_position[2]-hand.stabilized_palm_position[2]) ** 2)
                SampleListener.cnt = SampleListener.cnt + 1                                         

class letters:                                                              
    def _init(self):
        self.letter
        self.fing1                                              
        self.fing2                                              

    def isthis(self,f1,f2):
        
        cnt =0
        for i in f1:
         
            if i>(self.fing1[cnt]+.12) or i<(self.fing1[cnt]-.12):		
                return False
            cnt+=1
        cnt = 0
        for i in f2:
          
            if i>(self.fing2[cnt]+9) or i<(self.fing2[cnt]-9):
                return False
            cnt+=1
        return True

def main():
    listener = SampleListener()
    controller = Leap.Controller()                              
    controller.add_listener(listener)                           
    obj = []
    PIK="pickle.dat"
    os.system('cls')                                            
    while 1==1:                                                 
       what_to_do = raw_input("Enter your choice 'c' or 'l'or 'exit':")
       if what_to_do == "l":
           was_exited =1;
           SampleListener.flg = 1                                                     
           while 1==1:                                                                
                if SampleListener.flg_main == 1:                                       
                    letter = letters()
                    letter.letter = raw_input("Enter letter:")
                    letter.fing1 = copy.deepcopy(SampleListener.fr1)                   
                    letter.fing2 = copy.deepcopy(SampleListener.fr2)
                    obj.append(letter)
                    SampleListener.flg_main = 0                                        
                    break

       what_to_do = raw_input("Enter your choice 'c' or 'l'or 'exit':") 
       if what_to_do == "exit":
            print "hy"
            SampleListener.flg = 1
            with open('data.txt','a') as f:
                pickle.dump(letter.letter,f)
                pickle.dump(letter.fing1,f)
                pickle.dump(letter.fing2,f)
                

       what_to_do = raw_input("Enter your choice 'c' or 'l'or 'exit':") 
       if what_to_do == "c":
            SampleListener.flg = 1

            if was_exited == 0:
             with open('data.txt','rb') as f:
              obj=pickle.load(f)
                         
       while 1==1:                                                                
                
                if SampleListener.flg_main == 1:

                    
                    for o in obj:                                                       
                        
                    
                        x = SampleListener.fr1
                        y = SampleListener.fr2
                        
                        a = o.isthis(x,y)
                        
                        if a == True:                                                   
                            print o.letter
                            output = o.letter
                            l=ord(output)
                            if l>96:
                                PATH = "C:\Users\TRISHNA KOUTHANKAR\Downloads\sound"
                                files=filter(lambda filename: filename.split(".")[-1]=="mp3",os.listdir(PATH))
    
                                file_index = l-97
   

                                for filename in os.listdir("C:\Users\TRISHNA KOUTHANKAR\Desktop\correct output of number project"):
                                    pygame.mixer.init()
                                    pygame.mixer.music.load(files[file_index])
        
                                    pygame.mixer.music.play()   
                            elif l<96:
                                PATH = "C:\Users\TRISHNA KOUTHANKAR\Downloads\sound1"
                                files=filter(lambda filename: filename.split(".")[-1]=="mp3",os.listdir(PATH))
    
                                del files[2]
                                files[10:10]=['10.mp3']
    
                                file_index = l-48
   
                                for filename in os.listdir("C:\Users\TRISHNA KOUTHANKAR\Desktop\correct output of number project"):
                                    pygame.mixer.init()
                                    pygame.mixer.music.load(files[file_index])
        
                                    pygame.mixer.music.play()

                            '''if o.letter=='1':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\1.mp3'
                                clip = mp3play.load(filename)

                                clip.play()
    

                            elif o.letter == '2':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\2.mp3'
                                clip = mp3play.load(filename)
                                clip.play()


                            elif o.letter == '3':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\3.mp3'
                                clip = mp3play.load(filename)

                                clip.play()

                            elif o.letter == '4':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\4.mp3'
                                clip = mp3play.load(filename)

                                clip.play()

                            elif o.letter == '5':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\5.mp3'
                                clip = mp3play.load(filename)

                                clip.play()
                            elif o.letter == '6':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\6.mp3'
                                clip = mp3play.load(filename)

                                clip.play()
                            elif o.letter == '7':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\7.mp3'
                                clip = mp3play.load(filename)

                                clip.play()
                            elif o.letter == '8':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\8.mp3'
                                clip = mp3play.load(filename)

                                clip.play()
                            elif o.letter == '9':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\9.mp3'
                                clip = mp3play.load(filename)

                                clip.play()
                            elif o.letter == '10':
                                filename = r'C:\Users\TRISHNA KOUTHANKAR\Downloads\sound\10.mp3'
                                clip = mp3play.load(filename)

                                clip.play()'''


                                






                            break
                        print "false"
                    SampleListener.flg_main = 0
                    break

    try:
        sys.stdin.readline()                                
    except KeyboardInterrupt:                                   
        pass
    finally:
        controller.remove_listener(listener)
if __name__ == '__main__':
    main()
