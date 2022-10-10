#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include "zeros.hpp"
using namespace std;

int main(int argc, char* argv[]) {
	char* num = strdup(argv[1]);
	unsigned long long int l = strlen(num);
	unsigned long long int ctr = 0;
	vector<int> results;
	while ((ctr + 2) % l != 0) {
		int left_digit = num[ctr] - '0';
		int right_digit = num[ctr+2] - '0';
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
			vector<int> common;
			std::set_intersection(left.begin(), left.end(), right.begin(), right.end(), common.begin());
			if (common.size() == 0 || common.size() > 1) {
				left.clear(); right.clear();
				common.clear();
				continue;
			} else if (common.size() == 1) {
				results.push_back(common[0]);
                                common.clear();
				continue;
			}
		}	
		ctr += 2;
	}
	return 0;
}
