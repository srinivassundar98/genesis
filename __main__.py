from mcq import run_test,score, questions1, questions2, questions3
import csv

scores = run_test(score, questions1, questions2, questions3)

print(scores)

newScores = []

newScores.append([str(1), str(scores)])

print (newScores)

filename = "sampleDB.csv"

with open(filename, 'w') as sample_db:
    csvWriter = csv.writer(sample_db)

    csvWriter.writerows(newScores)