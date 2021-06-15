import time

def main():
    duration_day = 24 * 60 * 60

   
    epoch_offset = time.localtime(0)
    now = time.localtime()
    yesterday = time.localtime(time.time()- duration_day)
    tomorrow = time.localtime(time.time()+ duration_day)

    #print(yesterday)
    #TODO1 print the 4 times like below:
    #15-06-2021
    #print("yesterday:",

    now_month = now.tm_mon
    now_year = now.tm_year
    now_day = now.tm_mday
    print(now_day, now_month, now_year, sep="-")
    print(yesterday.tm_wday, yesterday.tm_mday, yesterday.tm_mon, yesterday.tm_year, sep="/")

    
    
    
main()
