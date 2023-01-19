import os
import base64
from model import saveds
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, session


app = Flask(__name__)
#app.secret_key = b'\xb6x(\xd67\x1f\xa7\x15\x92\xf1VqU\xe9|\xbcqu\xac\xf6\x16\xa8\x8f\xe5'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
    
@app.route('/',  methods=("GET", "POST"))
def index():
    return render_template('template.html')



@app.route('/calcs',  methods=("GET", "POST"))
def calcs():

    return render_template('index.html')

@app.route('/cverl', methods=['GET', 'POST'])
def cverl():
    return render_template('calc_cverl.html')

@app.route('/calc_cverl', methods=['GET', 'POST'])
def calc_cverl():
    
    #result = None
    oborot_shin = None
    main_time_obrabotka = None
    general_time_obrabotka=None
    

    material_cverl = request.form['material_cverl'] 
    first_input1 = request.form['Input1_cverl']
    second_input1 = request.form['Input2_cverl']

    try:
        error = 'На ноль делить нельзя'
        #oborots = 1000
        pi = 3.14
        rez = None
        podacha_rez = None
        Input1_cverl = float(first_input1)
        Input2_cverl = float(second_input1)



        #-----------------------------------------------------------------#
        #                Сталь углеродистая                               #
        #-----------------------------------------------------------------#

        if material_cverl == "uglerodistaya":
            rez = 10
            if Input1_cverl <= 2:
                podacha_rez = 0.03
            else:
                if (Input1_cverl >= 3) and (Input1_cverl <= 5):
                    podacha_rez = 0.07
                else:
                    if (Input1_cverl >= 6) and (Input1_cverl <= 8):
                        podacha_rez = 0.1
                    else:
                        if (Input1_cverl >= 9) and (Input1_cverl <= 12):
                            podacha_rez = 0.16
                        else:
                            if (Input1_cverl >= 13) and (Input1_cverl <= 16):
                                podacha_rez = 0.2
                            else:
                                if (Input1_cverl >= 17) and (Input1_cverl <= 25):
                                    podacha_rez = 0.25
                                else:
                                    if (Input1_cverl >= 26) and (Input1_cverl <= 40):
                                        podacha_rez = 0.32
                                    else:
                                        if (Input1_cverl >= 41) and (Input1_cverl <= 63):
                                            podacha_rez = 0.4
                                        else:
                                            if (Input1_cverl >= 64) and (Input1_cverl <= 80):
                                                podacha_rez = 0.5
                                            else:
                                                podacha_rez = 0
                                                return error
            oborot_shin =  (1000*rez)/(pi*Input1_cverl)  
            main_time_obrabotka = Input2_cverl/(oborot_shin*podacha_rez)
            general_time_obrabotka = (1.32*main_time_obrabotka)/60                               
        elif material_cverl == 'legirovannaya':
            rez = 8
            if Input1_cverl <= 2:
                podacha_rez = 0.02
            else:
                if (Input1_cverl >= 3) and (Input1_cverl <= 5):
                    podacha_rez = 0.05
                else:
                    if (Input1_cverl >= 6) and (Input1_cverl <= 8):
                        podacha_rez = 0.08
                    else:
                        if (Input1_cverl >= 9) and (Input1_cverl <= 12):
                            podacha_rez = 0.12
                        else:
                            if (Input1_cverl >= 13) and (Input1_cverl <= 16):
                                podacha_rez = 0.14
                            else:
                                if (Input1_cverl >= 17) and (Input1_cverl <= 25):
                                    podacha_rez = 0.18
                                else:
                                    if (Input1_cverl >= 26) and (Input1_cverl <= 40):
                                        podacha_rez = 0.23
                                    else:
                                        if (Input1_cverl >= 41) and (Input1_cverl <= 63):
                                            podacha_rez = 0.27
                                        else:
                                            if (Input1_cverl >= 64) and (Input1_cverl <= 80):
                                                podacha_rez = 0.32
                                            else:
                                                podacha_rez = 0
                                                return error
            oborot_shin =  (1000*rez)/(pi*Input1_cverl) 
            main_time_obrabotka = Input2_cverl/(oborot_shin*podacha_rez) 
            general_time_obrabotka = (1.32*main_time_obrabotka)/60  
        elif material_cverl == 'nerjaveushaya':
            rez = 6
            if Input1_cverl <= 2:
                podacha_rez = 0.02
            else:
                if (Input1_cverl >= 3) and (Input1_cverl <= 5):
                    podacha_rez = 0.05
                else:
                    if (Input1_cverl >= 6) and (Input1_cverl <= 8):
                        podacha_rez = 0.08
                    else:
                        if (Input1_cverl >= 9) and (Input1_cverl <= 12):
                            podacha_rez = 0.12
                        else:
                            if (Input1_cverl >= 13) and (Input1_cverl <= 16):
                                podacha_rez = 0.14
                            else:
                                if (Input1_cverl >= 17) and (Input1_cverl <= 25):
                                    podacha_rez = 0.18
                                else:
                                    if (Input1_cverl >= 26) and (Input1_cverl <= 40):
                                        podacha_rez = 0.23
                                    else:
                                        if (Input1_cverl >= 41) and (Input1_cverl <= 63):
                                            podacha_rez = 0.27
                                        else:
                                            if (Input1_cverl >= 64) and (Input1_cverl <= 80):
                                                podacha_rez = 0.32
                                            else:
                                                podacha_rez = 0
                                                return error
            oborot_shin =  (1000*rez)/(pi*Input1_cverl)
            main_time_obrabotka = Input2_cverl/(oborot_shin*podacha_rez) 
            general_time_obrabotka = (1.32*main_time_obrabotka)/60  
        elif material_cverl == 'zharoprochnaya':
            rez = 6
            if Input1_cverl <= 2:
                podacha_rez = 0.02
            else:
                if (Input1_cverl >= 3) and (Input1_cverl <= 5):
                    podacha_rez = 0.05
                else:
                    if (Input1_cverl >= 6) and (Input1_cverl <= 8):
                        podacha_rez = 0.08
                    else:
                        if (Input1_cverl >= 9) and (Input1_cverl <= 12):
                            podacha_rez = 0.12
                        else:
                            if (Input1_cverl >= 13) and (Input1_cverl <= 16):
                                podacha_rez = 0.14
                            else:
                                if (Input1_cverl >= 17) and (Input1_cverl <= 25):
                                    podacha_rez = 0.18
                                else:
                                    if (Input1_cverl >= 26) and (Input1_cverl <= 40):
                                        podacha_rez = 0.23
                                    else:
                                        if (Input1_cverl >= 41) and (Input1_cverl <= 63):
                                            podacha_rez = 0.27
                                        else:
                                            if (Input1_cverl >= 64) and (Input1_cverl <= 80):
                                                podacha_rez = 0.32
                                            else:
                                                podacha_rez = 0 
                                                return error   
            oborot_shin =  (1000*rez)/(pi*Input1_cverl)   
            main_time_obrabotka = Input2_cverl/(oborot_shin*podacha_rez) 
            general_time_obrabotka = (1.32*main_time_obrabotka)/60                                
        elif material_cverl == 'bronza':
            rez = 20
            if Input1_cverl <= 2:
                podacha_rez = 0.05
            else:
                if (Input1_cverl >= 3) and (Input1_cverl <= 5):
                    podacha_rez = 0.08
                else:
                    if (Input1_cverl >= 6) and (Input1_cverl <= 8):
                        podacha_rez = 0.14
                    else:
                        if (Input1_cverl >= 9) and (Input1_cverl <= 12):
                            podacha_rez = 0.2
                        else:
                            if (Input1_cverl >= 13) and (Input1_cverl <= 16):
                                podacha_rez = 0.25
                            else:
                                if (Input1_cverl >= 17) and (Input1_cverl <= 25):
                                    podacha_rez = 0.3
                                else:
                                    if (Input1_cverl >= 26) and (Input1_cverl <= 40):
                                        podacha_rez = 0.4
                                    else:
                                        if (Input1_cverl >= 41) and (Input1_cverl <= 63):
                                            podacha_rez = 0.5
                                        else:
                                            if (Input1_cverl >= 64) and (Input1_cverl <= 80):
                                                podacha_rez = 0.6
                                            else:
                                                podacha_rez = 0
                                                return error
            oborot_shin =  (1000*rez)/(pi*Input1_cverl)
            main_time_obrabotka = Input2_cverl/(oborot_shin*podacha_rez) 
            general_time_obrabotka = (1.32*main_time_obrabotka)/60  
        elif material_cverl == 'alluminii':
            rez = 40
            if Input1_cverl <= 2:
                podacha_rez = 0.05
            else:
                if (Input1_cverl >= 3) and (Input1_cverl <= 5):
                    podacha_rez = 0.14
                else:
                    if (Input1_cverl >= 6) and (Input1_cverl <= 8):
                        podacha_rez = 0.18
                    else:
                        if (Input1_cverl >= 9) and (Input1_cverl <= 12):
                            podacha_rez = 0.22
                        else:
                            if (Input1_cverl >= 13) and (Input1_cverl <= 16):
                                podacha_rez = 0.3
                            else:
                                if (Input1_cverl >= 17) and (Input1_cverl <= 25):
                                    podacha_rez = 0.4
                                else:
                                    if (Input1_cverl >= 26) and (Input1_cverl <= 40):
                                        podacha_rez = 0.45
                                    else:
                                        if (Input1_cverl >= 41) and (Input1_cverl <= 63):
                                            podacha_rez = 0.5
                                        else:
                                            if (Input1_cverl >= 64) and (Input1_cverl <= 80):
                                                podacha_rez = 0.6
                                            else:
                                                podacha_rez = 0
                                                return error
            oborot_shin =  (1000*rez)/(pi*Input1_cverl)
            main_time_obrabotka = Input2_cverl/(oborot_shin*podacha_rez)
            general_time_obrabotka = (1.32*main_time_obrabotka)/60    
        
        return render_template(
            'calc_cverl.html', 
            Input1_cverl=Input1_cverl,
            podacha_rez=podacha_rez,
            material_cverl=material_cverl,
            rez=rez,
            oborot_shin=oborot_shin,
            main_time_obrabotka=main_time_obrabotka,
            general_time_obrabotka=general_time_obrabotka,
            Input2_cverl=Input2_cverl,
            calculation_success=True)


    except ZeroDivisionError:
        render_template(
            'calc_cverl.html', 
            Input1_cverl=Input1_cverl,
            podacha_rez=podacha_rez,
            material_cverl=material_cverl,
            rez='На ноль делить нельзя',
            oborot_shin = '404',
            main_time_obrabotka='404',
            general_time_obrabotka='404',
            Input2_cverl=Input2_cverl,
            error="На ноль делить нельзя",
            calculation_succces=False
        )
    except ValueError:
        render_template(
            'calc_cverl.html', 
            Input1_cverl=first_input1,
            podacha_rez=podacha_rez,
            material_cverl=material_cverl,
            rez='На ноль делить нельзя',
            oborot_shin = '404',
            main_time_obrabotka='404',
            general_time_obrabotka='404',
            Input2_cverl=second_input1,
            error="На ноль делить нельзя",
            calculation_succces=False
        )

@app.route('/frez', methods=['GET', 'POST'])
def frez():
    return render_template('calc_frez.html')

@app.route('/calc_frez',  methods=['GET', 'POST'])
def calc_frez():
    material_frez=request.form['material_frez']
    diametr_frez=request.form['diametr_frez']
    first_input = request.form['Input1_frez']
    second_input = request.form['Input2_frez']
    thrid_input = request.form['Input3_frez']
    perek = None


    error2 = 'На ноль делить нельзя' 
    siem = None
    
    zub = None
    try:
       
        input1 = float(first_input)
        input2 = float(second_input)
        input3 = float(thrid_input)
        kolichestvo_frez = None
        V_frez = None
        pi = 3.14
        siem = int(diametr_frez)/2
        
        oborot_frez = None
        podacha_frez = None     
        time_prokhod_frez = None
        kol_frez = None
        time_frez = None        
        general_time_frez = None
        if diametr_frez <='25':
            kolichestvo_frez = 3
        else:
            if (diametr_frez >='26') and (diametr_frez < '63'):
                kolichestvo_frez = 4
            else:
                if diametr_frez == '63':
                    kolichestvo_frez = 5
                else:
                    error2
        if (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '6'):
            zub = 0.04
            V_frez = 19      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '8'):
            zub = 0.05
            V_frez = 17      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '10'):
            zub = 0.05
            V_frez = 27      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '12'):
            zub = 0.06
            V_frez = 29          
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '16'):
            zub = 0.05
            V_frez = 28      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '20'):
            zub = 0.05
            V_frez = 27      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '25'):
            zub = 0.06
            V_frez = 27      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '32'):
            zub = 0.06
            V_frez = 27      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '40'):
            zub = 0.05
            V_frez = 31      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '50'):
            zub = 0.05
            V_frez = 28      
        elif (material_frez=='uglerodistaya_legirovannaya') and (diametr_frez == '63'):
            zub = 0.04
            V_frez = 29      

    #----------------------------------------------------------------------#
    #----------------------------------------------------------------------#
    #----------------------------------------------------------------------#
    #----------------------------------------------------------------------#
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '6'):
            zub = 0.03
            V_frez = 19            
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '8'):
            zub = 0.03
            V_frez = 22
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '10'):
            zub = 0.03
            V_frez = 34
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '12'):
            zub = 0.04
            V_frez = 34
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '16'):
            zub = 0.03
            V_frez = 38
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '20'):
            zub = 0.03
            V_frez = 35
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '25'):
            zub = 0.04
            V_frez = 31
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '32'):
            zub = 0.04
            V_frez = 31
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '40'):
            zub = 0.03
            V_frez = 35
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '50'):
            zub = 0.03
            V_frez = 33
        elif (material_frez=='korozinostoikie_zharoprochnaya') and (diametr_frez == '63'):
            zub = 0.02
            V_frez = 33
    #----------------------------------------------------------------------#
    #----------------------------------------------------------------------#
    #----------------------------------------------------------------------#
    #----------------------------------------------------------------------#
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '6'):
            zub = 0.05
            V_frez = 48          
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '8'):
            zub = 0.07
            V_frez = 71
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '10'):
            zub = 0.05
            V_frez = 88
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '12'):
            zub = 0.08
            V_frez = 95
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '16'):
            zub = 0.07
            V_frez = 88
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '20'):
            zub = 0.07
            V_frez = 97
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '25'):
            zub = 0.09
            V_frez = 95
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '32'):
            zub = 0.08
            V_frez = 95
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '40'):
            zub = 0.08
            V_frez = 83
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '50'):
            zub = 0.07
            V_frez = 98
        elif (material_frez=='mednie_alluminii') and (diametr_frez == '63'):
            zub = 0.06 
            V_frez = 89            
        oborot_frez = ((1000*V_frez)/(pi*int(diametr_frez)))/2
        podacha_frez = kolichestvo_frez*zub*oborot_frez
        time_prokhod_frez = (input2 + int(diametr_frez))/podacha_frez
        kol_frez = (input1/int(diametr_frez))*(input3/siem)+(input1/int(diametr_frez))
        
        time_frez = kol_frez*time_prokhod_frez
        general_time_frez = (1.32*time_frez)/60
        perek = 0.7*int(diametr_frez)

        return render_template(
        'calc_frez.html',
        material_frez=material_frez,
        diametr_frez=diametr_frez,
        kolichestvo_frez=kolichestvo_frez,
        siem=siem,
        general_time_frez=general_time_frez,
        perek=perek,
        zub=zub,
        V_frez=V_frez,
        oborot_frez=oborot_frez,
        podacha_frez=podacha_frez,
        kol_frez=kol_frez,
        time_prokhod_frez=time_prokhod_frez,
        time_frez=time_frez,
        input1=input1,
        input2=input2,
        input3=input3,
        calculation_sussecc=True
        )
    except ZeroDivisionError:
        return render_template(
            'calc_frez.html',
            material_frez=material_frez,
            general_time_frez=general_time_frez,
            diametr_frez=diametr_frez,
            kolichestvo_frez=kolichestvo_frez,
            input1=input1,
            input2=input2,
            input3=input3,
            zub=zub,
            V_frez=V_frez,
            kol_frez=kol_frez,
            time_frez=time_frez,
            siem='404',
            perek='404',
            oborot_frez='404',
            podacha_frez='404',
            time_prokhod_frez='404',
            error2 = 'На ноль делить нельзя',
            calculation_sussecc=False
        )
        
    except ValueError:
        return render_template(
            'calc_frez.html',
            material_frez=material_frez,
            diametr_frez=diametr_frez,
            general_time_frez=general_time_frez,
            kolichestvo_frez=kolichestvo_frez,
            zub=zub,
            V_frez=V_frez,
            input1=input1,
            input2=input2,
            input3=input3,
            kol_frez=kol_frez,
            time_frez=time_frez,
            siem='404',
            perek='404',
            oborot_frez='404',
            podacha_frez='404',
            time_prokhod_frez='404',
            error2 = 'На ноль делить нельзя2',
            calculation_sussecc=False
        )


@app.route("/result",  methods=['GET', 'POST'])
def result():
    error = None
    error2 = '404' 
    podacha = None
    result = None

    result_prokhod = None
    result_kol_prokhod = None

    tresult_prokhod = None
    tresult_kolvo = 2
    main_time_result = None
    tresult = None
    res_minuts = None

    result_DONE=None
    result_time=None
    minuts_result = None


    vnytrenee_result_kolvo = None
    vnytrenee_main_time_result = None
    vnytrenee_result = None
    res_minuts_vnytrenee = None


    material = request.form['material']
    
    glubina = request.form['glubina']
    first_input = request.form['Input1']
    second_input = request.form['Input2']
    thrid_input = request.form['Input3']

    try:
        oborots = 1000
        V=0     
        error2 = 'На ноль делить нельзя'  
        pi = 3.14
        x=0
       
        
        input1 = float(first_input)
        input2 = float(second_input)
        input3 = float(thrid_input)
        
        #-----------------------------------------------------------------#   
        #-----------------------------------------------------------------#
        #                Сталь углеродистая
        #-----------------------------------------------------------------#
        # #
        # 
        # 
            
#--------------------------------------#
#Введите глубину резания ( e, мм ): 0,7#
#--------------------------------------#
        if material == "uglerod" and glubina == "0.7":
                if input1 <= 18:
                    V=190
                    podacha = 0.16   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=159
                        podacha = 0.33
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=121
                            podacha = 0.61
                        else:
                            if (input1 >=181):
                                podacha = 0
                                error2
                            
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)

                vnytrenee_result_kolvo = (input2-input1) / (2*0.7)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                result_kol_prokhod = abs((input1 - input2) / 2 * (0.7+1))
                
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60
#----------------------------------------#
#Введите глубину резания ( e, мм ): 1,5  #
#----------------------------------------#
        elif material == "uglerod" and glubina == "1.5":
                if input1 <= 18:
                    V=190 
                    podacha = 0.13  
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=171
                        podacha = 0.27  
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=146
                            podacha = 0.49
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=111
                                podacha = 0.88 
                            else:
                                if (input1 >=501):
                                    podacha = 0
                                    error2
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*1.5)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                result_kol_prokhod = abs((input1 - input2) / 2 * (1.5+1))
               
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60
#--------------------------------------#
#Введите глубину резания ( e, мм ): 2  #
#--------------------------------------#
        elif material == "uglerod" and glubina == "2":
                if input1 <= 18:
                    podacha = 0
                    error2   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=179
                        podacha = 0.24 
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=146
                            podacha = 0.43  
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=121
                                podacha = 0.77
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V=90
                                    podacha = 1.4
                                else:
                                    podacha = 0
                                    error2
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)

                vnytrenee_result_kolvo = (input2-input1) / (2*2)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60
                
                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (2+1))
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

#----------------------------------------#
#Введите глубину резания ( e, мм ): 3    #
#----------------------------------------#
                
        elif material == "uglerod" and glubina == "3":
                if input1 <= 18:
                    podacha = 0
                    error2   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=179
                        podacha = 0.21
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=159
                            podacha = 0.39
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=121
                                podacha = 0.7
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    podacha = 0
                                    error2 #1.24 (#Н/Д)
                                
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*3)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (3+1))
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

#----------------------------------------#
#Введите глубину резания ( e, мм ): 7    #
#----------------------------------------#

        elif material == "uglerod" and glubina == "7":
                if input1 <= 18:
                    podacha = 0
                    error2   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=131
                        podacha = 0.16  
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=118
                            podacha = 0.3
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=94
                                podacha = 0.54
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V=83
                                    podacha = 0.91
                                else:
                                    podacha = 0
                                    error2
                                
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*7)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (7+1))
                
                result_DONE = result_prokhod * result_kol_prokhod 
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

       
        #-----------------------------------------------------------------#   
        #-----------------------------------------------------------------#
        # 
        # 
        #               Сталь нержавеющая и жаропрочная
        #-----------------------------------------------------------------#
        # #
        # 
        #     

#----------------------------------------#
#Введите глубину резания ( e, мм ): 0,7  #
#----------------------------------------#        
        elif material == "nerj" and glubina == "0.7":
                if input1 <= 18:
                    V=165
                    podacha = 0.13   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=144
                        podacha = 0.17
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=144
                            podacha = 0.20
                        else:
                            if (input1 >=181) and (input1 <= 500):
                                podacha = 0.28
                                V=130
                            else:
                                if (input1 >= 501) and (input1 <= 3150):
                                    V= 84
                                    podacha = 0.75
                                else:  
                                    podacha = 0
                                    error2
                            
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)

                vnytrenee_result_kolvo = (input2-input1) / (2*0.7)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                result_kol_prokhod = abs((input1 - input2) / 2 * (0.7+1))
                
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

#----------------------------------------#
#Введите глубину резания ( e, мм ): 1,5  #
#----------------------------------------#   

        elif material == "nerj" and glubina == "1.5":
                if input1 <= 18:
                    V=165 
                    podacha = 0.10
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=165
                        podacha = 0.14 
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=144
                            podacha = 0.16
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=130
                                podacha = 0.23
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V = 103
                                    podacha = 0.60
                                else:
                                    podacha = 0
                                    error2
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*1.5)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                result_kol_prokhod = abs((input1 - input2) / 2 * (1.5+1))
               
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

#----------------------------------------#
#Введите глубину резания ( e, мм ): 2    #
#----------------------------------------#  

        elif material == "nerj" and glubina == "2":
                if input1 <= 18:
                    V=165
                    podacha=0.10 
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=165
                        podacha = 0.13
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=165
                            podacha = 0.14
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=130
                                podacha = 0.21
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V=103
                                    podacha = 0.54
                                else:
                                    podacha = 0
                                    error2
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)

                vnytrenee_result_kolvo = (input2-input1) / (2*2)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60
                
                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (2+1))
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

#----------------------------------------#
#Введите глубину резания ( e, мм ): 3    #
#----------------------------------------#  
                
        elif material == "nerj" and glubina == "3":
                if input1 <= 18:
                    podacha = 0
                    error2   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=165
                        podacha = 0.10
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=165
                            podacha = 0.13
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=144
                                podacha = 0.18
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    podacha = 0
                                    error2 #1.24 (#Н/Д)
                                
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*3)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (3+1))
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

#----------------------------------------#
#Введите глубину резания ( e, мм ): 7    #
#----------------------------------------#  

        elif material == "nerj" and glubina == "7":
                if input1 <= 18:
                    podacha = 0
                    error2   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        podacha = 0
                        error2 
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=92
                            podacha = 0.10
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=92
                                podacha = 0.14
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V=72
                                    podacha = 0.37
                                else:
                                    podacha = 0
                                    error2
                                
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*7)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (7+1))
                
                result_DONE = result_prokhod * result_kol_prokhod 
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

        #-----------------------------------------------------------------#   
        #-----------------------------------------------------------------#
        # 
        # 
        #               Медь и аллюминий
        #-----------------------------------------------------------------#
        # #
        # 
        #     
#----------------------------------------#
#Введите глубину резания ( e, мм ): 0,7  #
#----------------------------------------# 
        elif material == "alumin" and glubina == "0.7":
                if input1 <= 18:
                    V=468
                    podacha = 0.20   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=319
                        podacha = 0.43
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=261
                            podacha = 0.73
                        else:
                            if (input1 >=181) and (input1 <= 500):
                                podacha = 1.20
                                V=205
                            else:
                                if (input1 >= 501) and (input1 <= 3150):
                                    V= 124
                                    podacha = 2.50
                                else:  
                                    podacha = 0
                                    error2
                            
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)

                vnytrenee_result_kolvo = (input2-input1) / (2*0.7)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                result_kol_prokhod = abs((input1 - input2) / 2 * (0.7+1))
                
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

#----------------------------------------#
#Введите глубину резания ( e, мм ): 1,5  #
#----------------------------------------# 

        elif material == "alumin" and glubina == "1.5":
                if input1 <= 18:
                    V=468
                    podacha = 0.17
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=375
                        podacha = 0.36
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=261
                            podacha = 0.62
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=205
                                podacha = 1.03
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V = 124
                                    podacha = 2.20
                                else:
                                    podacha = 0
                                    error2
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*1.5)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                result_kol_prokhod = abs((input1 - input2) / 2 * (1.5+1))
               
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60

#----------------------------------------#
#Введите глубину резания ( e, мм ): 2    #
#----------------------------------------# 

        elif material == "alumin" and glubina == "2":
                if input1 <= 18:
                    V=468
                    podacha=0.14
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=375
                        podacha = 0.32
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=319
                            podacha = 0.55
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=261
                                podacha = 0.92
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V=161
                                    podacha = 1.98
                                else:
                                    podacha = 0
                                    error2
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)

                vnytrenee_result_kolvo = (input2-input1) / (2*2)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60
                
                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (2+1))
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60
                
#----------------------------------------#
#Введите глубину резания ( e, мм ): 3    #
#----------------------------------------# 

        elif material == "alumin" and glubina == "3":
                if input1 <= 18:
                    V=468
                    podacha=0.13 
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=422
                        podacha = 0.71
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=319
                            podacha = 0.50
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=261
                                podacha = 0.85
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V=161
                                    podacha = 1.82
                                else:
                                    podacha = 0
                                    error2 
                                
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*3)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (3+1))
                
                result_DONE = result_prokhod * result_kol_prokhod
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60


#----------------------------------------#
#Введите глубину резания ( e, мм ): 7    #
#----------------------------------------# 

        elif material == "alumin" and glubina == "7":
                if input1 <= 18:
                    podacha = 0
                    error2   
                else:
                    if (input1 >= 19) and (input1 <= 50):
                        V=346
                        podacha=0.24 
                    else:
                        if (input1 >=51) and (input1<=180):
                            V=308
                            podacha = 0.40
                        else:
                            if (input1 >=181) and (input1 <=500):
                                V=214
                                podacha = 0.67
                            else:
                                if (input1 >=501) and (input1 <= 3150):
                                    V=168
                                    podacha = 1.47
                                else:
                                    podacha = 0
                                    error2
                                
                result = (oborots*V) / (pi * input1)
                result_prokhod = (input3 + 2) / (result * podacha)


                vnytrenee_result_kolvo = (input2-input1) / (2*7)+1
                vnytrenee_main_time_result = vnytrenee_result_kolvo * result_prokhod
                vnytrenee_result = (1.32*vnytrenee_main_time_result) / 60
                res_minuts_vnytrenee = vnytrenee_result * 60

                #Режимы резания, торцевое точение и отрезка#
                tresult_prokhod = (input1 + 2) / (podacha * result)
                main_time_result = tresult_kolvo * tresult_prokhod
                tresult = (1.32 * main_time_result) / 60
                res_minuts = tresult * 60
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                result_kol_prokhod = abs((input1 - input2) / 2 * (7+1))
                
                result_DONE = result_prokhod * result_kol_prokhod 
                result_time = (1.32 * result_DONE) / 60
                minuts_result = result_time * 60
        else:
            podacha = 0
            error2
                




        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            input3=input3,
            V=V,
            podacha=podacha,
            material=material,
            result=result,
            vnytrenee_result_kolvo=vnytrenee_result_kolvo,
            vnytrenee_result=vnytrenee_result,
            vnytrenee_main_time_result=vnytrenee_main_time_result,
            res_minuts_vnytrenee=res_minuts_vnytrenee,
            result_prokhod=result_prokhod,
            tresult_prokhod=tresult_prokhod,
            tresult_kolvo=tresult_kolvo,
            tresult=tresult,
            minuts_result=minuts_result,
            res_minuts=res_minuts,
            main_time_result=main_time_result,
            result_kol_prokhod=result_kol_prokhod,
            
            result_DONE=result_DONE,
            result_time=result_time,
            calculation_success=True
        )
        
    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            input3=input3,
            error2=error2,
            V=V,
            material=material,
            result="На ноль делить нельзя",
            result_prokhod = "error",
            tresult_prokhod='error',
            tresult_kolvo='error',
            tresult='error',
            vnytrenee_main_time_result='error',
            vnytrenee_result_kolvo='error',
            vnytrenee_result='error',
            res_minuts_vnytrenee='error',
            res_minuts='error',
            main_time_result='error',
            result_kol_prokhod='error',
            result_DONE='error',
            result_time='error',
            minuts_result='ERROR',
            #result_oborot="BAD",
            calculation_success=False,
            error="You cannot divide by zero"
        )
        
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            input3=thrid_input,
            error2=error2,
            V=V,
            material=material,
            result="Bad Input",
            result_prokhod = "error",
            tresult_prokhod='error',
            tresult_kolvo='error',
            vnytrenee_result_kolvo='error',
            vnytrenee_main_time_result='error',
            vnytrenee_result='error',
            res_minuts_vnytrenee='error',
            tresult='error',
            res_minuts='error',
            main_time_result='error',
            result_kol_prokhod='error',
            result_DONE='error',
            minuts_result='ERROR',
            result_time='error',
            #result_oborot=result_oborot,
            calculation_success=False,
            error="Cannot perform numeric operations with provided input"
        )

    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
 