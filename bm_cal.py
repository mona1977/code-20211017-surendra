#Developer : Surendra Gupta
#Date : 17-Oct-2021
#Objective : Prepare BMI report according input JSON data
import json
def BMIcal():
    # Open and Load JSON file
    with open('BMCAL.json', 'r') as openjson:
        params = json.load(openjson)   
    # Setup BMI age and their result
    RangeBMI={0:[0,18.5],1:[18.5,24.9],2:[25,29.9],3:[30,34.9],4:[35,39.9],5:[40,50]}
    Riskhealth=["Malnutrition risk","Low risk","Enhanced risk","Medium risk","High risk","Very high risk"]
    CategoryBMI=["Underweight","Normal weight","Overweight","Moderately obese","Severely obese","Very severely obese"]
    
    Final_Result={}
    i=1
    for Item in params:
        BMI=round(Item["WeightKg"]/(Item["HeightCm"]/100)**2,2)
        for key in RangeBMI:
            if key==5:
                Final_Result[i]=[BMI,Riskhealth[key],CategoryBMI[key]]
                break
            if BMI >= RangeBMI[key][0] and BMI < RangeBMI[key+1][0]:
                Final_Result[i]=[BMI,Riskhealth[key],CategoryBMI[key]]
                break
        i+=1

    return Final_Result

if __name__=='__main__':
    Final_Result=BMIcal()
    total_overweighted_person=0
    for key in Final_Result:
        if "Overweight" in Final_Result[key]:
            total_overweighted_person+=1
    print(Final_Result)
    print(f"Total Number of Overweighted person {total_overweighted_person}")