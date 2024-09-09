#include <iostream>

using namespace std;
void generate_all_permutations(int n) {
    for(int i = 1; i <= n; i++) {
        cout << i;
        generate_all_permutations();
    }
}
int main()
{
    cout << "PROGRAM TO GENERATE ALL PERMUTATIONS OF S = {1,2,3,...,n}" << endl;
    cout << "Input n: ";
    int n;
    cin >> n;
    vector<vector<int>> all_permutations = generate_all_permutations(n);
}
