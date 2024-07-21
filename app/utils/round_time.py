from datetime import datetime, timezone, timedelta

def round_time(dt=None, roundTo=60*60):
   '''
   Округление времени
   '''

   if dt == None : dt = datetime.now()
   seconds = (dt.replace(tzinfo=None) - dt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)