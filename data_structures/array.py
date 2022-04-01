import ctypes

class Array:

    def __init__(self):
        self.n = 0      #eleman sayısı
        self.capacity=1 #kapasite
        self.A=self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        if not 0<=k<=self.n:
            return IndexError("k is out of the bounds!")
        return self.A[k]

    def append(self,element):
        
        if self.n==self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n]=element
        self.n+=1

    def _resize(self,new_cap):

        B=self.make_array(new_cap)
        for i in range(self.n):
            B[i]=self.A[i]

        self.A=B
        self.capacity=new_cap

        return self.A

    def __str__(self):
        return " ".join([str(i) for i in self.A])

    def make_array(self,new_cap):
        return (new_cap*ctypes.py_object)()

arr = Array()
arr.append("element")
arr.append("1")
arr.append("element2")
arr.append("2")

print(arr)
print(len(arr))