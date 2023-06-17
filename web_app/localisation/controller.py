from flask import Blueprint,request,render_template
#
from app.localisation import grasp,visualisation,normalisation
#
import numpy as np
#
blueprint_localisation = Blueprint(
    'localisation',
    __name__,
    template_folder='../templates',
    url_prefix='/localisation'
)
#
@blueprint_localisation.app_template_filter('petty')
def decor_result(result):
    return list(result.values())[0][0]
#
@blueprint_localisation.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        len_S=[]
        lensemble_L = request.form['element']
        lensemble_S = request.form['matrix'].split('-')[:-1]
        print(lensemble_S)
        for s in lensemble_S :
            #d = set(int(a) for a in s.split(',') if a not in [''])
            d = set(int(a) for a in s.split(' ') if a != '')
            if d != '':
                len_S.append(d)
        #lensemble_C = [int(a) for a in request.form['cout'].split(',')]
        lensemble_C = [int(a) for a in request.form['cout'].split(' ') ]
        # return grasp(lensemble_C,lensemble_S)
        print(lensemble_L)
        print(len_S)
        print(lensemble_C)
        #
        best_sol,best_cout = grasp(lensemble_C,len_S)
        sol = list(np.where (best_sol == 1)[0]+1)
        #
        #data = normalisation('C:/Users/Yalidine Express/PycharmProjects/saraPFE/static/data/statition.xlsx')
        data = normalisation('C:/Program Files/localisationBySara-main/static/data/statition.xlsx')
        visual,path = visualisation(sol,data)
        #
        print(path)
        return render_template('result.html',best_sol=sol,best_cout=best_cout,visual=visual,path=path)
    return render_template('index.html')