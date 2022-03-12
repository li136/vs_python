#include<cstdio>
#include<algorithm>
#include<map>
using namespace std;

int main()
{
    int target,numsSize;
    int nums[1000];
    map<int, int >mp;
    scanf("%d",&target);
    scanf("%d",&numsSize);
    for(int i=0;i<numsSize;i++){
        scanf("%d",nums+i);
        mp[nums[i]]=i;
    }
    for(int i=0;i<numsSize;i++){
        if(mp.find(target - nums[i]) != mp.end()){
            printf("%d  %d",i,mp[target - nums[i]]);
            break;
        }
    }
    scanf("%d",&nums);

    return 0;
}