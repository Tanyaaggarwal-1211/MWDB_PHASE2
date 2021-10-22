import csv
import pickle
import Utilities


def getRankMatrix():

    input_file = ''

    latent = None

    if input_file is not None:
        with open(input_file) as file:
            latent = pickle.load(file)

    if latent:
        n = input('enter n')
        m = input('enter m')

        simp = latent['simp']

        transition = Utilities.transform_transition_matrix(simp, n)
        ascos = Utilities.perform_ascos_similarity(transition)
        ranks = Utilities.get_rank(ascos, m)

        with open('8.csv', 'w') as out:
            csv_writer = csv.writer(out, delimiter=',')
            csv_writer.writerow(['Subject', 'Score'])
            for a in ranks:
                csv_writer.writerow(a)
