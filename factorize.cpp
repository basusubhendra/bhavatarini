#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <mysql/mysql.h>
#include <boost/lexical_cast.hpp>
#include "zeros.hpp"
using namespace std;
using namespace boost;
#define NZEROS 101

int is_bookmarked_triplet(int* triplet) {
	if (triplet[1] != 0) return -1;
	if (triplet[0] == 3 && triplet[2] == 1) return 0;
	if (triplet[0] == 2 && triplet[2] == 7) return 1;
	return -1;
}

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

bool is_riemann_zero(unsigned long long int long_counter, int& order) {
	if (long_counter == 1) {
		order = 1;
		return true;
	}
	MYSQL* conn;
	conn = mysql_init(NULL);
	mysql_real_connect(conn, "localhost", "root", "", "zeros", 3306, NULL, 0);
	std::string base_query = "SELECT id from zeros WHERE value=";
	base_query += boost::lexical_cast<std::string>(long_counter);
	MYSQL_RES *res;
	mysql_query(conn, (char*) base_query.c_str());
	res = mysql_store_result(conn);
	if (!res) {
		mysql_close(conn);
		return false;
	}
	unsigned long long int nrows = mysql_num_rows(res);
	order = nrows;
	mysql_close(conn);
	if (nrows > 0) {
		return true;
	} else {
		return false;
	}
	return false;
}

int main(int argc, char* argv[]) {
	FILE* testcase = fopen("testcases/latest.txt","r");
	char* num = new char[301];
	fscanf(testcase, "%300s\n", num);
	num[300] = '\0';
	//	char* num = strdup(argv[1]);
	unsigned long long int l = strlen(num);
	unsigned long long int ctr = 0;
	int* hash_table = (int*) calloc(8, sizeof(int));
	int* triplet = (int*) calloc(3, sizeof(int));
	int idx = 0, index = 0;
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
				++ctr;
				continue;
			} else if (common.size() == 1) {
				bool success = update_hash_table(ctr % 8, hash_table);
				if (success) {
					triplet[idx++] = ctr % 8;
					if (idx % 3 == 0) {
						index++;
						int type = 0;
						if ((type = is_bookmarked_triplet(triplet)) >= 0) {
							int order = 0;
							bool is_zero = is_riemann_zero(index, order);
							if (type == 0) {
								cout << "Pi " << "\t\t" << (int) is_zero << "\t\t" << order << endl;
							} else if (type == 1) {
								cout << "E " << "\t\t" << (int) is_zero << "\t\t" << order << endl;
							}
						}
						triplet = (int*) calloc(3, sizeof(int));
						idx = 0;
						if (index % NZEROS == 0) {
							delete [] hash_table;
							exit(2);
						}
					}
					success = false;
					delete [] hash_table;
	                                hash_table = (int*) calloc(8, sizeof(int));
				}
				common.clear();
				++ctr;
				continue;
			}
		}	
			++ctr;
	}
	return 0;
}
