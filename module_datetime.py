import datetime
st = datetime.datetime(2012,11,2,3,1,34,1234)
nwo = datetime.datetime.now()
sen = nwo-st
print(sen)#چاپ فاصله زمانی به صورت روز، ساعت، دقیقه و ثانیه
print(st.ctime())#سال و روز و ماه و زمان دقیق وارد شده
print(st.date())#تاریخ دقیق تاریخ وارد شده
print(st.hour)#ساعت تاریخ و زمان وارد شده
print(st.day)#روز تاریخ وارد شده
print(st.month)#ماه تاریخ وارد شده
print(st.minute)#دقیقه ی تاریخ وارد شده
print(st.second)#سانی ی تاریخ وارد شده
print(st.microsecond)#میکرو سانیه ی تاریخ وارد شده
print(st.year)#سال تاریخ وارد شده
print(sen.days)#تعداد کل روزهایی که بین زمان فعلی و زمان مشخص شده فاصله هست
print(sen.microseconds)# تعداد میکروثانیه‌های باقیمانده بعد از آخرین ثانیه
print(sen.seconds)#تعداد ثانیه‌های باقی‌مانده در روز آخر فاصله زمانی 