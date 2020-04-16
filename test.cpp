#include <iostream>

using namespace std;

class ListNode{
    public:
        string sname;
        float temp;
        ListNode *next;
};

int main(){
    ListNode A, B, C, D, E;

    // 先建三個相串節點
    A.sname = "Peter";
    A.temp = 36.0;
    A.next = &B;
    B.sname = "Bosh";
    B.temp = 36.3;
    B.next = &C;
    C.sname = "Angel";
    C.temp = 39.0;
    C.next = NULL;

    // 開頭新增一節點
    ListNode newNode;
    newNode.sname = "Josh";
    newNode.temp = 36.9;
    newNode.next = &A;

    ListNode *current = &newNode;

    // // 刪除含有Bosh的節點
    // ListNode *current = &newNode,      
    //          *previous = 0;

    // while (current != 0 && current->sname != "Bosh") {  // Traversal
    //     previous = current;                       // 如果current指向NULL
    //     current = current->next;                  // 或是current->data == x
    // } 

    //     if (current == 0) {                 // list沒有要刪的node, 或是list為empty
    //     cout << "There is no " << "the Student" << " in list.\n";
    //     // return;
    // }
    // else if (current == newNode) {        // 要刪除的node剛好在list的開頭
    //     newNode = current->next;          // 把first移到下一個node
    //     delete current;                 // 如果list只有一個node, 那麼first就會指向NULL
    //     current = 0;                    // 當指標被delete後, 將其指向NULL, 可以避免不必要bug
    //     // return;                     
    // }
    // else {                              // 其餘情況, list中有欲刪除的node, 
    //     previous->next = current->next; // 而且node不為first, 此時previous不為NULL
    //     delete current;
    //     current = 0;
    //     // return;
    // }


    while(current != NULL){

        printf("address=%p, ",current); // 印出節點位置
        cout<<"name="<<current->sname<<" "; // 印出節點資料
        printf("temp=%f ", current->temp);
        printf("next=%p\n",current->next); //印出下一個節點位置
        current=current->next; // 將ptr指向下一個節點
    }

    return 0;

}