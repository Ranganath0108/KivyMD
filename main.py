from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

screen_helper = """
ScreenManager:
    MainScreen:
    Secondary:
    ThirdScreen:
    LastScreen:
    AboutScreen:
<MainScreen>
    name:'main'
    MDToolbar:
        title: 'VTU SGPA CALUCLATOR(only for 2019-20)'
        type:'top'
        pos_hint: {'center_x':0.5,'center_y':0.95}
        
    MDRectangleFlatButton:
        text:'Lets start!...'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:root.manager.current='second'
    Image:
        source:'vtu.jpg'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint_x:0.2
        size_hint_y:0.2
        
<MyField@MDTextField>:
    max_text_length:2
    mode:"rectangle"
    helper_text: "Enter your external marks of previous sem"
    helper_text_mode: "on_focus"
    input_filter:'int'
<MyiField@MDTextField>:
    max_text_length:2
    mode:"rectangle"
    helper_text: "Enter your internal marks of even sem"
    helper_text_mode: "on_focus"
    input_filter:'int'
<MyLabel@MDLabel>:
    halign:'center'
<MyMainLabel@MDTextField>:
    halign:'center'
    font_style:'H1'
    
    
<MyGrid@MDGridLayout>:
    padding:10
    spacing:40
        
<MyButton@MDRectangleFlatButton>:
    pos_hint: {'center_x':0.5,'center_y':0.5}
    text_color:0,0,0,1
    md_bg_color:0,0,1,0.4

    

<Secondary>
    name:'second'
    BoxLayout:
        orientation:'vertical'
        spacing:10
        padding:130
        MyMainLabel:
            text:"ENTER THE EXTERNAL MARKS OF PREVIOUS SEM(for 60)" 
        
        MyField:
            id:esub_1
            hint_text: "SUBJECT1"
        MyField:
            id:esub_2
            hint_text: "SUBJECT2"
        MyField:
            id:esub_3
            hint_text: "SUBJECT3"
        MyField:
            id:esub_4
            hint_text: "SUBJECT4"
        MyField:
            id:esub_5
            hint_text: "SUBJECT5"
        MyField:
            id:esub_6
            hint_text: "SUBJECT6"
        MyField:
            id:esub_7
            hint_text: "SUBJECT7"
        MyField:
            id:esub_8
            hint_text: "SUBJECT8"
        MyField:
            id:esub_9
            hint_text: "SUBJECT9"
        MyButton:
            text:"Next->"
            on_press:app.avg_of_external([esub_1.text,esub_2.text,esub_3.text,esub_4.text,esub_5.text,esub_6.text,esub_7.text,esub_8.text,esub_9.text])
            on_release:root.manager.current='third'
        MyButton:
            text:"BACK"
            on_release:root.manager.current='main'
            
<ThirdScreen>
    name:'third'
    BoxLayout:
        orientation:'vertical'
        spacing:10
        padding:100
        MyMainLabel:
            text:"ENTER THE INTERNAL MARKS OF THIS SEM(for 40)"    
        MyiField:
            id:insub_1
            hint_text: "SUBJECT1"
        MyiField:
            id:insub_2
            hint_text: "SUBJECT2"
        MyiField:
            id:insub_3
            hint_text: "SUBJECT3"
        MyiField:
            id:insub_4
            hint_text: "SUBJECT4"
        MyiField:
            id:insub_5
            hint_text: "SUBJECT5"
        MyiField:
            id:insub_6
            hint_text: "SUBJECT6"
        MyiField:
            id:insub_7
            hint_text: "SUBJECT7"
        MyiField:
            id:insub_8
            hint_text: "SUBJECT8"
        MyiField:
            id:insub_9
            hint_text: "SUBJECT9"
        MyButton:
            text:"Next->"
            on_press:app.finalaization([insub_1.text,insub_2.text,insub_3.text,insub_4.text,insub_5.text,insub_6.text,insub_7.text,insub_8.text,insub_9.text])
            on_release:root.manager.current='last'
        MyButton:
            text:"BACK"
            on_release:root.manager.current='main'

            
<LastScreen>
    name:'last'
    
    BoxLayout:
        orientation:'vertical'
        spacing:5
        padding:50
        MyMainLabel:
            text:"RESULTS"
        MyGrid:
            cols:2
            MyLabel:
                text:"SGPA"
            MyLabel:
                id:sgpa_label
                text:" "
            MyLabel:
                text:"Percentage"
            MyLabel:
                id:percentage_label
                text:" "
            MyLabel:
                text:"Total Marks for 900"
            MyLabel:
                id:total_label
                text:" "    
        MyButton:
            on_press:sgpa_label.text=app.sgpa
            text:"SGPA"
        MyButton:
            on_press:percentage_label.text=app.percentage
            text:"PERCENTAGE"
        MyButton:
            on_press:total_label.text=app.result
            text:"TOTAL"
        MyButton:
            on_press:root.manager.current='about'
            text:"About"
        MDRectangleFlatButton:
            pos_hint: {'center_x':0.5,'center_y':0.5}
            text_color:1,1,1,1
            md_bg_color:1,0,0,0.7
            text:"Quit"
            on_press:app.stop()
    
<AboutScreen>
    name:'about'
    BoxLayout:
        orientation:'vertical'
        padding:130
        spacing:10  
        MDLabel:
            text:"About:"
            font_style:'H3'
            text_color:0,0,0,1
            valign:"top"
        MyLabel:
            text:"This is the app Developed using kivy and kivyMd package of python  for vtu students based on the circular relesead on 31 JUL 2020,With REF No:VTU/PS/2020-21/1386"
        MDLabel:
            text:"Disclaimer!!"
            text_color:1,0,0,1
            valign:"top"
        MyLabel:
            text:"Developer is not responsible for any error occur in the app"
        MyLabel:
            text:"Developercontact:ranganathswamy.ys@gmail.com "
        MDRectangleFlatButton:
            pos_hint: {'center_x':0.5,'center_y':0.5}
            text_color:1,1,1,1
            md_bg_color:1,0,0,0.7
            text:"Quit"
            on_press:app.stop()
            
           
   """


class MainScreen(Screen):
    pass


class Secondary(Screen):
    pass


class ThirdScreen(Screen):
    pass


class LastScreen(Screen):
    pass
class AboutScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(Secondary(name='second'))
sm.add_widget(ThirdScreen(name='third'))
sm.add_widget(LastScreen(name='last'))
sm.add_widget(LastScreen(name='about'))


class DemoApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.CIE = []
        self.dummy_list = []
        self.credits = [3, 4, 3, 3, 3, 3, 2, 2, 1]
        self.SEE = 0
        self.dummy_inlist = []
        self.result = []
        self.obtained_grade = []
        self.final_result = []
        self.sgpa = 0
        self.percentage = 0
        self.total = 900

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_string(screen_helper)

        return screen

    def avg_of_external(self, val=[]):
        self.list = val

        for i in self.list:
            a = int(i)
            self.dummy_list.append(a)
        ext_to_50 = list(map(lambda a: ((a / 60) * 50), self.dummy_list))
        self.SEE = (sum(ext_to_50) / len(ext_to_50))

    def finalaization(self, val=[]):
        List = val
        for i in List:
            self.dummy_inlist.append(int(i))
        self.CIE = list(map(lambda b: ((b / 40) * 50), self.dummy_inlist))
        self.result = list(map(lambda x: x + self.SEE, self.CIE))
        for a in self.result:
            if a >= 90 and a <= 100:
                self.obtained_grade.append(10)
            elif a >= 80 and a < 90:
                self.obtained_grade.append(9)
            elif a >= 70 and a < 80:
                self.obtained_grade.append(8)
            elif a >= 60 and a < 70:
                self.obtained_grade.append(7)
            elif a >= 50 and a < 60:
                self.obtained_grade.append(6)
            elif a >= 45 and a < 50:
                self.obtained_grade.append(5)
            elif a >= 40 and a < 45:
                self.obtained_grade.append(4)
            else:
                self.obtained_grade.append(0)
        self.final_result = list(map(lambda n1, n2: n1 * n2, self.credits, self.obtained_grade))
        self.sgpa = (sum(self.final_result) / sum(self.credits))
        self.sgpa = str(self.sgpa)
        self.percentage = (sum((self.result)) / self.total) * 100
        self.percentage = str(self.percentage)
        self.result = sum(self.result)
        self.result = str(self.result)


DemoApp().run()
