import pandas as pd
import streamlit as st
import viz
import understand
import mlalgo
class start:
    def fileupload(self):
        self.file=st.file_uploader('Upload file',type=['CSV','XLSX'])
        if self.file is not None:
            try:
                self.data=pd.read_csv(self.file)
                return self.data
            except:
                try:
                    self.data=pd.read_excel(self.file)
                    return self.data
                except:
                    st.warning('Supported CSV, EXCEL files only')
    def opt(self):
        self.option=st.sidebar.selectbox('What to do',['','Visualize','Analyze','Machine Learning'])
        return self.option
if __name__=='__main__':
    st.title('Data World - helps you to deal with Data')
    obj=start()
    data=obj.fileupload()
    to_do=obj.opt()
    if data is not None:
        if to_do=='Analyze':
            understand.analyse_class.analyse_fun(data)
        if to_do=='Visualize':
            viz.viz_class.visualization(data)
        if to_do=='Machine Learning':
            mlalgo.ml_class.algo(data)
