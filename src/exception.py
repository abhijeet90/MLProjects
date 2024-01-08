import sys
# any exception that is controlled, the sys library will automatically have that information 
import logging

# whenever the exception gets raised we want to push this like our custom own exception
def error_message_detail(error,error_detail:sys):
    # error_detail will present inside the sys
    
    _,_,exc_tb = error_detail.exc_info()
    '''exc_info() is the execution info and this will give you three information
    first two information we are not intereseting, we are interested in last information
    exc_tb will give info like on which file the exception has occured, on which line number the 
    exception has occured  '''
    
    file_name=exc_tb.tb_frame.f_code.co_filename
    # By this we will be able to get the filename
    
    
    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    # exc_tb.tb_lineno --> this is for line number
    
    return error_message
    
# whenever error raises we will call the function error_message_details()

# Create our own customeException class which is inheriting from exception

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        # error_detail is tracked by sys
    
    def __str__(self):
        return self.error_message
        # whenever we try to print it, we will be getting error message over here
        
            
        