#include <stdio.h>
#include <stdlib.h> 
float cm_to_m(float cm){return cm/100;}
float m_to_cm(float m){return m*100;}
float m_to_km(float m){return m/1000;}
float km_to_m(float km){return km*1000;}
float inch_to_cm(float in){return in*2.54;}
float cm_to_inch(float cm){return cm/2.54;}
float g_to_kg(float g){return g/1000;}
float kg_to_g(float kg){return kg*1000;}
float sec_to_hr(float s){return s/3600;}
float hr_to_sec(float h){return h*3600;}
float hr_to_day(float h){return h/24;}
float day_to_hr(float d){return d*24;}
float c_to_f(float c){return (c*1.8)+32;}
float f_to_c(float f){return (f-32)*(5.0/9.0);}
float c_to_k(float c){return c+273.15;}
float k_to_c(float k){return k-273.15;}
float l_to_ml(float l){return l*1000;}
float ml_to_l(float ml){return ml/1000;}
float j_to_cal(float j){return j/4.184;}
float cal_to_j(float cal){return cal*4.184;}
float pa_to_bar(float pa){return pa/100000;}
float bar_to_pa(float bar){return bar*100000;}
float pa_to_psi(float pa){return pa/6895;}
float psi_to_pa(float psi){return psi*6895;}
float torr_to_pa(float torr){return torr*133.322;}
float pa_to_torr(float pa){return pa/133.322;}
float ms_to_kmh(float ms){return ms*3.6;}
float kmh_to_ms(float kmh){return kmh/3.6;}
float mileps_to_kmh(float mileps){return mileps*5794;}
float kmh_to_mileps(float kmh){return kmh/5794;}
float gcm3_to_kgm3(float gcm3){return gcm3*1000;}
float kgm3_to_gcm3(float kgm3){return kgm3/1000;}
float hp_to_w(float hp){return hp*745.7;}
float w_to_hp(float w){return w/745.7;}
float Mbyteps_to_mbps(float Mbyteps){return Mbyteps/8;}
float mbps_to_Mbyteps(float mbps){return mbps*8;}
float mgdl_to_mmolL(float mgdl){return mgdl/18.018;}
float mmolL_to_mgdl(float mmolL){return mmolL*18.018;}
float gold_purity(float karat){return (karat/24)*100;}
float knot_to_kmph(float knot){return knot*1.85;}
float kmph_to_knot(float kmph){return kmph/1.85;}


int main()
{
    FILE *inputFile = NULL; 
    FILE *outputFile = NULL;
    
    int conversion_choice;
    float input_value;
    float result = 0.0;
    
    inputFile = fopen("input_txt","r");
    if (inputFile == NULL)
    {
        return 1;
    }
    
    if (fscanf(inputFile,"%d %f",&conversion_choice,&input_value) != 2)
    {
        goto cleanup; 
    }

    switch (conversion_choice)
    {
        case 1:
        result=cm_to_m(input_value);
        break;

        case 2:
        result=m_to_cm(input_value);
        break;

        case 3:
        result=m_to_km(input_value);
        break;

        case 4:
        result=km_to_m(input_value);
        break;

        case 5:
        result=inch_to_cm(input_value);
        break;

        case 6:
        result=cm_to_inch(input_value);
        break;

        case 7:
        result=g_to_kg(input_value);
        break;

        case 8:
        result=kg_to_g(input_value);
        break;

        case 9:
        result=sec_to_hr(input_value);
        break;

        case 10:
        result=hr_to_sec(input_value);
        break;

        case 11:
        result=hr_to_day(input_value);
        break;

        case 12:
        result=day_to_hr(input_value);
        break;

        case 13:
        result=c_to_f(input_value);
        break;

        case 14:
        result=f_to_c(input_value);
        break;

        case 15:
        result=c_to_k(input_value);
        break;

        case 16:
        result=k_to_c(input_value);
        break;

        case 17:
        result=l_to_ml(input_value);
        break;

        case 18:
        result=ml_to_l(input_value);
        break;

        case 19:
        result=j_to_cal(input_value);
        break;

        case 20:
        result=cal_to_j(input_value);
        break;

        case 21:
        result=pa_to_bar(input_value);
        break;

        case 22:
        result=bar_to_pa(input_value);
        break;

        case 23:
        result=pa_to_psi(input_value);
        break;

        case 24:
        result=psi_to_pa(input_value);
        break;

        case 25:
        result=torr_to_pa(input_value);
        break;

        case 26:
        result=pa_to_torr(input_value);
        break;

        case 27:
        result=ms_to_kmh(input_value);
        break;

        case 28:
        result=kmh_to_ms(input_value);
        break;

        case 29:
        result=mileps_to_kmh(input_value);
        break;

        case 30:
        result=kmh_to_mileps(input_value);
        break;

        case 31:
        result=gcm3_to_kgm3(input_value);
        break;

        case 32:
        result=kgm3_to_gcm3(input_value);
        break;

        case 33:
        result=hp_to_w(input_value);
        break;

        case 34:
        result=w_to_hp(input_value);
        break;

        case 35:
        result=Mbyteps_to_mbps(input_value);
        break;

        case 36:
        result=mbps_to_Mbyteps(input_value);
        break;

        case 37:
        result=mgdl_to_mmolL(input_value);
        break;

        case 38:
        result=mmolL_to_mgdl(input_value);
        break;

        case 39:
        result=gold_purity(input_value);
        break;

        case 40:
        result=knot_to_kmph(input_value);
        break;

        case 41:
        result=kmph_to_knot(input_value);
        break;

        default:
        result=-999.99;
        break;
    }

    outputFile = fopen("output_txt","w");
    if (outputFile == NULL)
    {
        goto cleanup; 
    }

    fprintf(outputFile,"%.2f",result);

    goto cleanup; 

cleanup:
    if (outputFile != NULL)
    {
        fclose(outputFile);
    }
    
    if (inputFile != NULL)
    {
        fclose(inputFile);
    }
    
    return 0;
}



