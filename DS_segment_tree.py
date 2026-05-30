from typing import List


# Segment Tree: Point Update and Range Query
class SegmentTree:
    # 3 operations: build, query and point_update
    # Space: max 4n for the tree array, Time: O(n) to build the tree, O(logn) for query and update
    # everything starts from root node which has range 0,n-1 and idx 1, then we break into 2 for left and right child and so on until we reach leaf node which has range of single element

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(1, 0, self.n-1, arr) # always start from root node which has range 0,n-1

    # T: O(n) to build the tree, S: O(n) for the tree array
    def _build(self, idx, node_start, node_end, arr):
        if node_start == node_end: # set the leaf node of Segment Tree using value at index of array
            self.tree[idx] = arr[node_start]
            return
        else: # there is still range, need to break into 2 again
            mid = (node_start + node_end) // 2
            self._build(2*idx, node_start, mid, arr)
            self._build(2*idx+1, mid+1, node_end, arr)
            # both children set now use them to update the value for parent
            self.tree[idx] = self.tree[2*idx] + self.tree[2*idx+1]

    # T: O(logn) to query, S: O(1) for the query function
    def _query(self, idx, node_start, node_end, qs, qe):
        if qe < node_start or node_end < qs: # no overlap
            return 0
        if qs <= node_start and node_end <= qe: # node completely inside query, return full data
            return self.tree[idx]
        # Partial case: need to retrieve from both the children
        mid = (node_start + node_end) // 2
        left = self._query(2*idx, node_start, mid, qs, qe)
        right = self._query(2*idx+1, mid+1, node_end, qs, qe)
        return left + right

    def query(self, qs, qe):
        return self._query(1, 0, self.n-1, qs, qe) # always start from root node which has range 0,n-1 and idx 1

    # T: O(logn) to update, S: O(1) for the update function
    def _point_update(self, idx, pos, value, node_start, node_end):
        if pos < node_start or node_end < pos: # no overlap
            return
        if node_start == pos == node_end: # complete overlap
            self.tree[idx] = value
            return
        # need to find in left and right where to insert
        mid = (node_start + node_end) // 2
        self._point_update(2*idx, pos, value, node_start, mid)
        self._point_update(2*idx+1, pos, value, mid+1, node_end)
        # Need to correct the parent value as left or right would have been updated
        self.tree[idx] = self.tree[2*idx] + self.tree[2*idx+1]

    def point_update(self, pos, value):
        self._point_update(1, pos, value, 0, self.n-1) # always start from root node which has range 0,n-1 and idx 1


class LazySegmentTree:
    def __init__(self):
        self.tree=[]
        self.n=0

    def build_tree(self,arr):
        self.n=len(arr)
        self.tree=[0]*(4*self.n+1)
        self.lazy_tree=[0]*(4*self.n+1)
        self._build_tree(arr,1,0,self.n-1)

    def _build_tree(self,arr,index,s,e):
        if s==e:
            self.tree[index]=arr[s]
        else:
            mid=(s+e)//2
            self._build_tree(arr,2*index,s,mid)
            self._build_tree(arr,2*index+1,mid+1,e)
            self.tree[index]=self.tree[2*index]+self.tree[2*index+1]

    def _set_and_push_lazy_values(self,index,s,e):
        # first check if any update remaining on this node
        if self.lazy_tree[index]:
            self.tree[index]+=self.lazy_tree[index]*(e-s+1)
            # push to children
            if s!=e:
                self.lazy_tree[2*index]+=self.lazy_tree[index]
                self.lazy_tree[2*index+1]+=self.lazy_tree[index]
            self.lazy_tree[index]=0
            
    def query(self,qs,qe):
        return self._query(1,0,self.n-1,qs,qe)
    
    def _query(self,index,s,e,qs,qe):
        self._set_and_push_lazy_values(index,s,e)
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

    def range_update(self,rs,re,value):
        self._range_update(1,0,self.n-1,rs,re,value)
    
    def _range_update(self,index,s,e,rs,re,value):
        
        self._set_and_push_lazy_values(index,s,e)
        
        # no overlap
        if re<s or e<rs:
            return 
        
        # full overlap
        if rs<=s and e<=re:
            self.tree[index]+=value*(e-s+1)
            if s!=e:
                self.lazy_tree[2*index]+=value
                self.lazy_tree[2*index+1]+=value
            return
        
        # Partial
        mid=(s+e)//2
        self._range_update(2*index,s,mid,rs,re,value)
        self._range_update(2*index+1,mid+1,e,rs,re,value)
        self.tree[index]=self.tree[2*index]+self.tree[2*index+1]

    def point_update(self,update_index,value):
        self._point_update(1,0,self.n-1,update_index,value)
    
    def _point_update(self,index,s,e,update_index,value):
        if update_index<s or update_index>e:
            return 
        if update_index==s and s==e:
            self.tree[index]=value
            return
        mid=(s+ e)//2
        self._point_update(2*index,s,mid,update_index,value)
        self._point_update(2*index+1,mid+1,e,update_index,value)
        self.tree[index]=self.tree[2*index]+self.tree[2*index+1]

