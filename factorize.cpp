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

int _decode_(int* triplet) {
	if (triplet[0] == 0 && triplet[1] == 0 && triplet[2] == 0) {
		return 0;
	} else if (triplet[0] == 0 && triplet[1] == 0 && triplet[2] == 1) {
		return 1;
	} else if (triplet[0] == 0 && triplet[1] == 1 && triplet[2] == 0) {
		return 2;
	} else if (triplet[0] == 0 && triplet[1] == 1 && triplet[2] == 1) {
		return 3;
	} else if (triplet[0] == 1 && triplet[1] == 0 && triplet[2] == 0) {
		return 4;
	} else if (triplet[0] == 1 && triplet[1] == 0 && triplet[2] == 1) {
		return 5;
	} else if (triplet[0] == 1 && triplet[1] == 1 && triplet[2] == 0) {
		return 6;
	} else if (triplet[0] == 1 && triplet[1] == 1 && triplet[2] == 1) {
		return 7;
	}
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

bool is_riemann_zero(unsigned long long int long_counter) {
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
	vector<int*>* result = new vector<int*>();
	int* hash_table = (int*) calloc(8, sizeof(int));
	int* triplet = (int*) calloc(3, sizeof(int));
	int idx = 0;
	int index = 0;
	unsigned long long int long_counter = 0, short_counter = 0;
	int* long_triplet = (int*) calloc(3, sizeof(int));
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
						result->push_back(triplet);
						long_counter++;
						int type = 0;
						if ((type = is_bookmarked_triplet(triplet)) >= 0) {
							bool is_zero = is_riemann_zero(long_counter);
							if (type == 0) {
								//cout << "Pi " << endl;
								long_triplet[index] = (int) is_zero;
								++index;
							} else if (type == 1) {
								//cout << "E " << endl;
								long_triplet[index] = (int) is_zero;
								++index;
							}
							//cout << "index = " << index << endl;
							if (index % 3 == 0) {
								++short_counter;
								if (is_riemann_zero(short_counter)) {
									cout << "Short Counter " << short_counter << "\t\t" << _decode_(long_triplet) << "\n" ;
								        system("a=1; read a");
								}
								delete [] long_triplet;
								long_triplet = (int*) calloc(3, sizeof(int));
								index = 0;
							}
						}
						triplet = (int*) calloc(3, sizeof(int));
						idx = 0;
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
	delete result;
	return 0;
}
