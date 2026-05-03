class Solution {
public:
    bool rotateString(std::string s, std::string goal) {
        // Check if the lengths are different
        if (s.length() != goal.length()) {
            return false;
        }

        // Create a new string by concatenating s with itself
        std::string doubledString = s + s;

        // Use find to search for goal in doubledString
        // If find does not return std::string::npos,
        // then goal is a substring
        return doubledString.find(goal) != std::string::npos;
    }
};