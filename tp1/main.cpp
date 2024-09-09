//TP 2023/2024: Zadaća 1, Zadatak 1
#include <iostream>
#include <cmath>
#include <array>
#include <vector>
#include <string>
#include <stdexcept>
bool imalNegativnih = false;
enum class TretmanNegativnih {IgnorirajZnak, Odbaci, TretirajKao0, PrijaviGresku};
int MozeJedanKvadrat(int n){
    return n == int(sqrt(n)) * int(sqrt(n));
}
int mozeDvaKvadrata(int n){
    for(int i = 0; i*i < n; i++){
        if(MozeJedanKvadrat(n - i*i)) return true;
    }
    return false;
}
// Nije koristena funkcija:
int MozeDvaKvadrata(int n){
    int parnost4mod3 = 0;
    int d = 2;
    while(n > 1){
        while(n % d != 0){
            if(parnost4mod3 % 2 == 1){
                return 0;
            }
            d++;
            parnost4mod3 = 0;
        }
        if(d % 4 == 3){
            parnost4mod3++;
        }
        n /= d;
    }
    if(parnost4mod3 % 2 == 1) return 0;
    return 1;
}
int mozeTriKvadrata(int n){
    for(int i = 0; i*i < n; i++){
        int m = n - i*i;
        for(int j = 0; j*j < m; j++){
            if(MozeJedanKvadrat(m-j*j)) return true;
        }
    }
    return false;
}
// Nije koristena funkcija:
int MozeTriKvadrata(int n){
    if(n % 4 != 0 && n % 8 != 7) return 1;
    while(n % 4 == 0){
        n /= 4;
    }
    if(n % 2 == 0) return 1;
    if(n % 8 == 7) return 0;
    return 1;
}
int BrojKvadrata(int n){
    if(n == 0) return 0;
    if(n < 0) throw std::domain_error("Broj mora biti nenegativan");
    if(MozeJedanKvadrat(n)) return 1;
    if(mozeDvaKvadrata(n)) return 2;
    if(mozeTriKvadrata(n)) return 3;
    return 4;
}
std::array<std::vector<int>, 5> RazvrstajPoBrojuKvadrata(std::vector<int> v, TretmanNegativnih tretman){
    std::array<std::vector<int>, 5> arr;
    for(int i = 0; i < v.size(); i++){
        int broj = v.at(i);
        int original = broj;
        bool jestNegativan = broj < 0;
        if(broj < 0){
            switch(tretman){
            case TretmanNegativnih::IgnorirajZnak:
            broj *= -1;
            break;
            case TretmanNegativnih::Odbaci:
            continue;
            break;
            case TretmanNegativnih::TretirajKao0:
            broj = 0;
            break;
            default:
            throw std::domain_error("Nije predvidjeno razvrstavanje negativnih brojeva");
            }
        }
        int k = BrojKvadrata(broj);
        if(jestNegativan && tretman == TretmanNegativnih::IgnorirajZnak){
            broj *= (-1);
        }
        if(original < 0 && tretman == TretmanNegativnih::TretirajKao0){
            broj = original;
        }
        arr.at(k).push_back(broj);
    }
    return arr;
}
bool JelCifra(char c){
    return c >= '0' && c <= '9';
}
bool JelBroj(const std::string& str){
    for(int i = 0; i < str.length(); i++){
        if(str.at(0) == '-') {
            std::cout << "Nije podrzano razvrstavanje negativnih brojeva!" << std::endl;
            imalNegativnih = true;
        }
        if(!JelCifra(str.at(i))) return false;
    }
    return true;
}
int main ()
{
    try{
    std::vector<int> v = {100,-200,1394,-7620,111};
    auto rez=RazvrstajPoBrojuKvadrata(v,TretmanNegativnih::TretirajKao0);
    std::cout<<"Rezultati razvrstavanja po broju kvadrata: \n";
    for(int i=0;i<5;i++){
        if(rez.at(i).size()==0)continue;
        std::cout<<i<<": ";
        for(int i:rez.at(i))std::cout<<i<<" ";
        std::cout<<std::endl;

    }}
    catch(std::domain_error e){
        std::cout<<e.what();
    }
}
