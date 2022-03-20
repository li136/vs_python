class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> ant;
        int n= s.size();
        int ans=0;
        int a=0;
        int t=0;
        for(int i=0;i<n;i++){
            if(ant.find(s[i]) == ant.end()){
                ant[s[i]]=1;
                a++;
                ans=max(ans,a);
            }
            else{
                a=0;
                ant.clear();
                i=t++;
            }
        }
        return ans;
    }
};