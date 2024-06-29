import tkinter as tk
from tkinter import messagebox

# Sample Questions
oop_questions = [
    ("What does OOP stand for?", ["Object-Oriented Programming", "Object-Oriented Process", "Objective Programming", "Operational Programming"], 1),
    ("Which feature of OOP indicates code reusability?", ["Polymorphism", "Inheritance", "Encapsulation", "Abstraction"], 2),
    ("Which language does not support OOP?", ["C++", "Java", "Python", "C"], 4),
    ("Which of these is a blueprint for creating objects?", ["Class", "Object", "Method", "Function"], 1),
    ("What is encapsulation?", ["Wrapping data and methods together", "Hiding data", "Using functions", "Inheritance of data"], 1),
    ("Which OOP concept means exposing only necessary information?", ["Abstraction", "Encapsulation", "Inheritance", "Polymorphism"], 1),
    ("Which is not a type of inheritance?", ["Single", "Multiple", "Hybrid", "Integer"], 4),
    ("What is polymorphism?", ["Multiple forms", "Encapsulation", "Data hiding", "Inheritance"], 1),
    ("Which keyword is used to create a class in Python?", ["def", "class", "new", "create"], 2),
    ("What is the relation between class and object?", ["Class is an instance of an object", "Object is an instance of a class", "Class and object are the same", "Class is a template for objects"], 4)
]

cpp_questions = [
    ("Which of these is not a C++ data type?", ["int", "float", "char", "real"], 4),
    ("Which symbol is used to comment a single line in C++?", ["//", "/*", "#", "<!--"], 1),
    ("How do you insert a comment in C++ that spans multiple lines?", ["//", "/* ... */", "# ... #", "-- ... --"], 2),
    ("Which function is the entry point for a C++ program?", ["start()", "init()", "main()", "begin()"], 3),
    ("Which of these operators is used to access members of a class in C++?", [".", "::", "->", "->*"], 3),
    ("Which keyword is used to define a constant in C++?", ["const", "let", "constant", "define"], 1),
    ("What is the default access specifier for members of a class in C++?", ["public", "private", "protected", "global"], 2),
    ("Which keyword is used to inherit a class in C++?", ["inherit", "extends", "inherits", "public"], 4),
    ("Which of these is the correct syntax for a for loop in C++?", ["for i = 1 to 10", "for (int i = 0; i < 10; i++)", "for (i in range(10))", "for (i = 1 to 10)"], 2),
    ("Which operator is used for input in C++?", [">>", "<<", "==", "&&"], 1)
]

arduino_questions = [
    ("Which language is primarily used for Arduino programming?", ["Python", "Java", "C/C++", "BASIC"], 3),
    ("What is the function used to set the mode of a pin?", ["pinMode()", "setPinMode()", "definePinMode()", "pinSetup()"], 1),
    ("Which function reads the value from a digital pin?", ["digitalRead()", "analogRead()", "readDigital()", "getDigitalValue()"], 1),
    ("Which function sends a signal to a digital pin?", ["sendDigital()", "digitalWrite()", "writeDigital()", "digitalSignal()"], 2),
    ("How do you begin serial communication in Arduino?", ["Serial.start()", "Serial.begin()", "Serial.open()", "Serial.init()"], 2),
    ("Which function delays the program for a specific time in milliseconds?", ["delay()", "pause()", "wait()", "sleep()"], 1),
    ("What is the main loop function called in Arduino?", ["loop()", "run()", "mainLoop()", "execute()"], 1),
    ("What is the correct way to initialize an analog pin?", ["pinMode()", "analogMode()", "analogSetup()", "analogRead()"], 1),
    ("Which of these is a type of sensor you can connect to Arduino?", ["Thermistor", "LCD", "LED", "Resistor"], 1),
    ("Which board is the most basic Arduino board?", ["Arduino Mega", "Arduino Nano", "Arduino Uno", "Arduino Micro"], 3)
]

web_questions = [
    ("Which language is used for structuring a web page?", ["CSS", "JavaScript", "HTML", "PHP"], 3),
    ("Which language is used for styling web pages?", ["HTML", "CSS", "JavaScript", "PHP"], 2),
    ("Which language is used for client-side scripting?", ["HTML", "CSS", "JavaScript", "PHP"], 3),
    ("What does CSS stand for?", ["Colorful Style Sheets", "Cascading Style Sheets", "Creative Style Sheets", "Computer Style Sheets"], 2),
    ("Which HTML element is used to link to a CSS file?", ["<css>", "<style>", "<link>", "<script>"], 3),
    ("Which of these is not a valid HTML tag?", ["<div>", "<span>", "<main>", "<layout>"], 4),
    ("Which HTML attribute is used to specify inline styles?", ["style", "css", "design", "format"], 1),
    ("What does DOM stand for?", ["Document Object Model", "Data Object Model", "Document Oriented Model", "Display Object Management"], 1),
    ("Which of these is a CSS framework?", ["React", "Angular", "Bootstrap", "Vue"], 3),
    ("Which HTML element is used to define a hyperlink?", ["<link>", "<a>", "<href>", "<url>"], 2)
]

# Mapping course names to question sets
course_map = {
    "OOP": oop_questions,
    "C++": cpp_questions,
    "Arduino": arduino_questions,
    "Web Design": web_questions
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Software Engineering Quiz")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")  # Background color

        self.question_index = 0
        self.score = 0
        self.current_questions = []
        self.selected_course = tk.StringVar()

        self.create_course_selection_screen()

    def create_course_selection_screen(self):
        self.clear_screen()

        label = tk.Label(self.root, text="Select a Course", font=("Arial", 18), bg="#f0f0f0", fg="#333333")
        label.pack(pady=20)

        for course in course_map.keys():
            button = tk.Button(self.root, text=course, font=("Arial", 14), bg="#007BFF", fg="white",
                               command=lambda c=course: self.start_quiz(c))
            button.pack(pady=10, ipadx=10, ipady=5)

    def start_quiz(self, course):
        self.selected_course.set(course)
        self.current_questions = course_map[course]
        self.question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_screen()
        
        if self.question_index < len(self.current_questions):
            question, options, correct_option = self.current_questions[self.question_index]
            
            question_label = tk.Label(self.root, text=question, font=("Arial", 14), wraplength=500, justify="left", bg="#f0f0f0", fg="#333333")
            question_label.pack(pady=20)

            self.var = tk.IntVar()
            for i, option in enumerate(options):
                radio_btn = tk.Radiobutton(self.root, text=option, variable=self.var, value=i+1, font=("Arial", 12),
                                           bg="#f0f0f0", fg="#333333", selectcolor="lightgrey")
                radio_btn.pack(anchor="w")

            button_frame = tk.Frame(self.root, bg="#f0f0f0")
            button_frame.pack(pady=20)
            
            next_button = tk.Button(button_frame, text="Next", font=("Arial", 12), bg="#28a745", fg="white", command=self.next_question)
            next_button.grid(row=0, column=0, padx=10)

            if self.question_index > 0:
                prev_button = tk.Button(button_frame, text="Previous", font=("Arial", 12), bg="#17a2b8", fg="white", command=self.previous_question)
                prev_button.grid(row=0, column=1, padx=10)

        else:
            self.show_score()

    def next_question(self):
        self.check_answer()
        self.question_index += 1
        self.show_question()

    def previous_question(self):
        if self.question_index > 0:
            self.question_index -= 1
            self.show_question()

    def check_answer(self):
        selected_option = self.var.get()
        correct_option = self.current_questions[self.question_index][2]
        if selected_option == correct_option:
            self.score += 1

    def show_score(self):
        self.clear_screen()
        result_text = f"You scored {self.score} out of {len(self.current_questions)}"
        result_label = tk.Label(self.root, text=result_text, font=("Arial", 18), bg="#f0f0f0", fg="#333333")
        result_label.pack(pady=20)

        restart_button = tk.Button(self.root, text="Choose Another Course", font=("Arial", 14), bg="#007BFF", fg="white", command=self.create_course_selection_screen)
        restart_button.pack(pady=10, ipadx=10, ipady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
