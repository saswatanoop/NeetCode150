class SegmentTree:
    def __init__(self):
        self.tree=[]
        self.n=0

    def build_tree(self,arr):
        self.n=len(arr)
        self.tree=[0]*(4*self.n+1)
        self._build_tree(arr,1,0,self.n-1)

    def _build_tree(self,arr,index,s,e):
        if s==e:
            self.tree[index]=arr[s]
        else:
            mid=(s+e)//2
            self._build_tree(arr,2*index,s,mid)
            self._build_tree(arr,2*index+1,mid+1,e)
            self.tree[index]=self.tree[2*index]+self.tree[2*index+1]


    def query(self,qs,qe):
        return self._query(1,0,self.n-1,qs,qe)
    
    def _query(self,index,s,e,qs,qe):
        # no overlap
        if qe<s or e<qs:
            return 0
        # full overlap
        if qs<=s and e<=qe:
            return self.tree[index]
        # Partial
        mid=(s+ e)//2
        left=self._query(2*index,s,mid,qs,qe)
        right=self._query(2*index+1,mid+1,e,qs,qe)
        return left+right

    def update(self,update_index,value):
        self._update(1,0,self.n-1,update_index,value)
    
    def _update(self,index,s,e,update_index,value):
        if update_index<s or update_index>e:
            return 
        if update_index==s and s==e:
            self.tree[index]=value
            return
        mid=(s+ e)//2
        self._update(2*index,s,mid,update_index,value)
        self._update(2*index+1,mid+1,e,update_index,value)
        self.tree[index]=self.tree[2*index]+self.tree[2*index+1]

        
