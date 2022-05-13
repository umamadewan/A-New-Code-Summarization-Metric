from nltk.translate.bleu_score import sentence_bleu


def calculate_bleu(references, candidates):
    reference = [references.split(" ")]
    candidate = candidates.split(" ")
    score = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
    return score

