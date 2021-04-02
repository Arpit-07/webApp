import time

class webApp:
    def __init__(self):
        print("""Select Level: 
                 Press 1 for Easy
                 Press 2 for Medium
                 Press 3 for Hard
                 """)
        l = int(input("Enter the choice: "))
        self.selectLevel(l)
        
    def selectLevel(self, level):
        if level == 1:
            self.easy()
        elif level == 2:
            self.medium()
        elif level == 3:
            self.hard()
        else:
            return "Invalid level"
    
    def easy(self):
        print("Easy Selected!")
        time.sleep(2)
        self.countdown()
        self.questions()
    
    def medium(self):
        print("Medium Selected!")
        time.sleep(2)
        self.countdown()
        self.questions()
        
    def hard(self):
        print("Hard Selected!")
        time.sleep(2)
        self.countdown()
        self.questions()
        
    def questions(self):
        sol = ['A', 'B', 'D', 'B', 'B']
        ques = ["What is getattr() used for? \n (A) To access the attribute of the object \n (B) To delete an attribute \n (C) To check if an attribute exists or not \n (D) To set an attribute",
        "What is setattr() used for? \n (A) To access the attribute of the object \n (B) To set an attribute \n (C) To check if an attribute exists or not \n (D) To delete an attribute \n",
        "What is Instantiation in terms of OOP terminology? \n (A) Deleting an instance of class \n (B) Modifying an instance of class \n (C) Copying an instance of class \n (D) Creating an instance of class \n", 
        "___ is used to create an object. \n (A) class \n (B) constructor \n (C) user-defined functions \n (D) In-built functions \n",
        "___ represents an entity in the real world with its identity and behavior. \n (A) A method \n (B) An object \n (C) A class \n (D) An operator \n"]
        points = 0
        q = 0 
        responses = []
        while True and q < len(ques):
            print("Question - ", q+1, "\n",ques[q])
            answer = input("Enter option: ")
            if answer in {'a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'}:
                u = answer.upper()
                responses.append(u)
                if sol[q] == u:
                    points += 1 
            else:
                print("Invalid option")
                continue
            
            q += 1    
            
        result = {1: "Poor", 2: "Bad", 3: "Good", 4: "Strong", 5: "Very Strong"}
        res = result.get(points, 'Weak')
        k = 'Your knowledge '
        p = 'points'
        upper_banner = '+' + ((len(p) + 4) * '-') + '|' +((len(k) + 4) * '-') + '+'
        lower_banner = '+' + ((len(p) + 4) * '-') + '|' +((len(k) + 4) * '-') + '+'
        heading = '|' + p.center((len(p) + 4)) + '|' +k.center((len(k) + 4)) + '|'
        report = '|' + str(points).center((len(p) + 4)) + '|' + res.center((len(k) + 4)) + '|'
        print(upper_banner)
        print(heading)
        print(lower_banner)
        print(report)
        print(lower_banner)
        print("Your answers were: ", responses)
        print("Correct solutions: ", sol)
        
    def countdown(self):
        cnt = 3
        while cnt != 0:
            mins, secs = divmod(cnt, 60)
            time.sleep(1)
            timer = '{:02d}:{:02d} seconds left'.format(mins, secs)
            print(timer, end="\r")
            cnt -= 1
        print("Time Lapsed")
        
if __name__ == "__main__":
    webApp()
    