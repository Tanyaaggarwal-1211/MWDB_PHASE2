import csv
import pickle
import Utilities


def test():

    input_file = ''
    latent = None

    if input_file is not None:
        with open(input_file) as file:
            latent = pickle.load(file)

    if latent:

        n = input('enter n')
        m = input('enter m')

        sub1 = input('Enter subject ID 1')
        sub2 = input('Enter subject ID 2')
        sub3 = input('Enter subject ID 3')
        subject_ids = [sub1, sub2, sub3]

        simp = latent['simp']

        transition = Utilities.transform_transition_matrix(simp, n)
        rank = Utilities.get_rank_with_seeds(transition, m, subject_ids)

        ranks = Utilities.get_rank(rank, m)

        with open('9.csv', 'w') as out:

            csv_writer = csv.writer(out, delimiter=',')
            csv_writer.writerow(['Subject', 'Score'])
            for a in ranks:
                csv_writer.writerow(a)
