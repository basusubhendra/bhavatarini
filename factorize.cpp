#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include "zeros.hpp"
using namespace std;

bool update_hash_table(int ctr, int* hash_table) {
	if (hash_table[ctr] == 0) {
		hash_table[ctr] = 1;
	} else if (hash_table[ctr] == 1) {
		return false;
	}	       
	for (int i = 0; i < 8; ++i) {
		if (hash_table[i] == 0) return false;
	}
	return true;
}

bool is_satisfiable(int* triplet, float& score) {
	bool satisfiable = true;
	if (triplet[0] == 0 || triplet[1] == 0 || triplet[2] == 0) {
		satisfiable = false;
	}
	if (satisfiable) {
		if ((triplet[0] < triplet[1] && triplet[1] > triplet[2]) || (triplet[0] > triplet[1] && triplet[1] < triplet[2])) {
		} else {
			satisfiable = false;
		}
	}
	if (satisfiable) {
		if (triplet[0] == triplet[2]) {
			score = 0.5;
		} else {
			score = 1.0;
		}
	} else {
		if (triplet[0] == triplet[1] || triplet[1] == triplet[2] || triplet[0] == triplet[2]) {
			score = 0.5;
		} else {
			score = 1.0;
		}
	}
	return satisfiable;
}

int main(int argc, char* argv[]) {
	FILE* testcase = fopen("testcases/latest.txt","r");
	char* num = new char[301];
	fscanf(testcase, "%300s\n", num);
	num[300] = '\0';
	//	char* num = strdup(argv[1]);
	unsigned long long int l = strlen(num);
	unsigned long long int ctr = 0;
	vector<int*>* result = new vector<int*>();
	int* hash_table = (int*) calloc(8, sizeof(int));
	int* triplet = (int*) calloc(3, sizeof(int));
	int idx = 0;
	while (1) {
		int left_digit = num[ctr % l] - '0';
		int right_digit = num[(ctr + 2) % l] - '0';
		std::vector< std::vector<int> > left_ending = left_endings[ctr % 7][left_digit];
		std::vector< std::vector<int> > right_ending = right_endings[(ctr+1) % 7][right_digit];
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
			std::sort(left.begin(), left.end());
			std::sort(right.begin(), right.end());
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
#ifdef _DEBUG
				cout << "ctr = " << ctr % 8 << endl;
#endif
				bool success = update_hash_table(ctr % 8, hash_table);
				if (success) {
					triplet[idx++] = ctr % 8;
					if (idx % 3 == 0) {
						result->push_back(triplet);
						cout << "Triplet "<< endl;
						for (int i = 0; i < 3; ++i) {
							cout << triplet[i] << " , ";
						}
						float score = 0.0;
						bool satisfiable = is_satisfiable(triplet, score);
						if (satisfiable) {
							cout << "satisfiable" << "\t\t" << score << endl;
						} else {
							cout << "not satisfiable" << "\t\t" << score << endl;
						}
						system("a=1; read a");
						triplet = (int*) calloc(3, sizeof(int));
						idx = 0;
					}
					success = false;
					delete [] hash_table;
	                                hash_table = (int*) calloc(8, sizeof(int));
				}
				common.clear();
				ctr++;
				continue;
			}
		}	
		++ctr;
	}
	delete result;
	return 0;
}
