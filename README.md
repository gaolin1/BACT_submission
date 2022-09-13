### **Requirements**
- Python 3 (tested on versions 3.9 and 3.10 on mac/windows)
- Required packages:
1. [pandas](https://pandas.pydata.org/docs/getting_started/install.html) (install command: `pip install pandas`)
2. [msoffcypto](https://github.com/nolze/msoffcrypto-tool) (install command: `pip install msoffcrypto-tool`)
3. [streamlit](https://streamlit.io) (install command: `pip install streamlit`)
4. [numpy](https://numpy.org/install/) (install command: `pip install numpy`)
5. [tkinter](https://docs.python.org/3/library/tkinter.html) (install command: `pip install tk`)
6. [PySimpleGUI](https://www.pysimplegui.org/en/latest/) (install command: `pip install pysimplegui`)
---

to run the script, right click on the `simple_gui.py` file and launch with **python launcher** 
---

### This script has two function options
> <img width="744" alt="image" src="https://user-images.githubusercontent.com/28236780/189788476-23872f64-afb2-430f-b50c-7194cd4a33e0.png">
* First function: Process Epic exported file
  * select `Browse` to select the Epic output Excel file
  * enter the password below on the next field
  * click on `Import` to import the data
  * *optional* to import additional file, select `Click import additional exports`
    * <img width="717" alt="image" src="https://user-images.githubusercontent.com/28236780/189789058-1fc3adcf-ed9f-452f-ae03-480669ec06b3.png">
    * follow similar procedure as the first file, browse to select, enter password and then select `Import Additional`
> <img width="734" alt="image" src="https://user-images.githubusercontent.com/28236780/189789326-150961d9-e4d6-41f6-9869-3aa6b8077b8a.png">
  * Once ready, select `Process` to prep the data
    * use Browse to enter the desired export file name, then select `Confirm`
  * script will perform data transformation:
    * `gram positives` (first specimen removed, contains only Staphylococcus aureus, Enterococcus (excluding gallinarum and casseliflavus))
    * `all` results (unfiltered)   

---
> <img width="744" alt="image" src="https://user-images.githubusercontent.com/28236780/189788476-23872f64-afb2-430f-b50c-7194cd4a33e0.png">
* Second function: Web visualization tool for organism counts
  * click `Launch Analytics Dashboard`
  * <img width="759" alt="image" src="https://user-images.githubusercontent.com/28236780/152625345-74a3d27e-fbe3-48f8-a712-f6ee45371678.png">
  * first use `browse files` to selec the processed file
  * then select either `complete data` or `first specimen only`
  * <img width="759" alt="image" src="https://user-images.githubusercontent.com/28236780/152625728-54d6bf0d-b262-4078-80df-2a358e8c3483.png">
  * choose desired `organisms`, followed by `antibiotic`, `interpretation`, and `specimen type`.
    * to note: antibiotic, interpretation and specimen type will be filter subsequent selections. 
  * <img width="744" alt="image" src="https://user-images.githubusercontent.com/28236780/152625863-57436241-4310-4ad5-8c30-e3235e72f076.png">
  * then the data table will appear, followed by a `count` of unique specimen IDs 
  * to stop the web program, use "control + c" in terminal to stop the program
