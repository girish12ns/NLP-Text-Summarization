import os



class Data_Validation:
    def __init__(self,config):
        self.config=config

    def check_data_validation_files(self)->bool:
        validation=None

        all_files=os.listdir(os.path.join('artifacts','data_ingestion','Summarizer_data','Summerizing_data','samsum_dataset'))
        
        for file in all_files:
            if file not in self.config.ALL_REQUIRES_FILES:
                validation=False
                with open(self.config.STATUS_FILE,"w") as f:
                    f.write("validation_status:{}".format(validation))
            else:
                validation=True
                with open(self.config.STATUS_FILE,"w") as f:
                    f.write("validation_status:{}".format(validation))
        return validation