/**
 * You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
 * 
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(new Comparator<ListNode>() {
            public int compare(ListNode nn1, ListNode nn2) {
                int n1 = nn1.val;
                int n2 = nn2.val;
                return n1 - n2;
            }
        });
        
        for (ListNode node : lists) {
            if (node != null)
                pq.add(node);
        }
        
        ListNode head = new ListNode();
        ListNode curr = head;
        
        while (!pq.isEmpty()) {
            ListNode smallest = pq.poll();
            curr.next = smallest;
            curr = curr.next;
            if (smallest.next != null) {
                pq.add(smallest.next);
            }
        }
        
        return head.next;
        
    }
}