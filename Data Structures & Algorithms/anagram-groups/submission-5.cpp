class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        map<vector<int>, vector<string>> all;

        for (string s : strs){
            vector<int> count(26, 0);
            for (int i=0; i<s.length(); i++){
                count[s[i] - 'a']++;
            }
            all[count].push_back(s);
        }
        vector<vector<string>> res;
        for (auto& elt : all){           
            res.push_back(elt.second);
        }

        return res;
    }
};
