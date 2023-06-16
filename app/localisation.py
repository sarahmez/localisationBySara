import numpy as np
import pandas as pd
import time
#
def grasp(c, S, max_iter=1000, alpha=0.5):  # c les couts / les ensembles à couvrir
    n = len(c)  # le nombre d'éléments à couvrir
    m = len(S)  # le nombre d'emplacements candidats
    best_sol = None  # initialiser la sol à zero/vide
    best_cost = np.inf  # initialiser la sol opt à l'infinie
    for _ in range(max_iter):
        # Construction de la solution initiale
        sol = np.zeros(m)  # initialiser la sol courante avec un vect de 0 de longueur m
        non_couvertes = set(range(
            n))  # initialiser la var non_couvertes qui présente les lignes non couvertes à un ensemble contenant toutes les lignes
        while len(non_couvertes) > 0:  # tant qu'il ya encore des lignes non couvertes
            candidates = [i for i in range(m) if len(
                S[i] & non_couvertes) > 0]  # S[i] l'ensemble des éléments couverts par l'emplacement candidat i.
            if len(candidates) == 0:
                break
                # la recherche d'un ensemble à ajouter à la solution actuelle
            cout = np.array([c[i] for i in
                             candidates])  # la création d'un tableau contenant les couts des emplacements qui peuvent etre ajoutés à la solution courante
            min_cout = np.min(cout)  # définir le cout min
            max_cout = np.max(cout)  # définir le cout max
            seuil = min_cout + alpha * (max_cout - min_cout)  # calculer le seuil pour créer la RCL
            RCL = [candidates[i] for i in range(len(candidates)) if cout[i] <= seuil]  # la création de la RCL
            e_choisi = np.random.choice(RCL)  # chosir aléatoirement un ensemble candidat parmi la liste RCL
            sol[e_choisi] = 1  # ajouter l'ensemble choisi aléatoirement à la solution courante
            non_couvertes -= S[e_choisi]  # mise à jours de la liste des lignes non couvertes

        # Recherche locale
        while True:
            # Trouver l'emplacement à supprimer de la solution
            indices = [i for i in range(m) if sol[
                i] == 1]  # la création d'une une liste des indices des emplacements actuellement présents dans la solution
            if len(indices) == 0:
                break
            à_supp = np.random.choice(
                indices)  # choisir aléatoirement un indice de la liste indices qui présente l'emplacement candidat qui sera supp de la solution.
            sol[à_supp] = 0  # supp l'indice choisi aléatoirement de la solution

            # Trouver le meilleur ensemble à ajouter à la solution
            # liste des indices des candidats non encore présents dans la solution courante et qui couvre encore des elements non encore couverts
            candidates = [i for i in range(m) if sol[i] == 0 and len(S[i] & non_couvertes) > 0]

            if len(candidates) == 0:
                sol[
                    à_supp] = 1  # mise a jour de la sol en ajoutant l'emplacement dans la solution courante ( choix aléatoire !)
                break
            cout = np.array([c[i] for i in candidates])  # liste des couts
            min_cout = np.min(cout)
            max_cout = np.max(cout)
            seuil = min_cout + alpha * (max_cout - min_cout)
            RCL = [candidates[i] for i in range(len(candidates)) if cout[i] <= seuil]
            e_choisi = np.random.choice(RCL)
            sol[e_choisi] = 1
            non_couvertes -= S[e_choisi]  # mise à jour des lignes non encore couvertes

        # Vérifier si la solution courante est la meilleure trouvée jusqu'à présent
        cout = np.sum(sol * c)  # le calcul du cout total de la solution trouvée
        if cout < best_cost:
            best_cost = cout
            best_sol = sol.copy()
    return best_sol, best_cost
#
def normalisation(src):
    #
    data = []
    #'../static/data/statition.xlsx'
    df = pd.read_excel(src)
    #
    #print(df)
    #
    data_v = list(zip(df['Emplacement condidat'],df['Longitude '],df['Latitude ']))
    #
    for index,element in enumerate(data_v):
        d={}
        d[index+1]=element
        data.append(d)
    #
    #print(df.columns)
    return data

def visualisation(sol,commun):
    #
    path = []
    result = [s for s in commun if list(s.keys())[0] in sol]
    #print(result)
    for r in result:
        l=[]
        l.append(list(r.values())[0][1])
        l.append(list(r.values())[0][2])
        path.append(l)
    #
    print(result)
    return result,path
    #
if __name__ == '__main__':

    normalisation('../static/data/statition.xlsx')
    #normalisation('../static/data/long lat emplacements gis.xlsx')
    #print(grasp([100, 80, 250, 120, 90, 100, 100, 100, 120, 120, 100, 120, 100, 100, 80, 120, 100, 120, 90, 100, 120, 90, 120, 90, 120, 100, 110],[{7}, {5, 6}, {1, 12}, {10, 12}, {11}, {1, 5}, {13}, {9, 10}, {5}, {9, 10, 3, 12}, {11}, {9, 2}, {9, 10}, {9}, {2}, {9, 10}, {4}, {10, 12},{11}, {6}, {8}, {8}, {9, 10, 3}, {1, 5}, {11}, {1, 5}, {12}]))
    #print(grasp([100, 80, 250, 120, 90, 100, 100, 100, 120, 120, 100, 120, 100, 100, 80, 120, 100, 120, 90,90, 100, 120, 90, 120, 90, 120, 100, 110],[{7}, {5, 6}, {1, 12}, {10, 12}, {11}, {1, 5}, {13}, {9, 10}, {5}, {9, 10, 3, 12}, {11}, {9, 2}, {9, 10}, {9}, {2}, {9, 10}, {4}, {10, 12}, set(), {11}, {6}, {8}, {8}, {9, 10, 3}, {1, 5}, {11}, {1, 5}, {12}]))
    #visualisation([2,3],normalisation('../static/data/statition.xlsx'))