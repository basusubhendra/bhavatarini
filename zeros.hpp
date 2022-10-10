#ifndef _ZEROS_
#define _ZEROS_
#include <vector>
using namespace std;
std::vector< std::vector< std::vector< std::vector<int> > > > left_endings = { {  { { 1 }, { 1 } }, { { 1 }, { 4 } }, { { 2 }, {1, 5 } }, { { 3 }, { 0, 2, 7 } } , { { 4 }, { 0, 3, 8, 9 } } , { { 3 }, { 2, 6, 9 } }, { { 4 }, { 0, 5, 7, 9 } }, { { 4 }, { 2, 5, 7, 9 } }, { { 4 }, { 2, 4, 7, 8 } }, { { 4 }, { 2, 4, 5, 8 } } }, {  { { 3 }, { 4, 8, 9 } }, { { 2 }, { 0, 3 } }, { { 3 }, { 0,4,9 } }, { { 1 }, { 3 } }, { { 3 }, { 1,6,7 } }, { { 4 }, { 0,1,7,8 } }, { { 1 }, { 4 } }, { { 4 }, { 0,1,4,5 } }, { { 2 }, { 0,8 } }, { { 3 }, { 3,5,7 } } }, {  { { 5 }, { 0,1,2,6,7 } }, { { 3 }, { 1,3,4 } }, { { 0 }, { }  }, { { 4 }, { 1,2,3,4 } }, { { 3 }, { 2,4,9 } }, { { 2 }, { 4,8 } }, { { 1 }, { 5 } }, { { 3 } , { 0,3,7 } }, { { 3 } , { 0,3,7 } }, { { 3 }, { 1,3,7 } } }, {  { { 3 }, { 4,5,9 } }, { { 4 }, { 0,2,7,8 } }, { { 4 }, { 2,4,5,7 } }, { { 4 }, { 1,4,5,7 } }, { { 3 }, { 4,6,7 } } , { { 1 },{ 1 } } , { { 1 }, { 7 } } , { { 3 }, { 0,3,9 } } , { { 1 }, { 6 } } , { { 1 }, { 1 } }  }, {  { { 3 } , { 3,6,8 } }, { { 4 } , { 1,3,7,8 } }, { { 2 }, { 0,5 } }, { { 1 } , { 8 } }, { { 3 }, {6,7,8 } }, { { 4 }, { 0,1,2,4 } }, { { 3 }, { 1,2,4 } }, { { 4 }, { 0,1,3,8 } }, { { 1 }, { 7 } }, { { 2 }, { 1,8 } } }, {  { { 4 }, { 3,4,6,7 } }, { { 4 }, { 1,5,7,9 } }, { { 2 }, { 4,7 } }, { { 4 }, { 2,4,7,8 } }, { { 2 }, { 0,9 } }, { { 1 }, { 4 } }, { { 2 }, { 3,9 }  }, { { 3 }, { 1,2,7 } }, { { 6 }, { 1,3,4,5,7,9 } }, { { 0 }, { } } }, {  { { 1 }, { 1 } }, { { 3 } , { 0,1,9 } }, { { 2 } , { 1,5 } }, { { 3 } , { 2,4,9 } }, { { 3 } , { 0,4,7 } }, { { 3 }, { 0,1,7 } }, { { 1 } , { 1 } }, { { 5 } , { 3,4,5,6,8 } }, { { 1 }, { 0 } }, { { 4 } , { 0,2,4,9 } } } };
std::vector< std::vector< std::vector< std::vector<int> > > >  right_endings = { {  { { 3 } , { 3,4,6 } }, { { 2 }, { 0,2 }  }, { { 5 }, { 3,5,7,8,9 } }, { { 1 }, { 4 } }, { { 3 }, { 1,8,9 } }, { { 4 }, { 2,6,7,9 } }, { { 1 }, { 5 } }, { { 4 }, { 3,6,7,8 } }, { { 3 }, { 4,8,9 } }, { { 4 }, { 4,5,6,7 } } }, {  { { 5 } , { 1,2,5,7,8 } }, { { 3 }, { 4,5,7 } }, { { 0 }, { }  }, { { 3 } , { 1, 3, 9 } }, { { 4 }, { 0,2,6,7 } }, { { 2 }, { 7,9 }  }, { { 1 }, { 4 } }, { { 3 }, { 4,5,9 }  }, { { 3 }, { 0,5,8 }  }, { { 2 } , { 0,2 } }, }, {  { { 3 } , { 0,7,8 }  }, { { 4 } , { 0,1,3,9 }  }, { { 3 } , { 0,3,4 } }, { { 5 } , { 1,3,7,8,9 }  }, { { 4 } ,{ 1,3,4,5 } }, { { 1 }, { 6 } }, { { 1 }, { 0 } }, { { 4 }, { 0,7,8,9 } }, { { 1 }, { 5 } }, { { 1 }, { 4 } } }, {  { { 2 }, { 1,7 } }, { { 3 }, { 3,5,9} }, { { 2 }, { 1, 2 }  }, { { 1 }, { 7 } } , { { 4 } , { 0,2,3,4}  }, { { 3 }, { 0,2,3 } }, { { 2 }, { 4,8 } }, { { 5 }, { 1, 2, 3, 4, 6 } }, { { 1 }, { 1 } }, { { 2 }, { 0, 7 } } }, {  { { 3 }, { 2,5,7 } }, { { 5 }, { 1, 5, 6, 7, 9 } }, { { 2 }, { 5, 6 } }, { { 3 }, { 0,1,7 } }, { { 2 }, { 5, 6 } }, { { 1 }, { 2 } }, { { 2 }, { 0, 4 } }, { { 3 }, { 1, 4, 8 } }, { { 6 }, { 0,1,3,4,7,9 }  }, { { 0 }, { } } }, {  { { 1 }, { 4 } }, { { 3 }, { 1, 7, 8 }  }, { { 2 }, { 3, 7 }  }, { { 3 }, { 0,6,8 } }, { { 5 }, { 0,2,3,5,8} }, { { 2} , { 1, 8 }  }, { { 1 }, { 0 } }, { { 6 }, { 0, 1, 2, 3, 7, 8 }  }, { { 1 }, { 3 }  }, { { 4 }, { 1, 4, 6, 8 } } }, {  { { 5 } , { 1, 4, 5, 8, 9 }  }, { { 5 } , { 0, 1, 2, 5, 6 }  }, { { 2 }, { 3,9 } }, { { 1} , { 7}  }, { { 4 }, { 3, 4 , 7, 9 } }, { { 2 } , { 2,7 }  }, { { 1 } , { 7 }  }, { { 2 }, { 4,5 }  }, { { 1 }, { 7 } }, { { 3 } , { 1, 3, 9 } } } };
#endif
