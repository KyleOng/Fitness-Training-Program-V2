from Tkinter import*
from datetime import date
import Tkinter as tk
import ttk
import tkMessageBox
import time
import random

app=Tk()
app.geometry("600x600")
app.resizable(0,0)
app.title("MMU Fitness Training Program")

#Frame 1 Varaible
today=date.today()

#Frame 2 Variable
Gender=StringVar()
Height=StringVar()
Weight=StringVar()

#Frame 3 Variable
Body=StringVar()

#Frame 4 Variable
ExercisePart=StringVar()

#Frame 5 Variable
Reps=StringVar()

#Frame 6 Variable
ID=StringVar()
Password=StringVar()

CaloriesBurnedArray=[]

f1 = Frame(app)
f2 = Frame(app)
f3 = Frame(app)
f4 = Frame(app)
f5 = Frame(app)
f6 = Frame(app)
f7 = Frame(app)


def raise_frame(frame):
    frame.tkraise()
    
for frame in (f1, f2, f3, f4, f5, f6, f7):
    frame.grid(row=0, column=0, sticky='news')

def update_timeText():
    current = time.strftime("%H:%M:%S")
    timeText.configure(text=current)
    timeText.cget("text")
    f1.after(1000, update_timeText)
    
def BMI():
    Value1=Gender.get()
    Value2=Height.get()
    Value3=Weight.get()
    try:
        if float(Value2)>0:
            if float(Value3)>0:
                BMI = float(Value3)/(float(Value2)*float(Value2)/10000)
                
                if Value1=="Male":                    
                    BMILabel.config(text="Your BMI is " + str("%.4f" %BMI)+" kg/m2")
                    if BMI<=18.5:
                        StatusLabel.config(text="Underweight",fg="blue")
                    elif BMI<=24.9:
                        StatusLabel.config(text="Normal",fg="green")                
                    else:
                        StatusLabel.config(text="Overweight",fg="red")
                    StatusLabel.cget("text")    
                else:
                    BMILabel.config(text="Your BMI is " + str("%.4f" %BMI)+" kg/m2")
                    if BMI<=16.5:           
                        StatusLabel.config(text="Underweight",fg="blue")                
                    elif BMI<=22.9:
                        StatusLabel.config(text="Normal",fg="green")                
                    else:
                        StatusLabel.config(text="Overweight",fg="red")                
                    StatusLabel.cget("text")
            else:
                Height.set("")
                Weight.set("")
                BMILabel.config(text="")  
                StatusLabel.config(text="")
                StatusLabel.cget("text")
                tkMessageBox.showinfo("Error","Please input the correct integer")
        else:
            Height.set("")
            Weight.set("")
            BMILabel.config(text="")  
            StatusLabel.config(text="")
            StatusLabel.cget("text")
            tkMessageBox.showinfo("Error","Please input the correct integer")
    except ValueError:
        Height.set("")
        Weight.set("")
        BMILabel.config(text="")  
        StatusLabel.config(text="")
        StatusLabel.cget("text")
        tkMessageBox.showinfo("Error","Please input the correct integer")
        
        
def Proceed():
    StatusValue=StatusLabel.cget("text")    
    if StatusValue == "":
        Height.set("")
        Weight.set("")
        tkMessageBox.showinfo("Error","Your BMI has not yet calculated\nCaution: Insert the correct value and press Calculate button before press Proceed button ")
    else:
        raise_frame(f3)

def Accept():
    Value4 = Body.get()
    if Value4 == "":
        tkMessageBox.showinfo("Error","Please choose your body part")
    else:
        raise_frame(f4)
        Exercise()

def Exercise():   
    Value4 = Body.get()
    Value5 = StatusLabel.cget("text")

    Image7=PhotoImage(file="Bicepstrain.gif")
    Image8=PhotoImage(file="Chesttrain.gif")
    
    if Value4 == "Biceps":
        ExerciseLabel.config(text="\n"+ "You choose Biceps part Training")
        ImageLabel4.config(image=Image7)
        ImageLabel4.image=Image7
        if Value5 =="Underweight":
            BicepsDropbox=ttk.Combobox(f4,textvariable=ExercisePart, state='readonly',font=("Times New Roman",15))
            BicepsDropbox["values"]=("Concentration Curls", "Seated Dumbbell Curl","Reverse Barbell Curl")
            BicepsDropbox.current(0)
            BicepsDropbox.grid(row=4, column=0)
        elif Value5 =="Normal":
            BicepsDropbox=ttk.Combobox(f4,textvariable=ExercisePart, state='readonly',font=("Times New Roman",15))
            BicepsDropbox["values"]=("Preacher curls", "Standing One-Arm Cable","Close Grip Chin Up")
            BicepsDropbox.current(0)
            BicepsDropbox.grid(row=4, column=0)
        else:
            BicepsDropbox=ttk.Combobox(f4,textvariable=ExercisePart, state='readonly',font=("Times New Roman",15))
            BicepsDropbox["values"]=("Incline Dumbbell Curl", "Barbell Curls","Reverse Plate Curls")
            BicepsDropbox.current(0)
            BicepsDropbox.grid(row=4, column=0)
        AcceptButton2=Button(f4, text='Proceed', command=Description,font=("Times New Roman",15))
        AcceptButton2.grid(row=5, column=0, sticky=N+S)

    elif Value4 == "Chest":
        ExerciseLabel.config(text="\n"+ "You choose Chest part Training")
        ImageLabel4.config(image=Image8)
        ImageLabel4.image=Image8
        if Value5 =="Underweight":
            ChestDropbox=ttk.Combobox(f4,textvariable=ExercisePart, state='readonly',font=("Times New Roman",15))
            ChestDropbox["values"]=("Incline Bench Press", "Decline Bench Press","Dumbbell Bench Press")
            ChestDropbox.current(0)
            ChestDropbox.grid(row=4, column=0)
        elif Value5 =="Normal":
            ChestDropbox=ttk.Combobox(f4,textvariable=ExercisePart, state='readonly',font=("Times New Roman",15))
            ChestDropbox["values"]=("Bench Press", "Incline Dumbbell Press","Decline Barbell Pullover")
            ChestDropbox.current(0)
            ChestDropbox.grid(row=4, column=0)
        else:
            ChestDropbox=ttk.Combobox(f4,textvariable=ExercisePart, state='readonly',font=("Times New Roman",15))
            ChestDropbox["values"]=("Dumbbell Fly", "Standing Cable Chest Press","Dumbbell Pullover")
            ChestDropbox.current(0)
            ChestDropbox.grid(row=4, column=0)
        AcceptButton2=Button(f4, text='Proceed', command=Description,font=("Times New Roman",15))
        AcceptButton2.grid(row=5, column=0,  sticky=N+S)
    else:
        tkMessageBox.showinfo("Error","Please choose your body parts")
        
def Description():
    Value6 = ExercisePart.get()
    
    DesA1="1. Sit down on a flat bench with one dumbbell\n2. Use your right arm to pick the dumbbell up.\n3. Curl the weights forwards.\n4. Slowly begin to bring the dumbbells back to the position.\n5. Repeat the movement."
    DesB1="1. Sit on a flat bench with a dumbbell on each hand\n2. Rotate the palms of the hands so that they are facing your torso\n3. Curl the weights and start twisting the wrists\n4. Slowly begin to bring the dumbbells back to position.\n5. Repeat the movement"
    DesC1="1. Stand up with your torso upright.\n2. The palm of your hands should be facing down\n3. Curl the weight while contracting the biceps.\n4. Slowly begin to bring the bar back \n5. Repeat the movement"
    DesD1="1. You need a preacher bench and an E-Z bar.\n2. Grab the E-Z cur bar at the close inner handle. \n3. The palm of your hands should facing forward and tilted inwards.\n4. Slowly lower the bar until your upper arm is extended. \n4. Curl the weight up and hold it for a second.\n5. Repeat the movement."
    DesE1="1. Start out by grabbing single handle next to the low pulley machine.\n2. Make sure that your upper arm is stationary\n3. Slowly begin to curl the single handle upwards.\n4. Hold the contraction position as you squeeze the bicep .\n5. Repeat the movement with different arm"
    DesF1="1. Grab the pull up bar with the palms facing your torso.\n2. Keep your torso as straight as possible.\n3. Pull your torso up until your head is around the bar.\n4. After a few second, slowly lower your torso back.\n5. Repeat the movement for a few times."
    DesG1="1. Sit down on an incline bench with a dumbbell in each hand.\n2. Curl the right weight forward\n3. Rotate the hand so that the palm is facing up. \n4. Slowly begin to bring the dumbbell back to the point.\n5. Repeat the movement with the left hand. This equals one repetition.\n6. Continue alternating in this manner with a few repetitions"
    DesH1="1. Start by standing straight with \n2. A weighted plate held by both hands,\n3. Slowly lift up the weight as you breathe in.\n4. Slowly lower the weight down. \n5. Repeat for a few repetitions"
    DesI1="1. Standing up with your torso upright \n2. Hold a barbell at a shoulder width grip\n3. Curl the weights forward \n4. Hold the position a few second then bring down slowly.\n5. Repeat the movement"
    DesA2="1. Load the bar to an appropriate weight\n2. Lay on the bench \n3. Hold the weight above your chest\n4. Lower the bar to the sternum \n5. extend elbow to return the bar to the position."
    DesB2="1. Secure your legs and lay on the bench\n2. Lift the bar to the neck. \n3. Come down slowly until the bar is at your lower chest\n4. After the second pause, bring the bar back to the position\n5. Repeat the movement"
    DesC2="1. Lie down on a flat bench \n2. Palms facing each other\n3. Using the thighs to raise the dumbbells up\n4. Rotate your wrist forward,\n5. The dumbbells should be at the sides of your chest\n6. Press the dumbbells up, hold up a second \n7. Bring it down slowly."
    DesD2="1. Lie back on a flat bench \n2. Use a medium width grip at a 90 degree position.\n3. Push the bar toward you.\n4. Reverse motion until the bar touches the chest.\n5. Repeat the movement."
    DesE2="1. Lie back on an incline bench \n2. A dumbbell on each hand.\n3. Push the dumbbells up.\n4. Rotate wrist towards you.\n5. Lock your arms at the top, hold for a second and \n6. Slowly lower the height.\n7. Repeat the movement"
    DesF2="1. Lie down on a decline bench\n2. Reach for the barbell behind the head.\n3. Slowly lift the barbell up from the floor.\n4. Move the barbell back down in a semicircular motion \n5. Now bring the dumbbell up \n6. Repeat the movement"
    DesG2="1. Hold the dumbbell on each hand \n2. Lieon the bench of not more than 30 degree.\n3. Extend your arm above you with a slight bend on the elbow\n4. Rotate your wrist as the palm facing you\n5. Lower the arms to the side while extending your arm\n6. Rotating your wrist facing each other.\n7. Reverse the motion and repeat the whole movement"
    DesH2="1. Position dual pulleys to chest height.\n2. Position your upper arm at a 90 degree.\n3. Keep the body stationary \n4. Extend through elbows to press the handles forward.\n5. Pause at the top of the motion and repeat."
    DesI2="1. Place a dumbbell standing up on the chest\n2. Graps your dumbbell with both hands \n3. hold it straight over the chest at the arms length\n4. Slowly bring down the dumbbell in an arc behind your head.\n5. Reverse the motion and repeat the whole movement"
    
    ImageA1=PhotoImage(file="comA.gif")
    ImageB1=PhotoImage(file="comB.gif")
    ImageC1=PhotoImage(file="comC.gif")
    ImageD1=PhotoImage(file="comD.gif")
    ImageE1=PhotoImage(file="comE.gif")
    ImageF1=PhotoImage(file="comF.gif")
    ImageG1=PhotoImage(file="comG.gif")
    ImageH1=PhotoImage(file="comH.gif")
    ImageI1=PhotoImage(file="comI.gif")
    ImageA2=PhotoImage(file="comA2.gif")
    ImageB2=PhotoImage(file="comB2.gif")
    ImageC2=PhotoImage(file="comC2.gif")
    ImageD2=PhotoImage(file="comD2.gif")
    ImageE2=PhotoImage(file="comE2.gif")
    ImageF2=PhotoImage(file="comF2.gif")
    ImageG2=PhotoImage(file="comG2.gif")
    ImageH2=PhotoImage(file="comH2.gif")
    ImageI2=PhotoImage(file="comI2.gif")
        
    if Value6<>"":
        if Value6=="Concentration Curls":
            ExerciseTitle.config(text="Concentration Curls")
            ImageLabel9.config(image=ImageA1)
            ImageLabel9.image=ImageA1
            DescLabel.config(text=DesA1)
            
                
        elif Value6=="Seated Dumbbell Curl":
            ExerciseTitle.config(text="Seated Dumbbell Curl")
            ImageLabel9.config(image=ImageB1)
            ImageLabel9.image=ImageB1
            DescLabel.config(text=DesB1)
                
        elif Value6=="Reverse Barbell Curl":
            ExerciseTitle.config(text="Reverse Barbell Curl")
            ImageLabel9.config(image=ImageC1)
            ImageLabel9.image=ImageC1
            DescLabel.config(text=DesC1)
                
        elif Value6=="Preacher curls":
            ExerciseTitle.config(text="Preacher curls")
            ImageLabel9.config(image=ImageD1)
            ImageLabel9.image=ImageD1
            DescLabel.config(text=DesD1)
                
        elif Value6=="Standing One-Arm Cable":
            ExerciseTitle.config(text="Standing One-Arm Cable")
            ImageLabel9.config(image=ImageE1)
            ImageLabel9.image=ImageE1
            DescLabel.config(text=DesE1)
                
        elif Value6=="Close Grip Chin Up":
            ExerciseTitle.config(text="Close Grip Chin Up")
            ImageLabel9.config(image=ImageF1)
            ImageLabel9.image=ImageF1
            DescLabel.config(text=DesF1)
                
        elif Value6=="Incline Dumbbell Curl":
            ExerciseTitle.config(text="Incline Dumbbell Curl")
            ImageLabel9.config(image=ImageG1)
            ImageLabel9.image=ImageG1
            DescLabel.config(text=DesG1)
                
        elif Value6=="Barbell Curls":
            ExerciseTitle.config(text="Barbell Curls")
            ImageLabel9.config(image=ImageH1)
            ImageLabel9.image=ImageH1
            DescLabel.config(text=DesH1)
                
        elif Value6=="Reverse Plate Curls":
            ExerciseTitle.config(text="Reverse Plate Curls")
            ImageLabel9.config(image=ImageI1)
            ImageLabel9.image=ImageI1
            DescLabel.config(text=DesI1)
                
        elif Value6=="Incline Bench Press":
            ExerciseTitle.config(text="Incline Bench Press")
            ImageLabel9.config(image=ImageA2)
            ImageLabel9.image=ImageA2
            DescLabel.config(text=DesA2)
                
        elif Value6=="Decline Bench Press":
            ExerciseTitle.config(text="Decline Bench Press")
            ImageLabel9.config(image=ImageB2)
            ImageLabel9.image=ImageB2
            DescLabel.config(text=DesB2)
                
        elif Value6=="Dumbbell Bench Press":
            ExerciseTitle.config(text="Dumbbell Bench Press")
            ImageLabel9.config(image=ImageC2)
            ImageLabel9.image=ImageC2
            DescLabel.config(text=DesC2)
                
        elif Value6=="Bench Press":
            ExerciseTitle.config(text="Bench Press")
            ImageLabel9.config(image=ImageD2)
            ImageLabel9.image=ImageD2
            DescLabel.config(text=DesD2)
                
        elif Value6=="Incline Dumbbell Press":
            ExerciseTitle.config(text="Incline Dumbbell Press")
            ImageLabel9.config(image=ImageE2)
            ImageLabel9.image=ImageE2
            DescLabel.config(text=DesE2)
                
        elif Value6=="Decline Barbell Pullover":
            ExerciseTitle.config(text="Decline Barbell Pullover")
            ImageLabel9.config(image=ImageF2)
            ImageLabel9.image=ImageF2
            DescLabel.config(text=DesF2)
                
        elif Value6=="Dumbbell Fly":
            ExerciseTitle.config(text="Dumbbell Fly")
            ImageLabel9.config(image=ImageG2)
            ImageLabel9.image=ImageG2
            DescLabel.config(text=DesG2)
                
        elif Value6=="Standing Cable Chest Press":
            ExerciseTitle.config(text="Standing Cable Chest Press")
            ImageLabel9.config(image=ImageH2)
            ImageLabel9.image=ImageH2
            DescLabel.config(text=DesH2)
                
        elif Value6=="Dumbbell Pullover":
            ExerciseTitle.config(text="Dumbbell Pullover")
            ImageLabel9.config(image=ImageI2)
            ImageLabel9.image=ImageI2
            DescLabel.config(text=DesI2)
        raise_frame(f5)        
    else:
        DescLabel.config(text="")

def Calories():
    Value7 = Reps.get()
    try:
        if int(Value7) >0:
            CaloriesBurned= float(Value7) * 1.68
            Answer = tkMessageBox.askquestion("","Do you want to repeat the exercise?")
            if Answer == "yes":
                CaloriesBurnedArray.append(CaloriesBurned)
                raise_frame(f3)
                BodyDropbox.current(0)
                Reps.set("")    
                print CaloriesBurnedArray
            else:
                CaloriesBurnedArray.append(CaloriesBurned)
                raise_frame(f6)
                Summary()
                print CaloriesBurnedArray
        else:
            tkMessageBox.showinfo("Error","Please input the correct integer")
    except ValueError:
        tkMessageBox.showinfo("Error","Please input the correct integer")

def Summary():
    Value8 = StatusLabel.cget("text")
    Value9 = sum(CaloriesBurnedArray)
    Value10 = timeText.cget("text")

    SummaryLabel=Label(f6, text= "SUMMARY",font=("Times New Roman",20),fg="Magenta").grid(row=0, column=0)

    DateLabel = Label(f6, text="Date: "+str(today),font=("Times New Roman",15)).grid(row=1, column=0,sticky=W)
    
    TimeLabel = Label(f6, text = "Time: "+str(Value10),font=("Times New Roman",15)).grid(row=2, column=0,sticky=W)
    
    BMIsummaryLabel=Label(f6, text= "BMI: "+Value8,font=("Times New Roman",15)).grid(row=3, column=0,sticky=W)
    
    TotalCaloriesLabel=Label(f6, text= "Total Calories Burned: " + str(Value9),font=("Times New Roman",15)).grid(row=4, column=0,sticky=W)

    Nutrition()

def Nutrition():
    Value8 = StatusLabel.cget("text")
    UnderNutrition1="Cereal with milk and sugar \nFull-cream milk with fruit and honey \nMeat, fish or poultry \nPotato, sweet potato, rice or pasta \nVegetable or salad with salad dressing or mayonnaise \nSandwiches with chopped nuts"
    UnderNutrition2="Boiled egg or bacon or sausage \nFruit juice with dried fruit or energy bar \nMeat, fish or poultry \nPotato, sweet potato, rice or pasta \nVegetable or salad with salad dressing or mayonnaise \nSandwiches with peanut butter or cream cheese"
    UnderNutrition3="Wholewheat toast or roll with butter and jam \nMilky drink  \nMeat, fish or poultry \nPotato, sweet potato, rice or pasta \nVegetable or salad with salad dressing or mayonnaise \nSandwiches with egg mayonnaise"

    NormalNutrition1="Chicken breast \nWhey protein shake \nWhite rice, egg whites \nBeans, peas, and lentils \nWhole-grain bread \nGreen salad with fat-free dressing"
    NormalNutrition2="Turkey breast \nWhey protein shake \nBrown rice, egg whites \nCarrots, sweet potatoes or pumpkin  \nWhole-grain toast with low-sugar jam \nGreen salad with fat-free dressing"
    NormalNutrition3="Ground beef (95% lean) \nWhey protein shake \nPasta, egg whites \nBroccoli or kale  \nOatmeal with raisin bagels \nGreen salad with fat-free dressing"

    OverNutrition1="Rice, wholegrain bread and polenta \nDark green veggies, such as broccoli, kale\nLow-fat or fat-free milk \nLean protein such as fish, beans, peas, nuts, and seeds \nPlenty water and limit salt"
    OverNutrition2="Pasta, cereals, couscous and barley \nOrange veggies, such as pumpkin, and winter squash \nLow-fat yogurt \nLean protein such as fish, beans, peas, nuts, and seeds \nPlenty water and limit salt"
    OverNutrition3="Noodles, quinoa and oats \nBeans and peas, such as pinto beans, and split peas \nLow-fat cheese \nLean protein such as fish, beans, peas, nuts, and seeds \nPlenty water and limit salt"

    UnderNutrition=[UnderNutrition1,UnderNutrition2,UnderNutrition3]
    NormalNutrition=[NormalNutrition1,NormalNutrition2,NormalNutrition3]
    OverNutrition=[OverNutrition1,OverNutrition2,OverNutrition3]
    
    if Value8 == "Underweight":
        NutritionLabel.config(text=random.choice(UnderNutrition))
                              
    elif Value8 == "Normal":
        NutritionLabel.config(text=random.choice(NormalNutrition))
        
    else:
        NutritionLabel.config(text=random.choice(OverNutrition))
    Value11 = NutritionLabel.cget("text")

def Register():
    Value12 = ID.get()
    Value13 = Password.get()
    IDfile = open("ID.txt","r")
    
   
    try:
        
        if int(Value12)>0:
            if Value13<>"":
                counter=0
                while counter==0:
                    x=IDfile.readline()
                    if Value12 <> x.strip():
                        if x == "":
                            IDfile.close()
                            IDfile = open("ID.txt","a")
                            IDfile.write("\n"+str(Value12))
                            IDfile.close()
                                    
                            Passwordfile = open("Password.txt","a")
                            Passwordfile.close()
                            Passwordfile = open("Password.txt","a")
                            Passwordfile.write("\n"+str(Value12+Value13))
                            Passwordfile.close()

                            tkMessageBox.showinfo("Congratulation","Your account has been registered, you can login now")
                            counter=1
                        else:
                            counter=0
                    else:
                        tkMessageBox.showinfo("Error","This account has been registered, please use another ID")
                        counter=1
                    
                        
            else:
                tkMessageBox.showinfo("Error","Fill in your password")
        else:
            tkMessageBox.showinfo("Error","Username cannot leaved blank or inserted by using alphabet,negative value, and decimal")
        
    except ValueError:
        tkMessageBox.showinfo("Error","Username cannot leaved blank or inserted by using alphabet,negative value, and decimal")
    
def Authentication():
    
    Value8 = StatusLabel.cget("text")
    Value9 = sum(CaloriesBurnedArray)
    Value10 = timeText.cget("text")
    Value11 = NutritionLabel.cget("text")
    Value12 = ID.get()
    Value13 = Password.get()
    Value14 = str(Value12) + ".txt"

    IDfile = open("ID.txt","r")

    if Value12<>"":
        if Value13<>"":
            counter=0
            while counter==0:
                y=IDfile.readline()
                if Value12 <> y.strip():
                    if y == "":
                        IDfile.close()
                        tkMessageBox.showinfo("Error","Wrong ID,password or both")           
                        counter=1
                    else:
                        counter=0
                else:
                    IDfile.close()
                    Passwordfile = open("Password.txt","r")
                    counter2=0
                    while counter2==0:
                        y=Passwordfile.readline()
                        if (Value12+Value13) <> y.strip():
                            if y == "":            
                                tkMessageBox.showinfo("Error","Wrong ID,password or both")
                                Passwordfile.close()
                                counter2=1
                            else:
                                counter2=0
                        else:
                            raise_frame(f7)
                            Waterdes="Water is a necessity to humans,\nso you need to drink at least 8 glasses of water per day\nTry to reduce carbonated drinks and drink more green tea"
                            Sleepdes="An average person need to have at least 7 to 8 hours of sleep\nour body need to have enough rest\nso that it will increase the effectiveness of healthy diet or stay healthy"
                            Stressdes="Do you know that exercise or workout can reduce stress?\nWhen you exercise, you body release endorphins\nwhich can act as a painkiller\nwhich can also improve sleep and diet effectiveness"
                            
                            FactsTitle=Label(f7,text="Fitness Facts",font=("Times New Roman",20),fg="Blue").grid(row=0,column=0)
                            WaterLabel=Label(f7,text=Waterdes,font=("Times New Roman",15),justify=LEFT).grid(row=1,column=0,sticky=W)
                            SleepLabel=Label(f7,text=Sleepdes,font=("Times New Roman",15),justify=LEFT).grid(row=2,column=0,sticky=W)
                            StressLabel=Label(f7,text=Stressdes,font=("Times New Roman",15),justify=LEFT).grid(row=3,column=0,sticky=W)
                            HistoryTitle=Label(f7,text="\n"+"History",font=("Times New Roman",20),fg="Blue").grid(row=4,column=0)
                            
                            Descfile = open(Value14,"a")
                            Descfile.write("\n"+"Date: "+str(today)+"\n"+"Time: "+str(Value10)+"\n"+"BMI: "+str(Value8)+"\n"+"Total Calories Burned: "+str(Value9)+"\n"+"Nutrition Suggestion: "+ "\n"+ str(Value11)+"\n")
                            Descfile.close()

                            Descfile = open(Value14,"r")
                                              
                            SavedLabel = Descfile.readlines()

                            
                            scrollbar = Scrollbar(f7, orient="vertical")
                            box=Listbox(f7,yscrollcommand=scrollbar.set,width=50,font=("Times New Roman",15))
                            scrollbar.config(command=box.yview)
                            scrollbar.grid(row=7,column=1,sticky="news")

                            for i in SavedLabel:
                                box.insert(tk.END, str(i))
    

                            box.grid(row=7,column=0,sticky="news")

                            counter2=1
                    counter=1
        else:
            tkMessageBox.showinfo("Error","Wrong ID,password or both")
    else:
        tkMessageBox.showinfo("Error","Wrong ID,password or both")
    
       
#Frame 1
def About():
    tkMessageBox.showinfo("About","This is Fitness Training Program \n made by Group Supreme")
    
Image1 = PhotoImage(file="Gym.gif")
ImageLabel1=Label(f1, image=Image1, height=200)
ImageLabel1.grid(row=1,column=0)

Title = Label(f1, text="MMU Fitness Training", font=("Times New Roman",40),bg="grey")
Title.grid(row=1,column=0)

Date = Label(f1,text=(today),font=("Times New Roman",20)).grid(row=2,column=0)

timeText = Label(f1, text="", font=("Times New Roman",20))
timeText.grid(row=3,column=0)
update_timeText()

StartButton=Button(f1,text="Start",command=lambda:raise_frame(f2),font=("Times New Roman",20),bg="grey", width=10).grid(row=4,column=0)

BlankLabel2=Label(f1,text="").grid(row=5,column=0)

AboutButton=Button(f1,text="About",command=About,font=("Times New Roman",20),bg="grey", width=10).grid(row=6,column=0)

#Frame 2
def change_image(*args):
    Value1=Gender.get()
            
    Image2=PhotoImage(file="Boy.gif")
    Image3=PhotoImage(file="Girl.gif")
    
    if Value1=="Male":       
        ImageLabel2.config(image=Image2)
        ImageLabel2.image=Image2
    else:        
        ImageLabel2.config(image=Image3)
        ImageLabel2.image=Image3
    Height.set("")
    Weight.set("")
    BMILabel.config(text="")  
    StatusLabel.config(text="")
    StatusLabel.cget("text")

def change_height(*args):
    BMILabel.config(text="")  
    StatusLabel.config(text="")
    StatusLabel.cget("text")

def change_weight(*args):
    BMILabel.config(text="")  
    StatusLabel.config(text="")
    StatusLabel.cget("text")

F2TitleLabel=Label(f2,text="User's Biography",font=("Arial",10))
F2TitleLabel.grid(row=0, column=0, sticky=N)
   
Image2=PhotoImage(file="Boy.gif")
ImageLabel2=Label(f2,image=Image2)
ImageLabel2.grid(row=0,column=4)

GenderLabel=Label(f2,text="Gender:",font=("Times New Roman",20)).grid(row=3,column=3,sticky=E)
GenderDropbox= ttk.Combobox(f2,textvariable=Gender,state='readonly',font=("Times New Roman",15))
GenderDropbox["values"] = ("Male","Female")
GenderDropbox.current(0)
GenderDropbox.grid(column=4, row=3,sticky=W)
Gender.trace("w", change_image)

HeightLabel=Label(f2,text="Height:",font=("Times New Roman",20)).grid(row=4, column=3,sticky=E)
HeightSIunit=Label(f2,text="cm",font=("Times New Roman",20)).grid(row=4, column=5)
HeightEntry=Entry(f2,textvariable=Height,font=("Times New Roman",15)).grid(row=4, column=4,sticky=W)
Height.trace("w", change_height)

WeightLabel=Label(f2,text="Weight:",font=("Times New Roman",20)).grid(row=5, column=3,sticky=E)
WeightSIunit=Label(f2,text="kg",font=("Times New Roman",20)).grid(row=5, column=5)                          
WeightEntry=Entry(f2,textvariable=Weight,font=("Times New Roman",15)).grid(row=5, column=4, sticky=W)
Weight.trace("w", change_height)

CalculateBttn=Button(f2,text="Calculate",command= BMI,font=("Times New Roman",15)).grid(row=6, column=4, sticky=W)

BMILabel=Label(f2,text="",font=("Times New Roman",14))
BMILabel.grid(row=1, column=4, sticky=W)

StatusLabel=Label(f2,text="",font=("Times New Roman",15))
StatusLabel.grid(row=2, column=4)

ProceedBttn=Button(f2, text="Proceed",font=("Times New Roman",15), command= Proceed)
ProceedBttn.grid(row=6, column=4, sticky=E)

#Frame3
def change_part(*args):
    Value4 = Body.get()
    Image4=PhotoImage(file="Biceps_1.gif")
    Image5=PhotoImage(file="Chest_1.gif")
    
    
    if Value4 == "Chest":
        ImageLabel3.config(image=Image5)
        ImageLabel3.image=Image5
    else:
        ImageLabel3.config(image=Image4)
        ImageLabel3.image=Image4

F3TitleLabel=Label(f3,text="User's Body Parts Selection",font=("Arial",10))
F3TitleLabel.grid(row=0, column=0, sticky=W+N)

Image4=PhotoImage(file="Biceps_1.gif")
ImageLabel3=Label(f3,image=Image4)
ImageLabel3.grid(row=0,column=1)

BodyLabel=Label(f3,text="\n"+ "\n"+"Choose your body part",font=("Times New Roman",15)).grid(row=1, column=1,columnspan=2) 
BodyDropbox=ttk.Combobox(f3,textvariable=Body, state='readonly',font=("Times New Roman",15))
BodyDropbox["values"]=("Biceps", "Chest")
BodyDropbox.current(0)
BodyDropbox.grid(row=2, column=1, rowspan=2)

Body.trace("w", change_part)

AcceptButton1=Button(f3,text="Accept", command=Accept,font=("Times New Roman",15)).grid(row=4, column=1, rowspan=2, sticky=N+S)

#Frame 4
F4TitleLabel=Label(f4,text="User's Exercise Selection",font=("Arial",10))
F4TitleLabel.grid(row=0, column=0, sticky=W)

ExerciseLabel=Label(f4,text="",font=("Times New Roman",15))
ExerciseLabel.grid(row=2, column=0)

Image6=PhotoImage(file="")
ImageLabel4=Label(f4,image=Image6)
ImageLabel4.grid(row=1,column=0)

#Frame 5
F5TitleLabel=Label(f5,text="User's Exercise Description",font=("Arial",10))
F5TitleLabel.grid(row=0, column=0, sticky=W)

ExerciseTitle=Label(f5,text="",font=("Times New Roman",20))
ExerciseTitle.grid(row=2, column=0)

DescLabel=Label(f5,text="",font=("Times New Roman",15),justify=LEFT)
DescLabel.grid(row=3, column=0, sticky=W)

RepsLabel=Label(f5,text="Repetition: ",font=("Times New Roman",15)).grid(row=5,column=0)
RepsEntry=Entry(f5,textvariable=Reps,font=("Times New Roman",15)).grid(row=6,column=0)

CalculateBttn2=Button(f5,text="Calculate Calories Burn", command=Calories,font=("Times New Roman",15)).grid(row=7,column=0)

Image9=PhotoImage(file="")
ImageLabel9=Label(f5,image=Image9)
ImageLabel9.grid(row=1,column=0,sticky=N+S)

#Frame 6
NutritionTitle=Label(f6,text="Nutrition Suggestion: ",font=("Times New Roman",15),justify=LEFT)
NutritionTitle.grid(row=6,column=0,sticky=W)

NutritionLabel=Label(f6, text= "",font=("Times New Roman",15),justify=LEFT)
NutritionLabel.grid(row=7,column=0,sticky=W)

BlankLabel1=Label(f6,text="")
BlankLabel1.grid(row=8,column=0)

IDLabel=Label(f6,text="Username:",font=("Times New Roman",15))
IDLabel.grid(row=10,column=0,sticky=W)
IDEntry=Entry(f6,textvariable=ID,width=10,font=("Times New Roman",15))
IDEntry.grid(row=10,column=0)

PasswordLabel=Label(f6,text="Password:",font=("Times New Roman",15))
PasswordLabel.grid(row=11,column=0,sticky=W)
Passwordntry=Entry(f6,textvariable=Password,width=10,font=("Times New Roman",15),show="*")
Passwordntry.grid(row=11,column=0)

LoginButton=Button(f6,text="Login",font=("Times New Roman",15), command= Authentication, width=7).grid(row=12,column=0)
SignupButton=Button(f6,text="Sign up",font=("Times New Roman",15), command= Register, width=7).grid(row=13,column=0)

BlankLabel3=Label(f6,text="                                                                                                                  ",font=("Times New Roman",15)).grid(row=14,column=0)


raise_frame(f1)
app.mainloop()



