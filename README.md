### **Requirements**
- Python 3 (tested on versions 3.9 and 3.10 on mac/windows)
- Required packages:
1. [pandas](https://pandas.pydata.org/docs/getting_started/install.html) (install command: `pip install pandas`)
2. [msoffcypto](https://github.com/nolze/msoffcrypto-tool) (install command: `pip install msoffcrypto-tool`)
3. [streamlit](https://streamlit.io) (install command: `pip install streamlit`)
4. [numpy](https://numpy.org/install/) (install command: `pip install numpy`)
5. [tkinter](https://docs.python.org/3/library/tkinter.html) (install command: `pip install tk`)
---

to run the script, either 
1. enter `python3 find_it.py` in terminal (mac) or cmd (windows)
2. use right click on the find_it.py file and launch with **python launcher** 
---

### This script has two function options
> <img width="484" alt="image" src="https://user-images.githubusercontent.com/28236780/155803919-32f26232-615a-4770-a9d5-020675543a80.png">
* First function: Process Epic exported file
  * enter "Y" to enter the first function.
  * first prompt will ask for number of files to be processed/combined.
    * (this is due to limitations of Epic Find Susceptibility Report limiting to 6 months.)
  * then select the exported excel file from Epic in the dialog window.
    * <img width="456" alt="image" src="https://user-images.githubusercontent.com/28236780/155803043-923c6e4c-d892-4431-b089-933dd3b62a93.png">
    * enter the password to the file in terminal/cmd.
    * this process will repeat until all files are imported.
  * script will perform data transformation:
    * gram positives (first specimen removed, contains only Staphylococcus aureus, Enterococcus (excluding gallinarum and casseliflavus))
    * all results (unfiltered)   
  * Finally, enter the file name to save under the same folder: 
    * <img width="459" alt="image" src="https://user-images.githubusercontent.com/28236780/155802354-3a5b29c7-b9d6-4ff7-9d8b-08afef6fc25a.png">
    * to save under different folder, select the down arrow to expand the file dialog    
---
> <img width="491" alt="image" src="https://user-images.githubusercontent.com/28236780/152627151-da286fb3-9c4b-4214-9311-ec53316280bc.png">
* Second function: Web visualization tool for organism counts
  * enter "Y" to launch the streamlit app
  * <img width="759" alt="image" src="https://user-images.githubusercontent.com/28236780/152625345-74a3d27e-fbe3-48f8-a712-f6ee45371678.png">
  * first use **browse files** to selec the processed file
  * then select either "complete data" or "first specimen only" 
  * <img width="759" alt="image" src="https://user-images.githubusercontent.com/28236780/152625728-54d6bf0d-b262-4078-80df-2a358e8c3483.png">
  * choose desired organisms, followed by antibiotic, interpretation, and specimen type.
    * to note: antibiotic, interpretation and specimen type will be filter subsequent selections. 
  * <img width="744" alt="image" src="https://user-images.githubusercontent.com/28236780/152625863-57436241-4310-4ad5-8c30-e3235e72f076.png">
  * then the data table will appear, followed by a count of unique specimen IDs 
