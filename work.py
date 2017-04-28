#coding=utf8
import sys, os
import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

start_time = ''
end_time   = ''

def __get_serial_time(filename):
    serial_time_map = {}
    file_object = open(filename, 'r')
    try:
        for line in file_object:
            line=line.decode('utf-8')
            serial_time_map[line.split(',')[0].split(':')[1]] = line.split(',')[1]
    finally:
        file_object.close()
    print len(serial_time_map)
    return serial_time_map


def __get_elpase_time_map(serial_list,recv_from_migu_map,send_to_crm_map,recv_from_crm_map,send_to_migu_map):
    elapse_time_map = {}
    for elm in serial_list:
        t1 = datetime.datetime.strptime(recv_from_migu_map[elm],'%Y-%m-%d %H:%M:%S.%f')
        t2 = datetime.datetime.strptime(send_to_crm_map[elm],'%Y-%m-%d %H:%M:%S.%f')
        t3 = datetime.datetime.strptime(recv_from_crm_map[elm],'%Y-%m-%d %H:%M:%S.%f')
        t4 = datetime.datetime.strptime(send_to_migu_map[elm],'%Y-%m-%d %H:%M:%S.%f')
        elapse_time = (t4-t1)-(t3-t2)
        t = elapse_time.seconds*1000 + elapse_time.microseconds/1000
        if(t < 0):
            print"%s      %d" % (elm,t)
        #elif(t > 2000):
        #    print"%s      %d" % (elm,t)
        elapse_time_map[elm] = t
    return elapse_time_map

def __get_elaps_time(time1,time2):
    t1 = datetime.datetime.strptime(time1,'%Y-%m-%d %H:%M:%S.%f')
    t2 = datetime.datetime.strptime(time2,'%Y-%m-%d %H:%M:%S.%f')
    return (t2-t1).seconds*1000 + (t2-t1).microseconds/1000
    

def __calcuate_reslut(serial_elpase_time_map,sum_time):
    time_list = list(serial_elpase_time_map.values())
    print "结果: 最大耗时为 %lf ms" % max(time_list)
    print "结果: 最小耗时为 %lf ms" % min(time_list)
    print "结果：平均耗时   %lf ms" % (sum(time_list) / float(len(time_list)))
    print "结果：平均TPS为  %lf S" % (len(time_list) / float(sum_time/1000))


def __handle_by_file(recv_from_migu,send_to_crm,recv_from_crm,send_to_migu):
    recv_from_migu_map = __get_serial_time(recv_from_migu)
    send_to_crm_map    = __get_serial_time(send_to_crm)
    recv_from_crm_map  = __get_serial_time(recv_from_crm)
    send_to_migu_map   = __get_serial_time(send_to_migu)
    # 计算serial、时间差
    serial_list1 = set(recv_from_migu_map.keys()).intersection(set(send_to_migu_map.keys()))
    print "咪咕前置接收咪咕请求成功笔数：%d" % len(recv_from_migu_map)
    print "咪咕前置发送通知咪咕成功笔数：%d" % len(send_to_migu_map)
    print "咪咕前置实际成功笔数：%d" % len(serial_list1)

    serial_list2 = set(send_to_crm_map.keys()).intersection(set(recv_from_crm_map.keys()))
    print "省前置实际发送到省请求成功笔数：  %d" % len(send_to_crm_map)
    print "省前置实际成功接收到省返回笔数：  %d" % len(recv_from_crm_map)
    print "省前置实际成功笔数：  %d" % len(serial_list2)

    serial_list = serial_list1.intersection(serial_list2)
    print "实际成功总计笔数： %d" % len(serial_list)
    # 传入serial、4个time map返回时间差map
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    serial_elpase_time_map = __get_elpase_time_map(serial_list,recv_from_migu_map,send_to_crm_map,recv_from_crm_map,send_to_migu_map)
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    sum_time = __get_elaps_time(start_time,end_time)

    __calcuate_reslut(serial_elpase_time_map,sum_time)
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))




if __name__ == '__main__':
    start_time,end_time=sys.argv[1:3]
    #print start_time,end_time
    __handle_by_file('recv_from_migu','send_to_crm','recv_from_crm','send_to_migu')
    
