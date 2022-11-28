import gc
import tracemalloc
import json
import time

import GeneratedFunctions

'''Cette classe a pour but de tester sur des échantillons de tailles différentes les 
performances obtenues sur l'ensemble des fonctionnalités générées par notre algorithme. '''

def cpu_charge(csv, nbtest):
    functions = ['pos_max_max_bump_on_decreasing_sequence', 'pos_max_max_decreasing', 'pos_max_max_decreasing_sequence',
                 'pos_max_max_dip_on_increasing_sequence', 'pos_max_max_increasing', 'pos_max_max_increasing_sequence',
                 'pos_max_max_inflexion', 'pos_max_max_peak', 'pos_max_max_strictly_decreasing_sequence',
                 'pos_max_max_strictly_increasing_sequence', 'pos_max_max_summit', 'pos_max_max_zigzag',
                 'pos_max_min_bump_on_decreasing_sequence', 'pos_max_min_decreasing', 'pos_max_min_decreasing_sequence',
                 'pos_max_min_dip_on_increasing_sequence', 'pos_max_min_gorge', 'pos_max_min_increasing',
                 'pos_max_min_increasing_sequence', 'pos_max_min_inflexion', 'pos_max_min_strictly_decreasing_sequence',
                 'pos_max_min_strictly_increasing_sequence', 'pos_max_min_valley', 'pos_max_min_zigzag',
                 'pos_min_max_bump_on_decreasing_sequence', 'pos_min_max_decreasing', 'pos_min_max_decreasing_sequence',
                 'pos_min_max_dip_on_increasing_sequence', 'pos_min_max_increasing', 'pos_min_max_increasing_sequence',
                 'pos_min_max_inflexion', 'pos_min_max_peak', 'pos_min_max_strictly_decreasing_sequence',
                 'pos_min_max_strictly_increasing_sequence', 'pos_min_max_summit', 'pos_min_max_zigzag',
                 'pos_min_min_bump_on_decreasing_sequence', 'pos_min_min_decreasing', 'pos_min_min_decreasing_sequence',
                 'pos_min_min_dip_on_increasing_sequence', 'pos_min_min_gorge', 'pos_min_min_increasing',
                 'pos_min_min_increasing_sequence', 'pos_min_min_inflexion', 'pos_min_min_strictly_decreasing_sequence',
                 'pos_min_min_strictly_increasing_sequence', 'pos_min_min_valley', 'pos_min_min_zigzag']

    data = json.load(open(csv))

    print('\nTest n°' + nbtest.__str__() + '\n nombre de lignes à traiter: ' + len(data).__str__())
    print('-'*50)

    for function in functions:
        to_run = getattr(GeneratedFunctions, function)
        start = time.time()
        tracemalloc.start()
        gc.collect()
        before = tracemalloc.take_snapshot()
        to_run(data)
        after = tracemalloc.take_snapshot()
        stop = time.time()

        tracemalloc.stop()

        tmps_execution = stop - start

        print('\nTest de performance de la fonction: ' + function)
        stats = after.compare_to(before, 'lineno')
        stat = stats[:1].__str__().split('>')

        print(stat[2])
        print(f'Temps d\'éxecution: {tmps_execution:.2}s.')


cpu_charge('Json/accenture.json', 1)
cpu_charge('Json/amazon.json', 2)
cpu_charge('Json/microsoft.json', 3)
cpu_charge('Json/ibm.json', 4)
