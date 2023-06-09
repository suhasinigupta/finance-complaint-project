import sys

class financeException(Exception):

    def __init__(self,error_message:Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message=financeException.get_detailed_error_message(error_message=error_message, error_detail=error_detail)


    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)-> str:
        _, _, exc_inf= error_detail.exc_info()
        line_no= exc_inf.tb_frame.f_lineno
        file_name= exc_inf.tb_frame.f_code.co_filename

        error_message=f"Error occured in script: [{file_name}] at line no: [{line_no}] error message: [{error_message}] "

        return error_message

    def __str__(self):
            
        return self.error_message

    def __repr__(self):
            
        return financeException.__name__.str()