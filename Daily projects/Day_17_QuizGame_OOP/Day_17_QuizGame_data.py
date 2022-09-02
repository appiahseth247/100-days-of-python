"""
Go to https://opentdb.com/api_config.php to generate new set of verified questions and answer
Go to Code>FFormat code to reformat the JSON text copied from the website so that it will look a readable python dict
https://www.udemy.com/course/100-days-of-code/learn/lecture/19964936#questions/13330500 1:42~58, 2:40, 3:30
Edit the "keys" in def next_question (line 18, 19) to the keys of the new question set generated
this is for true/false questions
someone did for MCQs at https://replit.com/@appiahseth247/QuizMCQ#quiz_brain.py
"""

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament,"
             " you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

question_data1 = [
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "The Axolotl is an amphibian that can spend its whole life in a larval state.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "A slug&rsquo;s blood is green.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "Kangaroos keep food in their pouches next to their children.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "A bear does NOT defecate during hibernation. ",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "Rabbits are rodents.", "correct_answer": "False",
                       "incorrect_answers": ["True"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "A flock of crows is known as a homicide.",
                       "correct_answer": "False", "incorrect_answers": ["True"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "The Killer Whale is considered a type of dolphin.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "Rabbits can see what&#039;s behind themselves without turning their heads.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "The internet browser Firefox is named after the Red Panda.",
                       "correct_answer": "True", "incorrect_answers": ["False"]},
                      {"category": "Animals", "type": "boolean", "difficulty": "easy",
                       "question": "The freshwater amphibian, the Axolotl, can regrow it&#039;s limbs.",
                       "correct_answer": "True", "incorrect_answers": ["False"]}]

data3 = [
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "In baseball, how many fouls are an out?", "correct_answer": "0",
              "incorrect_answers": ["5", "3", "2"]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "Who won the 2015 Formula 1 World Championship?",
              "correct_answer": "Lewis Hamilton",
              "incorrect_answers": ["Nico Rosberg", "Sebastian Vettel", "Jenson Button"]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "How many points did LeBron James score in his first NBA game?",
              "correct_answer": "25", "incorrect_answers": ["19", "69", "41"]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "Who won the 2016 Formula 1 World Driver&#039;s Championship?",
              "correct_answer": "Nico Rosberg",
              "incorrect_answers": ["Lewis Hamilton", "Max Verstappen", "Kimi Raikkonen"]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "In bowling, what is the term used for getting three consecutive strikes?",
              "correct_answer": "Turkey",
              "incorrect_answers": ["Flamingo", "Birdie", "Eagle"]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "Which African American is in part responsible for integrating  Major League baseball?",
              "correct_answer": "Jackie Robinson",
              "incorrect_answers": ["Curt Flood", "Roy Campanella", "Satchell Paige"]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "What is the name of Manchester United&#039;s home stadium?",
              "correct_answer": "Old Trafford",
              "incorrect_answers": ["Anfield", "City of Manchester Stadium",
                                    "St James Park"]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "Which year did Jenson Button won his first ever Formula One World Drivers&#039; Championship?",
              "correct_answer": "2009", "incorrect_answers": ["2010", "2007", "2006"]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "Who won the UEFA Champions League in 2017?",
              "correct_answer": "Real Madrid C.F.",
              "incorrect_answers": ["Atletico Madrid", "AS Monaco FC", "Juventus F.C."]},
             {"category": "Sports", "type": "multiple", "difficulty": "easy",
              "question": "Which two teams played in Super Bowl XLII?",
              "correct_answer": "The New York Giants &amp; The New England Patriots",
              "incorrect_answers": ["The Green Bay Packers &amp; The Pittsburgh Steelers",
                                    "The Philadelphia Eagles &amp; The New England Patriots",
                                    "The Seattle Seahawks &amp; The Denver Broncos"]}
]
