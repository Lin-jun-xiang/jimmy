// #include <iostream>  
// using namespace std;  

// // *n 代表記憶體位置,而非值  
// void func(int *n){ 
//     *n = *n + 1;  
// }  

// int main(){
//     int a = 3;
//     cout<<a<<endl;  
//     func(&a); // &a 代表複製a的記憶體到func做處理
//     cout<<a<<endl;  
// return 0;  
// }  
//------------------------------------------------------- 涵式遞迴
// void countTo3(int);

// int main(){
//     countTo3(1);
//     int v[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
//     printf("%d\n", v[2][2]);
//     return 0;
// }

// void countTo3(int i){
//     if(i <= 3){
//         printf("%d\n", i );
//         countTo3(i+1); // 呼叫自己
//     }
// }
//------------------------------------------------------- 在涵式間傳遞陣列
// #include <stdio.h>;
// #include <stdlib.h>;
// #include <time.h>;

// void arrayRand(int v[10]);
// void arrayPrint(int v[10]);
// int arrayMax(int v[10]); // return value

// int main(){
//     srand(time(0));
//     int v[10];
//     arrayRand(v);
//     arrayPrint(v);
//     printf("Max: %d\n", arrayMax(v));
//     return 0;
// }

// void arrayRand(int v[10]){
//     for (int i =0; i < 10; i++){
//         v[i] = rand() %100;
//     }
// }

// int arrayMax(int v[10]){
//     int max = v[0] , i ;
//     for (i = 1; i<10; i++){
//         if(v[i] > max){
//             max = v[i];
//         }
//     }
//     return max; 
// }

// void arrayPrint(int v[10]){
//     for(int i =0; i < 10; i++){
//         printf("%d\n", v[i]);
//     }
//     printf("\n");
// }
//------------------------------------------------------- 涵式是否引用指標?
// #include <iostream>;

// using namespace std; 

// int func(int n);
// int func2(int *n);

// int main(){
//     int x = 10;
    
//     cout<<func(x)<<endl
//         << x<<endl;
    
//     cout<<"func2--x =>"<<func2(&x)<<endl;

//     return 0;
// }

// // x值只是複製給fun使用,故即使經過涵式運算,也不會有所影響。
// int func(int n){
//     n = n+1;
//     return n ;
// }

// // 參數n在此為"指標",呼叫func2時,將x的位址值傳遞給指標n,故會影響原本x值
// int func2(int *n){
//     *n = *n + 1;
//     return *n;
// }



//------------------------------------------------------- call by reference
// #include <iostream>;

// using namespace std;

// void func(int const x, int const y, int &sum, int &mul){
//     sum = x + y;
//     mul = x * y;
// }

// int main(){
//     int x = 2;
//     int y = 3;
//     int sum;
//     int mul;

//     func(x,y,sum,mul);

//     cout<< "sum = "<<sum<<endl
//         << "mul = "<<mul<<endl;
// }

//------------------------------------------------------- call by address
// #include <iostream>;

// using namespace std;

// void func(int const x, int const y, int* sum, int* mul){
//     *sum = x + y;
//     *mul = x * y;
// }

// int main(){
//     int x = 2;
//     int y = 3;
//     int sum;
//     int mul;

//     func(x,y,&sum,&mul);

//     cout<< "sum = "<<sum<<endl
//         << "mul = "<<mul<<endl;
// }

//------------------------------------------------------- test
// #include <stdlib.h>
// #include <iostream>
// #include <stdio.h>

// using namespace std;

// int main(){

//     int a = 10 , *b;

//     b = new int(); // b is a pointer, need to give its memory
//     *b = 3;
    
//     int *c = b;
    
//     cout<<b<<endl  // >> address
//         <<*b<<endl // >> int
//         <<*c<<endl // >> int
//         <<c<<endl; // >> address same as b

//     *c = 123;
//     a = *b;
//     cout<<"-------"<<endl
//         <<c<<endl // >> address same as former
//         <<*c<<endl // >> int 123
//         <<b<<endl // >> address same as former
//         <<*b<<endl // >> int 123
//         <<a<<endl; // int 123

//     *b = 321;
//     cout<<"-------"<<endl
//         <<b<<endl // >> address same as former
//         <<*b<<endl // >> int 321
//         <<c<<endl // >> address same as former
//         <<*c<<endl; // >> int 321
    
//     c = &a;
//     cout<<"-------"<<endl
//         <<a<<endl // >> int 123
//         <<c<<endl // >> address same as a
//         <<*c<<endl; // >> int 123

//     return 0;
// }

//------------------------------------------------------- 串列
// #include <stdio.h>
// #include <stdlib.h>

// struct node{

//     int data;
//     struct node *next;
    
// };
// typedef struct node Node; // 將struct node物件以Node作為別名


// // argc 是argument count(參數總和)的縮寫，代表包括指令本身的參數個數。系統會自動計算所輸入的參數個數
// //argv 則是argument value 的縮寫。代表參數值。也就是使用者在命令列中輸入的字串，每個字串以空白相隔。
// //同時，系統會自動將程式本身的名稱指定給argv[0] ，再將程式名稱後面所接續的參
// //數依序指定給argv[1] 、argv[2]…
// int main(int argc, char *argv[]){

//     Node a,b,c; // 創建三個節點
//     Node *ptr = &a; // 宣告ptr,並指向節點a

//     a.data = 12;
//     a.next = &b;
//     b.data = 30;
//     b.next = &c;
//     c.data = 64;
//     c.next = NULL;

//     while(ptr != NULL){
        
//         printf("address=%p, ",ptr); // 印出節點位置
//         printf("data=%d ",ptr->data); // 印出節點資料
//         printf("next=%p\n",ptr->next); //印出下一個節點位置
//         ptr=ptr->next; // 將ptr指向下一個節點

//     }

//     return 0;
// }

//------------------------------------------------------- 結構串列
// #include <stdio.h>
// #include <stdlib.h>
// #include <string>
// #include <iostream>

// using namespace std;
// // struct結構:含有不同型態的變數
// struct node{

//     string sname;
//     float temp;
//     struct node *next;

// };
// typedef struct node Students;

// int main(){
    
//     Students A,B,C;
//     Students *ptr = &A; // 宣告ptr指向A地址

//     A.sname = "Peter";
//     A.temp = 35.7;
//     A.next = &B;
//     B.sname = "Bosh";
//     B.temp = 36.3;
//     B.next = &C;
//     C.sname = "Angel";
//     C.temp = 39.0;
//     C.next = NULL;

//     while(ptr != NULL){

//         printf("address=%p, ",ptr); // 印出節點位置
//         cout<<"name="<<ptr->sname<<" "; // 印出節點資料
//         printf("temp=%f ", ptr->temp);
//         printf("next=%p\n",ptr->next); //印出下一個節點位置
//         ptr=ptr->next; // 將ptr指向下一個節點
//     }

//     return 0;

// }

//------------------------------------------------------- class物件1
// #include <iostream>
// using namespace std;

// class Student{

//     private:
//         float weight = 60;// kg
//         float height = 1.7;// m

//     public:
//         float bmi(){

//             return weight/(height*height);
//         }
// };

// main(){
    
//     Student x;
//     cout<<x.bmi()<<endl;
// }

//------------------------------------------------------- class物件2


















