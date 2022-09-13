from cgitb import enable
from itertools import count
from this import d
import PySimpleGUI as sg
from numpy.lib.function_base import append
import io
import msoffcrypto
import pandas as pd
import numpy as np
import xlsxwriter
import streamlit.bootstrap
from streamlit import config as _config
import sys
from streamlit import cli as stcli

def main():

    #main function: takes read path of the file and password and returns the dataframe
    def import_df(read_path, key):
        decrypted = io.BytesIO()
        #read_path = get_file()
        #key = input("\nEnter File Password: ")
        with open(read_path, "rb") as f:
            file = msoffcrypto.OfficeFile(f)
            file.load_key(password=key)
            file.decrypt(decrypted)
        df = pd.read_excel(decrypted)
        #print(df)
        return df

    def process_combined(df, write_path):
        df = process_df(df)
        df_complete = pivot(df)
        df_removed = remove_first_specimen(df, df_complete)
        export_df(df, df_removed, write_path)

    def process_df(df):
        df = df.set_index("Received")
        df = df.reset_index()
        #to ensure if ' ' will not cause loss of data
        df["Organism"] = df["Organism"].fillna("dummy")
        df["Antibiotic Interpretation"] = df["Antibiotic Interpretation"].fillna("dummy")
        df["Resulted"] = df["Resulted"].fillna("dummy")
        df["dummy"] = np.nan
        df.sort_values(by=["Received"], inplace=True)
        #print(df)
        return df
    
    def pivot(df):
        df = df.pivot_table(index=("Patient Name", "Organism", "Specimen ID", "Specimen Type", "MRN", "Received"), 
                            columns="Antibiotic", 
                            values="Antibiotic Interpretation", 
                            aggfunc="first"
                            )
        df = df.reset_index()
        df = df.replace('dummy',np.nan)
        df = df.sort_values("Specimen ID")
        #df.drop_duplicates()
        #print(df)
        return df

    def remove_first_specimen(df, df_complete):
        df_staphyl = df_complete[df_complete["Organism"].str.contains("Staphylococcus aureus", na=False)]
        df_staphyl_sorted = df_staphyl.sort_values(by="Received")
        df_staphyl_removed = df_staphyl_sorted.drop_duplicates(subset=["Patient Name"])
        df_entero = df_complete[df_complete["Organism"].str.contains("Enterococcus", na=False)]
        df_entero = df_entero[~df_entero["Organism"].str.contains("gallinarum", na=False)]
        df_entero_removed = df_entero[~df_entero["Organism"].str.contains("casseliflavus", na=False)]
        df_entero_sorted = df_entero_removed.sort_values(by="Received")
        df_entero_ready = df_entero_sorted.drop_duplicates(subset="Patient Name")
        df_removed = df_staphyl_removed.append(df_entero_ready)
        #use the specimen ID of filtered df and back finds the specimen ID and organism
        gp_list = df_removed["Specimen ID"].tolist()
        organism_list = df_removed["Organism"].tolist()
        df = df.set_index("Specimen ID")
        df = df.loc[gp_list]
        df = df.reset_index()
        df = df.set_index("Organism")
        df = df.loc[organism_list]
        return df
    
    def export_df(df1, df2, write_path):
        write = pd.ExcelWriter(write_path, engine='xlsxwriter')
        df1.to_excel(write, "Complete")
        df2.to_excel(write, "First Specimen (Gram Positive)")
        write.save()

    sg.SetOptions(font="any 16")

    def main_window():
        layout = [
            [sg.Text("Choose the Epic output file", text_color="yellow")],
            [sg.InputText(key="-FILE_PATH-", enable_events=True),
            sg.FileBrowse(initial_folder="./", file_types=(("Excel files", "*.xlsx"),))],
            [sg.Text("Enter file password below",  text_color="yellow")],
            [sg.InputText(key="-PWD-", password_char="*")],
            [sg.Button("Import"),sg.Button("Click to import Additional Exports")],
            [sg.Text("Caution: data must be imported prior to process", text_color="yellow")],
            [sg.Button("Process")],
            [sg.Text("   ")],
            [sg.Text("Usage: dashboard can be launched if processed file have been created previously", text_color="yellow")],
            [sg.Button("Launch Analytics Dashboard")],
            [sg.Text("   ")],
            [sg.Exit()]
        ]
        window = sg.Window("HHS Isolates Analysis", layout=layout, finalize=True)
        return window

    def file_save_window():
        layout = [
            [sg.InputText(key="-SAVE_PATH-", enable_events=True),
            sg.FileSaveAs(initial_folder="./", file_types=(("Excel files", "*.xlsx"),), default_extension="*.xlsx")],
            [sg.Button("Confirm"), sg.Button("Cancel")]
        ]
        window = sg.Window("Export Processed File", layout=layout, finalize=True, relative_location=[-100, -100])
        return window        

    def file_input_window():
        layout = [
            [sg.Text("Choose the Epic output file", text_color="yellow")],
            [sg.InputText(key="-FILE_PATH_ADD-"),
            sg.FileBrowse(initial_folder="./", file_types=(["Excel files", "*.xlsx"],))],
            [sg.Text("Enter file password below",  text_color="yellow")],
            [sg.InputText(key="-PWD_ADD-", password_char="*")],
            [sg.Button("Import Additional"), sg.Button("Cancel")]
        ]
        window = sg.Window("Additional Epic Outputs", layout=layout, finalize=True, relative_location=[-100, -100])
        return window

    window1, window2 = main_window(), None

    while True:
        window, event, values = sg.read_all_windows()
        if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            elif window == window1:     # if closing win 1, exit program
                break
        if event == "Import":
            df = import_df(values["-FILE_PATH-"], values["-PWD-"])
        if event == "Click to import Additional Exports" and not window2:
            window2 = file_input_window()
        if event == "Import Additional":
            df_new = import_df(values["-FILE_PATH_ADD-"], values["-PWD_ADD-"])
            df = pd.concat([df, df_new])
            sg.popup("Import Successful")
            window.close()
        if event == "Process":
            window2 = file_save_window()
        if event == "Confirm":
            write_path = values["-SAVE_PATH-"]
            process_combined(df, write_path)
            sg.popup("File save sucessful, saved under " + write_path)
            window.close()
        if event == "Launch Analytics Dashboard":
            sys.argv = ['streamlit', 'run', 'sub.py']
            sys.exit(stcli.main())
    
    window.close()

if __name__ == '__main__':
    main()