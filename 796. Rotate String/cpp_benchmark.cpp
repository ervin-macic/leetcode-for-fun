#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <random>
using namespace std;

struct TestCase {
    string s;
    string goal;
    string name;
};

bool rotateFind(const string& s, const string& goal) {
    if (s.size() != goal.size()) return false;
    return (s + s).find(goal) != string::npos;
}

bool rotateManual(const string& s, const string& goal) {
    if (s.size() != goal.size()) return false;

    string d = s + s;
    int n = d.size(), m = goal.size();

    for (int i = 0; i <= n - m; i++) {
        bool ok = true;

        for (int j = 0; j < m; j++) {
            if (d[i + j] != goal[j]) {
                ok = false;
                break;
            }
        }

        if (ok) return true;
    }

    return false;
}

string rotateByK(const string& s, int k) {
    k %= s.size();
    return s.substr(k) + s.substr(0, k);
}

string randomString(int n) {
    static mt19937 rng(12345);
    uniform_int_distribution<int> dist(0, 25);

    string out;
    out.reserve(n);

    for (int i = 0; i < n; i++)
        out += char('a' + dist(rng));

    return out;
}

double benchFind(const string& s, const string& goal, int reps) {
    volatile bool ans;
    auto start = chrono::high_resolution_clock::now();

    for (int i = 0; i < reps; i++)
        ans = rotateFind(s, goal);

    auto end = chrono::high_resolution_clock::now();
    return chrono::duration<double>(end - start).count();
}

double benchManual(const string& s, const string& goal, int reps) {
    volatile bool ans;
    auto start = chrono::high_resolution_clock::now();

    for (int i = 0; i < reps; i++)
        ans = rotateManual(s, goal);

    auto end = chrono::high_resolution_clock::now();
    return chrono::duration<double>(end - start).count();
}

int main() {
    vector<TestCase> tests;

    tests.push_back({"abcde", "cdeab", "small_true"});
    tests.push_back({"abcde", "abced", "small_false"});

    string s = string("abcdefg");
    for (int i = 0; i < 1000; i++) s += "abcdefg";
    tests.push_back({s, rotateByK(s, 300), "medium_true"});
    tests.push_back({s, string(s.rbegin(), s.rend()), "medium_false"});

    s = string(5000, 'a') + "b";
    tests.push_back({s, rotateByK(s, 2000), "repeat_true"});
    tests.push_back({s, string(s.size(), 'a'), "repeat_false"});

    s = randomString(10000);
    tests.push_back({s, rotateByK(s, 4321), "random_true"});
    tests.push_back({s, randomString(10000), "random_false"});

    s = "";
    for (int i = 0; i < 20000; i++) s += "xyz12345";
    tests.push_back({s, rotateByK(s, 7777), "large_true"});

    string bad = s;
    bad.back() = 'Q';
    tests.push_back({s, bad, "large_false"});

    for (auto& tc : tests) {
        bool a = rotateFind(tc.s, tc.goal);
        bool b = rotateManual(tc.s, tc.goal);

        if (a != b) {
            cout << "Mismatch on " << tc.name << endl;
            continue;
        }

        double t1 = benchFind(tc.s, tc.goal, 200);
        double t2 = benchManual(tc.s, tc.goal, 200);

        cout << tc.name
             << " | find=" << t1
             << "s | manual=" << t2
             << "s | x" << (t2 / t1)
             << endl;
    }
}