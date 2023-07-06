# import pandas as pd
# class test:
#     def main():
#         a="test1"
#         print(a)
# class B(test):
#     pass
# class C(B):
#     pass
# class D(C):
#     print("test35")
# obj=D
# test.main()  

import pandas as pd
import numpy as np
class Test:
    def main():
        abc={
            "Name":["Subhojit","Indrasish","Ram"],
            "Age":["18","18","19"],
            "Gender":["MALE","MALE","MALE"],
            "Address":["Saratpally","Saradapally","GT road"]
        }
        xyz=pd.DataFrame(abc)
        print(xyz)
Test.main()        
    