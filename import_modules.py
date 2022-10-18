#!/usr/bin/env python3

"""Alta3 Research | RRoss
Lab 30 Importing Modules"""

#create trivia dictionary

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

#define variables
question = trivia["question"]
correct= trivia["correct_answer"]
incorrect1= trivia["incorrect_answers"][0]
incorrect2= trivia["incorrect_answers"][1]
incorrect3= trivia["incorrect_answers"][2]

import html

#print question and answers
print(html.unescape(question))
print(html.unescape(correct))
print(html.unescape(incorrect3))
print(html.unescape(incorrect2))
print(html.unescape(incorrect1))
