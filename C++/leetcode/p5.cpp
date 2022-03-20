class Solution {
public:
    string longestPalindrome(string s) {
        int n=s.size();
        int ans=1;
        string anss;
        anss.append(1, s[0]);
        for(int i=0;i<n;i++){
            for(int j=i+ans;j<n;j++){
                int qwe=1;
                int m=(j-i)/2 + 1;
                for(int k=0;k<m;k++){
                    if(s[i+k]!=s[j-k]){
                        qwe=0;break;
                    }
                }
                if(qwe){
                    if((j-i+1)>ans){
                        ans=j-i+1;
                        anss=s.substr(i,j-i+1);
                    }
                }
            }
        }
        return anss;
    }
};