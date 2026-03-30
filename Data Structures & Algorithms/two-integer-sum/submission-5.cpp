class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int, int> count;

        for (int i=0; i<nums.size(); i++){
            if (count.count(target - nums[i])){
                return {count[target-nums[i]], i};
            }
            else{
                count[nums[i]] = i;
            }
        }
    }
};
