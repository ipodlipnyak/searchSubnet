import numpy as np
import unittest

class TestSubnetSearch(unittest.TestCase):
    def test_first_sub_is_common(self):
        self.assertEqual(searchSubnet(['192.167.1.12','192.168.2.34']), '192')
        
    def test_second_sub_is_common(self):
        self.assertEqual(searchSubnet(['192.168.1.12','192.168.2.34']), '192.168')
        
    def test_third_sub_is_common(self):
        self.assertEqual(searchSubnet(['192.168.1.12','192.168.1.34']), '192.168.1')
        
    def test_no_sub_is_common(self):
        self.assertEqual(searchSubnet(['193.168.1.12','192.168.1.34']), '')


def searchSubnet(ip_list):
    '''
    Build subs matrix from ip list 
    then check which subs from first ip are common amongst others
    '''
    ip_matrix = np.array([[int(sub) for sub in ip.split('.')] for ip in ip_list])
    ip_sample = ip_matrix[0]
    
    count_subs = [ip_matrix[:, index].tolist().count(sub) for index, sub in enumerate(ip_sample)]
    common_subs = list(genCommonSubs(count_subs, len(ip_matrix), ip_sample))
    
    return '.'.join(common_subs)    

def genCommonSubs(count_subs, ips_count, ip_sample):
    for index, count in enumerate(count_subs):
        if ips_count != count: return
        yield str(ip_sample[index])

if __name__ == "__main__" :
    unittest.main()