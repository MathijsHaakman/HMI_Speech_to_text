import os
import requests
import re


def calculate_scores(reference: str, guess: str):
    """
    Calculates the precision, recall and f-score for a given sentence
    :param reference: The original and correct sentence.
    :param guess: The sentence guessed by the bot
    :return: List of 3 lists. First one contains precision, second one the recall score and the last one the f-score.
             All 3 lists are ordered: [micro, macro]
    """
    regex = re.compile('[.,]')  # Filter these characters from the sentence
    reference_list = regex.sub('', reference.lower()).split(' ')
    guess_list = regex.sub('', guess.lower()).split(' ')
    precision = get_precision(reference_list, guess_list)
    recall = get_recall(reference_list, guess_list)
    micro_f_score = get_f_score(precision[0], recall[0])
    macro_f_score = get_f_score(precision[1], recall[1])
    # print("{};{};{};{};{};{}".format(reference_list, guess_list, precision, recall, micro_f_score, macro_f_score))
    return [precision, recall, [micro_f_score, macro_f_score]]


def get_precision(reference_list: list, guess_list: list):
    unique_set = set(guess_list)
    correct = [0] * len(unique_set)
    total = [0] * len(unique_set)
    for i, word_to_match in enumerate(unique_set):
        for j, word in enumerate(guess_list):
            if word == word_to_match:
                total[i] += 1
                if j < len(reference_list):
                    if reference_list[j] == word_to_match:
                        correct[i] += 1
    return [get_micro_average(correct, total), get_macro_average(correct, total)]


def get_recall(reference_list: list, guess_list: list):
    unique_set = set(reference_list)
    correct = [0] * len(unique_set)
    total = [0] * len(unique_set)
    for i, word_to_match in enumerate(unique_set):
        for j, word in enumerate(reference_list):
            if word == word_to_match:
                total[i] += 1
                if j < len(guess_list):
                    if guess_list[j] == word_to_match:
                        correct[i] += 1
    return [get_micro_average(correct, total), get_macro_average(correct, total)]


def get_f_score(precision, recall):
    try:
        return (2 * precision * recall) / (precision + recall)
    except ZeroDivisionError:
        return 0


def get_macro_average(correct: list, total: list):
    precisions = [0] * len(correct)
    for i in range(len(correct)):
        if correct[i] != 0:
            precisions[i] = correct[i] / total[i]
    return (1 / len(correct)) * sum(precisions)


def get_micro_average(correct: list, total: list):
    return sum(correct) / sum(total)


with open(os.path.join("Results", "results.csv"), 'r') as list:
    list.readline()
    line = list.readline()
    print("number;wrr,wer;micro precision;macro precision;micro recall;macro recall;micro f-score;macro f-score")
    while line:
        data = line.split(";")
        reference = data[1]
        guess = data[3]

        r = requests.post(
            "http://api.robbit.me",
            json={
                "guess": guess,
                "reference": reference
            }
        ).json()
        scores = calculate_scores(reference, guess)

        print("{};{};{};{};{};{};{};{};{}".format(data[0], r["wrr"], r["wer"], scores[0][0], scores[0][1], scores[1][0], scores[1][1], scores[2][0], scores[2][1]))
        line = list.readline()
