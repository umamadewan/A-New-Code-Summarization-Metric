import pandas

import missing_identifiers
import repeat
import calculate_bleu_score


def main():
    df = pandas.read_csv('error_categories.csv')
    for data in df:
        if data == 'PoS Tagging of Human Written Comment':
            header_human = data
        if data == 'PoS Tagging of Model\'s Prediction':
            header_model = data
        if data == 'Model\'s Prediction':
            header_prediction = data
        if data == 'Human Written Comment':
            header_human_comment = data

    itr = 0
    for datum_prediction, datum_human, datum_model, datum_human_comment \
            in zip(df[header_prediction], df[header_human], df[header_model], df[header_human_comment]):
        if pandas.isna(datum_human) or pandas.isna(datum_model) or pandas.isna(datum_prediction) \
                or pandas.isna(datum_human_comment) or datum_human == header_human \
                or datum_model == header_model or datum_human_comment == header_human_comment \
                or datum_prediction == header_prediction:
            continue
        score = 0
        score += repeat.is_repetition(datum_prediction)
        score += missing_identifiers.check_missing_identifiers(missing_identifiers.return_nouns(datum_human),
                                                          missing_identifiers.return_nouns(datum_model))

        df.loc[itr, 'Score'] = score
        normalization = (score+3)/11
        bleu_score = calculate_bleu_score.calculate_bleu(datum_human_comment, datum_prediction)
        df.loc[itr, 'Normalized Score'] = round(normalization, 2)
        df.loc[itr, 'Bleu Score'] = round(bleu_score, 2)
        itr += 1

    df.to_csv("final.csv", index=False)


if __name__ == "__main__":
    main()
