from discordc2.logger.log_type import Log_Type

class Logger:

    def log(msg, lt: Log_Type):
        print(lt.value + msg)
        pass