import matplotlib.pyplot as plt
import pandas as pd

#def rock_classes (UCS,E):
    #pass

df=pd.DataFrame({"UCS":[4000,5000,10000,2000,50000,55000,55000,47000,35000,12000,15000,45000],"E":[400000,1000000,2000000,21000000,15000000,5000000,6000000,8000000,5000000,8000000,15000000,6000000],"Mec_Facies":[1,2,3,4,3,2,3,2,2,3,1,2]})

def check_units(df=df):
    data = df.copy()
    units_acceptable = ["PSI","Pa","MPa","GPa"]
    
    def check():
        while "check":
            unit = input(f"This scripts works with {units_acceptable}.\nWhich one is your data using?\n")
            if unit in units_acceptable:
                if unit == "PSI":
                    return data
                elif unit == "Pa":
                    data["UCS"] = data["UCS"] / 6895.12515
                    data["E"] = data["E"] / 6895.12515
                    return data
                elif unit == "MPa":
                    data["UCS"] = data["UCS"] * 145.038
                    data["E"] = data["E"] * 145.038
                    return data
                elif unit == "GPa":
                    data["UCS"] = data["UCS"] * 145038
                    data["E"] = data["E"] * 145038
                    return data
            else:
                print ("Write down correctly!!!")
    data = check()
    print ("Dataframe in PSI units!!")
    print(data)
    return data


def plot_deere_miller_graph_log_psi (df=df):
    data = df.copy()
    #data.UCS = [item*1000 for item in data.UCS]
    #data.E = [item*1000000 for item in data.E]

    data = check_units(data)

    def check_true_or_false(question):
        while "Wrong Answer":
            answer = str(input(question+' (y/n): ')).lower().strip()
            if answer[:1] == 'y':
                return True
            elif answer[:1] == 'n':
                return False
            else:
                print("Write Yes or No, please!!!")

    rock_class_name=[]
    if check_true_or_false("Does this data have rock_class data?") == True:
        def check_column_exist(question):
            while "Wrong Answer":
                answer = str(input(question))
                if answer in data.columns:
                    return answer
                else:
                    print("Digite correto!!!")
                    
        data_column = data.columns
        rock_class_name = check_column_exist("Please, enter the name of Rock Class column:\n"
                                +f"{data_column}:\n")
        
        if data[rock_class_name].any != int or float:
            data["color_id"] = data[rock_class_name].astype("category").cat.codes
        else:
            data["color_id"] = data[rock_class_name]
    else:
        data["color_id"]=1
    
    #x_Pa= [num*1000 for num in UCS]
    #y_Pa= [num*1000000 for num in E]
    
    fig, ax = plt.subplots(figsize=(10,10),dpi=90)
    fig.canvas.draw()

    """
    colors={"A":"blue","AH":"","AL":"",
    "B":"","BH":"","BL",
    "C":"","CH":"","CL":"",
    "D":"","DH":"","DL":"",
    "E":"","EH":"","EL":""
    }"""
    #ax.scatter(data["UCS]",data["E"], c = data.Mec_Facies.astype.cat.codes ,z order=3)
    ax.scatter(data.UCS,data.E,c=data.color_id,zorder=3)
    ax.set_title("Rock Classification for Intact Rocks\nDeere & Miller, 1966")
    ax.set_ylabel("Young's Modulus\nE (PSI)")
    ax.set_xlabel("Unconfined Compressive Strength - UCS (PSI)")
    ax.grid(True,which="both")


    # high modulus ration line
    xh1 = 1000
    yh1 = 500000
    xh2 = 65000
    yh2 = 32500000
    ax.plot([xh1,xh2],[yh1,yh2],color="g")

    # low modulus ration line
    xl1 = 1000
    yl1 = 200000
    xl2 = 65000
    yl2 = 13000000
    ax.plot([xl1,xl2],[yl1,yl2],color="g")

    #Graph limits
    ax.set_xlim(1000,65000)
    ax.set_ylim(300000,22000000)

    #Graph axis labels
    #ax.set_xticks([1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000])
    #ax.set_xticklabels(["1","2","3","4","5","6","7","8","9","10","20","30","40","50","60"])
    #ax.set_yticklabels([300000,500000,1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000,20000000])

    # Strength limits
    ax.axvline(4000,color="r")
    ax.axvline(8000,color="r")
    ax.axvline(16000,color="r")
    ax.axvline(32000,color="r")
    
    # Annotations
    bbox_props = dict(boxstyle="round", fc="w", ec="0.8", alpha=0.9)
    ax.text(2000,19000000, "E\nVery Low Strengh", ha="center", va="center", size=10,bbox=bbox_props)
    ax.text(5800,19000000, "D\nLow Strengh", ha="center", va="center", size=10,bbox=bbox_props)
    ax.text(11300,19000000, "C\nMedium Strengh", ha="center", va="center", size=10,bbox=bbox_props)
    ax.text(23000,19000000, "B\nHigh Strengh", ha="center", va="center", size=10,bbox=bbox_props)
    ax.text(46000,19000000, "A\nVery High Strengh", ha="center", va="center", size=10,bbox=bbox_props)

    bbox_props2 = dict(boxstyle="round4", fc=(0.8, 0.9, 0.9), ec="b", lw=1,alpha=0.2)
    hmr = ax.text(8000,5500000, "High Modulus Ratio", ha="center", va="center", rotation=45,
                size=15,
                bbox=bbox_props2)
    bb1 = hmr.get_bbox_patch()
    bb1.set_boxstyle("round4", pad=0.6)

    amr = ax.text(8000,2500000, "Average Modulus Ratio", ha="center", va="center", rotation=45,
                size=15,
                bbox=bbox_props2)
    bb2 = amr.get_bbox_patch()
    bb2.set_boxstyle("round4", pad=0.6)

    lmr = ax.text(8000,1000000, "Low Modulus Ratio", ha="center", va="center", rotation=45,
                size=15,
                bbox=bbox_props2)
    bb2 = lmr.get_bbox_patch()
    bb2.set_boxstyle("round4", pad=0.6)

    ax.set_yscale("log")
    ax.set_xscale("log")
    #plt.grid(True)
    plt.show()
     

def class_mec_facies_deere_miller_psi(df=df):

    data = df.copy()

    #data.UCS = [item*1000 for item in data.UCS]
    #data.E = [item*1000000 for item in data.E]
    
    data=check_units(data)

    data["Modulus_Ratio"] = data["E"] / data["UCS"]

    def strength_UCS(UCS):
        if UCS<4000:
            return "E"
        elif 4000 <= UCS < 8000:
            return "D"
        elif 8000 <= UCS < 16000:
            return "C"
        elif 16000 <= UCS < 32000:
            return "B"
        else:
            return "A" 

    def modulus_ratio (Modulus_Ratio):
        if Modulus_Ratio >=500:
            return "H"
        elif Modulus_Ratio <=200:
            return "L"
        else:
            return "-"

    data["strengh_class"]=data["UCS"].apply(strength_UCS)
    data["Modulus_Ratio_class"]=data["Modulus_Ratio"].apply(modulus_ratio)  
    data["Deere_&_Miller_Class"]=data["strengh_class"]+data["Modulus_Ratio_class"]

    return data



#if __name__=='__main__':
    #plot_deere_miller_graph_log_psi()
    #class_mec_facies_deere_miller_psi()
    check_units()