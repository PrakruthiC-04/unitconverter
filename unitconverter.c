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



