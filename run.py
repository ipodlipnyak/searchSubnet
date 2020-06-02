import numpy as np

'''
build subs matrix from ip list then check wich subs from first ip are common amongst others
'''
def searchSubnet(ip_list):
    ip_matrix = np.array([[int(sub) for sub in ip.split('.')] for ip in ip_list])
    
    count_subs = [ip_matrix[:, index].tolist().count(sub) for index, sub in enumerate(ip_matrix[0])]
    common_subs = [str(ip_matrix[0][index]) for index, count in enumerate(count_subs) if count == len(ip_matrix)]
    
    return '.'.join(common_subs)

if __name__ == "__main__" :
    ip_list = ['192.168.1.12','192.168.2.34']
    result = searchSubnet(ip_list)
    print(result)
