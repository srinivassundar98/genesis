from easy_question import easy_question
from medium_question import medium_question
from hard_question import hard_question

easy_question_prompt = [
    "1. Which among the following best describes encapsulation? \n a) It is a way of combining various data members "
    "into a single unit \n b) It is a way of combining various member functions into a single unit \n c) It is a way "
    "of combining various data members and member functions intoa single unit which can operate on any data \n d) It "
    "is a way of combining various data members and member functions that operate on those data members into a single "
    "unit\n\n ",
    "2. Which among the following violates the principle of encapsulation almost always? \n\n a) Local variables\n "
    "b) Global variables\n c) Public variables\n d) Array variables\n\n",
    "3. 3.Which among the following best defines abstraction?\n a) Hiding the implementation\n b) Showing the "
    "important data\n c) Hiding the important data\n d) Hiding the implementation and showing only some features\n\n ",
    "4.Higher the level of abstraction, higher are the details.\n a) True \n b) False\n\n "
]

medium_question_prompt = [
    "1. The process of initializing through a copy constructor is known as ...............\nA) copy \n"
    "process\nB) copy registration\nC) copy initialization\nD) initialization process\n\n ",
    "2. Which among the following is not applicable for the static member functions?\n"
    "a) Variable pointers\nb) void pointers\nc) this pointer\nd) Function pointers\n\n",
    "3. Which among the following is correct definition for static member functions?\n"
    "a) Functions created to allocate constant values to each object\n"
    "b) Functions made to maintain single copy of member functions for all objects\n"
    "c) Functions created to define the static members\nd) Functions made to manipulate static programs\n\n ",
    "4. The static member functions __________________\n"
    "a) Have access to all the members of a class\n"
    "b) Have access to only constant members of a class\n"
    "c) Have access to only the static members of a class\nd) Have direct access to all members of cricket\n",

]

hard_question_prompt = [
    "1. Which is the correct syntax for declaring static data member?\na) static memberName dataType;\nb) dataType "
    "static memberName;\nc) memberName static dataType;\nd) static dataType memberName;\n\n ",
    "2. The static data member ______________________\n\na) Must be defined inside the class\nb) Must be defined "
    "outside the class\nc) Must be defined in main function\nd) Must be defined using constructor ",
    "3. In a program, If there exists a function template with two parameters andnormal function say void add(int , "
    "int), so add(3,4) will_____________________ .\na. Invoke function template body as it is generic one\nb. Invokes "
    "normal function as it exactly matches with its prototype\nc. Not be called and Compiler issues warning\nd. Not "
    "be called and Compiler issues ambiguity in calling add()\n\n ",
    "4. Which among the following best defines static variables members?\n"
    "a) Data which is allocated for each object separately\nb) Data which is common to all the objects of a class\n"
    "c) Data which is common to all the classes\nd) Data which is common to a specific method\n\n"
]

questions1 = [easy_question(easy_question_prompt[0], "d"),
              easy_question(easy_question_prompt[1], "b"),
              easy_question(easy_question_prompt[2], "d"),
              easy_question(easy_question_prompt[3], "b"),
              ]
questions2 = [medium_question(medium_question_prompt[0], "c"),
              medium_question(medium_question_prompt[1], "c"),
              medium_question(medium_question_prompt[2], "b"),
              medium_question(medium_question_prompt[3], "c"),
              ]
questions3 = [hard_question(hard_question_prompt[0], "d"),
              hard_question(hard_question_prompt[1], "b"),
              hard_question(hard_question_prompt[2], "b"),
              hard_question(hard_question_prompt[3], "b"),

              ]


def run_test(quest1, quest2, quest3):
    score = 0
    flag =[]
    incorrect = 0

    for easy_question in quest1:

        ans = input(easy_question.prompt)

        if ans == easy_question.answer:
            score += 1

            if score >= 2:
                break
        else:
            incorrect += 1
            flag=easy_question.prompt
            print("you got this question incorrect\n"+ str(flag))
    for medium_question in quest2:

        ans = input(medium_question.prompt)

        if ans == medium_question.answer:
            score += 1
            if score >= 4:
                break
        else:
            incorrect += 1
            flag = medium_question.prompt
            print("you got this question incorrect\n" + str(flag))
    for hard_question in quest3:

        ans = input(hard_question.prompt)

        if ans == hard_question.answer:
            score += 1
        else:
            incorrect += 1
            flag = hard_question.prompt
            print("you got this question incorrect\n" + str(flag))


    print("your score is: " + str(score))
    print("number of incorrect questions is: " + str(incorrect))


run_test(questions1, questions2, questions3)
