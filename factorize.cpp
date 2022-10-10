#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include "zeros.hpp"
using namespace std;

int main(int argc, char* argv[]) {
	FILE* testcase = fopen("testcases/latest.txt","r");
	char* num = new char[301];
	fscanf(testcase, "%300s\n", num);
	num[300] = '\0';
	unsigned long long int l = strlen(num);
	unsigned long long int ctr = 0;
	vector<int> results;
	FILE* fp = fopen64("./pi.txt","r");
	while (1) {
		char pp = 0;
		fscanf(fp, "%c", &pp);
		int left_digit = num[ctr % l] - '0';
		int right_digit = num[(ctr + 2) % l] - '0';
		std::vector< std::vector<int> > left_ending = left_endings[ctr % 7][left_digit];
		std::vector< std::vector<int> > right_ending = right_endings[ctr % 7][right_digit];
		if (left_ending[0][0] > 0 && right_ending[0][0] > 0) {
			vector<int> left;
			for (int i = 0; i < left_ending[0][0]; ++i) {
				left.push_back(left_ending[1][i]);
			}
			vector<int> right;
			for (int i = 0; i < right_ending[0][0]; ++i) {
				right.push_back(right_ending[1][i]);
			}
			unsigned int sz1 = left.size();
			unsigned int sz2 = right.size();
			int sz = -1;
			if (sz1 > sz2) {
				sz = sz1;
			} else {
				sz = sz2;
			}
			std::vector<int> common(sz);
			std::vector<int>::iterator it;
			it=std::set_intersection (left.begin(), left.end(), right.begin(), right.end(), common.begin());
			common.resize(it-common.begin());
			if (common.size() == 0 || common.size() > 1) {
				left.clear(); right.clear();
				common.clear();
				ctr++;
				continue;
			} else if (common.size() == 1) {
				results.push_back(common[0]);
				if (common[0] == (pp - '0')) {
					cout << " ctr = " << ((((ctr > 0) && ((ctr + 1)  % l)==0))? l:((ctr + 1) % l)) << endl;
					cout << "pi = \t" << pp - '0' << endl;
					cout << common[0] << endl;
					cout << "Pi Matches\n";
					system("a=1;read a");
				}
				common.clear();
				ctr++;
				continue;
			}
		}	
		++ctr;
	}
	for (int i = 0; i < results.size(); ++i) {
		cout << results[i] << " , ";
	}
	cout << endl;
	fclose(fp);
	return 0;
}
