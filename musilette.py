
RANGES = {
    # Intervalles de la gamme majeure
    0: [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], 
    # Intervalles de la gamme mineure naturelle
    1: [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    # Intervalles de la gamme mineure harmonique 
    2: [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1] 
}

RANGES_NAMES = {
    'fr': ['Majeur', 'Mineur naturel', 'Mineur harmonique']
}

# Nombre total de notes
N = 12

# Nombre de nombre par gamme
N_T = 7

NOTES = {
    'fr': ['DO', 'DO#', 'RE', 'RE#', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI']
}

CHORDS = {
    'fr': {
        0: ['', 'm', 'm', '', '', 'm', 'dim'],
        1: ['m', 'dim', '', 'm', 'm', '', ''], 
        2: ['', 'm', 'm', '', '', 'm', 'dim']
    }
}

def get_notes_from_range(r, t):
    """ Return all notes from a given range"""
    # calcul du tableau de notes
    tab = []
    for i in range(N):   
        n = (i - t)%N
        tab.append(RANGES[r][n])
    
    return tab 
    
def get_range_chords(r):
    return []
     

def export_range(res, lg):
    notes = [NOTES[lg][(n + res['keynote'] )% 12] for n in range(N) if res['notes'][(n + res['keynote'] )% 12]]
    return {
        'keynote': NOTES[lg][res['keynote']], 
        'range': RANGES_NAMES[lg][res['range']], 
        'notes': notes, 
        'pourcentage': res['pourcentage']
        # 'Accords': [notes[i] + CHORDS[lg][res['range']][i] for i in range(N_T)]
    }
   
   
def print_range(r):
    print r['Tonique'] + ' ' + r['Gamme']
    print r['Accords']
    print 
    

## traitement
def range_ranking(given_notes):
    result = []

    # pour chaque tonique:
    for t in range(N):
        # pour chaque mode:
        #for m in range(0, 12):
        # pour chaque gamme:
        for r in range(len(RANGES)):
            # re-initialisation du pourcentage
            pourcentage = 0.0
            # obtention de toutes les notes de la gamme consideree
            range_notes = get_notes_from_range(r, t) 
            # pour chaque note connue:
            for i in given_notes:
                # si la note connue est dans la gamme:
                if range_notes[i] == 1:
                    #alors pourcentage += 1
                    pourcentage += 1
                else:
                    pourcentage -= 1
            
            pourcentage = (pourcentage/len(given_notes)) * 100
            result.append({'keynote': t, 
                           # 'mode': m,
                           'range': r,
                           'notes': range_notes,
                           'pourcentage': pourcentage})

    return result

def main(notes, lg):
     # Compute pourcentage for every registered ranges
    unsorted_ranking = range_ranking(notes)
    sorted_ranking = sorted(unsorted_ranking, key=lambda g: g['pourcentage'], reverse=True)
    
    best_results = [r for r in sorted_ranking if r['pourcentage'] == sorted_ranking[0]['pourcentage']]
    return best_results


def get_ranges(given_notes, lg='fr'):
    
    errors = {}
    results = []
    # Clean user entry
    print 'g' + str(given_notes)
    notes = [NOTES['fr'].index(n) for n in given_notes]

    print 'n' + str(notes)

    try:
        best_results = main(notes, lg)
    except Exception as e:
        errors['status'] = 'error'
        errors['message'] = e
        return errors

    errors['status'] = 'success'
    errors['message'] = ''
    errors['result'] = [export_range(r, lg) for r in best_results]

    return errors


if __name__ == '__main__':

    #TODO: Test that arrays have consistents length
    
    # Get entry from user
    notes = [0, 2, 4, 5, 7, 9, 11]
    lg = 'fr'
    print [NOTES[lg][i] for i in notes]
    print
    print "Ces notes correspondent a la gamme:"
    
    #TODO: Clean user entry

    best_results = main(notes, lg)
        
    for r in best_results:
        print export_range(r, lg)

