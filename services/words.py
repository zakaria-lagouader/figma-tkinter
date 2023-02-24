from datetime import date, timedelta
import pandas as pd
import csv

def add_word(word: str, translation: str, is_correct: bool):
    with open('learned_words.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            if is_correct == True:
                writer.writerow([word, translation, True, date.today(), date.today() + timedelta(days=7)])
            else:
                writer.writerow([word, translation, False, date.today(), date.today() + timedelta(days=1)])

def word_of_today():
    df = pd.read_csv('learned_words.csv')
    todays_words = df.loc[df['Reminder'] == str(date.today())]
    return todays_words.to_dict("records")





    
