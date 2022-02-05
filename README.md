### **Requirements**
- Python 3 (tested on versions 3.9 and 3.10 on mac/windows)
- Required packages:
1. [pandas](https://pandas.pydata.org/docs/getting_started/install.html) (command: `pip install pandas`)
2. [msoffcypto](https://github.com/nolze/msoffcrypto-tool) (command: `pip install msoffcrypto-tool`)
3. [streamlit](https://streamlit.io) (command: `pip install streamlit`)
4. [numpy](https://numpy.org/install/) (command: `pip install numpy`)


to run the script, either 
1. enter `python3 find_it.py` in terminal (mac) or cmd (windows)
2. use right click on the find_it.py file and launch with **python launcher** 


### This script has two function options
* First function: Process Epic exported file
  * <img width="455" alt="image" src="https://user-images.githubusercontent.com/28236780/152625057-0fc18684-3319-4672-9155-2cf6a32a004b.png">
  * enter "Y" to enter the first function.
  * first prompt will ask for number of files to be processed/combined.
  * (this is due to limitations of Epic Find Susceptibility Report limiting to 6 months.)
  * then enter path to the first file, password, then repeat for all reports.
  * script will perform data transformation and export out two dataframes and export out as excel files:
    * gram positives (first specimen removed, contains only Staphylococcus aureus, Enterococcus (excluding gallinarum and casseliflavus))
    * all results (unfiltered)   
  * Finally, enter path to procssed file with two excel pages (Complete and Frist Specimen (Gram Positive)).
    * please remember to add the excel extension at the end (xlsx.
    * to export within the same directory, simply enter the file name (sample.xlsx).
* Second function: Web visualization tool for organism counts
  * <img width="759" alt="image" src="https://user-images.githubusercontent.com/28236780/152625345-74a3d27e-fbe3-48f8-a712-f6ee45371678.png">
  * enter "Y" to launch the streamlit app
  * first use **browse files** to selec the processed file
  * then select either "complete data" or "first specimen only" 
  * <img width="759" alt="image" src="https://user-images.githubusercontent.com/28236780/152625728-54d6bf0d-b262-4078-80df-2a358e8c3483.png">
  * choose desired organisms, followed by antibiotic, interpretation, and specimen type.
    * to note: antibiotic, interpretation and specimen type will be filter subsequent selections. 
  * <img width="744" alt="image" src="https://user-images.githubusercontent.com/28236780/152625863-57436241-4310-4ad5-8c30-e3235e72f076.png">
  * then the data table will appear, followed by a count of unique specimen IDs 
