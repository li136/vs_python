class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> ant;
        int n= s.size();
        int ans=0;
        int a=0;
        int b=0;
        while( b<n ){
            if(ant[s[b]]!=0){
                int x=1;
                while(x){
                    if (s[a] == s[b])
					    x = 0;
				    ant[s[a]] = 0;
				    a++;
                }
            }else{
                ant[s[b]]=1;
                b++;
                ans=max(ans,b-a);
            }
        }
        return ans;
    }
};