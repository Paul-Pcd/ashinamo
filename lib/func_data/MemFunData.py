#!/usr/bin/env python
#-*- coding:utf-8 -*-
""" pymonitor client module: ��ȡ�ڴ�����, �� /proc/meminfo �ļ� """
""" @Author: baoyiluo@gmail.com
    @Site: www.pythoner.cn
    @Date: 2013-04-10
    @Version: v0.2
    @Note:
        /proc/meminfo ���������ݵĽ��ͣ�
[root@hpcstack ~]# head -n 4 /proc/meminfo 
MemTotal:        1017812 kB
MemFree:           67768 kB
Buffers:           10280 kB
Cached:           283708 kB
MemTotal:���ڴ��С
MemFree:�����ڴ��С
Buffers��Cached�����̻���Ĵ�С
Buffers��Cached������
buffers��ָ���������豸���Ļ����С����ֻ��¼�ļ�ϵͳ��metadata�Լ� tracking in-flight pages.
cached���������ļ������塣

"""
def get_ProcMeminfo():
    """ ��ȡ�ڴ�����
    @Return: (status, msgs, results)
            status = INT, Fuction execution status, 0 is normal, other is failure.
            msgs = STRING, If status equal to 0, msgs is '', otherwise will be filled with error message.
            results = DICT {
                    'memtotal': 1017812, #��λ���� KB
                    'memused': 283708
            }
    """
    now_data = {}
    status = 0; msgs=""; results="";
    try:
        raw_data = file('/proc/meminfo').read()
        temps = raw_data.strip().split('\n')
        for temp in temps:
            tmp = temp.split()
            now_data[tmp[0]]=tmp[1]
        results={}
        results['memtotal']=int(now_data['MemTotal:'])
        #results['memused']=int(now_data['MemTotal:'])-int(now_data['MemFree:'])-int(now_data['Buffers:'])-int(now_data['Cached:'])
        results['memused']=int(now_data['MemTotal:'])-int(now_data['MemFree:'])
        results['buffers']=int(now_data['Buffers:'])
        results['cached']=int(now_data['Cached:'])
        return (status,msgs,results)
    except Exception,e:
        return (-1, 'data error!', '')

if __name__ == "__main__":
    print get_ProcMeminfo()
